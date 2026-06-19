# Boot Branding Validation Checklist

## Plymouth Theme

```bash
plymouth-get-default-theme
```

- [ ] Returns `yasseros`

```bash
ls /usr/share/plymouth/themes/yasseros/
```

- [ ] `yasseros.plymouth` present
- [ ] `yasseros.script` present
- [ ] `assets/` directory present

```bash
cat /etc/plymouth/plymouthd.conf
```

- [ ] `Theme=yasseros`
- [ ] `ShowDelay=0`

## Boot Visual

- [ ] Boot shows Deep Space (#0D1117) background — not the default Raspberry Pi OS rainbow
- [ ] YasserBlue (#4493F8) progress bar visible at ~82% screen height
- [ ] No Raspberry Pi logo or coloured bars visible
- [ ] Status messages appear in Snow (#E6EDF3) below the progress bar

## LightDM Greeter

```bash
cat /etc/lightdm/lightdm-gtk-greeter.conf
```

- [ ] `background=` points to `/usr/share/yasseros/wallpapers/yasseros-default-1920.png`
- [ ] `icon-theme-name=Papirus-Dark`
- [ ] `clock-format=%H:%M`

- [ ] Login screen shows YasserOS wallpaper (not default Raspberry Pi OS background)
- [ ] Clock is displayed in 24h format

## LightDM Session Config

```bash
cat /etc/lightdm/lightdm.conf.d/50-yasseros.conf
```

- [ ] `user-session=xfce`

## Initramfs

```bash
lsinitramfs /boot/initrd.img-$(uname -r) | grep plymouth
```

- [ ] Plymouth binaries present in initramfs
- [ ] `yasseros.script` present in initramfs
