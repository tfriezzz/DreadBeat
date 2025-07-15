import sys
import ctypes

if sys.platform == "linux":
    libx11 = ctypes.cdll.LoadLibrary("libX11.so.6")
    libx11.XInitThreads()


# import asyncio
# import bleak
import tkinter
import threading
from src.ble.scanner import BLEScanner
from config.device_config import DEVICE_CONFIG

test_ble = BLEScanner(DEVICE_CONFIG["device_mac"])


root = tkinter.Tk()
root.title("DreadBeat")
root.geometry("300x150")


hr_value = tkinter.StringVar(value="waiting")
tkinter.Label(root, text="Heart Rate").pack()
hr_label = tkinter.Label(root, textvariable=hr_value)
hr_label.pack()


def update_gui():
    hr_value.set(test_ble.hr)
    root.after(500, update_gui)


def run_ble():
    test_ble.ble_run()


threading.Thread(target=run_ble, daemon=True).start()
update_gui()
root.mainloop()
