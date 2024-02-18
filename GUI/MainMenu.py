import tkinter as tk
from GUI.Window import Window
from PIL import Image, ImageTk
from Services.SettingsService import Settings

class MainMenu(Window):

    def __init__(self):
        super().__init__()

        self.set_size(1080, 650)

        self.settings = Settings()
        text_size = self.settings.GetIntSetting("font_size")
        title_size = round(text_size*2)
        label_size = round(text_size*1.25)

        frame = tk.Frame(self.window, name="frame")

        self.img = ImageTk.PhotoImage(Image.open("./Resources/Images/babblebuddy.png"))
        
        title_canvas = tk.Canvas(frame, width=self.img.width()+25, height=self.img.height())
        title_canvas.pack()

        title_canvas.create_image(self.img.width()//2+25,self.img.height()//2, image=self.img)

        info_label = tk.Label(frame, font=("Arial", label_size), wraplength=275,
                              text="Break language barriers with BabbleBuddy!\n\nConvert audio into captions and translate into multiple languages in real-time.")
        info_label.pack(pady=5)

        start_button = tk.Button(frame, text="Start", font=("Arial",label_size), width=10, name="start-btn")
        start_button.pack(pady=5)

        settings_button = tk.Button(frame, text="Settings", font=("Arial",label_size), width=10, name="settings-btn")
        settings_button.pack(pady=5)

        exit_button = tk.Button(frame, text="Exit", font=("Arial",label_size), width=10, name="exit-btn", command=lambda:self.window.quit())
        exit_button.pack(pady=5)

        frame.pack(pady=15)

    def set_start_command(self, command):
        self.children()["start-btn"].configure(command=command)

    def set_settings_command(self, command):
        self.children()["settings-btn"].configure(command=command)