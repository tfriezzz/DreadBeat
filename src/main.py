import sys
import ctypes

if sys.platform == "linux":
    libx11 = ctypes.cdll.LoadLibrary("libX11.so.6")
    libx11.XInitThreads()


import tkinter as tk
import threading
from config.device_config import DEVICE_CONFIG

from src.ble.scanner import BLEScanner
from src.ui.ekg import EKGMonitor


def main():
    my_device = DEVICE_CONFIG["device_mac"]
    root = tk.Tk()
    canvas = tk.Canvas(root, width="300", height="150", bg="black")
    canvas.pack()

    test_scanner = BLEScanner(my_device)

    # test_ekg = EKGMonitor(root, canvas, test_scanner.hr)
    test_ekg = EKGMonitor(root, canvas, "120")
    test_ekg.run()

    threading.Thread(target=test_scanner.run, daemon=True).start()
    # print(f"test: {test_ekg.heart_rate}")

    root.mainloop()


if __name__ == "__main__":
    main()
