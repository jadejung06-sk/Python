import tkinter as tk
from turtle import width
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.geometry('600x500')
window.config(padx=20, pady=20)
file = './password-manager-start/logo.png'
canvas = tk.Canvas(width=200, height= 200)
logo_img = tk.PhotoImage(file = file) # ★
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column=1, row=0)

web_label = tk.Label(text = "Website: ")
web_list = tk.Entry(width = 35)
web_list.grid(column=1, row =1, columnspan=2) # ★
web_label.grid(column=0, row=1)

email_label = tk.Label(text = "Email/Username: ")
email_list = tk.Entry( width=35)
email_list.grid(column=1, row= 2, columnspan=2)
email_label.grid(column=0, row=2)

pw_label = tk.Label(text = "Password: ")
pw_list = tk.Entry(width=21)
pw_list.grid(column=1, row=3)
pw_label.grid(column=0, row=3)

add_btn = tk.Button(text="Add", width = 36)
add_btn.grid(column=1, row=4, columnspan=2)
gen_pw_btn = tk.Button(text = "Generate Password")
gen_pw_btn.grid(column=2, row=3)

window.mainloop()