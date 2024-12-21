import os
import tkinter as tk
import re

class Register:
    def __init__(self, email="", password="",encryption_instance=None):
        self.email = email
        self.password = password
        self.encryption = encryption_instance

    def register(self):
        reg_window = tk.Tk()
        reg_window.title("Register")
        reg_window.geometry("300x200")

        email_label = tk.Label(reg_window, text="Email")
        email_label.pack()
        email_entry = tk.Entry(reg_window)
        email_entry.pack()

        userpass_label = tk.Label(reg_window, text="Password")
        userpass_label.pack()
        userpass_entry = tk.Entry(reg_window)
        userpass_entry.pack()

        confirm_label = tk.Label(reg_window, text="Confirm Password")
        confirm_label.pack()
        confirm_entry = tk.Entry(reg_window)
        confirm_entry.pack()

        def check_register():
            email = email_entry.get()
            password = userpass_entry.get()
            confirm = confirm_entry.get()
            email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_pattern, email):
                tk.messagebox.showerror("", "Invalid email format")

            elif password == confirm and len(password) > 0:
                self.email = email
                self.password = self.encryption.encrypted(password)
                self.confirm = confirm
                with open("users.txt", 'a') as file:
                    file.write(f"{self.email} | {self.password}\n")
                tk.messagebox.showinfo("", "Registered successfully!")
                reg_window.destroy()

            elif len(password) == 0 or len(email) == 0:
                tk.messagebox.showerror("", "Please fill in all fields")
            else:
                tk.messagebox.showerror("", "Passwords do not match")

        register_button = tk.Button(reg_window, text="Register", command=check_register)
        register_button.pack()
        reg_window.mainloop()


    def Check_user(self):
        if os.path.exists("users.txt") and os.path.getsize("users.txt") > 0:
            return True
        else:
            with open("users.txt", 'w') as file:
                return False