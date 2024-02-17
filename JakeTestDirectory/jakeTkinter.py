import tkinter

def build_window(voice):
    window = tkinter.Tk()
    window.title("Babel Buddy")
    label = tkinter.Label(window,text=voice)
    window.mainloop()

