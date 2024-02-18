import tkinter as tk
from Services.SettingsService import Settings

class Window:

    def __init__(self) -> None:
        self.window = tk.Tk()

        settings = Settings()

        self.window.wm_title("BabbleBuddy")
        self.set_size(settings.GetSetting("width"), settings.GetSetting("height"))

    def set_size(self, width: int, height: int):
        self.window.geometry("%dx%d+%d+%d" % (width, height, self.window.winfo_screenwidth()/2-width/2, self.window.winfo_screenheight()/2-height/2))

    def children(self):
        return self.window.winfo_children()[0].children

    def start(self):
        self.window.mainloop()

    def hide(self):
        self.window.withdraw()

    def show(self):
        self.window.deiconify()

    def disable(self):
        self.window.wm_attributes("-disabled", True)

    def enable(self):
        self.window.wm_attributes("-disabled", False)

    def focus(self):
        self.window.lift()

