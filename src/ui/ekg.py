import tkinter


# root = tkinter.Tk()
# canvas = tkinter.Canvas(root, width="300", height="150", bg="black")
# canvas.pack()


class EKGMonitor:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.heart_rate = 0
        self.shape = []

    def run(self):
        self.__animate()

    def wave_shape(self):
        pass

    def set_heart_rate(self):
        pass

    def __animate(self):
        self.canvas.delete("pulse")
        self.canvas.create_line(0, 75, 300, 75, fill="green", width=2, tags="pulse")
        self.root.after(200, lambda: self.canvas.delete("pulse"))
        self.root.after(1000, self.__animate)


# if __name__ == "main":
# pass
# ekg = EKGMonitor(canvas)
# ekg.run()
# root.mainloop()
