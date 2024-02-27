import tkinter as tk
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Beach Side Restaurant")
        self.geometry("600x600")
               
        self.background_image = Image.open("abc.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_widgets()
        self.load_menu_items()
        self.total = None
 
       
    def create_widgets(self):
        self.order_items = []
 
        self.title_label = ttk.Label(self, text="Welcome, Please Select food", font=10)
        self.title_label.place(x=40, y=30)
 
        self.item_label = ttk.Label(self, text="Select an item:", font=10)
        self.item_label.place(x=40, y=120)
 
        self.item_combobox = ttk.Combobox(self, state="readonly")
        self.item_combobox.place(x=200, y=120)
 
        self.quantity_label = ttk.Label(self, text="Enter quantity:", font=10)
        self.quantity_label.place(x=40, y=160)
 
        self.quantity_entry = ttk.Entry(self)
        self.quantity_entry.place(x=200, y=160)
 
        self.add_button = ttk.Button(self, text="Add Item", command=self.add_item)
        self.add_button.place(x=40, y=200)
 
        self.order_label = ttk.Label(self, text="Order:", font=10)
        self.order_label.place(x=40, y=250)
 
        self.order_listbox = tk.Listbox(self)
        self.order_listbox.place(x=160, y=250, width=300, height=120)
 
        self.calculate_button = ttk.Button(self, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.place(x=40, y=390)
 
        self.total_label = ttk.Label(self, text="Total amount:", font=10)
        self.total_label.place(x=40, y=430)
       
        # self.total_amount = ttk.Label(self, textvariable= self.total)
        # self.total_amount.place(x=160, y=430)
 
        self.receipt_button = ttk.Button(self, text="Print Receipt", command=self.print_receipt)
        self.receipt_button.place(x=40, y=470)
       
        self.exit_button = ttk.Button(self,text="EXIT",command=self.destroy)
        self.exit_button.place(x=40,y=500)
 
    def load_menu_items(self):
        host = 'localhost'
        user = 'root'
        password = 'Osc@r1519'
        database = 'project_oscar'
        try:
            self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
            cursor = self.conn.cursor()
            cursor.execute("SELECT item_name FROM menu")
            menu_items = [item[0] for item in cursor.fetchall()]
            self.item_combobox["values"] = menu_items
            cursor.close()
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)
 
    def add_item(self):
        item = self.item_combobox.get()
        quantity = self.quantity_entry.get()
 
        if item and quantity.isdigit():
            price = self.get_price(item)
            total = int(quantity) * price
            self.order_items.append((item, int(quantity), price, total))
            self.order_listbox.insert(tk.END, f"{item} x{quantity} ({price} x {quantity} = {total})")
            # self.quantity_entry.delete(0, tk.END)
        else:
            print("Invalid input")
 
    def get_price(self, item):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT price FROM menu WHERE item_name = %s", (item,))
            price = cursor.fetchone()[0]
            cursor.close()
            return price
        except mysql.connector.Error as e:
            print("Error fetching price:", e)
    def calculate_total(self):
        total_amount = sum(item[-1] for item in self.order_items) if self.order_items else 0
        self.total = total_amount
        self.total_label.config(text=f"Total amount: {self.total}")
 
            # else:
            #     print("Invalid input")
 
 
 
    def print_receipt(self):
        receipt_text = "Receipt:\n"
        for item, quantity, price, item_total in self.order_items:
         receipt_text += f"{item} x{quantity} ({price} x {quantity} = {item_total})\n"
         receipt_text += f"Total: {self.total}\n"
 
    # Display receipt in a messagebox
        messagebox.showinfo("Receipt", receipt_text)
 
    # Optionally, you can save the receipt to the database here if needed
        self.save_order_to_db()
 
    def save_order_to_db(self):
        try:
          cursor = self.conn.cursor()
          cursor.executemany("INSERT INTO orders(item_text, quantity, total_price, status) VALUES (%s, %s, %s, %s)",
                           [(item, quantity, item_total, 'pending') for item, quantity, _, item_total in self.order_items])
          self.conn.commit()
          cursor.close()
        except mysql.connector.Error as e:
          print("Error saving order to database:", e)
 
 
 
 
if __name__ == "__main__":
    app = Application()
    app.mainloop()