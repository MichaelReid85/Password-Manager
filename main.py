import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(9, 12))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pw_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    email = email_input.get()
    password = pw_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pw_input.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="dim gray")

canvas = Canvas(width=300, height=300, bg="dim grey", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_text = Label(text="Website: ", bg="dim grey", font=("Ariel", 15, "bold"))
web_text.grid(row=1, column=0, sticky="E")
email_text = Label(text="Email/Username: ", bg="dim grey", font=("Ariel", 15, "bold"))
email_text.grid(row=2, column=0, sticky="E")
pw_text = Label(text="Password: ", bg="dim grey", font=("Ariel", 15, "bold"))
pw_text.grid(row=3, column=0, sticky="E")

# Entries
web_input = Entry(width=35, font=("Ariel", 15))
web_input.grid(row=1, column=1, columnspan=2, sticky="EW")
web_input.focus()
email_input = Entry(width=35, font=("Ariel", 15))
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "email@something.com")
pw_input = Entry(width=21, font=("Ariel", 15))
pw_input.grid(row=3, column=1, sticky="EW")


# Buttons
add_btn = Button(text="Add", bg="lime green", width=35, font=("Ariel", 13, "bold"), command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")
pw_gen = Button(text="Generate Password", bg="red", font=("Ariel", 13, "bold"), command=generate_password)
pw_gen.grid(row=3, column=2, sticky="EW")
search = Button(text="Search", bg="cyan", font=("Ariel", 13, "bold"), command=find_password)
search.grid(row=1, column=2, sticky="EW")


window.mainloop()
