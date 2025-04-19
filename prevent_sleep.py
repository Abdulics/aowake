import ctypes
import time
import random
import pyautogui
import tkinter as tk
from threading import Thread
import sys
import os
import subprocess

# Constants for Windows
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class PreventSleepApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AOwake - Always On")
        self.root.geometry("300x150")
        self.running = False
        self.caffeinate = None

        icon_path = resource_path("icon.png")
        try:
            self.root.iconphoto(False, tk.PhotoImage(file=icon_path))
        except Exception as e:
            print(f"Icon not loaded: {e}")

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def prevent_sleep(self):
        if sys.platform.startswith('win'):
            ctypes.windll.kernel32.SetThreadExecutionState(
                ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
            )
            print("Sleep prevention enabled on Windows.")
        elif sys.platform == 'darwin':
            self.caffeinate = subprocess.Popen(['caffeinate'])
            print("Sleep prevention enabled on macOS.")

    def scroll_screen(self, count):
        if count <= 10:
            pyautogui.scroll(35)
        elif count <= 20:
            pyautogui.scroll(-35)
        else:
            count = 0
        return count            

    def reset_sleep(self):
        if sys.platform.startswith('win'):
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
            print("Sleep reset on Windows.")
        elif sys.platform == 'darwin':
            if self.caffeinate:
                self.caffeinate.terminate()
                print("Sleep reset on macOS.")

    def move_mouse(self):
        pyautogui.FAILSAFE = False
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(600, 150)
        count = 0

        while self.running:
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            current_x, current_y = pyautogui.position()
            new_x = min(max(current_x + x, 0), screen_width - 1)
            new_y = min(max(current_y + y, 0), screen_height - 1)
            pyautogui.moveTo(new_x, new_y, duration=random.uniform(0.5, 1.5))
            count += 1
            count = self.scroll_screen(count)
            time.sleep(random.uniform(5, 15))

    def start(self):
        if not self.running:
            self.running = True
            self.prevent_sleep()
            self.thread = Thread(target=self.move_mouse)
            self.thread.daemon = True
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()
            self.reset_sleep()
            print("AOwake stopped.")

    def on_close(self):
        self.stop()
        self.root.destroy()

def show_splash_screen(duration=3):
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("300x200+500+300")

    icon_path = resource_path("icon.png")
    try:
        splash.iconphoto(False, tk.PhotoImage(file=icon_path))
    except:
        pass

    canvas = tk.Canvas(splash, width=300, height=200, bg='black', highlightthickness=0)
    canvas.pack()

    try:
        img = tk.PhotoImage(file=icon_path)
        canvas.create_image(150, 60, image=img)
    except:
        pass

    canvas.create_text(150, 140, text="AOwake: Waking Up...",
                       fill="white", font=("Helvetica", 12, "bold"))

    splash.after(duration * 1000, splash.destroy)
    splash.mainloop()
