# Project Launcher

The Project Launcher page in Yasser Control Center lets you browse, open, and
manage local project folders without leaving the control center.

## How It Works

On load the page scans `~/Projects` (or the directory set in
`YASSEROS_PROJECTS_DIR`) and lists every immediate subdirectory as a project
row. Up to 50 projects are shown.

## Project Row

Each row shows:
- Folder icon + project name + full path
- A **git** badge when the folder contains a `.git` directory or file
- An **Open in Terminal** button — launches `xfce4-terminal` with its working
  directory set to the project
- An **Open in File Manager** button — opens the folder via `xdg-open` or thunar

## Configuration

Set a custom projects root by adding the following to `~/.bashrc` or
`~/.profile`:

```bash
export YASSEROS_PROJECTS_DIR=/path/to/your/projects
```

Restart Yasser Control Center for the change to take effect.

## Refresh

Click the refresh button (↺) in the top-right corner of the page to re-scan the
projects directory without restarting the app.

## Limits

- Hidden directories (names starting with `.`) are excluded
- Maximum 50 projects displayed at once; open the folder in the file manager to
  browse more
