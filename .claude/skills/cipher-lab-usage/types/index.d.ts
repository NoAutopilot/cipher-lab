export type AccountRow = {
  account: string
  live: number
  live_roles: string[]
  five_pct: number | null
  five_resets: string
  seven_pct: number | null
  seven_resets: string
  age_min: number | null
}
export type Usage = { utc: string; accounts: AccountRow[] }

declare module 'claude-code' {
  interface PluginState {
    'cipher-lab-usage': { usage: Usage | null; error: string; lastPost: string }
  }
}
