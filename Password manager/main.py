from tkinter import *
from tkinter.messagebox import showinfo,askyesno
import random
import pyperclip
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
            with open(file="data.txt",mode="a") as file:
                file.write(f"{website_input.get()} | {emailUsername_input.get()} | {password_input.get()}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)
                showinfo(title="message", message="Password saved successfully.")

        else:
            showinfo(title="message", message="Password has not been saved.",icon="error")
    else:
        showinfo(title="message", message="Please fill out all the fields.",icon="error")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=40,padx=40)
window.title("Password manager")
canvas = Canvas(width=200,height=200)

img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1,row=0)


website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

emailUsername_label = Label(text="Email/Username:")
emailUsername_label.grid(column=0, row=2)

password_label = Label(text="Password:",pady=5)
password_label.grid(column=0,row=3)



website_input = Entry(width=43)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)

emailUsername_input = Entry(width=43)
emailUsername_input.insert(0,"examplemail@gmail.com")
emailUsername_input.grid(row=2,column=1,columnspan=2)

password_input = Entry(width=25)
password_input.grid(column=1,row=3)



generate_button = Button(text="Generate password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=write_data)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()