from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
pw_input = Entry(width=21)
pw_input.grid(row=3, column=1, sticky="EW")

# Buttons
add_btn = Button(text="Add",  bg="white", width=35)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")
pw_gen = Button(text="Generate Password", bg="white")
pw_gen.grid(row=3, column=2, sticky="EW")


window.mainloop()
