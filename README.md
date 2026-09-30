<div align="center">

# ⃤ D E V I L X ⃤

### ✦ Multi-Toolkit Security & Information Gathering Framework ✦

![Version](https://img.shields.io/badge/Version-2.0-198c6c?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux-2d4a2d?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-BSL--1.0-8a6d3b?style=for-the-badge&logo=open-source-initiative&logoColor=white)

**One menu. Eighty-nine tools. Zero dead links.**

DevilX turns a messy pile of 130 copy-pasted installers into a clean, audited
framework: breach checks, offline validators, web scraping, hash cracking,
password generation, a curated tool installer and a browser OSINT launcher -
all in one typographic terminal UI.

</div>

---

## 📋 Table of Contents

- [🎯 Why DevilX?](#-why-devilx)
- [🧭 Tool Purpose](#-tool-purpose)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [✨ Features](#-features)
- [🔄 What Changed in v2.0](#-what-changed-in-v20)
- [🖥️ Preview](#️-preview)
- [🧰 Tech Stack](#-tech-stack)
- [⚠️ Disclaimer](#️-disclaimer)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Developer](#-developer)

---

## 🎯 Why DevilX?

> Most "all-in-one hacking tools" are 4,000 lines of copy-paste: dead GitHub
> links, hardcoded API keys, brute-force modules that only get you banned,
> and menus that crash if you press the wrong key.
>
> **DevilX v2.0 is the opposite.** Every tool URL is verified live, every
> third-party API key is gone, every module exits cleanly on Ctrl+C, and the
> whole thing is honest about what it does: *authorized* security auditing
> and OSINT - not crime.

---

## 🧭 Tool Purpose

DevilX exists to put a **legal, first-party security toolkit** in one terminal:

1. **Audit your own accounts** - check passwords against real breach corpora
   (HaveIBeenPwned k-anonymity - your password never leaves your machine), look
   up email addresses in a keyless breach database, and rate password strength
   by entropy.
2. **Gather information legitimately** - trace IPs, validate emails (syntax +
   MX), phone numbers (E.164) and IBANs (mod-97, fully offline) without
   shipping your data to someone else's API key.
3. **Analyze and archive web pages** - pull titles, links, forms, emails and
   clone a page with its assets for offline review.
4. **Recover and test hashes** - dictionary cracking with automatic algorithm
   detection (MD5 → SHA-512).
5. **Generate real passwords** - `secrets`-based generation, not `random`.
6. **Install third-party security tools safely** - a curated, URL-verified
   catalog of 89 tools with a single generic install engine.
7. **Launch OSINT research waves** - 20 curated browser sources, one wave at
   a time, each opened only after your confirmation.

> **What it deliberately does not do:** no Gmail/Facebook/Instagram brute
> force, no SMS bombers, no hardcoded API keys, no phishing-game tools.

---

## 🚀 Quick Start

```bash
git clone https://github.com/MrHacker-X/DevilX.git
cd DevilX
bash setup.sh
python3 devilx.py
```

First run? Type `9` for the built-in **Doctor** - it verifies your Python,
modules, wordlists and network in one shot.

```bash
python3 devilx.py --doctor    # full environment check
python3 devilx.py --check     # quick connectivity check
python3 devilx.py -v          # version
```

---

## 📦 Installation

```bash
git clone https://github.com/MrHacker-X/DevilX.git
cd DevilX
bash setup.sh
python3 devilx.py
```

`setup.sh` detects your package manager automatically - no more Termux-only
`apt` blasting.

| Platform  | Status       | Notes                                   |
|-----------|--------------|-----------------------------------------|
| Kali      | ✅ Supported | apt detected natively                   |
| Ubuntu    | ✅ Supported | apt detected natively                   |
| Debian    | ✅ Supported | apt detected natively                   |
| Parrot    | ✅ Supported | apt detected natively                   |
| Arch      | ✅ Supported | pacman                                  |
| Fedora    | ✅ Supported | dnf                                     |
| openSUSE  | ✅ Supported | zypper                                  |
| Alpine    | ✅ Supported | apk                                     |
| Termux    | ✅ Supported | pkg, no root needed                     |
| Windows   | ⚠️ Partial   | pure-Python modules work; installer needs WSL |

<details>
<summary><b>🔍 Manual installation (no script)</b></summary>

<br>

```bash
git clone https://github.com/MrHacker-X/DevilX.git
cd DevilX
python3 -m pip install --user requests beautifulsoup4 colorama
python3 devilx.py
```

Only three Python dependencies beyond the standard library: `requests`,
`beautifulsoup4` and `colorama`. If any are missing, affected modules tell you
exactly what to install instead of crashing.

</details>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Security Audit** | Password breach check via HaveIBeenPwned k-anonymity (password never sent), entropy-based strength meter, keyless email breach lookup (XposedOrNot) |
| 🌐 **Web Scraping** | Page analysis (title, links, forms, images, emails) and page cloning with assets - pure requests + BeautifulSoup |
| 🕵️ **Information Gathering** | IP/domain trace with Google Maps link, email MX validation, E.164 phone check, offline IBAN mod-97 checksum - zero API keys |
| 🔓 **Hash Cracking** | Auto-detects MD5/SHA-1/SHA-224/SHA-256/SHA-384/SHA-512 by length, dictionary attack on a 1M+ word wordlist |
| 🔑 **Password Generator** | Cryptographically secure (`secrets` module), configurable length and count, optional save-to-file |
| 🧰 **Tool Installer** | Curated catalog of **89 verified tools** in 6 categories, single generic engine (git/apt/pip), installs to `~/DevilX-tools` |
| 🧭 **Web Info Launcher** | 20 OSINT sources in 3 waves (domain intel, DNS/WHOIS, headers/stack) - one wave at a time, each URL confirmed before opening |
| 🩺 **Doctor & Check** | `--doctor` verifies python, modules, git, wordlists, network; `--check` is the quick version |
| 🛡️ **Safe Exit** | Ctrl+C, EOF or `q` anywhere exits cleanly (code 130) - never a traceback |
| 🎨 **Typographic UI** | Block-letter banner, muted palette, clean options-only menus, press-enter pauses - no ASCII-art escape hazards |

<details>
<summary><b>📖 The 6 tool-installer categories</b></summary>

<br>

| Category | Tools | Examples |
|----------|-------|----------|
| Recon & scanners | 13 | nmap, nikto, seeker, RED_HAWK, BruteX, ScannerX |
| Web exploitation | 10 | sqlmap, fsociety, slowloris, SploitX, CloneWeb |
| OSINT & social | 10 | Osintgram, SocialBox, TeleGram-Scraper, DecodeX |
| Phishing (authorized testing) | 3 | saycheese, maskphish, mrphish |
| Payloads & post-exploitation | 9 | thc-hydra, Traper-X, DVR-Exploiter, HXP-Ducky |
| Utility & environment | 44 | Tool-X, termux-desktop, TermuxArch, LinuxX |

Every URL was re-verified live for v2.0 - 12 moved repositories were updated
to their new owners and 10 dead repositories were removed.

</details>

---

## 🔄 What Changed in v2.0

| | v1.1.2 | v2.0 |
|---|--------|------|
| **Codebase** | 3,923 lines, 130 copy-paste installer functions | Clean single file, one generic install engine + data table |
| **Brute-force modules** | Gmail SMTP / Facebook / Instagram credential attacks (dead cookies, IG crash bug) | ❌ Removed - replaced with **Breach & Password Audit** (HIBP k-anonymity, 100% legal) |
| **API keys** | 4 hardcoded AbstractAPI keys exposed in source | ❌ Removed - replaced with offline validators (mod-97 IBAN, MX email, E.164 phone) |
| **Tool catalog** | ~102 raw URLs, 10 dead, 12 moved, 1 sketchy leak tool | **89 verified tools**, moved URLs fixed, dead & sketchy removed |
| **Tool install** | 1,700 lines of duplicated `git clone` code | Single `install_tool()` engine: git (shallow) / apt / pip |
| **Web Info** | 10 tabs spam-opened at once, hardcoded `souqana.com` bug | 3 waves, one at a time, per-URL confirmation, bug fixed |
| **Hash cracker** | Manual algorithm selection | Auto-detection by hash length + SHA-3 support |
| **Password gen** | `random` + array, weak | `secrets` module, configurable, save option |
| **UI** | ASCII art, 6 inconsistent menu formats | Block-letter wordmark, unified typographic UI, muted palette |
| **Exit handling** | `exit()` calls killing the whole tool mid-flow | Central `SafeExit` - Ctrl+C/EOF/`q` always clean (exit 130) |
| **Wordlist input** | Custom wordlist silently ignored (variable bug) | Fixed - validated before use |
| **Setup** | Termux-only `apt` blasting, lolcat + instaloader bloat | Package-manager detection (apt/dnf/yum/pacman/zypper/apk/pkg), `--user` pip fallback |
| **CLI** | None | `-v/--version`, `--doctor`, `--check`, `-m module -t target` one-shot |
| **Config cruft** | Unused torrc + instapy config shipped | Removed |

---

## 🖥️ Preview

<div align="center">
<img src="https://i.ibb.co/jP19s5x5/Screenshot-From-2026-09-30-23-23-58.png " alt="DevilX v2.0 main menu" width="760">
</div>

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.8+ (standard library first) |
| Networking | `requests` with a zero-dependency `urllib` fallback |
| Parsing | `beautifulsoup4` (html.parser) |
| Security | `hashlib`, `secrets`, k-anonymity breach queries |
| System | `subprocess`, `shutil` - git/apt/dnf/yum/pacman/zypper/apk/pkg detection |
| UI | colorama palette, auto-disabled on pipes/NO_COLOR |

---

## ⚠️ Disclaimer

> **1.** DevilX is built for **authorized security auditing, education and
> OSINT research** only.
>
> **2.** You are responsible for complying with all applicable local, state,
> national and international laws. Attacking systems without explicit written
> permission is illegal almost everywhere.
>
> **3.** The breach-check and validator modules query third-party public
> services - do not use them against data you have no right to test.
>
> **4.** The third-party tools in the installer catalog are **not authored or
> maintained by DevilX**; each carries its own license and risk.
>
> **5.** The developer assumes **no liability** for misuse or damage caused
> by this program. By using DevilX you accept full responsibility for your
> actions.

---

## 🤝 Contributing

Contributions are welcome - especially verified tool URLs for the installer
catalog.

```bash
# 1. Fork the repository
# 2. Create your branch
git checkout -b feature/awesome-addition
# 3. Commit and push
git commit -m "Add: awesome addition"
git push origin feature/awesome-addition
# 4. Open a Pull Request
```

Found a dead tool URL or a bug? Open an [issue](https://github.com/MrHacker-X/DevilX/issues).

---

## 📜 License

This project is licensed under the **Boost Software License 1.0** - see
[LICENSE](LICENSE) for details.

---

## 👨‍💻 Developer

| | |
|---|---|
| **Developer** | MrHacker-X |
| **GitHub** | [github.com/MrHacker-X](https://github.com/MrHacker-X) |
| **Email** | contact@vritrasec.com |
| **Website** | [vritrasec.com](https://vritrasec.com) |
| **Network** | [link.vritrasec.com](https://link.vritrasec.com) |

---

<div align="center">

**⃤ DevilX ⃤** - *Audit what you own. Learn what you test.*

⭐ **Found it useful? Star the repo - it keeps the catalog maintained.** ⭐

</div>
