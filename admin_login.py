from tkinter import *
from PIL import ImageTk,Image





root = Tk()
root.title("Admin User")
root.geometry("500x500")
root.configure(bg='yellow')
bg_image = Image.open("abcd.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


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