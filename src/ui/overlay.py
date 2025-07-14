import sys
import ctypes

if sys.platform == "linux":
    libx11 = ctypes.cdll.LoadLibrary("libX11.so.6")
    libx11.XInitThreads()


import tkinter


root = tkinter.Tk()
root.title("DreadBeat")


hr_label = tkinter.Label(root, text="Heart Rate")
hr_label.pack()

root.mainloop()
