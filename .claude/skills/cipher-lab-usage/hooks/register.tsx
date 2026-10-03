import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Usage } from '../types'

// Usage bars across the cipher-lab accounts (owner, 3 Oct 2026). Every session that loads this posts its own
// account's real 5-hour / 7-day bars (account-wide: every session and subagent on the login is in them) to
// USAGE.tsv on origin/main, at most once per account per 15 min, and shows every account's latest bars.

const PANE = 'cipher-lab-usage'
const REPO = '/home/user/cipher-lab'
const EVERY_MS = 5 * 60 * 1000
const usage = atom({ plugin: 'cipher-lab-usage', key: 'usage' } as const, null as Usage | null)
const error = atom({ plugin: 'cipher-lab-usage', key: 'error' } as const, '')
const lastPost = atom({ plugin: 'cipher-lab-usage', key: 'lastPost' } as const, '')

const pct = (p: number | null) => (p === null ? '--' : `${Math.round(p)}%`)
const bar = (p: number | null, w = 10) => {
  if (p === null) return '·'.repeat(w)
  const n = Math.max(0, Math.min(w, Math.round((p / 100) * w)))
  return '█'.repeat(n) + '░'.repeat(w - n)
}

export const statusLine = (u: Usage) =>
  u.accounts
    .filter(a => a.five_pct !== null || a.seven_pct !== null)
    .map(a => `a${a.account} 5h ${pct(a.five_pct)} 7d ${pct(a.seven_pct)}`)
    .join(' · ') || 'usage: no bars posted yet'

const postOwn = async ($: any) => {
  const u = await $.session.usage()
  const five = u.rateLimits.find((r: any) => r.kind === 'five_hour')
  const seven = u.rateLimits.find((r: any) => r.kind === 'seven_day')
  if (!five && !seven) return 'no rate-limit windows on this session'
  const argv = ['python3', 'tools/account_usage.py', '--post', 'auto', '--source', 'mod', '--push']
  if (five) argv.push('--five', String(five.percentUsed), '--five-resets', five.resetsAt ?? '')
  if (seven) argv.push('--seven', String(seven.percentUsed), '--seven-resets', seven.resetsAt ?? '')
  const r = await $.process.run(argv, { cwd: REPO, timeoutMs: 90000 })
  return (r.stdout || r.stderr || '').trim().slice(0, 200)
}

const refresh = async ($: any, alsoPost: boolean) => {
  if (alsoPost) {
    try {
      const said = await postOwn($)
      await update($, lastPost, () => said)
    } catch (err) {
      await update($, lastPost, () => `post failed: ${String(err).slice(0, 150)}`)
    }
  } else {
    await $.process.run(['git', 'fetch', '-q', 'origin', 'main'], { cwd: REPO, timeoutMs: 60000 })
  }
  const r = await $.process.run(['python3', 'tools/account_usage.py', '--json', '--ref', 'origin/main'], {
    cwd: REPO,
    timeoutMs: 60000,
  })
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
    await $.command.register({ name: 'usage', description: 'Usage bars across the cipher-lab accounts' })
    void refresh($, true)
    $.clock.every(EVERY_MS, () => void refresh($, true))
    return started
  })

  on('command.run', { command: 'usage' }, async $ => {
    await refresh($, true)
    await $.ui.open({ id: PANE, title: 'Usage bars, all accounts' })
    const u = await read($, usage)
    return { text: u ? statusLine(u) : 'Usage pane opened.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const u = await read($, usage)
    const err = await read($, error)
    const said = await read($, lastPost)
    if (!u) return <Text dimColor>{err || 'Loading usage bars...'}</Text>
    return (
      <Box flexDirection="column">
        <Text bold>Usage bars, {u.utc} UTC</Text>
        {u.accounts.map(a => (
          <Box flexDirection="column" marginTop={1}>
            <Text bold>
              Account {a.account} · {a.live} live
              {a.age_min === null ? ' · no reading yet' : ` · read ${a.age_min} min ago`}
            </Text>
            <Text color={(a.five_pct ?? 0) >= 80 ? 'yellow' : undefined}>
              5-hour {bar(a.five_pct)} {pct(a.five_pct)}
              {a.five_resets ? `  resets ${a.five_resets.slice(11, 16)} UTC` : ''}
            </Text>
            <Text color={(a.seven_pct ?? 0) >= 80 ? 'yellow' : undefined}>
              7-day  {bar(a.seven_pct)} {pct(a.seven_pct)}
              {a.seven_resets ? `  resets ${a.seven_resets.slice(0, 16).replace('T', ' ')} UTC` : ''}
            </Text>
          </Box>
        ))}
        <Box marginTop={1}>
          <Text dimColor>Each account's bars come from any of its sessions running this mod. Refresh every 5 min.</Text>
        </Box>
        {said ? <Text dimColor>this session: {said}</Text> : null}
        {err ? <Text color="red">{err}</Text> : null}
      </Box>
    )
  })
}
