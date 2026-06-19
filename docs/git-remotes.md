# Git Remote Configuration

## YasserOS Repository Remotes

### origin — YasserOS GitHub Repository

```bash
git remote add origin https://github.com/YASSERRMD/YasserOS.git
```

| Property | Value                                       |
|---------|---------------------------------------------|
| Name     | origin                                      |
| URL      | https://github.com/YASSERRMD/YasserOS.git  |
| Purpose  | Primary remote — push/pull YasserOS code    |

### pi-gen Submodule Remote

The pi-gen submodule has its own remote configuration:

```bash
# Inside pi-gen/
git remote -v
# origin https://github.com/RPi-Distro/pi-gen.git
```

This is managed automatically by git submodule. Do not change the submodule remote.

## Cloning YasserOS (Fresh Setup)

```bash
# Clone YasserOS with submodules
git clone --recurse-submodules https://github.com/YASSERRMD/YasserOS.git

# Or clone then initialise submodules
git clone https://github.com/YASSERRMD/YasserOS.git
cd YasserOS
git submodule update --init --recursive
```

## Remote Verification

```bash
# Verify YasserOS remotes
git remote -v

# Expected output:
# origin  https://github.com/YASSERRMD/YasserOS.git (fetch)
# origin  https://github.com/YASSERRMD/YasserOS.git (push)

# Verify pi-gen submodule state
git submodule status
# Expected: <hash> pi-gen (heads/master)
```

## Git Config for This Repository

```bash
git config user.name "YASSERRMD"
git config user.email "arafath.yasser@gmail.com"
```

These should match the commit author on all YasserOS commits.
