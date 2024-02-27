from tkinter import *

from tkinter import messagebox


            
root = Tk()
root.title("Create a new user")
root.geometry("500x500")
root.configure(bg='yellow')
registernewcustomer=Frame(root)
registernewcustomer.pack()


Label(registernewcustomer, text="Creating a new ID", font=("Helvetica", 20)).pack(pady=10)

Label(registernewcustomer, text="customer_name").pack(pady=5)
E1= Entry(registernewcustomer, width=30) 
E1.pack(pady=5)

Label(registernewcustomer, text="customer_age").pack(pady=5)
E2=Entry(registernewcustomer, width=30)
E2.pack(pady=5)

Label(registernewcustomer, text="customer_email").pack(pady=5)
E3=Entry(registernewcustomer, width=30)
E3.pack(pady=5)

Label(registernewcustomer, text="customer_contact").pack(pady=5)
E4= Entry(registernewcustomer, width=30)
E4.pack(pady=5)

Label(registernewcustomer, text="customer_username").pack(pady=5)
E5= Entry(registernewcustomer, width=12)
E5.pack(pady=5)

Label(registernewcustomer, text="customer_password").pack(pady=5)
E6 =Entry(registernewcustomer, width=30)
E6.pack(pady=5)

style = {'font': ('Arial',12),'bg':'#2C3E50','fg':"white",'bd':5}
submit_btn = Button(registernewcustomer,text="SUBMIT",**style)
submit_btn.pack(pady=5)

back_button = Button(registernewcustomer,text="EXIT",**style,command=root.destroy)
back_button.pack(pady=6)


pass

root.mainloop()
