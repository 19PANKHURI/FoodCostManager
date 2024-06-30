from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_Maggie.delete(0,END)
    entry_Dosa.delete(0,END)
    entry_Pizza.delete(0,END)
    entry_Burger.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Momos.delete(0,END)
    entry_Frenchfries.delete(0,END)


def Total():
        try:a1=int(Maggie.get())
        except:a1=0

        try:a2=int(Dosa.get())
        except:a2=0

        try:a3=int(Pizza.get())
        except:a3=0
        
        try:a4=int(Burger.get())
        except:a4=0

        try:a5=int(Cookies.get())
        except:a5=0

        try:a6=int(Momos.get())
        except:a6=0

        try:a6=int(Frenchfries.get())
        except:a7=0

#cost of each item
        c1=50*a1
        c2=150*a2
        c3=250*a3
        c4=80*a4
        c5=135*a5
        c6=45*a6
        c7=40*a7


        lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
        lbl_total.place(x=0,y=50)

        entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
        entry_total.place(x=20,y=100)

        totalcost=c1+c2+c3+c4+c5+c6+c7
        string_bill="Rs.",str('%.2f' %totalcost)
        Total_bill.set(string_bill)

Label(text="Bill Management",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#menu card

f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligrapy",15,"bold"),text="Maggie.....RS.50/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Dosa.....RS.150/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Pizza.....RS.250/plate",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Burger.....RS.80/plate",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Cookies.....RS.135/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Momos.....RS.45/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Frenchfries.....RS.40/plate",fg="black",bg="lightgreen").place(x=10,y=260)


#work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Maggie=StringVar()
Dosa=StringVar()
Pizza=StringVar()
Burger=StringVar()
Cookies=StringVar()
Momos=StringVar()
Frenchfries=StringVar()

Total_bill=StringVar()

#label

lbl_Maggie=Label(f1,font=("aria",20,"bold"),text="Maggie", width=12,fg="blue4")
lbl_Dosa=Label(f1,font=("aria",20,"bold"),text="Dosa", width=12,fg="blue4")
lbl_Pizza=Label(f1,font=("aria",20,"bold"),text="Pizza", width=12,fg="blue4")
lbl_Burger=Label(f1,font=("aria",20,"bold"),text="Burger", width=12,fg="blue4")
lbl_Cookies=Label(f1,font=("aria",20,"bold"),text="Cookies", width=12,fg="blue4")
lbl_Momos=Label(f1,font=("aria",20,"bold"),text="Momos", width=12,fg="blue4")
lbl_Frenchfries=Label(f1,font=("aria",20,"bold"),text="French fries", width=12,fg="blue4")



lbl_Maggie.grid(row=1,column=0)
lbl_Dosa.grid(row=2,column=0)
lbl_Pizza.grid(row=3,column=0)
lbl_Burger.grid(row=4,column=0)
lbl_Cookies.grid(row=5,column=0)
lbl_Momos.grid(row=6,column=0)
lbl_Frenchfries.grid(row=7,column=0)


#bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)



#enter
entry_Maggie=Entry(f1,font=("aria",20,"bold"),textvariable=Maggie,bd=6,width=8,bg="lightpink")
entry_Dosa=Entry(f1,font=("aria",20,"bold"),textvariable=Dosa,bd=6,width=8,bg="lightpink")
entry_Pizza=Entry(f1,font=("aria",20,"bold"),textvariable=Pizza,bd=6,width=8,bg="lightpink")
entry_Burger=Entry(f1,font=("aria",20,"bold"),textvariable=Burger,bd=6,width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,"bold"),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_Momos=Entry(f1,font=("aria",20,"bold"),textvariable=Momos,bd=6,width=8,bg="lightpink")
entry_Frenchfries=Entry(f1,font=("aria",20,"bold"),textvariable=Frenchfries,bd=6,width=8,bg="lightpink")

entry_Maggie.grid(row=1,column=1)
entry_Dosa.grid(row=2,column=1)
entry_Pizza.grid(row=3,column=1)
entry_Burger.grid(row=4,column=1)
entry_Cookies.grid(row=5,column=1)
entry_Momos.grid(row=6,column=1)
entry_Frenchfries.grid(row=7,column=1)


#button
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'), width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'), width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)
root.mainloop()




