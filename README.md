# 🐾 Bongo Cat Clicker (macOS Edition)

A high-speed, multi-threaded automatic key-spammer built with a sleek **Catppuccin-inspired** Python Tkinter GUI. Optimized for macOS to simulate natural, randomized keystrokes directly into **Bongo Cat**.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

# 🛠️ Installation & Setup

If you've never installed Python or used Terminal on macOS before, simply follow these steps.

## 1. Install Python 3

macOS doesn't include an up-to-date Python installation by default.

1. Visit the official Python website:
   https://www.python.org/downloads/

2. Download the latest **Python 3.x** installer.

3. Run the downloaded `.pkg` installer.

4. **Important:** After installation finishes, open the folder that appears and run:

```
Install Certificates.command
```

This installs SSL certificates required for downloading Python packages.

---

## 2. Download This Repository

### Option A — Using Git

Open **Terminal** (`⌘ + Space` → Terminal) and run:

```bash
git clone https://github.com/YOUR_USERNAME/BongoCatClicker-main.git
cd BongoCatClicker-main
```

### Option B — Download ZIP

1. Click the green **Code** button on GitHub.
2. Select **Download ZIP**.
3. Extract the ZIP file.
4. Open **Terminal**.
5. Type:

```bash
cd
```

Then drag the extracted folder into the Terminal window and press **Enter**.

---

## 3. Install Dependencies

Inside the project folder, run:

```bash
python3 -m pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install everything manually:

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
```

Increasing the interval values lowers CPS but makes input appear more human-like.

---

# 📦 Project Structure

```
BongoCatClicker/
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 📝 License

This project is distributed under the **MIT License**.

See the **LICENSE** file for more information.
