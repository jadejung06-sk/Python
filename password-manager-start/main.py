import tkinter as tk
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webname = web_list.get()
    mail = email_list.get()
    password = pw_list.get()
    if len(webname) > 0 and len(password) > 0 :
        is_ok = messagebox.askokcancel(title= webname, message=f'There are the details entered: \nEmail: {mail}\nPassword: {password}\nIs it ok to save?')
        if is_ok:
            path = './password-manager-start/data.txt'
            with open(path, 'a') as data_file:
                data_file.write(f'{webname} | {mail} | {password}\n')
            web_list.delete(0, 'end')
            pw_list.delete(0, 'end')
    else:
        messagebox.showwarning(title= 'Oops', message = f"Please don't leave any fields empty!")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
file = './password-manager-start/logo.png'
canvas = tk.Canvas(width=200, height= 200)
logo_img = tk.PhotoImage(file = file) # ★
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column=1, row=0)

web_label = tk.Label(text = "Website: ")
web_list = tk.Entry(window, width = 35)
web_list.focus()
web_list.grid(column=1, row =1, columnspan=2) # ★
web_label.grid(column=0, row=1)

email_label = tk.Label(text = "Email/Username: ")
email_list = tk.Entry(width=35)
email_list.insert(0, "jjs0615@naver.com")
email_list.grid(column=1, row= 2, columnspan=2)
email_label.grid(column=0, row=2)

pw_label = tk.Label(text = "Password: ")
pw_list = tk.Entry(window, width = 19, show="*")
pw_list.grid(column=1, row=3)
pw_label.grid(column=0, row=3)

add_btn = tk.Button(text="Add", width = 35, command=save)
add_btn.grid(column=1, row=4, columnspan=2)
gen_pw_btn = tk.Button(text = "Generate Password")
gen_pw_btn.grid(column=2, row=3)

window.mainloop()