import { expect, test } from 'claude-code/testing'

const SAMPLE = {
  utc: '2026-10-03 04:00',
  today: '3 Oct 2026',
  accounts: [
    { account: '2', cost_today: 213.5, rows_today: 60, cost_yesterday: 278, live: 3, live_roles: ['X (account 2)'],
      rl_status: '?', rl_type: '', resets_utc: '', rl_seen_utc: '' },
    { account: '4', cost_today: 302.9, rows_today: 81, cost_yesterday: 844, live: 4, live_roles: [],
      rl_status: 'allowed_warning', rl_type: 'seven_day', resets_utc: '2026-10-03 08:00', rl_seen_utc: '2026-10-03 04:00' },
  ],
}

test('/usage reads account_usage.py and sets the status line', async ($, on) => {
  const argvs: string[][] = []
  on('process.run', async (_$, e) => {
    const argv = [...e.argv]
    argvs.push(argv)
    return argv[0] === 'python3'
      ? { value: { exitCode: 0, stdout: JSON.stringify(SAMPLE), stderr: '' } }
      : { value: { exitCode: 0, stdout: '', stderr: '' } }
  })
  const statuses: (string | undefined)[] = []
  on('ui.status', async (_$, e) => {
    statuses.push(e.text)
    return { value: undefined }
  })
  on('ui.open', async () => ({ value: undefined as never }))
  const r = await $.command.run({ command: 'usage' })
  expect(r.text).toContain('Usage pane opened')
  expect(argvs.some(a => a.includes('tools/account_usage.py'))).toBe(true)
  expect(statuses.some(s => (s ?? '').includes('a4 4live $303'))).toBe(true)
})
