import tkinter as tk
from Services.SettingsService import Settings

class Window:

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.iconbitmap("Resources/Images/BBicon-2.ico")

        settings = Settings()

        self.window.wm_title("BabbleBuddy")
        self.set_size(settings.GetIntSetting("width"), settings.GetIntSetting("height"))

    def set_size(self, width: int, height: int):
        self._width = width
        self._height = height
        self.window.geometry("%dx%d+%d+%d" % (width, height, self.window.winfo_screenwidth()/2-width/2, self.window.winfo_screenheight()/2-height/2))

    def getSize(self):
        if hasattr(self, "_width") and hasattr(self, "_height"):
            return (self._width, self._height)

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

    def translate(self, x, y):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], x, y))

    def translateX(self, x):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], x, self.window.winfo_y()))

    def translateY(self, y):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], self.window.winfo_x(), y))

    def center(self):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], self.window.winfo_screenwidth()//2, self.window.winfo_screenheight()//2))

    def centerX(self):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], self.window.winfo_screenwidth()//2, self.window.winfo_y()))

    def centerY(self):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], self.window.winfo_x(), self.window.winfo_screenheight()//2))

    def anchorTopCenter(self):
        self.window.wm_geometry("%dx%d+%d+%d" % (self.getSize()[0], self.getSize()[1], self.window.winfo_screenwidth()//2, 0))
