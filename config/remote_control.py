"""
remote_control — fail-safe remote alert module for CLI tools.

Fetches public CDN config and applies startup/exit actions.
Any failure is a silent no-op so the host CLI never crashes.
"""

from __future__ import annotations

import re
import sys
import time
import webbrowser
from urllib.parse import urlsplit

__all__ = ["RemoteControl", "valid_url", "CDN_URL"]

CDN_URL = "https://cdn.vritrasec.com/cli-remote-config/config.json"
MAX_SIZE = 1024 * 1024
DEFAULT_TIMEOUT = 5
# Pause after printing so the user can actually read the line.
DEFAULT_MESSAGE_DELAY = 1.5

# Quick reject for garbage / accidental text in the url field.
URL_PATTERN = re.compile(r"^https://[^\s<>'\"\\]+$", re.IGNORECASE)


def valid_url(value):
    """Return True only for a clean, credential-free HTTPS URL."""
    if not isinstance(value, str) or not value:
        return False

    if not URL_PATTERN.fullmatch(value):
        return False

    try:
        parsed = urlsplit(value)
    except ValueError:
        return False

    if parsed.scheme.lower() != "https":
        return False

    if not parsed.hostname:
        return False

    if parsed.username is not None or parsed.password is not None:
        return False

    if parsed.port is not None and parsed.port <= 0:
        return False

    return True


def _strict_bool(value, expected):
    """True only when value is exactly the boolean `expected`."""
    return value is expected


