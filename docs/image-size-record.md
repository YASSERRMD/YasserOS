# Image Size Record

## Purpose

Track YasserOS image sizes across versions to detect size regressions and guide optimisation.

## Recorded Image Sizes

| Version        | Date       | Compressed | Uncompressed | Notes                        |
|---------------|-----------|------------|--------------|------------------------------|
| v0.0.1-alpha  | (pending)  | TBD        | TBD          | First build — Phase 20 target |

*To be updated after first successful build.*

## How to Measure Image Size

```bash
# Compressed size
ls -lh deploy/*.img.xz

# Uncompressed size (without fully decompressing)
xz -l deploy/*.img.xz

# Root filesystem usage (from within a booted image or mounted rootfs)
df -h /
```

## Size Targets

| Component          | Target Size (uncompressed) |
|-------------------|---------------------------|
| /boot/firmware    | ~512 MB (fixed)            |
| Base system (stage0–2) | ~1.5 GB               |
| XFCE + stage-yasseros | ~1.0 GB                |
| Yasser Control Center | ~50 MB                 |
| **Total image**   | **~3.0–4.0 GB**            |
| **Compressed**    | **~800 MB – 1.5 GB**       |

## Size Optimisation Notes

If image grows beyond target:
1. Review packages added to `00-packages` — remove unused ones
2. Run `apt-get clean` in the stage chroot script (pi-gen does this, but verify)
3. Check for large files inadvertently included in the `files/` overlay
4. Consider splitting optional packages into a separate "full" image variant

## Reference: Raspberry Pi OS Image Sizes

For comparison, official images:
- Raspberry Pi OS Lite (bookworm): ~400 MB compressed, ~2.1 GB uncompressed
- Raspberry Pi OS with Desktop: ~1.1 GB compressed, ~4.8 GB uncompressed

YasserOS aims to be comparable to Raspberry Pi OS with Desktop (~5 GB uncompressed).
