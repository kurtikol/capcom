# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TaskPulse
class Color:
    """ANSI color codes with optional disable."""

    _codes = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "dim": "\033[2m",
        "underline": "\033[4m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "hidden": "\033[8m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }

    @classmethod
    def off(cls):
        cls._disabled = True
        cls._codes["reset"] = ""
        for k, v in list(cls._codes.items()):
            cls._codes[k] = ""
        return cls

    @classmethod
    def on(cls):
        cls._disabled = False
        for k, v in list(cls._codes.items()):
            if k == "reset":
                continue
            cls._codes[k] = f"\033[{v}"
        return cls

    def __getattr__(self, name):
        if name.startswith("_") or name not in self._codes:
            raise AttributeError(name)
        if self._disabled:
            return ""
        return self._codes[name]

    def __call__(self, *args, **kwargs):
        if self._disabled:
            return ""
        return f"{self._codes['reset']}{self._codes['bold']}" if "bold" in self._codes else self._codes['bold']
