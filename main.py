from tkinter import *

typing = False
timer = None

def start(event):
    global typing, timer
    if typing:
        label.config(text="Keep typing or you lose it all!")
        if timer:
            window.after_cancel(timer)
        timer = window.after(5000, delete)
    else:
        typing = True

def delete():
    global typing
    label.config(text="Sorry you were not quick enough!")
    entry.delete('1.0', END)
    typing = False


window = Tk()
window.title("Disappearing Text")
window.minsize(500, 500)
window.config(pady=20, padx=20)
window.bind('<Key>', start)


label = Label(text="Start typing your masterpiece!", font=('Arial', 30))
label.pack()
entry = Text()
entry.pack()
entry.focus()

window.mainloop()