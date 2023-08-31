from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for a in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for x in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    # generated_password = ""
    # for char in password_list:
    #     generated_password += char

    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email = user_input.get()
    website = website_input.get()
    password = password_input.get()

    if email == "" or website == "" or password == "":
        messagebox.askretrycancel(title=website,
                                  message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="website",
                            message=f"These are the details entered: \nEmail: {email} \n"
                                                     f"Password: {password} \nIs it ok to save?")

        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website} | {email} | {password}\n")
            file.close()

            website_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, )
website_input.focus()

user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "buse@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
