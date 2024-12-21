from tkinter import *


class PasswordManager:
    def __init__(self):
        from generate_password import PasswordGenerator
        from save_pass import PasswordSaver
        from check_password import PasswordChecker
        from search import PasswordSearcher
        from show_passwords import PasswordViewer
        from encrypted import Encryption
        from register import Register
        from forgotpass import EmailSender

        self.encryption = Encryption()
        self.forgotpass = EmailSender(encryption_instance=self.encryption)
        self.generator = PasswordGenerator()
        self.saver = PasswordSaver(self.encryption)
        self.checker = PasswordChecker(self.encryption)
        self.searcher = PasswordSearcher(self.encryption,self.forgotpass)
        self.viewer = PasswordViewer(self.checker,self.forgotpass)
        self.register = Register(encryption_instance=self.encryption)
    def main_window(self):
        window = Tk()
        window.geometry("550x500")
        canvas = Canvas(width=450, height=350)
        img = PhotoImage(file="logo.png")
        canvas.create_image(210, 129, image=img)
        canvas.pack(side="top")

        website = Label(window, text="Website", font=("Arial", 12, "normal"))
        website.place(x=80, y=250)
        website_entry = Entry(window, width=35)
        website_entry.place(x=149, y=253)

        username = Label(window, text="Email/Username", font=("Arial", 12, "normal"))
        username.place(x=25, y=275)
        username_entry = Entry(window, width=55)
        username_entry.place(x=149, y=278)

        password_label = Label(window, text="Password", font=("Arial", 12, "normal"))
        password_label.place(x=70, y=300)
        password_entry = Entry(window, width=35)
        password_entry.place(x=149, y=303)

        password_button = Button(window, text="Generate Password", command=lambda: self.generator.generate_password(password_entry))
        password_button.place(x=370, y=298)

        save_password_button = Button(window, text="Save", command=lambda: self.saver.save_password(website_entry.get(), username_entry.get(), password_entry.get(), website_entry, username_entry, password_entry), width=47)
        save_password_button.place(x=147, y=335)

        search_button = Button(window, text="Search", command=lambda: self.searcher.search(website_entry.get(), username_entry.get()), width=15)
        search_button.place(x=370, y=250)

        show_passwords_button = Button(window, text="Show Passwords", command=self.viewer.show_passwords)
        show_passwords_button.place(x=147, y=400)

        window.mainloop()

if __name__ == "__main__":
    manager = PasswordManager()
    if not manager.register.Check_user():
        manager.register.register()
        if manager.register.Check_user():
            manager.main_window()
    else:
        manager.main_window()
