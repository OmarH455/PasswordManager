from tkinter import *
from tkinter import messagebox
import os

class PasswordSaver:
    def __init__(self, encryption_instance):
        self.encryption = encryption_instance

    def save_password(self, website, username, password, website_entry, username_entry, password_entry):
        # Ensure the file exists
        if not os.path.exists("my_passwords.txt"):
            with open("my_passwords.txt", 'w') as file:
                pass

        if website and username and password:
            with open("my_passwords.txt", 'r') as file:
                lines = file.readlines()
            found = False
            for i in range(len(lines)):
                if self.encryption.encrypted(f"{website} | {username} ") in lines[i]:
                    found = True
                    confirm = messagebox.askyesno("Overwrite Password", f"A password for {website} with this username already exists. Do you want to overwrite it?")
                    if confirm:
                        lines[i] = self.encryption.encrypted(f"{website} | {username} | {password}\n")
                        with open("my_passwords.txt", 'w') as file:
                            file.writelines(lines)
                            messagebox.showinfo("", "The password has been updated")
                        break
            if not found:
                data = f"{website} | {username} | {password}\n"
                with open("my_passwords.txt", 'a') as file:
                    file.write(self.encryption.encrypted(data))
                    messagebox.showinfo("", "Added successfully!")

            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
