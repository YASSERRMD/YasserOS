# Branding Governance

## Overview

This document defines how branding decisions are made, documented, and maintained in YasserOS.

## Governance Model

YasserOS is a solo project. Branding "governance" is therefore a personal decision framework to prevent:
- Inconsistent visual identity across the OS
- Undocumented design decisions that are hard to revisit
- Scope creep into branding work that delays functional work

## Branding Decision Hierarchy

```
1. ADR (Architecture Decision Record)   ← highest authority
   For: major brand direction changes (new logo, palette change, etc.)

2. branding/ documents                  ← specifications
   For: detailed specifications that implement ADR decisions

3. stage-yasseros/files/               ← implementation
   For: actual files deployed into the OS image

4. Commit messages                      ← change log
   For: tracking what changed and when
```

## When to Write a Branding ADR

Create an ADR (in `docs/adr/`) for:
- Changing the primary colour palette
- Choosing a different icon theme
- Changing the desktop environment (e.g., XFCE → KDE)
- Choosing a logo design
- Changing the typography system

Do NOT create an ADR for:
- Minor colour adjustments (update the palette spec instead)
- Adding a new wallpaper variant
- Updating icon sizes

## Branding Change Process

1. **Identify the change** — what visual element is changing?
2. **Check existing specs** — does a specification already cover this?
3. **Update the spec** — revise the relevant branding/ document
4. **Create ADR if major** — record the decision rationale
5. **Implement in stage-yasseros** — apply the change to the actual image files
6. **Validate visually** — boot the image and check the result

## Design Freeze

During the Phase 1–20 build period, the branding is **in specification mode** (documents define intent) not **in implementation mode** (files actually deployed). Branding specifications can change freely.

After Phase 20, branding changes should be:
- Intentional (reviewed against the branding documents)
- Incremental (don't redesign everything at once)
- Validated (boot and check before committing)

## Asset Ownership

| Asset Type          | Owner (Directory)      | Sign-off Required |
|--------------------|------------------------|-------------------|
| Logo               | `assets/logos/`        | ADR               |
| Colour palette     | `branding/color-palette.md` | ADR if major change |
| Wallpapers         | `assets/wallpapers/`   | None (creative freedom) |
| Icon theme choice  | `branding/icon-requirements.md` | ADR      |
| Font choice        | `branding/typography-specification.md` | ADR if changed |
| Boot splash design | `branding/` + `stage-yasseros/` | ADR     |

## Anti-patterns to Avoid

- **Do not** change the colour palette without updating `color-palette.md`
- **Do not** install a new icon theme without updating `icon-requirements.md`
- **Do not** use a different logo variant in different places (use the specs)
- **Do not** make branding changes without testing on the actual OS
