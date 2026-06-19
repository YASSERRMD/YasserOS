# OS Identity Validation Checklist

## Purpose

Verify that YasserOS branding correctly replaces Raspberry Pi OS identity in the built image.

## /etc/os-release

```bash
cat /etc/os-release
```

- [ ] `NAME="YasserOS"` (not "Raspberry Pi OS")
- [ ] `VERSION` contains "YasserOS"
- [ ] `ID=yasseros`
- [ ] `ID_LIKE` includes `debian`
- [ ] `PRETTY_NAME` starts with "YasserOS"
- [ ] `HOME_URL` points to YASSERRMD/YasserOS GitHub

## /etc/issue

```bash
cat /etc/issue
```

- [ ] Contains "YasserOS" (not "Raspbian" or "Raspberry Pi OS")
- [ ] Contains version number

## /etc/issue.net

```bash
cat /etc/issue.net
```

- [ ] Contains "YasserOS"
- [ ] Contains GitHub URL

## Hostname

```bash
hostname
cat /etc/hostname
```

- [ ] Returns `yasseros` (not `raspberrypi`)

## MOTD (Message of the Day)

```bash
# View without logging in (from /etc/motd)
cat /etc/motd
# Or see on login
```

- [ ] Contains "YasserOS" name and tagline
- [ ] Does NOT contain default Raspberry Pi OS MOTD

## YasserOS Release File

```bash
cat /etc/yasseros/release
```

- [ ] `YASSEROS_NAME="YasserOS"` present
- [ ] Version, codename, arch fields populated

## Build Metadata

```bash
cat /usr/share/yasseros/build-metadata
```

- [ ] File exists
- [ ] Version field matches expected release version

## systemd Hostname

```bash
hostnamectl
```

- [ ] Static hostname: `yasseros`
- [ ] Operating System shows "YasserOS" (reads from os-release)

## Raspberry Pi OS Residue Check

```bash
grep -r "Raspberry Pi OS" /etc/os-release /etc/issue /etc/issue.net /etc/motd 2>/dev/null
grep -r "raspbian" /etc/os-release 2>/dev/null | grep -v "ID_LIKE"
```

- [ ] No "Raspberry Pi OS" strings in identity files (except os-release ID_LIKE)
- [ ] `/etc/hostname` does not contain "raspberrypi"
