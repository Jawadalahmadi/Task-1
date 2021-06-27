

from tkinter import *


UI=Tk()
UI.title('User interface')
UI.geometry("1800x1200")
UI.configure(bg='black')

lbl=Label(UI, text="Robotic arm control panel", fg="light blue", bg="Black", font=("Times", 32))
lbl.place(x=650, y= 15)

s1 = Scale(UI, from_=0, to=180, length= 600, bg="black", fg="white",activebackground="black",highlightthickness=0, tickinterval=90, orient=HORIZONTAL)
s1.place(x=600, y=133)
lbl1=Label(UI, text="Montior 1", bg="black", fg="light blue",font=("Times", 14))
lbl1.place(x=500, y=152)

s2 = Scale(UI, from_=0, to=180, length= 600, bg="black", fg="white",activebackground="black",highlightthickness=0, tickinterval=90, orient=HORIZONTAL)
s2.place(x=600, y=266)
lbl2=Label(UI, text="Montior 2", bg="black", fg="light blue",font=("Times", 14))
lbl2.place(x=500, y=285)

s3 = Scale(UI, from_=0, to=180, length= 600, bg="black", fg="white",activebackground="black",highlightthickness=0, tickinterval=90, orient=HORIZONTAL)
s3.place(x=600, y=399)
lbl3=Label(UI, text="Montior 3", bg="black", fg="light blue",font=("Times", 14))
lbl3.place(x=500, y=418)

s4 = Scale(UI, from_=0, to=180, length= 600, bg="black", fg="white",activebackground="black",highlightthickness=0, tickinterval=90, orient=HORIZONTAL)
s4.place(x=600, y=532)
lbl4=Label(UI, text="Montior 4", bg="black", fg="light blue",font=("Times", 14))
lbl4.place(x=500, y=551)

s5 = Scale(UI, from_=0, to=180, length= 600, bg="black", fg="white",activebackground="black",highlightthickness=0, tickinterval=90, orient=HORIZONTAL)
s5.place(x=600, y=655)
lbl5=Label(UI, text="Montior 5", bg="black", fg="light blue",font=("Times", 14))
lbl5.place(x=500, y=674)

s6 = Scale(UI, from_=0, to=180, length= 600, bg="black", fg="white",activebackground="black",highlightthickness=0, tickinterval=90, orient=HORIZONTAL)
s6.place(x=600, y=799)
lbl6=Label(UI, text="Montior 6", bg="black", fg="light blue",font=("Times", 14))
lbl6.place(x=500, y=818)


btn1=Button(UI, text="Save", bg="black", fg="light blue",activebackground="black",font=("Times", 20))
btn1.place(x= 815, y=880)
btn2=Button(UI, text="Run", bg="black", fg="light blue",activebackground="black",font=("Times", 20))
btn2.place(x= 915, y=880)
UI.mainloop()
