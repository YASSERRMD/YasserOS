# YasserOS Color Palette

## Primary Palette

| Role            | Name       | Hex      | RGB              | Usage                              |
|----------------|-----------|----------|------------------|------------------------------------|
| Background     | Deep Space | #0D1117  | 13, 17, 23       | Desktop background, dark UI areas  |
| Surface        | Midnight   | #161B22  | 22, 27, 34       | Panel, window chrome               |
| Surface Raised | Carbon     | #21262D  | 33, 38, 45       | Cards, sidebar items               |
| Border         | Graphite   | #30363D  | 48, 54, 61       | Dividers, borders                  |
| Primary Text   | Snow       | #E6EDF3  | 230, 237, 243    | Primary readable text              |
| Secondary Text | Mist       | #8B949E  | 139, 148, 158    | Secondary, placeholder text        |

## Accent Colours

| Role           | Name       | Hex      | RGB              | Usage                              |
|---------------|-----------|----------|------------------|------------------------------------|
| Primary Accent | YasserBlue | #4493F8 | 68, 147, 248     | Buttons, links, active states      |
| Success        | Mint       | #3FB950  | 63, 185, 80      | Success indicators, confirmations  |
| Warning        | Amber      | #D29922  | 210, 153, 34     | Warnings, attention needed         |
| Error          | Ruby       | #F85149  | 248, 81, 73      | Errors, destructive actions        |
| Highlight      | Violet     | #A371F7  | 163, 113, 247    | Special UI highlights, branding    |

## Dark Mode (Default)

YasserOS defaults to dark mode. The palette above is designed for dark mode.

Dark mode configuration in XFCE: based on Greybird-dark or a custom GTK theme using the palette above.

## Light Mode (Optional)

Light mode variant (for users who prefer it):

| Role           | Hex      | Notes                      |
|---------------|----------|----------------------------|
| Background     | #FFFFFF  | Pure white                  |
| Surface        | #F6F8FA  | GitHub-light style          |
| Surface Raised | #EAEEF2  |                             |
| Primary Text   | #24292F  |                             |
| Secondary Text | #57606A  |                             |
| Primary Accent | #0969DA  | Darker blue for light bg    |

## Gradient

The YasserOS brand gradient (used in wallpaper and splash):

```
Linear gradient: 135°
  From: #0D1117 (Deep Space)
  Via:  #1C2333 (Space Blue)
  To:   #21262D (Carbon)
```

Accent gradient (for highlights, optional):
```
Linear gradient: 135°
  From: #4493F8 (YasserBlue)
  To:   #A371F7 (Violet)
```

## Colour Accessibility

Text contrast ratios (dark mode):
- Snow on Deep Space: 15.3:1 (AAA — excellent)
- Mist on Deep Space: 4.6:1 (AA — acceptable)
- YasserBlue on Deep Space: 4.7:1 (AA — acceptable for UI elements)

## CSS Variables (for GTK / web contexts)

```css
:root {
  --yas-bg: #0D1117;
  --yas-surface: #161B22;
  --yas-surface-raised: #21262D;
  --yas-border: #30363D;
  --yas-text-primary: #E6EDF3;
  --yas-text-secondary: #8B949E;
  --yas-accent: #4493F8;
  --yas-success: #3FB950;
  --yas-warning: #D29922;
  --yas-error: #F85149;
  --yas-violet: #A371F7;
}
```
