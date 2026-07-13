# 🐾 Bongo Cat Clicker (macOS Edition)

A high-speed, multi-threaded automatic key-spammer built with a sleek **Catppuccin-inspired** Python Tkinter GUI. Optimized for macOS to simulate natural, randomized keystrokes directly into **Bongo Cat**.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Install Dependencies

```bash
python3 -m pip install pyautogui pynput pyobjc
```

---

# 🔒 Required macOS Permissions

Because the application monitors global keyboard input and injects keystrokes into another application, macOS blocks it by default.

Grant **Accessibility** permissions:

1. Open **System Settings**
2. Go to:

```
Privacy & Security
    └── Accessibility
```

3. Enable the application you're using to run the script:

- Terminal
- Visual Studio Code
- PyCharm
- IDLE
- etc.

If it isn't listed:

- Click **+**
- Enter your password
- Select your application
- Enable it

Finally:

**Quit the application completely (`⌘ + Q`) and reopen it.**

The permission change won't take effect until the application restarts.

---

# 🚀 Running the Program

1. Launch **Bongo Cat**.

2. Open Terminal inside the project folder.

3. Run:

```bash
python3 main.py
```

The clicker GUI will open.

Press **P** anywhere on your Mac to toggle the clicker **ON** or **OFF**.

---

# ⚙️ Configuration

Open `main.py` and edit the configuration variables near the top of the file.

```python
# ── CONFIG ────────────────────────────────────────────────────────────────

BONGO_WINDOW_TITLE = "BongoCat"   # Window title to detect
TOGGLE_KEY   = "p"                # Global start/stop hotkey

INTERVAL_MIN = 0.02               # Minimum delay between key presses
INTERVAL_MAX = 0.03               # Maximum delay between key presses

HOLD_MIN     = 0.03               # Minimum key hold duration
HOLD_MAX     = 0.04               # Maximum key hold duration

# ──────────────────────────────────────────────────────────────────────────
