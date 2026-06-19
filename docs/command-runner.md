# Command Runner

The Command Runner page in Yasser Control Center lets you execute a curated set of
read-only system commands directly from the UI without opening a full terminal.

## Safe Command Whitelist

Only commands whose prefix appears in the whitelist below are permitted.
Any other input is rejected and the user is directed to open a terminal.

| Command prefix          | Purpose                          |
|-------------------------|----------------------------------|
| `df`                    | Disk usage                       |
| `free`                  | Memory usage                     |
| `uptime`                | System uptime and load           |
| `uname`                 | Kernel / OS information          |
| `lscpu`                 | CPU details                      |
| `lsusb`                 | Connected USB devices            |
| `lspci`                 | Connected PCI devices            |
| `ip`                    | Network interface information    |
| `hostname`              | System hostname                  |
| `whoami`                | Current user                     |
| `cat /proc/version`     | Kernel version string            |
| `cat /proc/cpuinfo`     | Detailed CPU information         |
| `cat /etc/os-release`   | OS release metadata              |
| `systemctl status`      | Systemd unit status              |
| `journalctl -n 20`      | Last 20 system log lines         |

## Command Log

Every command run through the Command Runner (whether successful or not) is
appended to:

```
~/.cache/ycc/commands.log
```

Each entry includes a timestamp, a status tag (`OK` or `ERROR`), the command
text, and the full output.

## Terminal Fallback

The **Open Terminal** button at the bottom of the page launches `xfce4-terminal`
for users who need to run commands outside the whitelist.
