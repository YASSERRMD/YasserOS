#!/bin/bash -e
# stage-yasseros: 01-run-chroot.sh
# Runs INSIDE the chroot (as if running on the Pi itself).
# Used for: systemctl, update-alternatives, user config, etc.

log() { echo "[stage-yasseros:run-chroot.sh] $1"; }

log "Starting stage-yasseros chroot-side setup"

# --- Desktop Environment Setup ---

# Set LightDM as the display manager
if command -v lightdm >/dev/null 2>&1; then
    log "Enabling LightDM display manager"
    systemctl enable lightdm
fi

# Set XFCE as the default desktop session for LightDM
log "Configuring default session to XFCE"
cat > /etc/lightdm/lightdm.conf.d/50-yasseros.conf << 'EOF'
[Seat:*]
user-session=xfce
EOF

# --- Networking ---

# Enable NetworkManager
if systemctl is-enabled NetworkManager 2>/dev/null | grep -q "disabled"; then
    log "Enabling NetworkManager"
    systemctl enable NetworkManager
fi

# Disable wpa_supplicant (NetworkManager manages Wi-Fi)
systemctl disable wpa_supplicant 2>/dev/null || true

# --- User Configuration ---

# Create user home directories
log "Setting up user home structure"
if id yasser >/dev/null 2>&1; then
    install -d -o yasser -g yasser /home/yasser/Desktop
    install -d -o yasser -g yasser /home/yasser/Documents
    install -d -o yasser -g yasser /home/yasser/Downloads
    install -d -o yasser -g yasser /home/yasser/Pictures
fi

# --- Icon and Theme Defaults ---

# Set Papirus-Dark as the default icon theme system-wide
log "Setting default icon theme"
mkdir -p /etc/gtk-3.0
cat > /etc/gtk-3.0/settings.ini << 'EOF'
[Settings]
gtk-icon-theme-name = Papirus-Dark
gtk-font-name = Cantarell 10
gtk-cursor-theme-name = Adwaita
EOF

# --- Audio ---

# Enable PulseAudio
if command -v pulseaudio >/dev/null 2>&1; then
    log "PulseAudio present — will autostart for user sessions"
fi

# --- First Boot Service ---

log "Installing YasserOS first-boot service"
systemctl enable yasseros-firstboot 2>/dev/null || log "First-boot service not yet installed (Phase 17)"

# --- Cleanup ---

log "Cleaning up apt caches"
apt-get clean
rm -rf /var/lib/apt/lists/*

log "Stage-yasseros chroot setup complete"