class RemoteControl:
    """
    Workflow
    --------
    1. Interactive mode only (no inline flags / -v / -h style usage).
    2. Fetch CDN JSON once.
    3. master_enable must be True — otherwise do nothing.
    4. If global.enable is True  → use global rules (ignore all tools).
       If global.enable is False → use tools[tool_id] when that tool is enabled.
    5. Per event (startup / exit):
         show_message True → print message
         startup only → brief read delay after message
         open_url True + valid HTTPS url → open browser
    """

    def __init__(
        self,
        tool_id,
        interactive=None,
        timeout=DEFAULT_TIMEOUT,
        allow_browser=True,
        debug=False,
        cdn_url=CDN_URL,
        message_delay=DEFAULT_MESSAGE_DELAY,
    ):
        self.tool_id = tool_id if isinstance(tool_id, str) else ""
        self.interactive = (
            self._detect_interactive()
            if interactive is None
            else bool(interactive)
        )
        self.timeout = self._safe_timeout(timeout)
        self.allow_browser = bool(allow_browser)
        self.debug = bool(debug)
        self.cdn_url = cdn_url if isinstance(cdn_url, str) and cdn_url else CDN_URL
        self.message_delay = self._safe_delay(message_delay)

        self._loaded = False
        self._rules = None

    @staticmethod
    def _detect_interactive():
        # Only bare launch (script name alone) counts as interactive.
        # Any -v / -h / inline flag means argv length > 1 → skip remote actions.
        try:
            return len(sys.argv) == 1
        except Exception:
            return False

    @staticmethod
    def _safe_timeout(value):
        try:
            timeout = float(value)
        except (TypeError, ValueError):
            return DEFAULT_TIMEOUT

        if timeout <= 0 or timeout > 120:
            return DEFAULT_TIMEOUT

        return timeout

    @staticmethod
    def _safe_delay(value):
        try:
            delay = float(value)
        except (TypeError, ValueError):
            return DEFAULT_MESSAGE_DELAY

        # Allow 0 (no pause) up to a few seconds.
        if delay < 0 or delay > 10:
            return DEFAULT_MESSAGE_DELAY

        return delay

    def _log(self, message):
        if not self.debug:
            return
        try:
            print(f"[RemoteControl] {message}", file=sys.stderr)
        except Exception:
            pass

    # ------------------------------------------------------------------ load

    def _load(self):
        """Fetch + resolve rules once. Never raises."""
        if self._loaded:
            return

        self._loaded = True
        self._rules = None

        try:
            self._load_unsafe()
        except Exception as exc:
            self._rules = None
            self._log(f"Load aborted: {exc}")

    def _load_unsafe(self):
        if not self.interactive:
            self._log("Non-interactive: skipped")
            return

        if not self.tool_id:
            self._log("Empty tool_id: skipped")
            return

        config = self._fetch_config()
        if config is None:
            return

        # 1. Master switch — sole source of truth for "show anything at all"
        if not _strict_bool(config.get("master_enable"), True):
            self._log("Master OFF or invalid — no actions")
            return

        # 2. Global section required and well-formed enough to decide
        global_rules = config.get("global")
        if not isinstance(global_rules, dict):
            self._log("Invalid global section — no actions")
            return

        global_enable = global_rules.get("enable")

        # 3a. Global ON → ignore every tool, use global rules only
        if _strict_bool(global_enable, True):
            self._rules = global_rules
            self._log("Using GLOBAL rules")
            return

        # 3b. Global must be explicitly False to fall through to tools
        if not _strict_bool(global_enable, False):
            self._log("Invalid global.enable — no actions")
            return

        # 4. Per-tool rules
        tools = config.get("tools")
        if not isinstance(tools, dict):
            self._log("Invalid tools section — no actions")
            return

        tool = tools.get(self.tool_id)
        if not isinstance(tool, dict):
            self._log(f"Tool missing: {self.tool_id}")
            return

        if not _strict_bool(tool.get("enable"), True):
            self._log(f"Tool OFF: {self.tool_id}")
            return

        self._rules = tool
        self._log(f"Using TOOL rules: {self.tool_id}")

    def _fetch_config(self):
        """GET CDN JSON. Returns dict or None. Never raises."""
        try:
            import requests
        except ImportError as exc:
            self._log(f"requests not available: {exc}")
            return None

        try:
            response = requests.get(
                self.cdn_url,
                headers={
                    "Accept": "application/json",
                    "Cache-Control": "no-cache",
                },
                timeout=self.timeout,
            )
        except Exception as exc:
            self._log(f"CDN request failed: {exc}")
            return None

        try:
            status = int(getattr(response, "status_code", 0) or 0)
        except Exception:
            status = 0

        if status != 200:
            self._log(f"CDN HTTP {status}")
            return None

        try:
            raw = response.content
        except Exception as exc:
            self._log(f"CDN body read failed: {exc}")
            return None

        if not isinstance(raw, (bytes, bytearray)):
            self._log("CDN body is not bytes")
            return None

        if len(raw) == 0:
            self._log("CDN body empty")
            return None

        if len(raw) > MAX_SIZE:
            self._log("CDN JSON exceeds size limit")
            return None

        try:
            config = response.json()
        except Exception as exc:
            self._log(f"CDN JSON parse failed: {exc}")
            return None

        if not isinstance(config, dict):
            self._log("CDN JSON root is not an object")
            return None

        return config

    # ---------------------------------------------------------------- events

    def _event(self, name):
        """Apply one startup/exit event. Never raises."""
        try:
            self._event_unsafe(name)
        except Exception as exc:
            self._log(f"{name} aborted: {exc}")

    def _event_unsafe(self, name):
        self._load()

        if self._rules is None:
            return

        event = self._rules.get(name)
        if not isinstance(event, dict):
            self._log(f"Invalid {name} section")
            return

        self._apply_message(event, name)
        self._apply_url(event, name)

    def _apply_message(self, event, name):
        if not _strict_bool(event.get("show_message"), True):
            self._log(f"{name} message skipped")
            return

        message = event.get("message")
        if not isinstance(message, str):
            self._log(f"{name} message invalid type")
            return

        try:
            print(message, flush=True)
        except Exception as exc:
            self._log(f"{name} print failed: {exc}")
            return

        # Read pause only on startup — exit should leave immediately.
        if name == "startup" and self.message_delay > 0:
            try:
                time.sleep(self.message_delay)
            except Exception as exc:
                self._log(f"{name} message delay skipped: {exc}")

    def _apply_url(self, event, name):
        if not _strict_bool(event.get("open_url"), True):
            self._log(f"{name} url open skipped (flag off)")
            return

        if not self.allow_browser:
            self._log(f"{name} url open skipped (browser disabled)")
            return

        url = event.get("url")
        if not valid_url(url):
            self._log(f"{name} url open skipped (invalid url)")
            return

        try:
            opened = webbrowser.open(url, new=2)
            self._log(f"{name} browser opened: {opened}")
        except Exception as exc:
            self._log(f"{name} browser error: {exc}")

    # ---------------------------------------------------------------- public

    def startup(self):
        self._event("startup")

    def exit(self):
        self._event("exit")

    def __enter__(self):
        self.startup()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.exit()
        except Exception:
            pass
        return False
