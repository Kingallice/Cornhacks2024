import tkinter
from tkinter import *

def updateLines(targetText: Text, newLine):
    targetText.tag_configure("center", justify='center')
    lines = targetText.get('0.0',END).splitlines()
    targetText.config(state='normal')
    targetText.delete('0.0', END)

    idx = 0
    if(len(lines) > 1):
        idx = 1
    targetText.insert('0.0', lines[idx] + "\n" + newLine, 'center')
    targetText.config(state='disabled')


def buildOverlay():

    def close():
        window.destroy()

    window = tkinter.Tk()

    #label = tkinter.Label(window, name='main', text='Text on the screen', font=('ARIAL','20'), fg='black', bg='white')
    lines = Text(window, name= 'main', height=2, width=50, font= ('Arial', '20'))
    lines.config(state='disabled')
    updateLines(lines, "[begin BabbleBuddy live captioning]\n")
    close_button = tkinter.Button(window, text="STOP", command=close, relief='groove', bg='grey', fg='white')
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)

    lines.pack(ipadx=10)
    close_button.pack(pady=5)

    return window


window = buildOverlay()

#testing
while True:
   updateLines(window.children["main"], input())
window.mainloop()
