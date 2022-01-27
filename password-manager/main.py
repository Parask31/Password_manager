from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = Website_entry.get()
    username = Username_entry.get()
    password = Password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(message="Please don't leave any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Details are as follows\n"
                                                                   f"Email/Username:{username}\n"
                                                                   f"Password:{password}")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
            Website_entry.delete(0, END)
            Password_entry.delete(0, END)
        else:
            Website_entry.delete(0, END)
            Password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
Website_label = Label(text="Website:")
Website_label.grid(row=1, column=0)
Username_label = Label(text="Email/Username:")
Username_label.grid(row=2, column=0)
Password_label = Label(text="Password:")
Password_label.grid(row=3, column=0)

# Entry
Website_entry = Entry(width=42)
Website_entry.grid(row=1, column=1, columnspan=2, sticky=E)
Website_entry.focus()
Username_entry = Entry(width=42)
Username_entry.grid(row=2, column=1, columnspan=2, sticky=E)
Username_entry.insert(0, "paruop@gmail.com")
Password_entry = Entry(width=24)
Password_entry.grid(row=3, column=1, sticky=E)

# Button
Generate_password_button = Button(text="Generate Password", command=password_generator)
Generate_password_button.grid(row=3, column=2, columnspan=1, sticky=W)
Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(row=4, column=1, columnspan=2, sticky=E)

window.mainloop()
