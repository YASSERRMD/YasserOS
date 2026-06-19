# Developer Workspace

YasserOS ships a curated set of developer tools pre-installed on every image so
you can start coding immediately after first boot.

## Package List

The following packages are added via `stage-yasseros/00-packages`:

| Package         | Purpose                                                    |
|-----------------|------------------------------------------------------------|
| `build-essential` | GCC, G++, make — everything needed to compile C/C++ code |
| `git`           | Version control (usually already in Raspberry Pi OS base) |
| `python3-venv`  | Create isolated Python virtual environments               |
| `python3-pip`   | Install Python packages from PyPI                         |
| `nano`          | Simple terminal text editor                               |
| *(micro)*       | Modern terminal editor — not in standard repos; install manually |

## Installing micro

`micro` is not in the standard Debian repos. Install it manually:

```bash
curl https://getmic.ro | bash
sudo mv micro /usr/local/bin/
```

## Developer Tools Page

The **Developer Tools** page in Yasser Control Center shows the installation
status of common dev tools at a glance, grouped by category:

- **Compilers & Build Tools** — gcc, make, build-essential
- **Version Control** — git
- **Python Tools** — python3, pip3, virtualenv
- **Editors** — nano, micro, vim

## Adding More Tools

To add more packages to the base image, edit `stage-yasseros/00-packages` and
rebuild the image with pi-gen.
