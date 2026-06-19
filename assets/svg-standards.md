# SVG Standards

## Source File Requirements

All SVG source files in `assets/` must:

1. **Use viewBox** (not fixed width/height) for scalability:
   ```xml
   <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
   ```

2. **Use named colours** from the brand palette (not inline hex):
   Define colours as CSS variables or named elements at the top:
   ```xml
   <defs>
     <style>
       .bg { fill: #0D1117; }
       .accent { fill: #4493F8; }
     </style>
   </defs>
   ```

3. **Flatten layers before export** — no hidden layers, no artboards

4. **Optimise SVG** — remove editor metadata, comments, unused definitions:
   ```bash
   svgo input.svg -o output-optimised.svg
   ```

5. **Name elements** with descriptive IDs:
   ```xml
   <path id="y-left-arm" .../>
   <path id="y-stem" .../>
   ```

## Wallpaper SVG Specifics

- viewBox: `0 0 1920 1080` (or proportional)
- No raster images embedded in wallpaper SVG
- Use SVG gradients for the background:
  ```xml
  <defs>
    <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0D1117"/>
      <stop offset="100%" style="stop-color:#21262D"/>
    </linearGradient>
  </defs>
  ```

## Icon SVG Specifics

- viewBox: `0 0 48 48`
- Minimum stroke width: 2px at 48×48
- All paths closed and filled (no open strokes in final icon)
- Test at 16×16 — must remain recognisable

## Editing Tools

Recommended: **Inkscape** (open source, Debian: `sudo apt install inkscape`)

Acceptable: Any SVG editor that produces clean, standard SVG output.

Do NOT use: Tools that produce proprietary extensions or embed raster images unnecessarily.
