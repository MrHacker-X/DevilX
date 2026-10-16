#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevilX v2.0 - Multi-Toolkit Security & Information Gathering Framework
Author  : MrHacker-X
Website : https://vritrasec.com
License : Boost Software License 1.0
"""

import argparse
import hashlib
import http.client
import json
import os
import re
import secrets
import shutil
import socket
import string
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import webbrowser

try:
    import requests
except ImportError:
    requests = None

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    from colorama import Fore, Style, init as colorama_init
except ImportError:
    Fore = Style = colorama_init = None

__version__ = "2.3"

# ============================================================
#  Appearance - muted house palette
# ============================================================


def _supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if not sys.stdout.isatty():
        return False
    return os.environ.get("TERM") != "dumb"


try:
    HAVE_COLORAMA = colorama_init is not None
except NameError:
    HAVE_COLORAMA = False

COLOR = _supports_color() and HAVE_COLORAMA

if COLOR:
    colorama_init()  # enables ANSI escape handling on Windows

WH = Style.BRIGHT + Fore.WHITE if COLOR else ""
YL = Fore.LIGHTYELLOW_EX if COLOR else ""
GR = Fore.LIGHTGREEN_EX if COLOR else ""
DM = Style.DIM + Fore.WHITE if COLOR else ""
RD = Fore.LIGHTRED_EX if COLOR else ""
XX = Style.RESET_ALL if COLOR else ""


def _c(token: str, text: str) -> str:
    return f"{token}{text}{XX}" if token else text

PROG = os.path.basename(sys.argv[0]) or "devilx.py"
RULE = "─" * 62

EXIT_WORDS = {"q", "quit", "exit", "back"}
EXIT_HINT = "q to go back"


class SafeExit(Exception):
    """Raised when the user backs out of a prompt (EOF or exit keyword)."""


# ============================================================
#  UI helpers
# ============================================================


def rule():
    print(_c(DM, RULE))


def header(text: str):
    print()
    rule()
    print(_c(YL, f"  {text}"))
    rule()


def kv(key: str, val: str, width: int = 22):
    print(f"  {_c(YL, key.ljust(width))}{_c(WH, str(val))}")


def item(num: str, label: str, desc: str = "", numw: int = 2):
    """Render a menu row - option label only; desc is accepted but not shown."""
    numcell = f"[{num}]".ljust(numw + 2)
    print(f"  {numcell} {_c(WH, label)}")


def say(text: str):
    print(f"  {_c(GR, '›')} {_c(WH, text)}")


def note(text: str):
    print(f"  {_c(DM, '·')} {_c(DM, text)}")


def err(text: str):
    print(f"  {_c(RD, '✗')} {_c(RD, text)}")


def warn(text: str):
    print(f"  {_c(YL, '!')} {_c(YL, text)}")


def ok(text: str):
    print(f"  {_c(GR, '✓')} {_c(GR, text)}")


def _clear():
    if sys.stdout.isatty():
        os.system("clear" if os.name != "nt" else "cls")


def ask(prompt: str, *, allow_empty: bool = False) -> str:
    """Prompt for a value. Empty input re-prompts unless allow_empty."""
    while True:
        print()
        try:
            raw = input(f"  {_c(YL, '?')} {_c(WH, prompt)}: ")
        except EOFError:
            raise SafeExit
        except KeyboardInterrupt:
            raise SafeExit
        val = raw.strip()
        if val.lower() in EXIT_WORDS:
            raise SafeExit
        if val or allow_empty:
            return val
        err("a value is required - type q to go back")


def confirm(prompt: str, *, default: bool = False) -> bool:
    try:
        raw = input(f"  {_c(YL, '?')} {_c(WH, prompt)} {_c(DM, '[y/N]' if not default else '[Y/n]')}: ")
    except (EOFError, KeyboardInterrupt):
        raise SafeExit
    val = raw.strip().lower()
    if not val:
        return default
    return val in ("y", "yes")


def pause(msg: str = "press enter to continue"):
    try:
        input(f"\n  {_c(DM, msg)}")
    except (EOFError, KeyboardInterrupt):
        raise SafeExit


# ============================================================
#  Block-letter wordmark (no ASCII-art escape hazards)
# ============================================================

_BLOCK_FONT = {
    "A": ["█▀█", "█▀█", "▀ ▀"],
    "B": ["██▄", "██▀", "▀▀▀"],
    "C": ["█▀▀", "█  ", "▀▀▀"],
    "D": ["█▄▀", "█ █", "▀▀▀"],
    "E": ["█▀▀", "█▀ ", "▀▀▀"],
    "F": ["█▀▀", "█▀ ", "▀  "],
    "G": ["█▀▀", "█ █", "▀▀▀"],
    "H": ["█ █", "█▀█", "▀ ▀"],
    "I": ["█", "█", "▀"],
    "J": [" █", " █", "▀▀"],
    "K": ["█ █", "██ ", "▀ ▀"],
    "L": ["█  ", "█  ", "▀▀▀"],
    "M": ["█▄█", "█ █", "▀ ▀"],
    "N": ["█▄ █", "█ ▀█", "▀  ▀"],
    "O": ["█▀█", "█ █", "▀▀▀"],
    "P": ["█▀█", "██▀", "▀  "],
    "Q": ["█▀█", "█▄█", "  ▀"],
    "R": ["█▀█", "██ ", "▀ ▀"],
    "S": ["█▀▀", "▀▀█", "▀▀▀"],
    "T": ["▀█▀", " █ ", " ▀ "],
    "U": ["█ █", "█ █", "▀▀▀"],
    "V": ["█ █", "█ █", " ▀ "],
    "W": ["█ █", "█▄█", "▀ ▀"],
    "X": ["█ █", " █ ", "▀ ▀"],
    "Y": ["█ █", " █ ", " ▀ "],
    "Z": ["▀▀█", " █ ", "▀▀▀"],
    " ": ["  ", "  ", "  "],
}


def _wordmark_rows(word: str) -> list:
    rows = ["", "", ""]
    for ch in word.upper():
        glyph = _BLOCK_FONT.get(ch, _BLOCK_FONT[" "])
        for i in range(3):
            rows[i] += glyph[i] + " "
    # keep uniform width (no per-row rstrip) so centering stays aligned
    return rows


BANNER_WIDTH = 62  # matches RULE - the whole header lives on one axis


def _center(text: str, width: int = BANNER_WIDTH) -> str:
    return text.center(width)


def banner():
    print()
    for row in _wordmark_rows("DEVILX"):
        print(_c(YL, _center(row)))
    print()
    print(_c(WH, _center("Multi-Toolkit Security & Information Gathering Framework")))
    print(_c(DM, _center("v2.0  ·  vritrasec.com")))
    print()
    print(_c(DM, RULE))
    print(_c(RD, _center("⚠  AUTHORIZED USE ONLY")))
    print(_c(DM, _center("audit systems you own or have written permission to test")))


# ============================================================
#  Networking helpers
# ============================================================


def _have(module) -> bool:
    return module is not None


class _Resp:
    """Uniform minimal HTTP response - the same shape from both backends."""

    __slots__ = ("status", "text", "content")

    def __init__(self, status: int, text: str, content: bytes):
        self.status = status
        self.text = text
        self.content = content


def http_get(url: str, timeout: float = 10.0):
    """GET via requests when available, else urllib.

    Always returns a _Resp (with .status, .text, .content) or None -
    never a raw requests.Response, never a bare string.
    """
    if _have(requests):
        try:
            r = requests.get(url, timeout=timeout, headers={"User-Agent": "DevilX/2.0"})
            return _Resp(r.status_code, r.text, r.content)
        except requests.RequestException:
            return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "DevilX/2.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            return _Resp(resp.status, raw.decode("utf-8", errors="replace"), raw)
    except Exception:
        return None


def _ensure_requests():
    if not _have(requests):
        err("the 'requests' package is required for this module - pip install requests")
        pause()
        return False
    return True


# ============================================================
#  Category 1 - Security Audit
# ============================================================

STRENGTH_TIERS = [
    (28, "critical", RD),
    (40, "weak", RD),
    (56, "fair", YL),
    (72, "good", GR),
    (10 ** 9, "strong", GR),
]


def _entropy_bits(pw: str) -> float:
    import math
    pool = 0
    if re.search(r"[a-z]", pw):
        pool += 26
    if re.search(r"[A-Z]", pw):
        pool += 26
    if re.search(r"[0-9]", pw):
        pool += 10
    if re.search(r"[^a-zA-Z0-9]", pw):
        pool += 33
    if pool == 0:
        return 0.0
    return len(pw) * math.log2(pool)


def _strength_report(pw: str):
    bits = _entropy_bits(pw)
    for threshold, label, col in STRENGTH_TIERS:
        if bits < threshold:
            break
    bar_len = 24
    filled = min(bar_len, int(bits / 100 * bar_len) + (1 if bits > 0 else 0))
    bar = "█" * filled + "░" * (bar_len - filled)
    pools = []
    if re.search(r"[a-z]", pw):
        pools.append("lower")
    if re.search(r"[A-Z]", pw):
        pools.append("upper")
    if re.search(r"[0-9]", pw):
        pools.append("digit")
    if re.search(r"[^a-zA-Z0-9]", pw):
        pools.append("symbol")
    print()
    kv("length", len(pw))
    kv("charset pool", " + ".join(pools) or "none")
    kv("entropy", f"{bits:.1f} bits")
    kv("strength", _c(col, label))
    print(f"  {_c(YL, 'meter'.ljust(22))}{_c(col, bar)}")


def _pwned_password_count(sha1: str):
    prefix, suffix = sha1[:5], sha1[5:].upper()
    resp = http_get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if resp is None or resp.status != 200:
        return None
    for line in resp.text.splitlines():
        parts = line.strip().split(":")
        if len(parts) == 2 and parts[0] == suffix:
            return int(parts[1])
    return 0


def audit_password():
    header("SECURITY AUDIT - PASSWORD")
    if not _ensure_requests():
        return
    pw = ask("password to audit (input hidden after entry)")
    if len(pw) < 4:
        warn("password too short to audit meaningfully")
        pause()
        return
    _strength_report(pw)
    note("querying HaveIBeenPwned via k-anonymity - the password itself is never sent")
    import hashlib as _hl
    sha1 = _hl.sha1(pw.encode()).hexdigest().upper()
    count = _pwned_password_count(sha1)
    print()
    if count is None:
        err("network unavailable - could not reach api.pwnedpasswords.com")
    elif count == 0:
        ok("not found in any known breach corpus - good")
    else:
        err(f"found {count:,} time(s) in known breaches - do NOT use this password")
    pause()


def _flatten_xon_breaches(data: dict) -> list:
    """XposedOrNot returns breaches as [["Name", ...]] - flatten defensively."""
    breaches = data.get("breaches") or []
    if breaches and isinstance(breaches[0], (list, tuple)):
        flat = []
        for group in breaches:
            flat.extend(group)
        return flat
    return list(breaches)


def audit_email_hibp():
    """Keyless email breach lookup via the XposedOrNot public API."""
    header("SECURITY AUDIT - EMAIL EXPOSURE")
    email = ask("email address")
    if "@" not in email or "." not in email.split("@")[-1]:
        err("that does not look like a valid email address")
        pause()
        return
    note("querying a keyless breach database - the address is sent as part of the lookup")
    resp = http_get("https://api.xposedornot.com/v1/check-email/" + urllib.parse.quote(email))
    print()
    if resp is None:
        err("network unavailable - could not reach api.xposedornot.com")
        pause()
        return
    if resp.status != 200:
        detail = ""
        try:
            detail = " - " + json.loads(resp.text).get("message", "")
        except (ValueError, AttributeError):
            pass
        warn(f"lookup refused (HTTP {resp.status}){detail} - address may be clean or service busy")
        pause()
        return
    try:
        data = json.loads(resp.text)
    except (ValueError, TypeError):
        warn("unparseable response - treating as no data")
        pause()
        return
    breaches = _flatten_xon_breaches(data)
    if not breaches:
        ok("no known breaches reference this address")
    else:
        warn(f"{len(breaches)} breach(es) found")
        for name in breaches[:12]:
            note(str(name))
        if len(breaches) > 12:
            note(f"… and {len(breaches) - 12} more")
        extra = http_get("https://api.xposedornot.com/v1/breach-analytics?email=" + urllib.parse.quote(email))
        if extra is not None and extra.status == 200:
            try:
                strength = json.loads(extra.text)["BreachMetrics"]["passwords_strength"][0]
                easy = strength.get("EasyToCrack", 0)
                plain = strength.get("PlainText", 0)
                strong = strength.get("StrongHash", 0)
                kv("password storage", f"{plain} plaintext · {easy} easy-to-crack · {strong} strong hash", 28)
            except (ValueError, KeyError, TypeError, IndexError):
                pass
    pause()


def check_iban(iban: str):
    s = re.sub(r"\s+", "", iban).upper()
    if not re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}", s):
        return False, "format invalid"
    reordered = s[4:] + s[:4]
    digits = "".join(str(int(ch, 36)) for ch in reordered)
    try:
        if int(digits) % 97 != 1:
            return False, "checksum failed (mod-97)"
    except ValueError:
        return False, "invalid characters"
    return True, "valid (mod-97 checksum passed)"


def check_email_syntax_mx(email: str):
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return False, "syntax invalid", False
    domain = email.split("@")[-1]
    mx_ok = False
    try:
        import dns.resolver  # optional
        answers = dns.resolver.resolve(domain, "MX")
        mx_ok = bool(answers)
    except ImportError:
        try:
            socket.getaddrinfo(domain, 25)
            mx_ok = True
        except socket.gaierror:
            mx_ok = False
    except Exception:
        mx_ok = False
    return True, "syntax valid", mx_ok


def check_phone_basic(phone: str):
    digits = re.sub(r"[^\d+]", "", phone)
    if digits.startswith("+"):
        core = digits[1:]
    else:
        core = digits
    if not core.isdigit():
        return False, "contains invalid characters"
    if not (7 <= len(core) <= 15):
        return False, f"length {len(core)} outside E.164 range (7-15)"
    return True, f"plausible E.164 number (+{core})"


def validators_menu():
    while True:
        _clear()
        banner()
        header("INFORMATION GATHERING - VALIDATORS")
        item("1", "Email validator", "syntax + domain MX lookup")
        item("2", "Phone validator", "E.164 format plausibility")
        item("3", "IBAN validator", "mod-97 checksum, fully offline")
        item("0", "Back")
        try:
            ch = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}")
            ch = ch.strip().lower()
        except (EOFError, KeyboardInterrupt):
            raise SafeExit
        if ch == "0":
            return
        if ch.isdigit() and ch != "0":
            ch = ch.zfill(2)
        try:
            if ch == "01":
                email = ask("email address")
                valid, msg, mx = check_email_syntax_mx(email)
                print()
                kv("syntax", "valid" if valid else "invalid")
                kv("domain MX", _c(GR, "reachable") if mx else _c(RD, "not reachable"))
                if not mx:
                    warn("domain does not accept mail - address is likely fake")
            elif ch == "02":
                phone = ask("phone number (with country code)")
                good, msg = check_phone_basic(phone)
                print()
                (ok if good else err)(msg)
            elif ch == "03":
                iban = ask("IBAN")
                good, msg = check_iban(iban)
                print()
                (ok if good else err)(msg)
            else:
                continue
        except SafeExit:
            return
        pause()


# ============================================================
#  Category 2 - Web Scraping
# ============================================================


def scrape_page():
    header("WEB SCRAPING - PAGE ANALYSIS")
    if not _ensure_requests() or BeautifulSoup is None:
        err("the 'beautifulsoup4' package is required - pip install beautifulsoup4")
        pause()
        return
    url = ask("page URL (include http:// or https://)")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    note(f"fetching {url}")
    resp = http_get(url)
    if resp is None:
        err("request failed - check the URL and your connection")
        pause()
        return
    if resp.status != 200:
        warn(f"server returned HTTP {resp.status} - parsing anyway")
    text = resp.text
    print()
    kv("status", resp.status)
    kv("size", f"{len(text):,} bytes")
    soup = BeautifulSoup(text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else "(none)"
    kv("title", title[:60])
    links = soup.find_all("a", href=True)
    forms = soup.find_all("form")
    imgs = soup.find_all("img", src=True)
    scripts = soup.find_all("script", src=True)
    print()
    kv("links", len(links))
    kv("forms", len(forms))
    kv("images", len(imgs))
    kv("external js", len(scripts))
    emails = sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)))
    if emails:
        print()
        say(f"{len(emails)} email(s) found in page")
        for e in emails[:10]:
            note(e)
    out = ask("save full HTML to file? enter a filename (or press enter to skip)", allow_empty=True)
    if out:
        try:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(text)
            ok(f"saved to {out}")
        except OSError as exc:
            err(f"could not save: {exc}")
    pause()


def clone_site():
    header("WEB SCRAPING - PAGE CLONE")
    if not _ensure_requests():
        return
    url = ask("page URL to clone")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    name = ask("output directory name", allow_empty=True) or "cloned_page"
    note(f"fetching {url}")
    resp = http_get(url)
    if resp is None:
        err("request failed - check the URL and your connection")
        pause()
        return
    if resp.status != 200:
        warn(f"server returned HTTP {resp.status} - saving anyway")
    html = resp.text
    os.makedirs(name, exist_ok=True)
    page_path = os.path.join(name, "index.html")
    with open(page_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    count = 0
    for match in re.findall(r'(?:src|href)=["\']([^"\']+\.(?:css|js|png|jpe?g|gif|svg|ico|webp))["\']', html, re.I):
        asset_url = urllib.parse.urljoin(url, match)
        local = os.path.basename(urllib.parse.urlparse(asset_url).path) or f"asset_{count}"
        if os.path.exists(os.path.join(name, local)):
            count += 1
            continue
        data = http_get(asset_url)
        if data is None:
            continue
        raw = data.content
        try:
            with open(os.path.join(name, local), "wb") as fh:
                fh.write(raw)
            count += 1
        except OSError:
            continue
    print()
    ok(f"cloned page + {count} asset(s) into ./{name}/")
    pause()


# ============================================================
#  Category 3 - Information Gathering
# ============================================================


def trace_ip():
    header("INFORMATION GATHERING - IP TRACE")
    target = ask("IP address or domain", allow_empty=True)
    query = target or ""
    if query:
        if not re.fullmatch(r"[\w.:-]+", query):
            err("invalid target")
            pause()
            return
    data = http_get("http://ip-api.com/json/" + urllib.parse.quote(query) + "?fields=66846719")
    if data is None:
        err("lookup failed - network unreachable or rate-limited")
        pause()
        return
    if data.status != 200:
        err(f"ip-api returned HTTP {data.status}")
        pause()
        return
    try:
        info = json.loads(data.text)
    except ValueError:
        err("unparseable response from ip-api.com")
        pause()
        return
    if info.get("status") != "success":
        err(info.get("message", "lookup failed"))
        pause()
        return
    print()
    for label, key in (("ip", "query"), ("country", "country"), ("region", "regionName"),
                       ("city", "city"), ("zip", "zip"), ("timezone", "timezone"),
                       ("isp", "isp"), ("org", "org"), ("as", "as")):
        if info.get(key):
            kv(label, info[key])
    if info.get("lat") and info.get("lon"):
        kv("map", f"https://www.google.com/maps?q={info['lat']},{info['lon']}")
    pause()


def info_menu():
    while True:
        _clear()
        banner()
        header("INFORMATION GATHERING")
        item("1", "IP / domain trace", "geo, ISP, ASN via ip-api.com")
        item("2", "Email validator", "syntax + MX reachability")
        item("3", "Phone validator", "E.164 plausibility check")
        item("4", "IBAN validator", "mod-97 checksum, offline")
        item("0", "Back")
        try:
            ch = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}")
            ch = ch.strip().lower()
        except (EOFError, KeyboardInterrupt):
            raise SafeExit
        if ch == "0":
            return
        if ch.isdigit() and ch != "0":
            ch = ch.zfill(2)
        try:
            if ch == "01":
                trace_ip()
            elif ch == "02":
                validators_menu_email()
            elif ch == "03":
                phone = ask("phone number (with country code)")
                good, msg = check_phone_basic(phone)
                print()
                (ok if good else err)(msg)
                pause()
            elif ch == "04":
                iban = ask("IBAN")
                good, msg = check_iban(iban)
                print()
                (ok if good else err)(msg)
                pause()
            elif ch == "9":
                _about()
        except SafeExit:
            return


def validators_menu_email():
    email = ask("email address")
    valid, msg, mx = check_email_syntax_mx(email)
    print()
    kv("syntax", "valid" if valid else "invalid")
    kv("domain MX", _c(GR, "reachable") if mx else _c(RD, "not reachable"))
    if not mx:
        warn("domain does not accept mail - address is likely fake")
    pause()


# ============================================================
#  Category 4 - Hash Cracking (dictionary)
# ============================================================

HASH_LENGTHS = {32: "md5", 40: "sha1", 56: "sha224", 64: "sha256", 96: "sha384", 128: "sha512"}

WORDLIST_CANDIDATES = [
    os.path.join("config", "wordlist", "wordlist.txt"),
    os.path.join("data", "wordlist.txt"),
    "/usr/share/wordlists/rockyou.txt",
]


def _find_wordlist() -> str:
    for path in WORDLIST_CANDIDATES:
        if os.path.isfile(path):
            return path
    return ""


def crack_hash():
    header("HASH CRACKING - DICTIONARY ATTACK")
    target = ask("hash to crack")
    algo = HASH_LENGTHS.get(len(target.strip()))
    wordlist = _find_wordlist()
    if not wordlist:
        err("no wordlist found - place one at config/wordlist/wordlist.txt")
        pause()
        return
    custom = ask(f"wordlist (enter for default: {wordlist})", allow_empty=True)
    if custom:
        if not os.path.isfile(custom):
            err(f"wordlist not found: {custom}")
            pause()
            return
        wordlist = custom
    else:
        note("default wordlist selected")
    if algo is None:
        algo = ask("algorithm (md5/sha1/sha224/sha256/sha384/sha512/sha3_256)", allow_empty=False).lower()
        if not hasattr(hashlib, algo):
            err(f"unsupported algorithm: {algo}")
            pause()
            return
    else:
        note(f"auto-detected algorithm: {algo} ({len(target.strip())} hex chars)")
    target = target.strip().lower()
    started = time.time()
    tried = 0
    found = None
    try:
        with open(wordlist, "r", errors="ignore") as fh:
            for line in fh:
                word = line.rstrip("\r\n")
                tried += 1
                try:
                    if hashlib.new(algo, word.encode()).hexdigest() == target:
                        found = word
                        break
                except (ValueError, TypeError):
                    continue
    except OSError as exc:
        err(f"cannot read wordlist: {exc}")
        pause()
        return
    elapsed = time.time() - started
    print()
    if found is not None:
        ok(f"cracked after {tried:,} tries in {elapsed:.2f}s")
        kv("plaintext", found)
    else:
        err(f"exhausted {tried:,} candidate(s) in {elapsed:.2f}s - no match")
    pause()


# ============================================================
#  Category 5 - Password Generator
# ============================================================


def generate_passwords():
    header("PASSWORD GENERATOR")
    length = ask("length (enter for 16)", allow_empty=True)
    length = int(length) if length.isdigit() and 4 <= int(length) <= 256 else 16
    count = ask("how many (enter for 5)", allow_empty=True)
    count = int(count) if count.isdigit() and 1 <= int(count) <= 100 else 5
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.?/"
    print()
    generated = []
    for _ in range(count):
        pw = "".join(secrets.choice(alphabet) for _ in range(length))
        generated.append(pw)
        say(pw)
    if confirm("save to file?"):
        fname = ask("filename", allow_empty=True) or "devilx_passwords.txt"
        try:
            with open(fname, "w", encoding="utf-8") as fh:
                fh.write("\n".join(generated) + "\n")
            ok(f"saved to {fname}")
        except OSError as exc:
            err(f"could not save: {exc}")
    pause()


# ============================================================
#  Category 6 - Tool Installer (curated, verified catalog)
# ============================================================

# install types: git  -> shallow clone + optional install script
#                apt  -> package manager
#                pip  -> python package
TOOLS = [
    # -- Recon & scanners
    {"name": "ScannerX", "repo": "https://github.com/MrHacker-X/ScannerX", "type": "git", "cat": "recon"},
    {"name": "InfoGX", "repo": "https://github.com/MrHacker-X/InfoGX", "type": "git", "cat": "recon"},
    {"name": "IPFindX (ex-TraceX)", "repo": "https://github.com/MrHacker-X/IPFindX", "type": "git", "cat": "recon"},
    {"name": "LocatorX (ex-TraceX-GUI)", "repo": "https://github.com/MrHacker-X/LocatorX", "type": "git", "cat": "recon"},
    {"name": "seeker", "repo": "https://github.com/thewhiteh4t/seeker", "type": "git", "cat": "recon"},
    {"name": "RED_HAWK", "repo": "https://github.com/Tuhinshubhra/RED_HAWK", "type": "git", "cat": "recon"},
    {"name": "nmap", "repo": "nmap", "type": "apt", "cat": "recon"},
    {"name": "nikto", "repo": "https://github.com/sullo/nikto", "type": "git", "cat": "recon"},
    {"name": "BruteX", "repo": "https://github.com/1N3/BruteX", "type": "git", "cat": "recon"},
    {"name": "userfinder", "repo": "https://github.com/machine1337/userfinder", "type": "git", "cat": "recon"},
    {"name": "httpfy", "repo": "https://github.com/devXprite/httpfy", "type": "git", "cat": "recon"},
    {"name": "ipdrone", "repo": "https://github.com/noob-hackers/ipdrone", "type": "git", "cat": "recon"},
    {"name": "IP Rover", "repo": "https://github.com/Cyber-Dioxide/IP_Rover", "type": "git", "cat": "recon"},
    # -- Web exploitation
    {"name": "sqlmap", "repo": "sqlmap", "type": "apt", "cat": "web"},
    {"name": "SploitX", "repo": "https://github.com/MrHacker-X/SploitX", "type": "git", "cat": "web"},
    {"name": "fsociety", "repo": "https://github.com/Manisso/fsociety", "type": "git", "cat": "web"},
    {"name": "slowloris", "repo": "https://github.com/gkbrk/slowloris", "type": "git", "cat": "web"},
    {"name": "CloneWeb", "repo": "https://github.com/MrHacker-X/CloneWeb", "type": "git", "cat": "web"},
    {"name": "DirAttack", "repo": "https://github.com/Ranginang67/DirAttack", "type": "git", "cat": "web"},
    {"name": "M-dork", "repo": "https://github.com/Ranginang67/M-dork", "type": "git", "cat": "web"},
    {"name": "websploit", "repo": "https://github.com/f4rih/websploit", "type": "git", "cat": "web"},
    {"name": "MyServer", "repo": "https://github.com/rajkumardusad/MyServer", "type": "git", "cat": "web"},
    {"name": "Xteam", "repo": "https://github.com/xploitstech/Xteam", "type": "git", "cat": "web"},
    {"name": "Hacked", "repo": "https://github.com/MrHacker-X/Hacked", "type": "git", "cat": "web"},
    # -- OSINT & social
    {"name": "Osintgram", "repo": "https://github.com/Datalux/Osintgram", "type": "git", "cat": "osint"},
    {"name": "osi.ig", "repo": "https://github.com/th3unkn0n/osi.ig", "type": "git", "cat": "osint"},
    {"name": "TeleGram-Scraper", "repo": "https://github.com/th3unkn0n/TeleGram-Scraper", "type": "git", "cat": "osint"},
    {"name": "SocialBox-Termux", "repo": "https://github.com/samsesh/SocialBox-Termux", "type": "git", "cat": "osint"},
    {"name": "PassX", "repo": "https://github.com/MrHacker-X/PassX", "type": "git", "cat": "osint"},
    {"name": "DecodeX", "repo": "https://github.com/MrHacker-X/DecodeX", "type": "git", "cat": "osint"},
    {"name": "Cracker-Tool", "repo": "https://github.com/cracker911181/Cracker-Tool", "type": "git", "cat": "osint"},
    {"name": "Gmail-Hack", "repo": "https://github.com/Zard2007/Gmail-Hack", "type": "git", "cat": "osint"},
    {"name": "GH05T-INSTA", "repo": "https://github.com/GH05T-HUNTER5/GH05T-INSTA", "type": "git", "cat": "osint"},
    {"name": "TORhunter", "repo": "https://github.com/Err0r-ICA/TORhunter", "type": "git", "cat": "osint"},
    # -- Phishing (authorized testing)
    {"name": "saycheese", "repo": "https://github.com/MrHacker-X/saycheese", "type": "git", "cat": "phish"},
    {"name": "maskphish", "repo": "https://github.com/jaykali/maskphish", "type": "git", "cat": "phish"},
    {"name": "mrphish", "repo": "https://github.com/noob-hackers/mrphish", "type": "git", "cat": "phish"},
    {"name": "seeker (alt)", "repo": "https://github.com/thewhiteh4t/seeker", "type": "git", "cat": "phish", "skip": True},
    # -- Payloads & post-exploitation
    {"name": "thc-hydra", "repo": "https://github.com/vanhauser-thc/thc-hydra", "type": "git", "cat": "post"},
    {"name": "Traper-X", "repo": "https://github.com/MrHacker-X/Traper-X", "type": "git", "cat": "post"},
    {"name": "Venomsploit", "repo": "https://github.com/Err0r-ICA/Venomsploit", "type": "git", "cat": "post"},
    {"name": "h-sploit-paylod", "repo": "https://github.com/jarvis-8520/h-sploit-paylod", "type": "git", "cat": "post"},
    {"name": "Asura", "repo": "https://github.com/princekrvert/Asura", "type": "git", "cat": "post"},
    {"name": "HXP-Ducky", "repo": "https://github.com/hackerxphantom/HXP-Ducky", "type": "git", "cat": "post"},
    {"name": "DVR-Exploiter", "repo": "https://github.com/Cyb0r9/DVR-Exploiter", "type": "git", "cat": "post"},
    {"name": "CAM-DUMPER", "repo": "https://github.com/LiNuX-Mallu/CAM-DUMPER", "type": "git", "cat": "post"},
    {"name": "termux-fingerprint", "repo": "https://github.com/MrHacker-X/termux-fingerprint", "type": "git", "cat": "post"},
    # -- Utility & anonymity
    {"name": "tunnel", "repo": "https://github.com/noob-hackers/tunnel", "type": "git", "cat": "util"},
    {"name": "termux-key", "repo": "https://github.com/tahmidrayat/termux-key", "type": "git", "cat": "util"},
    {"name": "Pycompile", "repo": "https://github.com/tahmidrayat/Pycompile", "type": "git", "cat": "util"},
    {"name": "termux-snippets", "repo": "https://github.com/mukeshkumarcharak/termux-snippets", "type": "git", "cat": "util"},
    {"name": "Tool-X", "repo": "https://github.com/ekadanuarta/Tool-X", "type": "git", "cat": "util"},
    {"name": "onex", "repo": "https://github.com/jackind424/onex", "type": "git", "cat": "util"},
    {"name": "toolss", "repo": "https://github.com/AnonHackerr/toolss", "type": "git", "cat": "util"},
    {"name": "WannaTool", "repo": "https://github.com/Err0r-ICA/WannaTool", "type": "git", "cat": "util"},
    {"name": "EasY_HaCk", "repo": "https://github.com/sabri-zaki/EasY_HaCk", "type": "git", "cat": "util"},
    {"name": "AllHackingTools", "repo": "https://github.com/mishakorzik/AllHackingTools", "type": "git", "cat": "util"},
    {"name": "AdminHack", "repo": "https://github.com/mishakorzik/AdminHack", "type": "git", "cat": "util"},
    {"name": "Dh-All", "repo": "https://github.com/DH-AL/Dh-All", "type": "git", "cat": "util"},
    {"name": "bannerX", "repo": "https://github.com/MrHacker-X/BannerX", "type": "git", "cat": "util"},
    {"name": "LinuxX", "repo": "https://github.com/MrHacker-X/LinuxX", "type": "git", "cat": "util"},
    {"name": "tstyle", "repo": "https://github.com/htr-tech/tstyle", "type": "git", "cat": "util"},
    {"name": "qurxin", "repo": "https://github.com/fikrado/qurxin", "type": "git", "cat": "util"},
    {"name": "jarvis-welcome", "repo": "https://github.com/AmshenShanu07/jarvis-welcome", "type": "git", "cat": "util"},
    {"name": "termux-desktop", "repo": "https://github.com/adi1090x/termux-desktop", "type": "git", "cat": "util"},
    {"name": "TermuxArch", "repo": "https://github.com/TermuxArch/TermuxArch", "type": "git", "cat": "util"},
    {"name": "modded-ubuntu", "repo": "https://github.com/modded-ubuntu/modded-ubuntu", "type": "git", "cat": "util"},
    {"name": "parrot-in-termux", "repo": "https://github.com/risecid/parrot-in-termux", "type": "git", "cat": "util"},
    {"name": "Termux-heroku-cli", "repo": "https://github.com/SKGHD/Termux-heroku-cli", "type": "git", "cat": "util"},
    {"name": "infect", "repo": "https://github.com/noob-hackers/infect", "type": "git", "cat": "util"},
    {"name": "hacklock", "repo": "https://github.com/noob-hackers/hacklock", "type": "git", "cat": "util"},
    {"name": "seeu", "repo": "https://github.com/noob-hackers/seeu", "type": "git", "cat": "util"},
    {"name": "kalimux", "repo": "https://github.com/noob-hackers/kalimux", "type": "git", "cat": "util"},
    {"name": "DarkFly", "repo": "https://github.com/Ranginang67/DarkFly-2019.1", "type": "git", "cat": "util"},
    {"name": "beyawak", "repo": "https://github.com/Ranginang67/beyawak", "type": "git", "cat": "util"},
    {"name": "Hackerwasi", "repo": "https://github.com/evildevill/Hackerwasi", "type": "git", "cat": "util"},
    {"name": "instahack", "repo": "https://github.com/evildevill/instahack", "type": "git", "cat": "util"},
    {"name": "pureblood", "repo": "https://github.com/cr4shcod3/pureblood", "type": "git", "cat": "util"},
    {"name": "007-TheBond", "repo": "https://github.com/Deadshot0x7/007-TheBond", "type": "git", "cat": "util"},
    {"name": "DefGen", "repo": "https://github.com/Err0r-ICA/DefGen", "type": "git", "cat": "util"},
    {"name": "Viridae", "repo": "https://github.com/Err0r-ICA/Viridae", "type": "git", "cat": "util"},
    {"name": "TermuxCyberArmy", "repo": "https://github.com/Err0r-ICA/TermuxCyberArmy", "type": "git", "cat": "util"},
    {"name": "GenVirus", "repo": "https://github.com/sowmiksudo/GenVirus", "type": "git", "cat": "util"},
    {"name": "B4Bomber", "repo": "https://github.com/mahendraplus/B4Bomber", "type": "git", "cat": "util"},
    {"name": "Beast_Bomber", "repo": "https://github.com/un1cum/Beast_Bomber", "type": "git", "cat": "util"},
    {"name": "WhSms", "repo": "https://github.com/cyberboyplas/WhSms", "type": "git", "cat": "util"},
    {"name": "Mega-File-Stealer", "repo": "https://github.com/ZechBron/Mega-File-Stealer", "type": "git", "cat": "util"},
    {"name": "AOXdeface", "repo": "https://github.com/Ranginang67/AOXdeface", "type": "git", "cat": "util"},
    {"name": "demozz", "repo": "https://github.com/demoza/demozz", "type": "git", "cat": "util"},
    {"name": "Hammer", "repo": "https://github.com/rk1342k/Hammer", "type": "git", "cat": "util"},
]

INSTALL_ROOT = os.path.join(os.path.expanduser("~"), "DevilX-tools")


def _pkg_cmd() -> str:
    """Detect the platform package manager binary."""
    if shutil.which("apt") or shutil.which("apt-get"):
        return "apt" if shutil.which("apt") else "apt-get"
    for pm in ("dnf", "yum", "pacman", "zypper", "apk"):
        if shutil.which(pm):
            return pm
    return ""


def _sudo_prefix() -> list:
    if os.geteuid() == 0:
        return []
    if os.name == "nt":
        return []
    return ["sudo"] if shutil.which("sudo") else []


def install_tool(entry: dict) -> bool:
    name = entry["name"]
    ttype = entry["type"]
    dest = os.path.join(INSTALL_ROOT, re.sub(r"[^\w.-]", "_", name))
    print()
    if ttype == "git":
        if os.path.exists(dest):
            warn(f"{name} already cloned at {dest} - pulling latest")
            cmd = ["git", "-C", dest, "pull"]
        else:
            os.makedirs(INSTALL_ROOT, exist_ok=True)
            cmd = ["git", "clone", "--depth", "1", entry["repo"], dest]
        say(" ".join(cmd))
        code = subprocess.call(cmd)
        if code != 0:
            err(f"clone/update failed for {name}")
            return False
        for marker in ("install.sh", "setup.sh"):
            marker_path = os.path.join(dest, marker)
            if os.path.isfile(marker_path):
                if confirm(f"run {marker} for {name}?"):
                    subprocess.call(["bash", marker_path], cwd=dest)
                break
        ok(f"{name} ready at {dest}")
        return True
    if ttype == "apt":
        pm = _pkg_cmd()
        if not pm:
            err("no supported package manager found (apt/dnf/yum/pacman/zypper/apk)")
            return False
        cmd = [pm, "install", "-y" if pm not in ("zypper",) else "-n", entry["repo"]]
        if pm in ("apt", "apt-get"):
            cmd = _sudo_prefix() + ["apt-get", "update"] if False else [pm, "install", "-y", entry["repo"]]
            cmd = _sudo_prefix() + cmd
        elif pm in ("dnf", "yum"):
            cmd = _sudo_prefix() + [pm, "install", "-y", entry["repo"]]
        elif pm == "pacman":
            cmd = _sudo_prefix() + [pm, "-S", "--noconfirm", entry["repo"]]
        elif pm == "zypper":
            cmd = _sudo_prefix() + [pm, "install", "-y", entry["repo"]]
        elif pm == "apk":
            cmd = _sudo_prefix() + [pm, "add", entry["repo"]]
        say(" ".join(cmd))
        code = subprocess.call(cmd)
        if code != 0:
            err(f"package install failed for {name}")
            return False
        ok(f"{name} installed via {pm}")
        return True
    if ttype == "pip":
        code = subprocess.call([sys.executable, "-m", "pip", "install", "--user", entry["repo"]])
        if code != 0:
            err(f"pip install failed for {name}")
            return False
        ok(f"{name} installed via pip --user")
        return True
    err(f"unknown install type: {ttype}")
    return False


def tools_menu():
    while True:
        _clear()
        banner()
        header("TOOL INSTALLER - CURATED CATALOG")
        cats = ["recon", "web", "osint", "phish", "post", "util", "all"]
        for i, cat in enumerate(cats, 1):
            n = sum(1 for t in TOOLS if t["cat"] == cat and not t.get("skip")) if cat != "all" else sum(1 for t in TOOLS if not t.get("skip"))
            labels = {"recon": "Recon & scanners", "web": "Web exploitation", "osint": "OSINT & social",
                      "phish": "Phishing (authorized testing)", "post": "Payloads & post-exploitation",
                      "util": "Utility & environment", "all": "Show full catalog"}
            item(str(i), labels[cat], f"{n} tool(s)")
        item("0", "Back")
        try:
            ch = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}")
            ch = ch.strip().lower()
        except (EOFError, KeyboardInterrupt):
            raise SafeExit
        if ch == "0":
            return
        if ch.isdigit() and ch != "0":
            ch = ch.zfill(2)
        try:
            if ch == "07":
                print()
                for i, t in enumerate([t for t in TOOLS if not t.get("skip")], 1):
                    print(f"  {_c(DM, str(i).rjust(3))}  {_c(WH, t['name'].ljust(26))}{_c(DM, t['type'] + '  ' + t['repo'])}")
                print()
                pick = ask("tool number to install (enter to go back)", allow_empty=True)
                if pick and pick.isdigit():
                    sel = [t for t in TOOLS if not t.get("skip")]
                    if 1 <= int(pick) <= len(sel):
                        install_tool(sel[int(pick) - 1])
                pause()
                continue
            if ch in ("01", "02", "03", "04", "05", "06"):
                cat = cats[int(ch) - 1]
                sel = [t for t in TOOLS if t["cat"] == cat and not t.get("skip")]
                print()
                for i, t in enumerate(sel, 1):
                    print(f"  {_c(DM, str(i).rjust(3))}  {_c(WH, t['name'].ljust(26))}{_c(DM, t['type'] + '  ' + t['repo'])}")
                print()
                pick = ask("tool number to install (enter to go back)", allow_empty=True)
                if pick and pick.isdigit():
                    if 1 <= int(pick) <= len(sel):
                        install_tool(sel[int(pick) - 1])
                pause()
        except SafeExit:
            return


# ============================================================
#  Category 7 - Web Info (browser-based OSINT launcher)
# ============================================================

WEBINFO_WAVES = [
    ("Domain intelligence", [
        ("VirusTotal relations", "https://www.virustotal.com/gui/domain/{d}/relations"),
        ("crt.sh certificates", "https://crt.sh/?q=%25.{d}"),
        ("Riddler pld search", "https://riddler.io/search?q=pld:{d}"),
        ("Riddler host search", "https://riddler.io/search?q=host:{d}"),
        ("Riddler keyword", "https://riddler.io/search?q=keyword%3A{d}&view_type=data_table"),
        ("FindSubdomains", "https://findsubdomains.com/subdomains-of/{d}"),
        ("DNS table", "https://dnstable.com/domain/{d}"),
        ("SecurityTrails apex", "https://securitytrails.com/list/apex_domain/{d}"),
        ("CertSpotter certs", "https://certspotter.com/api/v0/certs?domain={d}"),
        ("Google site:*", "https://www.google.com/search?q=site:*.{d}"),
        ("Google site:*.*", "https://www.google.com/search?q=site:*.*.{d}"),
    ]),
    ("Port, DNS & WHOIS", [
        ("ViewDNS portscan", "https://viewdns.info/portscan/?host={d}"),
        ("ViewDNS dnsreport", "https://viewdns.info/dnsreport/?domain={d}"),
        ("ViewDNS reverse whois", "http://viewdns.info/reversewhois/?q={d}"),
        ("ViewDNS whois", "https://viewdns.info/whois/?domain={d}"),
        ("DNSlytics domain", "https://dnslytics.com/domain/{d}"),
    ]),
    ("Headers & tech stack", [
        ("ThreatCrowd domain", "https://www.threatcrowd.org/domain.php?domain={d}"),
        ("SecurityHeaders", "https://securityheaders.com/?q={d}&followRedirects=on"),
        ("ViewDNS httpheaders", "https://viewdns.info/httpheaders/?domain={d}"),
        ("BuiltWith stack", "https://builtwith.com/{d}"),
    ]),
]


def webinfo_menu():
    while True:
        _clear()
        banner()
        header("WEB INFO - BROWSER OSINT LAUNCHER")
        note("one wave at a time · each URL opens in your browser after confirmation")
        for i, (wave_name, links) in enumerate(WEBINFO_WAVES, 1):
            item(str(i), wave_name, f"{len(links)} source(s)")
        item("0", "Back")
        try:
            ch = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}")
            ch = ch.strip().lower()
        except (EOFError, KeyboardInterrupt):
            raise SafeExit
        if ch == "0":
            return
        if ch.isdigit() and ch != "0":
            ch = ch.zfill(2)
        if not (ch in ("01", "02", "03")):
            continue
        try:
            domain = ask("target domain (e.g. example.com)")
            if "/" in domain or " " in domain or "." not in domain:
                err("enter a bare domain like example.com")
                pause()
                continue
            wave_name, links = WEBINFO_WAVES[int(ch) - 1]
            say(f"wave: {wave_name} - {len(links)} source(s)")
            for label, pattern in links:
                url = pattern.format(d=urllib.parse.quote(domain))
                if not confirm(f"open {label}?"):
                    note(f"skipped {label}")
                    continue
                webbrowser.open(url)
                ok(f"opened {label}")
                time.sleep(0.4)
        except SafeExit:
            return
        pause()


# ============================================================
#  About / doctor / version
# ============================================================


def _about():
    header("ABOUT DEVILX")
    kv("version", __version__)
    kv("author", "MrHacker-X")
    kv("website", "https://vritrasec.com")
    kv("network", "https://link.vritrasec.com")
    kv("license", "Boost Software License 1.0")
    print()
    say("DevilX bundles auditing, scraping, OSINT, hash-cracking, password")
    say("generation and a curated installer for 89 verified third-party tools.")
    print()
    warn("run only against systems you own or are authorized to test.")


def run_doctor():
    header("DOCTOR - ENVIRONMENT CHECK")
    checks = []

    def chk(label, good, detail=""):
        checks.append((label, good, detail))
        if good:
            ok(f"{label} - {detail}" if detail else label)
        else:
            err(f"{label} - {detail}" if detail else label)

    ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    chk("python 3.8+", sys.version_info >= (3, 8), ver)
    chk("requests", _have(requests), "installed" if _have(requests) else "pip install requests")
    chk("beautifulsoup4", BeautifulSoup is not None, "installed" if BeautifulSoup else "pip install beautifulsoup4")
    chk("colorama", HAVE_COLORAMA, "installed" if HAVE_COLORAMA else "pip install colorama")
    chk("git", shutil.which("git") is not None, shutil.which("git") or "not found")
    wl = _find_wordlist()
    chk("wordlist", bool(wl), wl or "config/wordlist/wordlist.txt missing")
    pw = os.path.join("config", "password", "pass.txt")
    chk("password list", os.path.isfile(pw), pw if os.path.isfile(pw) else "missing")
    pm = _pkg_cmd()
    chk("package manager", bool(pm), pm or "none detected")
    try:
        conn = http.client.HTTPSConnection("api.pwnedpasswords.com", timeout=5)
        conn.request("HEAD", "/range/AAAAA")
        resp = conn.getresponse()
        conn.close()
        chk("network (api.pwnedpasswords.com)", resp.status < 500, f"HTTP {resp.status}")
    except Exception as exc:
        chk("network (api.pwnedpasswords.com)", False, str(exc)[:50])
    print()
    good = sum(1 for _, g, _ in checks if g)
    kv("summary", f"{good}/{len(checks)} checks passed")
    pause()


# ============================================================
#  Main
# ============================================================


def main_menu_screen():
    print()
    header("MAIN MENU")
    item("1", "Security Audit", "breach & password checks")
    item("2", "Web Scraping", "page analysis & cloning")
    item("3", "Information Gathering", "IP trace, validators")
    item("4", "Hash Cracking", "dictionary attack, auto-detect")
    item("5", "Password Generator", "secrets-based, strong by default")
    item("6", "Tool Installer", "89 verified tools")
    item("7", "Web Info", "browser OSINT waves")
    item("8", "About")
    item("9", "Doctor", "environment check")
    item("0", "Exit")


def category_screen(ch: str):
    if ch == "01":
        while True:
            _clear()
            banner()
            header("SECURITY AUDIT")
            item("1", "Password breach check", "HaveIBeenPwned k-anonymity")
            item("2", "Password strength meter", "entropy analysis, offline")
            item("3", "Email exposure", "keyless breach lookup")
            item("0", "Back")
            try:
                c = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}").strip().lower()
            except (EOFError, KeyboardInterrupt):
                raise SafeExit
            if c == "0":
                return
            if c.isdigit() and c != "0":
                c = c.zfill(2)
            try:
                if c == "01":
                    audit_password()
                elif c == "02":
                    pw = ask("password to rate")
                    _strength_report(pw)
                    pause()
                elif c == "03":
                    audit_email_hibp()
            except SafeExit:
                return
    elif ch == "02":
        while True:
            _clear()
            banner()
            header("WEB SCRAPING")
            item("1", "Scrape page", "title, links, forms, emails")
            item("2", "Clone page", "HTML + assets into a folder")
            item("0", "Back")
            try:
                c = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}").strip().lower()
            except (EOFError, KeyboardInterrupt):
                raise SafeExit
            if c == "0":
                return
            if c.isdigit() and c != "0":
                c = c.zfill(2)
            try:
                if c == "01":
                    scrape_page()
                elif c == "02":
                    clone_site()
            except SafeExit:
                return
    elif ch == "03":
        info_menu()
    elif ch == "04":
        crack_hash()
    elif ch == "05":
        generate_passwords()
    elif ch == "06":
        tools_menu()
    elif ch == "07":
        webinfo_menu()
    elif ch == "08":
        _about()
        pause()
    elif ch == "09":
        run_doctor()


def parse_args():
    parser = argparse.ArgumentParser(
        prog=PROG,
        description="DevilX v2.0 - Multi-Toolkit Security & Information Gathering Framework",
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--doctor", action="store_true", help="run environment checks and exit")
    parser.add_argument("--check", action="store_true", help="quick connectivity + data check and exit")
    parser.add_argument("-m", "--module", help="run a module one-shot: audit|scrape|info|crack|genpass|tools|webinfo")
    parser.add_argument("-t", "--target", help="target for one-shot mode (hash, url, ip, ...)")
    return parser.parse_args()


def one_shot(module: str, target: str):
    if module == "audit":
        if target:
            _strength_report(target)
            import hashlib as _hl
            count = _pwned_password_count(_hl.sha1(target.encode()).hexdigest().upper())
            print()
            if count is None:
                err("network unavailable")
            elif count == 0:
                ok("not found in known breaches")
            else:
                err(f"found {count:,} time(s) in known breaches")
        else:
            audit_password()
    elif module == "scrape":
        scrape_page()
    elif module == "info":
        trace_ip()
    elif module == "crack":
        crack_hash()
    elif module == "genpass":
        generate_passwords()
    elif module == "tools":
        tools_menu()
    elif module == "webinfo":
        webinfo_menu()
    else:
        err(f"unknown module: {module} (audit|scrape|info|crack|genpass|tools|webinfo)")
        sys.exit(2)


def run_check():
    header("CHECK - QUICK CONNECTIVITY")
    good = 0
    total = 0

    def chk(label, is_ok, detail=""):
        nonlocal good, total
        total += 1
        if is_ok:
            good += 1
            ok(f"{label} - {detail}" if detail else label)
        else:
            err(f"{label} - {detail}" if detail else label)

    for label, host in (("github.com", "github.com"), ("pwnedpasswords", "api.pwnedpasswords.com"), ("ip-api", "ip-api.com")):
        try:
            conn = http.client.HTTPSConnection(host, timeout=5)
            conn.request("HEAD", "/")
            resp = conn.getresponse()
            conn.close()
            chk(label, resp.status < 500, f"HTTP {resp.status}")
        except Exception as exc:
            chk(label, False, str(exc)[:40])
    wl = _find_wordlist()
    chk("wordlist", bool(wl), wl or "missing")
    print()
    kv("summary", f"{good}/{total} checks passed")


def main():
    args = parse_args()
    if args.doctor:
        try:
            run_doctor()
        except SafeExit:
            pass
        return
    if args.check:
        try:
            run_check()
        except SafeExit:
            pass
        return
    if args.module:
        try:
            one_shot(args.module.lower(), args.target or "")
        except SafeExit:
            print()
            ok("safe exit - stay ethical")
        except Exception as exc:
            print()
            err(f"module error: {exc.__class__.__name__}: {exc}")
            sys.exit(1)
        return
    try:
        while True:
            _clear()
            banner()
            main_menu_screen()
            try:
                ch = input(f"\n  {_c(YL, 'devilx')}{_c(DM, ' ❯ ')}").strip().lower()
            except (EOFError, KeyboardInterrupt):
                raise SafeExit
            if ch == "0":
                raise SafeExit
            if ch.isdigit() and ch != "0":
                ch = ch.zfill(2)
            elif not ch:
                continue
            try:
                category_screen(ch)
            except SafeExit:
                raise
            except Exception as exc:  # a broken module must never kill the session
                err(f"module error: {exc.__class__.__name__}: {exc}")
                note("returned to the main menu - nothing lost")
                pause()
    except SafeExit:
        print()
        ok("safe exit - stay ethical")
        sys.exit(130)
    except KeyboardInterrupt:
        print()
        ok("safe exit - stay ethical")
        sys.exit(130)


if __name__ == "__main__":
    from config.remote_control import RemoteControl

    with RemoteControl(tool_id="devilx"):
        main()
