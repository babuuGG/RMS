import tkinter as tk

from tkinter import messagebox

from PIL import ImageTk,Image


menu_window = tk.Tk()
menu_window.title("ADMIN")
menu_window.geometry("500x400")

bg_image = Image.open("abcde.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(menu_window, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

heading_label = tk.Label(menu_window, text="WELCOME ADMIN", font=("Helvetica", 14, "bold"))
heading_label.grid(row=0, column=0, padx=10, pady=10)

display_button = tk.Button(menu_window, text="Display Menu")
display_button.grid(row=1, column=0, padx=10, pady=10)

add_button = tk.Button(menu_window, text="Add Item")
add_button.grid(row=2, column=0, padx=10, pady=10)

remove_button = tk.Button(menu_window, text="Remove Item")
remove_button.grid(row=3, column=0, padx=10, pady=10)

modify_button = tk.Button(menu_window, text="Modify Item")
modify_button.grid(row=4, column=0, padx=10, pady=10)

quit_button = tk.Button(menu_window, text="Quit", command=menu_window.destroy)
quit_button.grid(row=5, column=0, padx=10, pady=10)

menu_window.mainloop()