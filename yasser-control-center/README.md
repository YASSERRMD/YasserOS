# Yasser Control Center

A GTK4/libadwaita system management app for YasserOS.

## Technology Stack

| Component   | Technology                  |
|------------|------------------------------|
| UI toolkit  | GTK 4 + libadwaita           |
| Language    | Python 3.11+                 |
| Bindings    | PyGObject (gi.repository)    |
| Settings    | JSON file (~/.config/yasser-control-center/settings.json) |

## Running (development)

```bash
# From the repo root
cd yasser-control-center
./ycc
```

Requirements: `python3-gi`, `gir1.2-gtk-4.0`, `gir1.2-adw-1`

```bash
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1
```

## Architecture

```
yasser-control-center/
├── ycc                     ← launch script
├── src/yasser_control_center/
│   ├── __init__.py         ← version, app ID
│   ├── main.py             ← Adw.Application subclass
│   ├── window.py           ← Adw.ApplicationWindow + navigation
│   ├── settings.py         ← JSON settings persistence
│   ├── logging_config.py   ← logging setup
│   ├── pages/
│   │   ├── about.py        ← About YasserOS page (Phase 18)
│   │   └── system_info.py  ← System information page (Phase 19)
│   └── providers/
│       └── system.py       ← CPU/memory/storage/network providers (Phase 19)
└── tests/
```

## Modules

| Module          | Phase | Purpose                                          |
|----------------|-------|--------------------------------------------------|
| `about.py`      | 18    | YasserOS version, hobby disclaimer, vision       |
| `system_info.py`| 19    | Live CPU, memory, storage, network stats         |

## App ID

`com.yasseros.ControlCenter`
