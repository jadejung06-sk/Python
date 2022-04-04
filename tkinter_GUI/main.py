from tkinter import *

'''
learns how to use a grid function.
'''

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Labels
label = Label(text="I Am a Label", font = ("Arial", 24, "bold"))
label.config(text="Label")
label.config(padx = 50, pady = 50)

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

button = Button(text="Click Me", command=button_clicked)
button.grid(column = 1, row = 1)
# button.pack()

## new button
new_button = Button(text="New button", command = button_clicked)
new_button.grid(column=2, row = 0)

#Entries
entry = Entry(width=10)
print(entry.get())
entry.grid(column = 3, row = 2)
# entry.pack()
window.mainloop()