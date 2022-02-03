import tkinter
from tkinter.ttk import Button


END = 0
# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

window = tkinter.Tk()
window.title("My First GUI Programe")
window.minsize(width= 500, height = 300)

#Label
my_label = tkinter.Label(text = "I AM a Label", font = ("Arial", 24, "italic"))
my_label.pack()
my_label['text'] = 'New Text'
my_label.config(text = "New Text")

# Button
def button_clicked():
    my_label.config(text = input.get())

button = Button(text = "Click Me", command= button_clicked) # ★
button.pack()

# Entry
input = tkinter.Entry(width=30)
input.insert(index = END, string = "Some text to begin with")
input.pack()
# my_label.config(text = input.get()) # ★

# spinbox
spinbox = tkinter.Spinbox(from_ = 0, to = 10, width = 5)
spinbox.pack()

# checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text = "Is On?", variable = checked_state, command = checkbutton_used)
checkbutton.pack()


window.mainloop()
