import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)
    password_list = [ random.choice(letters) for _ in range(nr_letters) ]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    random.shuffle(password_list)
    password = ''.join(password_list)
    pw_list.insert(0, string = password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
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
gen_pw_btn = tk.Button(text = "Generate Password", command = generator)
gen_pw_btn.grid(column=2, row=3)

window.mainloop()