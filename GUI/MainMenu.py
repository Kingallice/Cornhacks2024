import tkinter as tk
from GUI.Window import Window
from PIL import Image, ImageTk

class MainMenu(Window):

    def __init__(self):
        super().__init__()

        frame = tk.Frame(self.window, name="frame")
        # logoPNG = Image.open('./Resources/Images/babblebuddy.png')
        
        
        # /img = tk.PhotoImage(master=frame, file='Resources/Images/babblebuddy.png', format="PNG")
        self.img = ImageTk.PhotoImage(Image.open("./Resources/Images/babblebuddy.png"))
        # print(image.height(), image.width())

        # logoPNG.
        title_canvas = tk.Canvas(frame, width=self.img.width()+25, height=self.img.height())
        title_canvas.pack()

        title_canvas.create_image(self.img.width()//2+25,self.img.height()//2, image=self.img)
    
    #    title_label = tk.Label(frame, text="BabbleBuddy", font=("Arial", 25))

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