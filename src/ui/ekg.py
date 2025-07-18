import tkinter


class EKGMonitor:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.heart_rate = 52  # test, change to 10 before launch
        self.shape = []
        self.x_green3 = 0
        self.x_green4 = -100
        self.x_black = -200

    def run(self):
        self.__animate()

    def wave_shape(self):
        pass

    def set_heart_rate(self, hr_source):
        self.heart_rate = int(hr_source)
        if self.heart_rate > 10:
            print(f"from ekg, new hr: {self.heart_rate}")

    def __animate(self):
        hr_in_ms = (60 / (int(self.heart_rate))) * 1000
        canvas_timing = int(self.canvas["width"])
        frame_rate = 5
        pulse_speed = canvas_timing / frame_rate
        # print(f"hr_test: {hr_in_ms}")
        self.canvas.delete("scan_line")
        # self.canvas.delete("pulse")
        if self.heart_rate > 10:
            self.canvas.create_line(
                self.x_green3 + 5,
                0,
                self.x_green3 + 5,
                150,
                fill="white",
                width=1,
                tags="scan_line",
            )

            self.canvas.create_line(
                self.x_green3,
                75,
                self.x_green3 + 5,
                75,
                fill="chartreuse3",
                width=2,
                tags="pulse",
            )

            self.canvas.create_line(
                self.x_green4,
                75,
                self.x_green4 + 5,
                75,
                fill="chartreuse4",
                width=2,
                tags="pulse",
            )

            self.canvas.create_line(
                self.x_black,
                75,
                self.x_black + 5,
                75,
                fill="black",
                width=2,
                tags="pulse",
            )

            self.x_green3 += frame_rate
            self.x_green4 += frame_rate
            self.x_black += frame_rate
            if self.x_green3 > 300:
                self.x_green3 = 0
            if self.x_green4 > 300:
                self.x_green4 = 0
            if self.x_black > 300:
                self.x_black = 0
            # self.root.after(200, lambda: self.canvas.delete("pulse"))
            self.root.after(int(int(hr_in_ms) / pulse_speed), self.__animate)
        else:
            self.root.after(500, self.__animate)

        # print(f"hr_test: {hr_in_ms}")


# if __name__ == "main":
