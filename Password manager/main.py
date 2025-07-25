from tkinter import *
from tkinter.messagebox import showinfo,askyesno
import random
import pyperclip
import json


def website_search():
    if len(website_input.get()) != 0:
        try:
            file = open(file="data.json", mode="r")

        except FileNotFoundError:
            showinfo(message="There is currently no data in the password manager.")

        else:
            data = json.load(file)
            if website_input.get() in data:
                showinfo(title=f"{website_input.get()}", message=f"Username: {data[website_input.get()]["username"]}\n Password: {data[website_input.get()]["password"]}")
            else:
                showinfo(title=f"{website_input.get()}", message="This website does not have any data stored.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0,END)
    password_input.insert(0,password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_data():

    if len(website_input.get()) != 0 and len(emailUsername_input.get()) != 0 and len(password_input.get()) != 0:
        if askyesno(title=f"{website_input.get()}",message=f"These are the details you entered: \n\nEmail: {emailUsername_input.get()}\nPassword: {password_input.get()}\n\nSave data?"):

            new_data = {
                website_input.get(): {
                    "username": emailUsername_input.get(),
                    "password": password_input.get()
                }
            }

            try:
                file = open(file="data.json", mode="r")
                data = json.load(file)

            except FileNotFoundError:
                file = open(file = "data.json",mode="w")
                json.dump(new_data,file)

            else:
                data.update(new_data)

                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                showinfo(title="message", message="Password saved successfully.")



        else:
            showinfo(title="message", message="Password has not been saved.",icon="error")
    else:
        showinfo(title="message", message="Please fill out all the fields.",icon="error")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=40,padx=40)
window.title("Password manager")
canvas = Canvas(width=200,height=220)

img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1,row=0)


website_label = Label(text="Website: ",pady=15)
website_label.grid(column=0,row=1)

emailUsername_label = Label(text="Email/Username:",padx=20,pady=15)
emailUsername_label.grid(column=0, row=2)

password_label = Label(text="Password:",pady=15)
password_label.grid(column=0,row=3)



website_input = Entry(width=43,background="#d8e6f0")
website_input.focus()
website_input.grid(row=1,column=1)

emailUsername_input = Entry(width=43,background="#d8e6f0")
emailUsername_input.insert(0,"examplemail@gmail.com")
emailUsername_input.grid(row=2,column=1)

password_input = Entry(width=43,background="#d8e6f0")
password_input.grid(column=1,row=3)


search_button = Button(text="Search",background="#fc0303",foreground="White",width=14, command= website_search)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate password",command=generate_password ,background="#fc0303",foreground="White")
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=write_data,background="#fc0303",foreground="White")
add_button.grid(column=1,row=4,columnspan=1)



window.mainloop()