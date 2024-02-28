from tkinter import *
import mysql.connector
from tkinter import messagebox
from Create_new_user import open_win
from PIL import Image, ImageTk
from menu import Application

def login():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306", 
            user="root",
            password="Roles@3337",
            database="project",
        )
        cursor = connection.cursor()
        customer_username = e1.get()
        customer_password = e2.get()
        query = "SELECT * FROM register where customer_username= %s and customer_password = %s"
        data = (customer_username, customer_password)
        cursor.execute(query, data)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("SUCCESS", "Login succesfull.")
            root.destroy()
            app = Application()
            app.mainloop()
        else:
            messagebox.showinfo("ERROR","please enter a valid email or password")
            # Close the main window after successful login
            
            # Open the application window
            

    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

root = Tk()

root.title('BEACH SIDE RESTAURANT')
root.geometry('550x600')
root.eval("tk::PlaceWindow . center")
bg = Image.open('b.jpg')
photo = ImageTk.PhotoImage(bg)
background = Label(root, image=photo)
background.pack(fill=BOTH, expand=True)
style = {'font': ('Arial', 12), 'bg': '#2C3E50', 'fg': "white", 'bd': 5}
l1 = Label(root, text="Welcome to Beach Side Restaurant", width=30, height=2, fg="red", font=10)
l1.place(x=150, y=80)

l2 = Label(root, text="Please login to Order", width=28, height=2, fg="red")
l2.place(x=50, y=150)

uName = Label(root, text="User Name", width=16, height=2, fg="red")
uName.place(x=50, y=195)
e1 = Entry(root, width=20)
e1.place(x=200, y=195)
PW = Label(root, text="Password", width=16, height=2, fg="red")
PW.place(x=50, y=235)
e2 = Entry(root,show="*")
e2.place(x=200, y=240)

submit = Button(root, text="LOGIN", command=login, **style)
submit.place(x=200, y=280)

arko_button2 = Button(root, text="Create New User", **style, command=open_win)
arko_button2.place(x=270, y=280)

def open_store1():
    root.destroy()
    from admin_login import store1
    store1()

arko_button4 = Button(root,text="ADMIN LOGIN",**style,command=open_store1)
arko_button4.place(x=200,y=320)

arko_button5 = Button(root, text="QUIT",**style,command=root.destroy)
arko_button5.place(x=200,y=360)


def open_new_portal():
    new_window = Tk()
    new_window.title("Create a new ID")
    aaa = Label(new_window, text="Click here to make a new account")
    aaa.pack(padx=20, pady=20)

    arko_button3 = Button(new_window, text="create a new id", command=open_new_portal)
    arko_button3.pack(padx=20, pady=20)

contact_us = Label(root, text="contact us:+9779765970448", fg="red", font=10)
contact_us.place(x=240, y=550)

root.mainloop()
