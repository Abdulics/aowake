import tkinter as tk
import signal
from prevent_sleep import PreventSleepApp, show_splash_screen

# Handle Ctrl+C in terminal
def signal_handler(sig, frame):
    print("Exiting...")
    try:
        root.destroy()
    except:
        pass

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    show_splash_screen()
    root = tk.Tk()
    app = PreventSleepApp(root)
    root.mainloop()
