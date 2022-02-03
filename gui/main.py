import tkinter
from tkinter.ttk import Button
from webbrowser import get

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
    my_label.config(text = "got clicked")

button = Button(text = "Click Me", command= button_clicked) # ★
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()
print(input.get()) # ★





window.mainloop()
