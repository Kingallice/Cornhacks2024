import tkinter

def close():
    window.destroy()

window = tkinter.Tk()

label = tkinter.Label(window, text='Text on the screen', font=('ARIAL','20'), fg='black', bg='white')
close_button = tkinter.Button(window, text="STOP", command=close, relief='groove', bg='grey', fg='white')
window.overrideredirect(True)
# window.geometry()
# window.lift()
window.wm_attributes("-topmost", True)


label.pack(ipady=10, ipadx=10)
close_button.pack(pady=5)
window.mainloop()

#window = Tk()
#window.wm_attributes('-transparentcolor','white')
#window.config(bg="white")
