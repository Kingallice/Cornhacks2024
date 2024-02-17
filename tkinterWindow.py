import tkinter

window = tkinter.Tk()

label = tkinter.Label(window, text='Text on the screen', font=('Times New Roman','80'), fg='black', bg='white')
window.overrideredirect(True)
window.geometry("+250+250")
window.lift()
window.wm_attributes("-topmost", True)
#window.wm_attributes("-disabled", True)
window.attributes("-fullscreen",True)
window.wm_attributes("-transparent", True)


label.pack()
label.mainloop()

#window = Tk()
#window.wm_attributes('-transparentcolor','white')
#window.config(bg="white")
