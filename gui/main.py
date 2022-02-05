from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Labels
label = Label(text="I Am a Label", font = ("Arial", 24, "bold"))
label.config(text="New Text")

### pack / place / grid
# label.pack(side ="left")
# label.place(x = 0, y = 0) # ★
# label.place(x = 0, y = 200) # ★
# label.place(x = 100, y = 200)
label.grid(column=0, row = 0 )

#Buttons
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text = new_text)

#calls action() when pressed
button = Button(text="Click Me", command=button_clicked)
button.grid(column = 1, row = 1)
# button.pack()

#Entries
entry = Entry(width=30)
print(entry.get())
entry.grid(column = 2, row = 2)
# entry.pack()
window.mainloop()