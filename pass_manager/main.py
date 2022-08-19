from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def gen_pass():
    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    pass_entry.insert(0, password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_text = web_entry.get()
    user_text = user_entry.get()
    pass_text = pass_entry.get()

    if web_text == "" or pass_text == "":

        messagebox.showinfo("Oops", "Please do not leave any fields empty!")
    else:
        answer = messagebox.askokcancel(
            web_text, f"These are the details entered:\nEmail: {user_text}\nPassword: {pass_text}\nIs it OK to save?")

        if answer:
            with open("data.txt", "a") as file:
                file.write(f"{web_text} | {user_text} | {pass_text}\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

pic = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=pic)

canvas.grid(row=0, column=1)


website = Label(text="Website:")
website.focus()
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)


web_entry = Entry(width=48)
web_entry.grid(row=1, column=1, columnspan=2)


user_entry = Entry(width=48)
user_entry.grid(row=2, column=1, columnspan=3)
user_entry.insert(0, "gskabdwal@gmail.com")


pass_entry = Entry(width=38)
pass_entry.grid(row=3, column=1)

gen_button = Button(text="Generate", command=gen_pass)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
