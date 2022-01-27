import tkinter

# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

window = tkinter.Tk()
window.title("My First GUI Programe")
window.minsize(width= 500, height = 300)

#Label
my_label = tkinter.Label(text = "I AM a Label", font = ("Arial", 24, "italic"))
my_label.pack(side = 'left')












window.mainloop()
