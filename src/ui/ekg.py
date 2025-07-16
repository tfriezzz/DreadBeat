import tkinter


# root = tkinter.Tk()
# canvas = tkinter.Canvas(root, width="300", height="150", bg="black")
# canvas.pack()


class EKGMonitor:
    def __init__(self, root, canvas, hr_source):
        self.root = root
        self.canvas = canvas
        self.heart_rate = int(hr_source)
        self.shape = []

    def run(self):
        self.__animate()

    def wave_shape(self):
        pass

    def set_heart_rate(self):
        # self.heart_rate = self.hr_source
        self.root.after(500, self.set_heart_rate)

    def __animate(self):
        hr_in_ms = (60 / self.heart_rate) * 1000
        print(f"hr_test: {hr_in_ms}")
        self.canvas.delete("pulse")
        self.canvas.create_line(0, 75, 300, 75, fill="green", width=2, tags="pulse")
        self.root.after(200, lambda: self.canvas.delete("pulse"))
        self.root.after(int(hr_in_ms), self.__animate)
        print(f"hr_test: {hr_in_ms}")


# if __name__ == "main":
# pass
# ekg = EKGMonitor(canvas)
# ekg.run()
# root.mainloop()
