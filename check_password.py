from tkinter import *
from tkinter import messagebox
class PasswordChecker:
    def __init__(self, encryption_instance):
        self.encryption = encryption_instance

    def check_password(self, ult_entry, pass_window):
        with open("users.txt", 'r') as file:
            lines = file.readlines()
            my_password = self.encryption.decrypt(lines[0].strip().split(" | ")[1])
        entered_password = ult_entry.get()
        if entered_password == my_password:
            dec_window = Tk()
            dec_window.title('Decrypted passwords')
            dec_window.geometry("500x650")
            y_place = 0

            with open("my_passwords.txt", 'r') as file:
                for line in file.readlines():
                    passwords = Label(dec_window, text=self.encryption.decrypt(line))
                    y_place += 25
                    passwords.place(x=0, y=y_place)
                    ult_entry.delete(0, END)
            pass_window.destroy()
        else:
            messagebox.showerror(" ", "Wrong Password!")
            pass_window.destroy()