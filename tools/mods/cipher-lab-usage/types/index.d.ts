export type AccountRow = {
  account: string
  cost_today: number
  rows_today: number
  cost_yesterday: number
  live: number
  live_roles: string[]
  rl_status: string
  rl_type: string
  resets_utc: string
  rl_seen_utc: string
}
export type Usage = { utc: string; today: string; accounts: AccountRow[] }

declare module 'claude-code' {
  interface PluginState {
    'cipher-lab-usage': { usage: Usage | null; error: string }
  }
}
