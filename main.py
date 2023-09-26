from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(web_input.get()) == 0 and len(pass_input.get()) == 0 and len(user_input.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Details",
                                       message=f"These are the details entered : \nWebsite: {web_input.get()}"
                                               f" \nEmail: {user_input.get()} \nPassword: {pass_input.get()} "
                                               f" \nIs it OK to save?")
        if is_ok:
            with open("Password_Manager.txt", "a") as file:
                file.write(f"{web_input.get()} | {user_input.get()} | {pass_input.get()}\n")
                web_input.delete(0, END)
                user_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:", font=(FONT_NAME, 14))
website_label.grid(row=1, column=0)
user_name_label = Label(text="Email/UserName:", font=(FONT_NAME, 14))
user_name_label.grid(row=2, column=0)
pass_label = Label(text="Password:", font=(FONT_NAME, 14))
pass_label.grid(row=3, column=0)

# Entry
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)
pass_input = Entry(width=35)
pass_input.grid(row=3, column=1, columnspan=2)

# Buttons
gen_pass_button = Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(row=3, column=3)
add_button = Button(text="Add", width=20, command=save)
add_button.grid(row=4, column=1)

screen.mainloop()
