import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Roles@3337",
    database="Project"
)

# Create a cursor object
cursor = db.cursor()

# Function to display the menu
def display_menu():
    menu_window = tk.Toplevel()
    menu_window.title("Menu")
    menu_window.geometry('400x300')

    try:
        # Establish connection and define cursor
        # Assuming you have already done this
        
        query = "SELECT item_text, quantity, total_price FROM orders WHERE status IN ('cooking', 'served','pending')"
        cursor.execute(query)
        menu = cursor.fetchall()
        headings = ['Item', "Quantity", "Total Price"]

        for i, heading in enumerate(headings):
            tk.Label(menu_window, text=heading, font=("Helvetica", 10, 'bold')).grid(row=0, column=i, padx=5, pady=5)

        for i, item in enumerate(menu):
            name, quantity, price = item
            row_number = i + 1
            tk.Label(menu_window, text=name).grid(row=row_number, column=0, padx=5, pady=5)
            tk.Label(menu_window, text=quantity).grid(row=row_number, column=1, padx=5, pady=5)
            tk.Label(menu_window, text=price).grid(row=row_number, column=2, padx=5, pady=5)

    except Exception as e:
        print(f'Error: {e}')
# Function to add an item
def add_item():
    def add_item_to_db():
        item_id = id_entry.get()
        item_name = item_entry.get()
        price = price_entry.get()
        try:
            sql = "INSERT INTO menu (item_id, item_name, price) VALUES (%s, %s, %s)"
            val = (item_id, item_name, price)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Item added successfully")
            add_window.destroy()
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', f'Error: {e}')

    add_window = tk.Toplevel(menu_window)
    add_window.title("Add Item")
    add_window.geometry('250x200')

    id_label = tk.Label(add_window, text="Item ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(add_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    item_label = tk.Label(add_window, text="Item Name:")
    item_label.grid(row=1, column=0, padx=5, pady=5)
    item_entry = tk.Entry(add_window)
    item_entry.grid(row=1, column=1, padx=5, pady=5)

    price_label = tk.Label(add_window, text="Price:")
    price_label.grid(row=2, column=0, padx=5, pady=5)
    price_entry = tk.Entry(add_window)
    price_entry.grid(row=2, column=1, padx=5, pady=5)

    add_button = tk.Button(add_window, text="Add Item", command=add_item_to_db)
    add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
# Function to remove an item
def remove_item():
    def remove_item_from_db():
        remove_item_id = item_entry.get()
        try:
            sql = "DELETE FROM menu WHERE item_id = %s"
            val = (remove_item_id,)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Item removed successfully")
            remove_window.destroy()
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', f'Error: {e}')

    remove_window = tk.Toplevel(menu_window)
    remove_window.title("Remove Item")
    remove_window.geometry('250x100')

    item_label = tk.Label(remove_window, text="Item ID:")
    item_label.grid(row=0, column=0, padx=5, pady=5)
    item_entry = tk.Entry(remove_window)
    item_entry.grid(row=0, column=1, padx=5, pady=5)

    remove_button = tk.Button(remove_window, text="Remove Item", command=remove_item_from_db)
    remove_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Function to modify an item
def modify_item():
    def modify_item_in_db():
        modify_item_id = id_entry.get()
        modify_item_name = item_entry.get()
        modify_item_price = price_entry.get()
        try:
            sql = "UPDATE menu SET item_name = %s, price = %s WHERE item_id = %s"
            val = (modify_item_name, modify_item_price, modify_item_id)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Success", "Item modified successfully")
            modify_window.destroy()
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', f'Error: {e}')

    modify_window = tk.Toplevel(menu_window)
    modify_window.title("Modify Item")
    modify_window.geometry('250x150')

    id_label = tk.Label(modify_window, text="Item ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(modify_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    item_label = tk.Label(modify_window, text="New Item Name:")
    item_label.grid(row=1, column=0, padx=5, pady=5)
    item_entry = tk.Entry(modify_window)
    item_entry.grid(row=1, column=1, padx=5, pady=5)

    price_label = tk.Label(modify_window, text="New Price:")
    price_label.grid(row=2, column=0, padx=5, pady=5)
    price_entry = tk.Entry(modify_window)
    price_entry.grid(row=2, column=1, padx=5, pady=5)

    modify_button = tk.Button(modify_window, text="Modify Item", command=modify_item_in_db)
    modify_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Main window
menu_window = tk.Tk()
menu_window.title("ADMIN")
menu_window.geometry("500x400")

bg_image = Image.open("abcde.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(menu_window, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

heading_label = tk.Label(menu_window, text="WELCOME ADMIN", font=("Helvetica", 14, "bold"))
heading_label.grid(row=0, column=0, padx=10, pady=10)

display_button = tk.Button(menu_window, text="Display Orders", command=display_menu)
display_button.grid(row=1, column=0, padx=10, pady=10)

add_button = tk.Button(menu_window, text="Add Item", command=add_item)
add_button.grid(row=2, column=0, padx=10, pady=10)

remove_button = tk.Button(menu_window, text="Remove Item", command=remove_item)
remove_button.grid(row=3, column=0, padx=10, pady=10)

modify_button = tk.Button(menu_window, text="Modify Item", command=modify_item)
modify_button.grid(row=4, column=0, padx=10, pady=10)

quit_button = tk.Button(menu_window, text="Quit", command=menu_window.destroy)
quit_button.grid(row=5, column=0, padx=10, pady=10)

menu_window.mainloop()
