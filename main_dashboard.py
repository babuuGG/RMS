from tkinter import *
from PIL import Image, ImageTk











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

submit = Button(root, text="LOGIN", **style)
submit.place(x=200, y=280)

arko_button2 = Button(root, text="Create New User", **style)
arko_button2.place(x=270, y=280)
arko_button4 = Button(root,text="ADMIN LOGIN",**style)
arko_button4.place(x=200,y=320)

arko_button5 = Button(root, text="QUIT",**style,command=root.destroy)
arko_button5.place(x=200,y=360)
contact_us = Label(root, text="contact us:+9779765970448", fg="red", font=10)
contact_us.place(x=240, y=550)

root.mainloop()