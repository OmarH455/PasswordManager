from tkinter import *
class PasswordViewer:
    def __init__(self, checker_instance,forgotpass_instance):
        self.checker = checker_instance
        self.forgotpass = forgotpass_instance

    def show_passwords(self):
        pass_window = Tk()
        pass_window.geometry("300x200")

        ult = Label(pass_window, text="Write your password")
        ult.pack()

        ult_entry = Entry(pass_window, width=25, show='*')
        ult_entry.pack()

        ult_button = Button(pass_window, text="Enter", command=lambda: self.checker.check_password(ult_entry, pass_window))
        ult_button.pack()


        def sent():
            if self.forgotpass.send_password_email():
                forgot_label=Label(pass_window,text="Password sent to your email")
                forgot_label.pack()
            else:
                forgot_label=Label(pass_window,text="Failed to send password to your email\ncheck your credentials and try again" )
                forgot_label.pack()
        forgot_button = Button(pass_window, text="Forgot Password", command=sent)
        forgot_button.pack()

        pass_window.mainloop()