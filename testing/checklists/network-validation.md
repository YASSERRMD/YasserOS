# Network Validation Checklist

## Prerequisites

Raspberry Pi 4 connected to network via Ethernet or Wi-Fi.

## Ethernet Connectivity

```bash
ip link show eth0
ip addr show eth0
```
- [ ] `eth0` interface is present and UP
- [ ] IP address assigned (DHCP or static)

```bash
ping -c 3 192.168.1.1  # or your router IP
```
- [ ] Router is reachable (local network)

## DNS Resolution

```bash
ping -c 3 google.com
nslookup google.com
```
- [ ] DNS resolution works
- [ ] `google.com` resolves to IP addresses

## Internet Connectivity

```bash
curl -s https://httpbin.org/get | head -5
```
- [ ] HTTPS requests succeed
- [ ] TLS certificate validation works

## Network Manager (Phase 15+)

```bash
systemctl status NetworkManager
nmcli general status
```
- [ ] `NetworkManager` service is active
- [ ] General status shows "connected"

```bash
nmcli device status
```
- [ ] Ethernet device shows "connected"
- [ ] Wi-Fi device shows "disconnected" (expected if not configured)

## Wi-Fi Module

```bash
ip link show wlan0
rfkill list
```
- [ ] `wlan0` interface present
- [ ] Wi-Fi is not blocked by rfkill (soft block may be present — expected)

## APT Repository Access

```bash
sudo apt update
```
- [ ] Reaches `archive.raspberrypi.com` (Raspberry Pi OS repo)
- [ ] Reaches `deb.debian.org` (Debian repo)
- [ ] No repository errors

## SSH Access (if ENABLE_SSH=1 in config)

```bash
# From another machine:
ssh yasser@yasseros.local
```
- [ ] mDNS resolves `yasseros.local`
- [ ] SSH connects successfully
- [ ] Password authentication works

## Hostname Resolution

```bash
hostname
hostname -I
avahi-daemon --check 2>/dev/null && echo "mDNS running"
```
- [ ] `hostname` returns `yasseros` or `yasseros-XXXX`
- [ ] `hostname -I` returns IP address(es)
- [ ] mDNS is running (Avahi service)
