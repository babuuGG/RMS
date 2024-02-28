from tkinter import *
import mysql.connector
from tkinter import messagebox

def open_win():
    def store():
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    port="3306",
                    user="root",
                    password="Roles@3337",
                    database="project",
                )
                cursor = connection.cursor()
                customer_name = E1.get()
                customer_age = E2.get()
                customer_email = E3.get()
                customer_contact= E4.get()
                customer_username = E5.get()
                customer_password = E6.get()
                query = "INSERT INTO register(customer_name,customer_age,customer_email,customer_contact,customer_username,customer_password) VALUES (%s,%s,%s,%s,%s,%s)"
                data = (customer_name,customer_age,customer_email,customer_contact,customer_username,customer_password) 
                cursor.execute(query,data)
                connection.commit()

                messagebox.showinfo("success","user is added succesfully")

            except Exception as e:
                print(f"Error:{e}")
                messagebox.showerror("Error",f"Error:{e}")    
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
            
            
root = Tk()
root.title("Create a new user")
root.geometry("500x500")
root.configure(bg='yellow') #tried every method to put a background image , but it showed error everytime
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
