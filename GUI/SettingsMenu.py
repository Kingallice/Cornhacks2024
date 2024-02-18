import tkinter as tk
from GUI.Window import Window

class SettingsMenu(Window):

    def __init__(self):
        super().__init__()
        self.window.wm_title("BabbleBuddy: Settings")

        frame = tk.Frame(self.window)

        title_label = tk.Label(frame, text="Settings", font=("Arial", 25))
        title_label.pack()

        back_button = tk.Button(frame, text="Back", font=("Arial",15), width=10, name="back-btn")
        back_button.pack(pady=5)

        frame.pack(pady=15)

    def set_back_command(self, command):
        self.children()["back-btn"].configure(command=command)