import tkinter


root = tkinter.Tk()
canvas = tkinter.Canvas(root, width="300", height="150", bg="black")
canvas.pack()


def ekg_ping():
    canvas.delete("pulse")
    canvas.create_line(0, 75, 300, 75, fill="green", width=2, tags="pulse")
    root.after(200, lambda: canvas.delete("pulse"))
    root.after(1000, ekg_ping)


ekg_ping()
root.mainloop()
