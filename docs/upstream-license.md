# Upstream License Reference

## pi-gen License

pi-gen is distributed under the **BSD 3-Clause License**.

Full license text: https://github.com/RPi-Distro/pi-gen/blob/master/LICENSE

```
BSD 3-Clause License

Copyright (c) 2015, 2016, 2017 Raspberry Pi (Trading) Ltd.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its contributors
  may be used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## YasserOS License

YasserOS uses the same **BSD 3-Clause License** as pi-gen to maintain license compatibility.

The YasserOS LICENSE file is in the repository root.

## Raspberry Pi OS (the built image)

The Raspberry Pi OS images built by pi-gen contain software under various open-source licenses:
- Linux kernel: GPL-2.0
- Debian packages: Mixed (GPL, LGPL, MIT, BSD, etc.)
- Raspberry Pi firmware: Proprietary (Broadcom) — redistributable

See the Raspberry Pi Foundation's license documentation for the built OS:
https://www.raspberrypi.com/about/legal/

## Yasser Control Center License

Yasser Control Center (in `yasser-control-center/`) is original work by YASSERRMD and is released under the BSD 3-Clause License.

## Custom Assets (Wallpapers, Logos)

Custom visual assets in `assets/` are original work by YASSERRMD. License: All Rights Reserved (personal project, not licensed for redistribution).

## License Compliance

When adding new packages to `stage-yasseros/00-packages`, verify that:
1. The package license is compatible with redistribution
2. The license is noted in the package list comment (for non-standard licenses)
3. Proprietary or copyleft packages are flagged for review

For a personal hobby OS, this is informal tracking only — but it's good practice.
