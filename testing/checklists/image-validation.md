# Image Validation Checklist

## Purpose

Comprehensive validation of a YasserOS image before it is published or distributed.

## Quick Validation (Artifact Only — No Hardware)

Run before flashing:

- [ ] Image filename matches `YYYY-MM-DD-YasserOS-*.img.xz` pattern
- [ ] SHA256 checksum file exists alongside the image
- [ ] `sha256sum --check *.sha256` returns OK
- [ ] `xz -l *.img.xz` reports a valid xz file (no corruption)
- [ ] Uncompressed size is in expected range (3–6 GB)
- [ ] Image can be partially read: `xz -dc *.img.xz | head -c 512 | xxd | head` (shows MBR)

## Full Validation (Requires Raspberry Pi 4)

See individual checklists for each validation domain:
- [boot-validation.md](boot-validation.md)
- [filesystem-validation.md](filesystem-validation.md)
- [package-validation.md](package-validation.md)
- [login-validation.md](login-validation.md)
- [network-validation.md](network-validation.md)
- [first-boot-validation.md](first-boot-validation.md)

## Validation Sign-Off Form

```
Image: YYYY-MM-DD-YasserOS-VERSION.img.xz
SHA256: <hash>
Validated by: YASSERRMD
Date: YYYY-MM-DD
Hardware: Raspberry Pi 4 (4GB / 8GB)
SD Card: <brand/size>

Checklist results:
  Image artifact: PASS / FAIL
  Boot: PASS / FAIL
  Filesystem: PASS / FAIL
  Packages: PASS / FAIL
  Login: PASS / FAIL
  Network: PASS / FAIL
  First boot: PASS / FAIL

Overall result: PASS / FAIL
Notes: <any issues or observations>
```

## Validation Failures

If validation fails, do NOT publish the image. Instead:
1. Note the failure in `docs/build-report.md`
2. Open a fix branch: `git checkout -b fix-<description>`
3. Investigate and fix
4. Rebuild and re-validate
