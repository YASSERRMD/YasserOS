# Login Validation Checklist

## LightDM Login Screen (Phase 15+)

- [ ] LightDM login screen appears after boot
- [ ] Login screen background matches YasserOS wallpaper (Phase 12+)
- [ ] Username field accepts input
- [ ] Username: `yasser` (or the configured FIRST_USER_NAME)
- [ ] Password prompt appears after entering username
- [ ] Incorrect password shows error message (does not hang)
- [ ] Correct password proceeds to desktop session

## Desktop Session Load (Phase 15+)

- [ ] XFCE session starts after login
- [ ] Desktop wallpaper loads (YasserOS default wallpaper — Phase 12+)
- [ ] Desktop icons are visible (if configured)
- [ ] XFCE panel loads (top or bottom bar)
- [ ] System clock in panel shows correct time
- [ ] Session manager works (logout/reboot from panel)

## Terminal Login (Headless, Phase 6–14)

For builds without desktop:
- [ ] Login prompt shows `yasseros login:` (not `raspberrypi login:` — Phase 10+)
- [ ] Username `yasser` is accepted
- [ ] Password prompt appears
- [ ] Successful login shows MOTD (Phase 10+) or default MOTD
- [ ] Shell prompt is functional

## User Configuration

```bash
id yasser
groups yasser
```
- [ ] `yasser` is UID 1000 (standard first user)
- [ ] `yasser` is in groups: `adm`, `sudo`, `video`, `audio`, `dialout`, `plugdev`

```bash
echo $SHELL
ls ~/.bashrc
```
- [ ] Default shell is bash
- [ ] `.bashrc` exists in home directory

## Sudo Access

```bash
sudo whoami
```
- [ ] Returns `root` without password (or prompts for password, depending on config)

## Session Security

- [ ] Screen lock activates after inactivity (XFCE screensaver — Phase 15+)
- [ ] Lock screen requires correct password to unlock

## Auto-login (if configured)

If LightDM auto-login is enabled in the config:
- [ ] Desktop loads automatically without password prompt
- [ ] Correct user (`yasser`) is auto-logged in
