from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

def store1():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Roles@3337",
            database="project",
        )
        cursor = connection.cursor()

        admin_username = E1.get()
        admin_password = E2.get()
        if admin_username.upper() == "ADMIN" and admin_password == "ROOT":
            messagebox.showinfo("Success", "Login Successful. Opening Admin Portal...")
            root.destroy()
            import admin_dashboard
            admin_dashboard
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except Exception as e:
        print(f"Error:{e}")
        messagebox.showerror("Error", f"Error:{e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def open_admin_portal():
    # Destroy the current window and open the admin portal here
    root.destroy()
    # Code to open the admin portal window goes here

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

submit_btn = Button(register_admin, text="SUBMIT", command=store1)
submit_btn.pack(pady=5)

root.mainloop()
