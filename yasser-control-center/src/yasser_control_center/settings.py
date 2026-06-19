"""Application settings model backed by GSettings or a plain JSON fallback."""

import json
import os
from pathlib import Path


_CONFIG_DIR = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "yasser-control-center"
_CONFIG_FILE = _CONFIG_DIR / "settings.json"

_DEFAULTS = {
    "theme": "system",
    "refresh_interval_seconds": 5,
    "show_hostname_in_titlebar": True,
}


class Settings:
    def __init__(self):
        self._data = dict(_DEFAULTS)
        self._load()

    def _load(self):
        if _CONFIG_FILE.exists():
            try:
                with _CONFIG_FILE.open() as f:
                    self._data.update(json.load(f))
            except (json.JSONDecodeError, OSError):
                pass

    def save(self):
        _CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with _CONFIG_FILE.open("w") as f:
            json.dump(self._data, f, indent=2)

    def get(self, key: str):
        return self._data.get(key, _DEFAULTS.get(key))

    def set(self, key: str, value):
        self._data[key] = value
        self.save()


# Module-level singleton
_settings = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
