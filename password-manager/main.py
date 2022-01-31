from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
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
    pyperclip.copy(password)

# ---------------------------- SEARCHING MECHANISM ------------------------------- #


def find_password():
    website = Website_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[website]['email']
            password = data[website]['password']

    except FileNotFoundError:
        messagebox.showerror(message="No data file found.")

    except KeyError:
        messagebox.showwarning(message=f"No such {website} found in the data file.")

    else:
        messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n"
                                                        f"Password: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = Website_entry.get().title()
    username = Username_entry.get()
    password = Password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
                }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="Please don't leave any fields empty.")

    else:
        try:
            with open("data.json", "r") as file:
                # Reading data from json file storing it
                data = json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", mode="w") as file:
                # Writing the data to json file
                json.dump(new_data, file, indent=4)

        else:
            # The old data loaded i.e. read from file is than updated here using update method
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Writing the data to json file
                json.dump(data, file, indent=4)

        finally:
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
Website_entry = Entry(width=23)
Website_entry.grid(row=1, column=1, sticky=E)
Website_entry.focus()
Username_entry = Entry(width=42)
Username_entry.grid(row=2, column=1, columnspan=2, sticky=E)
Username_entry.insert(0, "paruop@gmail.com")
Password_entry = Entry(width=23)
Password_entry.grid(row=3, column=1, sticky=E)

# Button
Search_button = Button(text="Search", command=find_password, width=15)
Search_button.grid(row=1, column=2, sticky=W)
Generate_password_button = Button(text="Generate Password", command=password_generator)
Generate_password_button.grid(row=3, column=2, columnspan=1, sticky=W)
Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(row=4, column=1, columnspan=2, sticky=E)

window.mainloop()
