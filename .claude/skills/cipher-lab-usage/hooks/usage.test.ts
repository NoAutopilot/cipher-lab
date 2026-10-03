import { expect, test } from 'claude-code/testing'

const SAMPLE = {
  utc: '2026-10-03 04:00',
  accounts: [
    { account: '2', live: 3, live_roles: [], five_pct: 41, five_resets: '', seven_pct: 77.5, seven_resets: '', age_min: 3 },
    { account: '4', live: 6, live_roles: [], five_pct: null, five_resets: '', seven_pct: null, seven_resets: '', age_min: null },
  ],
}

test('/usage posts this account\'s real bars and shows every account\'s', async ($, on) => {
  const argvs: string[][] = []
  on('session.usage', async () => ({
    value: { startedAt: 0, context: {}, cost: undefined,
      rateLimits: [{ kind: 'five_hour', percentUsed: 62.5, resetsAt: '2026-10-03T06:00:00Z' },
                   { kind: 'seven_day', percentUsed: 81, resetsAt: '2026-10-03T08:00:00Z' }] } as never,
  }))
  on('process.run', async (_$, e) => {
    const argv = [...e.argv]
    argvs.push(argv)
    return argv.includes('--json')
      ? { value: { exitCode: 0, stdout: JSON.stringify(SAMPLE), stderr: '' } }
      : { value: { exitCode: 0, stdout: 'pushed abc', stderr: '' } }
  })
  const statuses: (string | undefined)[] = []
  on('ui.status', async (_$, e) => { statuses.push(e.text); return { value: undefined } })
  on('ui.open', async () => ({ value: undefined as never }))
  const r = await $.command.run({ command: 'usage' })
  const post = argvs.find(a => a.includes('--push'))!
  expect(post).toContain('62.5')
  expect(post).toContain('81')
  expect(r.text).toContain('a2 5h 41% 7d 78%')
  expect(statuses.some(s => (s ?? '').includes('a2 5h 41%'))).toBe(true)
  expect(r.text.includes('$')).toBe(false)
})
