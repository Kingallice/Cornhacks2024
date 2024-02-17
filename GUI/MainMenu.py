import tkinter as tk

class MainMenu:

    def __init__(self):
        self.window = tk.Tk()

        self.window.wm_title("BabbleBuddy")
        w,h = 400,300

        (ws, hs) = (self.window.winfo_screenwidth(), self.window.winfo_screenheight())
        self.window.geometry("%dx%d+%d+%d" % (w, h, ws/2-w/2, hs/2-h/2))

        frame = tk.Frame(self.window)

        title_label = tk.Label(frame, text="BabbleBuddy", font=("Arial", 25))
        title_label.pack()

        info_label = tk.Label(frame, font=("Arial", 12), wraplength=275,
                              text="Break language barriers with BabbleBuddy!\n\nConvert audio into captions and translate into multiple languages in real-time.")
        info_label.pack(pady=5)

        start_button = tk.Button(frame, text="Start", font=("Arial",15), width=10, name="start-btn")
        start_button.pack(pady=5)

        settings_button = tk.Button(frame, text="Settings", font=("Arial",15), width=10, name="settings-btn")
        settings_button.pack(pady=5)

        frame.pack(pady=15)

    def start(self):
        self.window.mainloop()

    def set_start_command(self, command):
        self.window.children["start-btn"].configure(command=command)

    def set_settings_command(self, command):
        self.window.children["settings-btn"].configure(command=command)

    def hide_menu(self):
        self.window.withdraw()

    def show_menu(self):
        self.window.deiconify()