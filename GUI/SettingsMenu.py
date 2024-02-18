import tkinter as tk
from tkinter import ttk
from GUI.Window import Window
from Services.SettingsService import Settings
from Services.TranslationService import Translation

class SettingsMenu(Window):

    def __init__(self):
        super().__init__()
        self.window.wm_title("BabbleBuddy: Settings")

        self.set_size(400, 600)
        
        self.translate = Translation()
        self.settings = Settings()
        text_size = self.settings.GetIntSetting("font_size")
        title_size = round(text_size*2)
        label_size = round(text_size*1.25)

        frame = tk.Frame(self.window)

        title_label = tk.Label(frame, text="Settings", font=("Arial", title_size))
        title_label.pack()


        tk.Label(frame, text="Font Size", font=("Arial", label_size)).pack()
        self.font_size = tk.StringVar(frame, self.settings.GetIntSetting("font_size"))
        font_size_option = tk.Spinbox(frame, textvariable=self.font_size, from_=0, to=50, justify="right", increment=1, width=8, font=("Arial",text_size))
        font_size_option.pack(pady=5)

        tk.Label(frame, text="Source Language", font=("Arial", label_size)).pack()
        self.source_lang = tk.StringVar(frame, self.settings.GetSetting("source_lang"))
        source_lang_option = ttk.Combobox(frame, textvariable=self.source_lang, justify="right", values=["en-US","es-ES"], width=8, font=("Arial",text_size))
        source_lang_option.pack(pady=5)

        tk.Label(frame, text="Target Language", font=("Arial", label_size)).pack()
        self.target_lang = tk.StringVar(frame, self.settings.GetSetting("target_lang"))
        target_lang_option = ttk.Combobox(frame, textvariable=self.target_lang, justify="right", values=self.translate.GetLanguages(), width=8, font=("Arial",text_size))
        target_lang_option.pack(pady=5)

        tk.Label(frame, text="Anchor", font=("Arial", label_size)).pack()
        self.anchor = tk.StringVar(frame, self.settings.GetSetting("anchor"))
        anchor_option = ttk.Combobox(frame, textvariable=self.anchor, justify="right", values=["Top", "Bottom"], width=8, font=("Arial",text_size))
        anchor_option.pack(pady=5)

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
        self.window.protocol("WM_DELETE_WINDOW", command)

    def save_settings_clicked(self):
        self.settings.UpdateSetting("font_size", self.font_size.get())
        self.settings.UpdateSetting("source_lang", self.source_lang.get())
        self.settings.UpdateSetting("target_lang", self.target_lang.get())
        self.settings.UpdateSetting("anchor", self.anchor.get())
        # self.settings.UpdateSetting("source_lang", self.source_lang.get())

        #Idea is that anchor button is clicked and windows
        #Become Transparent. A rectangle / ui then follows the mouse. After that once you clicksomewhere
        #It places down an transparent box(where captions are shown) at an x + y position while also saving it to settings.
    def set_anchor_clicked(self):
        self.window.attributes('-alpha', 0.2)
        def get_move(event):
            x, y = event.x, event.y
            c.coords(rect, x - 10, y - 10, x + 10, y + 10)

        c = tk.Canvas(self.window)
        rect = c.create_rectangle(0, 0, 0, 100)
        c.bind('<Motion>', get_move)
        c.pack()