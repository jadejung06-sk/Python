from tkinter import *

window = Tk()
window.title("Miles to kilometer converter")
# window.geometry("250x130")
window.config(padx=10, pady=15)

# mile label
mile = Label(text="Miles", fg="black")
mile.grid(column=2, row=0)
mile.config(padx= 20, pady= 15)

#mile input
mile_input = Entry(width= 10)
mile_input.grid(column=1, row=0)

# km label
km = Label(text="km", fg="black")
km.grid(column=2, row=1)
km.config(padx= 20, pady= 5)

#km input
km_input = Entry(width= 10)
km_input.insert(index =0, string = 0)
km_input.grid(column=1, row=1)

# equal label
equal = Label(text="is equal to", fg="black")
equal.grid(column=0, row=1)
equal.config(padx= 10)

# btn
def btn_clicked():
    cal_km = float(mile_input.get()) * 1.609
    # print(mile_input.get())
    km_input.insert(index=0, string = f"{round(cal_km)}")

btn = Button(text="Calculate", command= btn_clicked).grid(column=1, row = 2)

window.mainloop()