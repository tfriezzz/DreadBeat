import sys
import ctypes

if sys.platform == "linux":
    libx11 = ctypes.cdll.LoadLibrary("libX11.so.6")
    libx11.XInitThreads()


import asyncio
import bleak
import tkinter
import threading
from src.ble.scanner import *

test_ble = connect("FB:44:08:78:C4:61")


root = tkinter.Tk()
root.title("DreadBeat")


hr_label = tkinter.Label(root, text="Heart Rate")
hr_label.pack()
# hr_data_label = tkinter.Label(root, text=f"test {hr}")


def run_ble():
    asyncio.run(test_ble)


threading.Thread(target=run_ble).start()

root.mainloop()
