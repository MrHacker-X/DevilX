#!/usr/bin/env bash
# DevilX v2.0 installer - detects your package manager, installs
# git, python3 and the two Python dependencies, then verifies.
# Author: MrHacker-X  ·  https://vritrasec.com  ·  BSL-1.0

set -u

C_WH=$'\033[1;97m'
C_YL=$'\033[38;5;179m'
C_GR=$'\033[38;5;150m'
C_DM=$'\033[38;5;245m'
C_RD=$'\033[38;5;174m'
C_XX=$'\033[0m'

if [ ! -t 1 ] || [ -n "${NO_COLOR:-}" ]; then
    C_WH="" C_YL="" C_GR="" C_DM="" C_RD="" C_XX=""
fi

say()  { printf '%s\n' "  ${C_GR}›${C_XX} ${C_WH}$*${C_XX}"; }
ok()   { printf '%s\n' "  ${C_GR}✓${C_XX} ${C_GR}$*${C_XX}"; }
err()  { printf '%s\n' "  ${C_RD}✗${C_XX} ${C_RD}$*${C_XX}"; }
note() { printf '%s\n' "  ${C_DM}·${C_XX} ${C_DM}$*${C_XX}"; }

IS_TERMUX=0
case "${PREFIX:-}" in
    *com.termux*) IS_TERMUX=1 ;;
esac

# ------------------------------------------------------------
#  Banner
# ------------------------------------------------------------
printf '%s\n' ""
printf '%s\n' "${C_YL}  █▀▀ █▀▀ █ █ █ █   █ █${C_XX}"
printf '%s\n' "${C_YL}  █ █ █▀  █ █ █ █    █${C_XX}"
printf '%s\n' "${C_YL}  ▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀ ▀ ▀${C_XX}"
printf '%s\n' ""
note "Multi-Toolkit Security & Information Gathering Framework - v2.0"
note "github.com/MrHacker-X  ·  vritrasec.com"
printf '%s\n' ""

# ------------------------------------------------------------
#  Package manager detection
# ------------------------------------------------------------
PM=""
if [ "$IS_TERMUX" -eq 1 ] && command -v pkg >/dev/null 2>&1; then
    PM="pkg"
elif command -v apt-get >/dev/null 2>&1; then
    PM="apt-get"
elif command -v apt >/dev/null 2>&1; then
    PM="apt"
elif command -v dnf >/dev/null 2>&1; then
    PM="dnf"
elif command -v yum >/dev/null 2>&1; then
    PM="yum"
elif command -v pacman >/dev/null 2>&1; then
    PM="pacman"
elif command -v zypper >/dev/null 2>&1; then
    PM="zypper"
elif command -v apk >/dev/null 2>&1; then
    PM="apk"
fi

SUDO=""
if [ "$IS_TERMUX" -eq 0 ] && [ "$(id -u)" -ne 0 ] && command -v sudo >/dev/null 2>&1; then
    SUDO="sudo"
fi

pm_install() {
    # pm_install pkg...
    case "$PM" in
        apt-get|apt|pkg) $SUDO "$PM" install -y "$@" ;;
        dnf|yum)         $SUDO "$PM" install -y "$@" ;;
        pacman)          $SUDO "$PM" -S --noconfirm --needed "$@" ;;
        zypper)          $SUDO "$PM" install -y "$@" ;;
        apk)             $SUDO "$PM" add "$@" ;;
        *)               return 1 ;;
    esac
}

pm_refresh() {
    case "$PM" in
        apt-get|apt)     $SUDO "$PM" update -y 2>/dev/null || $SUDO "$PM" update ;;
        pkg)             pkg update -y ;;
        dnf)             $SUDO "$PM" makecache --quiet 2>/dev/null || true ;;
        pacman)          $SUDO "$PM" -Sy ;;
        zypper|apk)      ;;  # zypper/apk refresh on demand
        *)               ;;
    esac
}

if [ -z "$PM" ]; then
    err "no supported package manager found (apt/pkg/dnf/yum/pacman/zypper/apk)"
    note "install git + python3 + pip manually, then: python3 -m pip install --user requests beautifulsoup4"
    exit 1
fi
ok "package manager detected: ${PM}"

# ------------------------------------------------------------
#  System packages
# ------------------------------------------------------------
note "refreshing package lists"
pm_refresh

for pkg in git python3; do
    if command -v "$pkg" >/dev/null 2>&1; then
        ok "$pkg already present"
    else
        say "installing $pkg"
        if ! pm_install "$pkg"; then
            err "could not install $pkg - install it manually and re-run"
            exit 1
        fi
    fi
done

if ! python3 -m pip --version >/dev/null 2>&1; then
    say "installing python3-pip"
    case "$PM" in
        apt-get|apt|pkg) pm_install python-pip 2>/dev/null || pm_install python3-pip ;;
        dnf|yum)         pm_install python3-pip ;;
        pacman)          pm_install python-pip ;;
        zypper)          pm_install python3-pip ;;
        apk)             pm_install py3-pip ;;
    esac
fi

# ------------------------------------------------------------
#  Python dependencies (requests, beautifulsoup4)
# ------------------------------------------------------------
for mod in requests bs4 colorama; do
    if python3 -c "import $mod" >/dev/null 2>&1; then
        ok "python module $mod already present"
    else
        say "installing python module $mod"
        if ! python3 -m pip install --user "$mod" >/dev/null 2>&1; then
            if ! python3 -m pip install "$mod" >/dev/null 2>&1; then
                err "could not install $mod - run: python3 -m pip install $mod"
            else
                ok "$mod installed"
            fi
        else
            ok "$mod installed"
        fi
    fi
done

# ------------------------------------------------------------
#  Final verification
# ------------------------------------------------------------
printf '%s\n' ""
if python3 -c "import requests, bs4, colorama" >/dev/null 2>&1 && command -v git >/dev/null 2>&1; then
    ok "all dependencies verified"
    note "launch with: python3 devilx.py"
    note "environment check: python3 devilx.py --doctor"
else
    err "verification failed - see the messages above"
    exit 1
fi
printf '%s\n' ""
