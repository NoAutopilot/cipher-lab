import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Usage } from '../types'

const PANE = 'cipher-lab-usage'
const REPO = '/home/user/cipher-lab'
const EVERY_MS = 3 * 60 * 1000
const usage = atom({ plugin: 'cipher-lab-usage', key: 'usage' } as const, null as Usage | null)
const error = atom({ plugin: 'cipher-lab-usage', key: 'error' } as const, '')

const statusLine = (u: Usage) =>
  'usage ' +
  u.accounts
    .filter(a => a.live > 0 || a.cost_today > 0 || a.rl_status !== '?')
    .map(a => `a${a.account} ${a.live}live $${Math.round(a.cost_today)}`)
    .join(' | ')

const refresh = async ($: any) => {
  await $.process.run(['git', 'fetch', '-q', 'origin', 'main'], { cwd: REPO, timeoutMs: 60000 })
  const r = await $.process.run(
    ['python3', 'tools/account_usage.py', '--json', '--ref', 'origin/main'],
    { cwd: REPO, timeoutMs: 60000 },
  )
  if (r.exitCode !== 0) {
    await update($, error, () => (r.stderr || 'account_usage.py failed').slice(0, 300))
    return
  }
  const u = JSON.parse(r.stdout) as Usage
  await update($, usage, () => u)
  await update($, error, () => '')
  $.ui.status(statusLine(u))
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const started = await next(e)
    await $.command.register({ name: 'usage', description: 'Show usage across the cipher-lab accounts' })
    void refresh($)
    $.clock.every(EVERY_MS, () => void refresh($))
    return started
  })

  on('command.run', { command: 'usage' }, async $ => {
    await refresh($)
    await $.ui.open({ id: PANE, title: 'Usage across accounts' })
    return { text: 'Usage pane opened.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const u = await read($, usage)
    const err = await read($, error)
    if (!u) return <Text dimColor>{err || 'Loading usage...'}</Text>
    return (
      <Box flexDirection="column">
        <Text bold>Accounts, {u.utc} UTC</Text>
        {u.accounts.map(a => (
          <Box flexDirection="column" marginTop={1}>
            <Text bold>
              Account {a.account}: {a.live} live, ${a.cost_today.toFixed(2)} today ({a.rows_today} workers), $
              {a.cost_yesterday.toFixed(2)} yesterday
            </Text>
            <Text color={a.rl_status.includes('warning') || a.rl_status === 'rejected' ? 'yellow' : undefined}>
              rate limit: {a.rl_status} {a.rl_type}
              {a.resets_utc ? `, resets ${a.resets_utc} UTC` : ''}
              {a.rl_seen_utc ? ` (seen ${a.rl_seen_utc.slice(11)})` : ' (no reading posted)'}
            </Text>
            {a.live_roles.slice(0, 8).map(r => (
              <Text dimColor>  {r}</Text>
            ))}
          </Box>
        ))}
        <Box marginTop={1}>
          <Text dimColor>Spend counts archived workers only (lags running work). Refreshes every 3 min.</Text>
        </Box>
        {err ? <Text color="red">{err}</Text> : null}
      </Box>
    )
  })
}
