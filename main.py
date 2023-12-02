from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    email = email_input.get()
    password = pw_input.get()

    empty = messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    if len(website) == 0 or len(password) == 0:
        return empty
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, END)
                pw_input.delete(0, END)




# Write to the data inside the entries to a data.txt file when the Add button is clicked

# Each website, email, and password combination should be on a new line inside the file.

# All fields need to be cleared after Add button is pressed


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_text = Label(text="Website: ", bg="white")
web_text.grid(row=1, column=0, sticky="E")
email_text = Label(text="Email/Username: ", bg="white")
email_text.grid(row=2, column=0, sticky="E")
pw_text = Label(text="Password: ", bg="white")
pw_text.grid(row=3, column=0, sticky="E")

# Entries
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2, sticky="EW")
web_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "email@something.com")
pw_input = Entry(width=21)
pw_input.grid(row=3, column=1, sticky="EW")

# Buttons
add_btn = Button(text="Add",  bg="white", width=35, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")
pw_gen = Button(text="Generate Password", bg="white")
pw_gen.grid(row=3, column=2, sticky="EW")


window.mainloop()
