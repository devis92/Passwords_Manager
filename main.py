from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import original.main as mn
import pandas as pd
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    pass_gen = mn.PassGen()
    password_entry.insert(0, pass_gen.password)
    pyperclip.copy(pass_gen.password)

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_pass():
    target_website_search = website_entry.get()
    try:
        # data = pd.read_json("data.json")
        # json_data  = data.to_dict()
        with open("data.json") as data_file:    
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if target_website_search in json_data:
            email =  json_data[target_website_search]["email"]
            password = json_data[target_website_search]["password"]
            messagebox.showinfo(title= target_website_search, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for { target_website_search } exists")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = password_entry.get()
    website_name = website_entry.get()
    username = username_entry.get()
    ####JSON FORMAT###########
    new_data = {
        website_name:{
            "email": username,
            "password": password,
        }
    }
    if len(username) == 0 or len(website_name) == 0:
        messagebox.showinfo(title="OOPS", message = "Dont leave the fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                    #saving updated data
                    json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
        
            with open("data.json", mode="w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
                
                print(data)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
    
    ######### TXT FORMAT #########
    # if len(username) == 0 or len(website_name) == 0:
    #     messagebox.showinfo(title="OOPS", message = "Dont leave the fields empty")
    # else:
    #     is_ok  = messagebox.askokcancel(  title=website_name, message=f"These are the details entered: \nEmail:{username}\nPassword: {password} \nIs it OK to save? ")
    #     if is_ok:    
    #         with open("pass_log.txt", mode="a") as file:
    #             file.write(f"{website_name} | {username} | {password}\n")
            
    #         password_entry.delete(0, END)
    #         website_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 20)
lock_img = PhotoImage(file ="logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image( 100, 100, image=lock_img)
canvas.grid( column=2, row=1)

website_label = Label(text="Website: ") 
website_label.grid( column=1, row=2, pady=5, sticky="E")

website_entry = Entry(width= 35)
website_entry.grid(column=2, row=2, sticky = "W", pady=5) #columnspan=2,

button_search = Button(text = "Search", width=13, command=search_pass)
button_search.grid(column=3, row=2, sticky = "E", pady=5)

username_label = Label(text="Email/Username: ")
username_label.grid( column=1, row=3, pady=5)

username_entry = Entry(width= 55)
username_entry.insert(END, "iqbol.adahamjonov@gmail.com")
username_entry.grid(column=2, row=3, columnspan=2,sticky = "W", pady=5)

password_label = Label(text="Password: ") 
password_label.grid( column=1, row=4, pady=5, sticky="E")

password_entry = Entry(width= 35) 
password_entry.grid(column=2, row=4, sticky = "W", pady=5)

button_gen = Button(text="Generate Password", command=password_generate)
button_gen.grid(column=3, row=4, sticky = "E", pady=5)

button_add = Button(text="Add", width=46, command= save_password)
button_add.grid(column=2, row=5, columnspan=2, sticky = "W", pady=5)
window.mainloop()
