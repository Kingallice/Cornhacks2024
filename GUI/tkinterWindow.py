import tkinter

def close():
    window.destroy()

window = tkinter.Tk()

label = tkinter.Label(window, text='Text on the screen', font=('Times New Roman','40'), fg='black', bg='white')
close_button = tkinter.Button(window, text="STOP", command=close)
window.overrideredirect(True)
# window.geometry()
# window.lift()
window.wm_attributes("-topmost", True)


label.pack()
close_button.pack()
window.mainloop()

#window = Tk()
#window.wm_attributes('-transparentcolor','white')
#window.config(bg="white")
