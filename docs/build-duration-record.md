# Build Duration Record

## Purpose

This document records actual observed build times across different environments to calibrate expectations and detect regressions.

## Recorded Build Times

| Date       | Environment                 | Stage     | Duration  | Notes                          |
|-----------|------------------------------|-----------|-----------|-------------------------------|
| (pending)  | MacBook Pro M2, Docker       | Full build | TBD       | First build — Phase 6 target  |

*To be updated after first successful build.*

## How to Record Build Time

```bash
# Time the full build
time ./scripts/build-yasseros.sh

# Or use the logging build script (timestamps in log)
./scripts/build-with-logging.sh
# Check logs/build-*.log for stage timings
```

## Reference Build Times (Expected)

Based on pi-gen documentation and community reports:

| Environment               | Clean Build | Cached Build |
|--------------------------|-------------|--------------|
| Modern PC (8-core, Docker)  | 20–30 min   | 8–12 min     |
| MacBook Pro M2 (Docker)     | 25–40 min   | 10–15 min    |
| GitHub Actions (2-core)     | 45–70 min   | 20–30 min    |
| Raspberry Pi 4 (native)     | 3–5 hours   | (not practical) |

## Stage Timing Breakdown (Approximate)

| Stage          | Duration  |
|---------------|-----------|
| stage0 (bootstrap) | 3–5 min  |
| stage1 (base)      | 5–8 min  |
| stage2 (lite)      | 5–10 min |
| stage-yasseros     | 5–15 min |
| image export       | 3–5 min  |
| xz compression     | 5–10 min |

## Performance Notes

- First build always takes longer (no apt cache)
- Subsequent builds are faster if `pi-gen/work/` directory is preserved
- `CLEAN=1` forces full rebuild (same as first build time)
- Docker on macOS is ~30% slower than Linux due to filesystem overhead
