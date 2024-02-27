from tkinter import *

from tkinter import messagebox




root = Tk()
root.title("Admin User")
root.geometry("500x500")




register_admin = Frame(root)
register_admin.pack()

Label(register_admin, text="Welcome Admin", font=("Helvetica", 20)).pack(pady=10)

Label(register_admin, text="Username").pack(pady=5)
E1 = Entry(register_admin, width=30)
E1.pack(pady=5)

Label(register_admin, text="Admin Password").pack(pady=5)
E2 = Entry(register_admin, width=30,show="*")
E2.pack(pady=5)

submit_btn = Button(register_admin, text="SUBMIT")
submit_btn.pack(pady=5)

root.mainloop()
