import tkinter as tk
from tkinter import ttk
from GUI.Window import Window
from Services.SettingsService import Settings

class SettingsMenu(Window):

    def __init__(self):
        super().__init__()
        self.window.wm_title("BabbleBuddy: Settings")
        self.settings = Settings()
    
        text_size = self.settings.GetIntSetting("font_size")
        title_size = round(text_size*2)
        label_size = round(text_size*1.25)

        frame = tk.Frame(self.window)

        title_label = tk.Label(frame, text="Settings", font=("Arial", title_size))
        title_label.pack()

        font_size_label = tk.Label(frame, text="Font Size", font=("Arial", label_size))
        font_size_label.pack()

        self.font_size = tk.StringVar(frame, self.settings.GetIntSetting("font_size"))
        font_size_option = tk.Spinbox(frame, textvariable=self.font_size, from_=0, to=50, justify="right", increment=1, width=10, font=("Arial",text_size))
        font_size_option.pack(pady=5)

        self.selected_lang = tk.StringVar(frame, self.settings.GetSetting("language"))
        lang_option = ttk.Combobox(frame, textvariable=self.selected_lang, values=["en-US","es-ES"], font=("Arial",text_size))
        lang_option.pack(pady=5)

        disclaimer_label = tk.Label(frame, text="*Setting changes will not reflect until next load!")
        disclaimer_label.pack(pady=2)

        save_button = tk.Button(frame, text="Save", font=("Arial",label_size), width=10, name="save-btn", command=self.save_settings_clicked)
        save_button.pack(pady=5)

        back_button = tk.Button(frame, text="Back", font=("Arial",label_size), width=10, name="back-btn")
        back_button.pack(pady=5)

        frame.pack(pady=15)

    def set_save_command(self, command):
        self.children()["save-btn"].configure(command=command)

    def set_back_command(self, command):
        self.children()["back-btn"].configure(command=command)

    def save_settings_clicked(self):
        self.settings.UpdateSetting("font_size", self.font_size.get())
        self.settings.UpdateSetting("language", self.selected_lang.get())