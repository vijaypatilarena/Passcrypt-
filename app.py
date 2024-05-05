import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] 

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword


def generate_passwords():
    numPasswords = int(num_passwords_entry.get())

    passwordLengths = []

    for i in range(numPasswords):
        length = int(password_length_entries[i].get())
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    passwords_label.config(state="normal")
    passwords_label.delete(1.0, tk.END)
    for i in range(numPasswords):
        passwords_label.insert(tk.END, "Password #" + str(i+1) + " = " + Password[i] + "\n")
    passwords_label.config(state="disabled")


def clear_passwords():
    passwords_label.config(state="normal")
    passwords_label.delete(1.0, tk.END)
    passwords_label.config(state="disabled")


def add_password_entry():
    global num_entries
    password_entry_frame.grid_rowconfigure(num_entries + 1, weight=1)
    password_length_entry = tk.Entry(password_entry_frame, width=5, font=('Arial', 12))
    password_length_entry.grid(row=num_entries, column=1, padx=5, pady=5)
    password_length_entries.append(password_length_entry)
    num_entries += 1


def remove_password_entry():
    global num_entries
    if num_entries > 1:
        password_length_entries[-1].destroy()
        password_length_entries.pop()
        num_entries -= 1


def display_about():
    about_text = "Developer: Siddhi Gurav\n\nVersion: 1.0"
    messagebox.showinfo("About", about_text)


root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f0f0f0")

num_passwords_label = tk.Label(root, text="How many passwords do you want to generate?", bg="#f0f0f0", font=('Arial', 12))
num_passwords_label.grid(row=0, column=0, padx=5, pady=5)

num_passwords_entry = tk.Entry(root, width=5, font=('Arial', 12))
num_passwords_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords, bg="#4caf50", fg="white", font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5, bd=2)
generate_button.grid(row=0, column=2, padx=5, pady=5)

password_entry_frame = tk.Frame(root, bg="#f0f0f0")
password_entry_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

password_length_label = tk.Label(password_entry_frame, text="Password Length", bg="#f0f0f0", font=('Arial', 12))
password_length_label.grid(row=0, column=1, padx=5, pady=5)

password_length_entries = [tk.Entry(password_entry_frame, width=5, font=('Arial', 12))]
password_length_entries[0].grid(row=1, column=1, padx=5, pady=5)

num_entries = 1

add_password_entry_button = tk.Button(root, text="Add Password Entry", command=add_password_entry, bg="#2196f3", fg="white", font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5, bd=2)
add_password_entry_button.grid(row=2, column=0, padx=5, pady=5)

remove_password_entry_button = tk.Button(root, text="Remove Password Entry", command=remove_password_entry, bg="#f44336", fg="white", font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5, bd=2)
remove_password_entry_button.grid(row=2, column=1, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear Passwords", command=clear_passwords, bg="#ff9800", fg="white", font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5, bd=2)
clear_button.grid(row=2, column=2, padx=5, pady=5)

about_button = tk.Button(root, text="About", command=display_about, bg="#607d8b", fg="white", font=('Arial', 12), relief=tk.RAISED, padx=10, pady=5, bd=2)
about_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

passwords_label = tk.Text(root, height=10, width=50, font=('Arial', 12))
passwords_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
passwords_label.config(state="disabled")

root.mainloop()
