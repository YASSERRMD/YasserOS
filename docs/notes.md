# Local Notes

The Notes page in Yasser Control Center is a lightweight Markdown note-taking
tool built directly into the control center. Notes are stored as plain `.md`
files so they can be opened in any text editor.

## Storage Location

```
~/.local/share/yasseros/notes/
```

Each note is a UTF-8 Markdown file. The directory is created automatically
when you create your first note.

## Features

- **Create note** — click the new-document icon to create a note with a
  timestamped filename (`note-YYYYMMDD-HHMMSS.md`)
- **Edit note** — select a note from the sidebar, type in the editor panel,
  then click **Save**
- **Delete note** — select a note and click the trash icon; deletion is
  immediate and not reversible
- **Markdown template** — every new note starts with a `# Note` heading and
  the creation date

## Markdown Template

```markdown
# Note

_Created: YYYY-MM-DD_

---

Write your note here.
```

## Tips

- Notes are plain files — back them up with `rsync`, git, or any sync tool
- Open the `~/.local/share/yasseros/notes/` folder in your file manager to
  bulk-rename or import notes
- Notes support full Markdown syntax; render them with any Markdown viewer
