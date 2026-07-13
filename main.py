import pyautogui
import time
import random
import threading
import tkinter as tk
from tkinter import font as tkfont
from pynput import keyboard
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionAll, kCGNullWindowID

pyautogui.PAUSE = 0

# ── CONFIG ──────────────────────────────────────────────────────────────────
BONGO_WINDOW_TITLE = "BongoCat"    
WINDOW_TITLE = "Bongo Cat Clicker" 
TOGGLE_KEY   = "p"                
INTERVAL_MIN = 0.02
INTERVAL_MAX = 0.03
HOLD_MIN     = 0.03
HOLD_MAX     = 0.04
DEBOUNCE     = 0.4
# ────────────────────────────────────────────────────────────────────────────

KEYS = [
    'a','b','c','d','e','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y',
    'z','0','1','2','3','4','5','6','7','8','9'
]

if TOGGLE_KEY.lower() in KEYS:
    KEYS.remove(TOGGLE_KEY.lower())

running      = False
lock         = threading.Lock()
_last_toggle = 0.0
status_label = None
btn_toggle   = None
root         = None

def find_and_focus():
    """Queries Mac OS WindowServer to check if BongoCat is running."""
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
    for window in window_list:
        # Get window owner name or window name
        owner_name = window.get('kCGWindowOwnerName', '')
        window_name = window.get('kCGWindowName', '')
        
        if BONGO_WINDOW_TITLE.lower() in owner_name.lower() or BONGO_WINDOW_TITLE.lower() in window_name.lower():
            return True
    return False

def press_key(key):
    try:
        pyautogui.keyDown(key)
        time.sleep(random.uniform(HOLD_MIN, HOLD_MAX))
        pyautogui.keyUp(key)
    except Exception as e:
        print(f"[press] Error on '{key}': {e}")

def auto_press_loop():
    global running
    last_focus = 0.0
    while True:
        with lock:
            is_running = running

        if not is_running:
            time.sleep(0.05)
            continue

        # Check if Bongo Cat is still open every 10 seconds
        now = time.time()
        if now - last_focus > 10.0:
            if not find_and_focus():
                set_status("Window not found", "#ffaa00")
                with lock:
                    running = False
                root.after(0, update_ui_state)
                continue
            last_focus = now

        try:
            press_key(random.choice(KEYS))
        except Exception as e:
            print(f"[loop] Error: {e}")

        time.sleep(random.uniform(INTERVAL_MIN, INTERVAL_MAX))

def set_status(text, color):
    if status_label and root:
        root.after(0, lambda: status_label.config(text=text, fg=color))

def update_ui_state():
    """Updates button text safely on the main thread."""
    global running
    if running:
        set_status("● Running", "#00ff88")
        btn_toggle.config(text=f"■ Stop  [{TOGGLE_KEY.upper()}]")
    else:
        set_status("● Stopped", "#ff4444")
        btn_toggle.config(text=f"▶ Start  [{TOGGLE_KEY.upper()}]")

def toggle_running():
    global running, _last_toggle
    now = time.time()
    if now - _last_toggle < DEBOUNCE:
        return
    _last_toggle = now

    with lock:
        running = not running
        state = running

    if state:
        if not find_and_focus():
            set_status("Window not found", "#ffaa00")
            with lock:
                running = False
            return
    
    update_ui_state()

def on_press_hotkey(key):
    """Callback for pynput global key listener."""
    try:
        if hasattr(key, 'char') and key.char == TOGGLE_KEY:
            # Tkinter likes UI updates triggered from root.after
            root.after(0, toggle_running)
    except Exception as e:
        print(f"Hotkey error: {e}")

def on_close():
    global running
    with lock:
        running = False
    root.destroy()

def build_gui():
    global root, status_label, btn_toggle

    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry("280x160")
    root.resizable(False, False)
    root.configure(bg="#1e1e2e")
    root.protocol("WM_DELETE_WINDOW", on_close)
    
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.95)

    f_title  = tkfont.Font(family="System", size=14, weight="bold")
    f_status = tkfont.Font(family="System", size=12)
    f_btn    = tkfont.Font(family="System", size=11)
    f_hint   = tkfont.Font(family="System", size=9)

    tk.Label(root, text="Bongo Cat Clicker",
             font=f_title, bg="#1e1e2e", fg="#cdd6f4").pack(pady=(14, 2))

    status_label = tk.Label(root, text="● Stopped",
                             font=f_status, bg="#1e1e2e", fg="#ff4444")
    status_label.pack(pady=2)

    btn_toggle = tk.Button(
        root, text=f"▶ Start  [{TOGGLE_KEY.upper()}]", font=f_btn,
        bg="#313244", fg="#cdd6f4", activebackground="#45475a",
        highlightbackground="#1e1e2e", 
        relief="flat", padx=12, pady=6, cursor="hand2",
        command=toggle_running
    )
    btn_toggle.pack(pady=10)

    tk.Label(root, text="Bongo Cat must be open to start",
             font=f_hint, bg="#1e1e2e", fg="#6c7086").pack()

    return root

def start_hotkey_listener():
    """Starts the Mac keyboard listener as a background thread."""
    listener = keyboard.Listener(on_press=on_press_hotkey)
    listener.daemon = True
    listener.start()

if __name__ == "__main__":
    start_hotkey_listener()
    threading.Thread(target=auto_press_loop, daemon=True).start()
    
    root = build_gui()
    print(f"[INFO] {TOGGLE_KEY.upper()} = Start/Stop | Close window to exit")
    root.mainloop()
