# Application Menu Customization

YasserOS adds a dedicated **YasserOS** category to the XFCE application menu containing all first-party tools.

## Menu Category

Defined in `stage-yasseros/files/usr/share/applications/yasseros.directory`:

```ini
[Desktop Entry]
Name=YasserOS
Type=Directory
Icon=yasseros-logo
```

XFCE menus pick up `.directory` files automatically when referenced by a menu configuration.

## Desktop Entries

| File | App | Icon |
|------|-----|------|
| `yasser-control-center.desktop` | Yasser Control Center | `preferences-system` |
| `yasseros-lab-mode.desktop` | Lab Mode | `applications-science` |
| `yasseros-ai-workspace.desktop` | AI Workspace | `starred` |
| `yasseros-docs.desktop` | YasserOS Documentation | `help-contents` |

All entries use `Categories=…;YasserOS;` so they appear under the YasserOS group.

## Custom Icon

The branded SVG logo is installed to:
```
/usr/share/icons/hicolor/scalable/apps/yasseros-logo.svg
```

Colors: Deep Space `#0D1117`, YasserBlue `#4493F8`, Violet `#A371F7`.

## Validation

Run from the build host to check all entries have required fields:
```bash
bash stage-yasseros/files/usr/share/applications/validate-desktop-entries.sh
```

## Adding New Entries

1. Create `stage-yasseros/files/usr/share/applications/<name>.desktop`
2. Include `Categories=…;YasserOS;` to appear in the YasserOS menu group
3. Run the validation script before committing
