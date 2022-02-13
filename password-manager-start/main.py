import tkinter as tk
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

web_title = tk.Label(text = "Website: ")
web_list = tk.Entry()
web_list.grid(column=1, row =1 )
web_title.grid(column=0, row=1)

email_title = tk.Label(text = "Email/Username: ")
email_list = tk.Entry()
email_list.grid(column=1, row= 2)
email_title.grid(column=0, row=2)

pw_title = tk.Label(text = "Password: ")
pw_list = tk.Entry()
pw_list.grid(column=1, row=3)
pw_title.grid(column=0, row=3)

add_btn = tk.Button(text="Add", width=20)
add_btn.grid(column=1, row=4)
gen_pw_btn = tk.Button(text = "Generate Password")
gen_pw_btn.grid(column=2, row=3)

window.mainloop()