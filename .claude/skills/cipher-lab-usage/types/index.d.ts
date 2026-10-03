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
export type Job = { id: string; account: string; text: string; state: 'running' | 'queued' | 'stale' | 'done'; start: string; end: string; summary: string; project: string }
export type ProjectGroup = { project: string; counts: Record<string, number>; jobs: Job[] }
export type Board = { utc: string; hours: number; projects: ProjectGroup[] }

declare module 'claude-code' {
  interface PluginState {
    'cipher-lab-usage': { usage: Usage | null; error: string; lastPost: string; board: Board | null }
  }
}
