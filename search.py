from tkinter import *
from tkinter import messagebox
import os

class PasswordSearcher:
    def __init__(self, encryption_instance, forgotpass_instance):
        self.encryption = encryption_instance
        self.forgotpass = forgotpass_instance

    def search(self, website_to_find, username_to_find):
        # Ensure the file exists
        if not os.path.exists("my_passwords.txt"):
            with open("my_passwords.txt", 'w') as file:
                pass

        with open("users.txt", 'r') as file:
            lines = file.readlines()
            my_password = self.encryption.decrypt(lines[0].strip().split(" | ")[1])
        found = False
        result_text = ""

        with open("my_passwords.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    website = self.encryption.decrypt(parts[0])
                    username = self.encryption.decrypt(parts[1])
                    password = self.encryption.decrypt(parts[2])

                    if (website == website_to_find and username == username_to_find) or (website == website_to_find and not username_to_find) or (username == username_to_find and not website_to_find):
                        found = True
                        result_text += f"Website: {website} | Username: {username} | Password: {password}\n\n\n"

        if not found:
            messagebox.showerror("", "Entry not found in your passwords")
            return

        entry_window = Tk()
        entry_window.title("It is Found!!")
        entry_window.geometry("300x200")

        entry_pass = Entry(entry_window, width=25, show='*')
        entry_pass.pack()

        def sent():
            if self.forgotpass.send_password_email():
                forgot_label=Label(entry_window,text="Password sent to your email")
                forgot_label.pack()
            else:
                forgot_label=Label(entry_window,text="Failed to send password to your email\ncheck your credentials and try again" )
                forgot_label.pack()

        forgot_button = Button(entry_window, text="Forgot Password", command=(sent))
        forgot_button.pack()
        def check_search_password():
            entered_password = entry_pass.get()
            if entered_password == my_password:
                entry_window.destroy()
                sp_window = Tk()
                sp_window.geometry("400x250")
                sp_window.title("Search Results")
                result_label = Label(sp_window, text=result_text)
                result_label.pack()
            else:
                messagebox.showerror(" ", "Wrong Password!")

        search_button = Button(entry_window, text="Enter", command=check_search_password)
        search_button.pack()
