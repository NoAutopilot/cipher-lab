# Projects

The registry. One row per project, updated by whoever changes its state. `estate` in `shell/projects.sh`
reads the live numbers from each repository; this file is the durable index.

| Project | Repository | What it is | Owner | Status | Blocked on |
|---|---|---|---|---|---|
| cipher-lab | NoAutopilot/cipher-lab | Reading historical ciphers nobody has read. Access-bound, not compute-bound. | Ryan | active, 10 targets | Two credentials to rotate; four archives to answer; see its `ASKS.md` |

## Adding a project

Run the `NEW-PROJECT.md` brief. It creates the repository, inherits `CONVENTIONS.md`, interviews you for
what counts as a result, lists the credentials a human must create, tests each access route, and adds the
row here. Do not hand-create a project repository; the point of the brief is that project three starts
smarter than project one did.

## Retiring a project

Change its status to `parked` or `closed` with a date and a one-line reason. Do not delete the row. A
closed project's lessons still roll up, and knowing what was abandoned and why is worth more than a tidy
table.
