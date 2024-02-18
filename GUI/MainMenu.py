import tkinter as tk
from GUI.Window import Window

class MainMenu(Window):

    def __init__(self):
        super().__init__()

        frame = tk.Frame(self.window, name="frame")

#        title_label = tk.Label(frame, text="BabbleBuddy", font=("Arial", 25))
#        title_label.pack()

        info_label = tk.Label(frame, font=("Arial", 12), wraplength=275,
                              text="Break language barriers with BabbleBuddy!\n\nConvert audio into captions and translate into multiple languages in real-time.")
        info_label.pack(pady=5)

        start_button = tk.Button(frame, text="Start", font=("Arial",15), width=10, name="start-btn")
        start_button.pack(pady=5)

        settings_button = tk.Button(frame, text="Settings", font=("Arial",15), width=10, name="settings-btn")
        settings_button.pack(pady=5)

        frame.pack(pady=15)

    def set_start_command(self, command):
        self.children()["start-btn"].configure(command=command)

    def set_settings_command(self, command):
        self.children()["settings-btn"].configure(command=command)