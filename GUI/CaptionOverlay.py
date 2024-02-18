import asyncio
import tkinter as tk
from GUI.Window import Window
from Services.RecognitionService import *
from Services.SettingsService import Settings

class CaptionOverlay(Window):

    def __init__(self) -> None:
        super().__init__()

        self.settings = Settings()

        self.set_size(self.window.winfo_screenwidth()//2, 100)
        # self.window.eval("tk::PlaceWindow . top")
        self.anchorTopCenter()

        frame = tk.Frame(self.window)

        lines = tk.Text(frame, name='caption-txt', height=2, font=('Arial', '20'))
        lines.config(state='disabled')
        self.update("[begin BabbleBuddy live captioning]")
        close_button = tk.Button(frame, text="STOP", width=30, height=20, name="stop-btn", relief='groove', bg='grey', fg='white')
        self.window.overrideredirect(True)
        self.window.wm_attributes("-topmost", True)

        lines.pack(ipadx=10, fill='x', side="top")
        close_button.pack(pady=5, side="bottom")

        frame.pack()


    def update(self, newLine):
        if newLine == None or len(newLine) == 0:
            return
        targetText = self.children()["caption-txt"]
        targetText.tag_configure("center", justify='center')
        lines = targetText.get('0.0', tk.END).splitlines()
        targetText.config(state='normal')
        targetText.delete('0.0', tk.END)

        idx = 0
        if(len(lines) > 1):
            idx = 1
        targetText.insert('0.0', lines[idx] + "\n" + newLine, 'center')
        targetText.config(state='disabled')

    def set_stop_command(self, command):
        self.children()["stop-btn"].configure(command=command)

    def show(self):
        super().show()
        self.begin_captioning()

    def begin_captioning(self):
        source = self.settings.GetSetting("source_lang")
        target = self.settings.GetSetting("target_lang")
        while(self.window.winfo_ismapped()):
            self.window.update()
            try:
                result = recognize_from_microphone(source, target)
                self.update(result)
            except:
                pass


    # def buildOverlay():

    #     def close():
    #         window.destroy()

    #     window = tkinter.Tk()

    #     #label = tkinter.Label(window, name='main', text='Text on the screen', font=('ARIAL','20'), fg='black', bg='white')
        
    #     return window

