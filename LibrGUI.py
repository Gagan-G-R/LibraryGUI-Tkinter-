Math={1:["A",10,"M"],2:["B",20,"B"],3:["C",30,"C"]}
import matplotlib.pyplot as plt
from matplotlib import style
import tkinter
from tkinter import *
from tkinter import ttk
window=Tk()
window.configure(bg="purple")
window.title("Gagan Project")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))
Book_Name=ttk.tkinter.StringVar()
Book_Id=ttk.tkinter.IntVar()
Book_Num=ttk.tkinter.IntVar()
Book_Cat=ttk.tkinter.StringVar()
Label_0=ttk.Label(window,text="Welcome to the Library",background="purple",foreground="white")
Label_0.grid(column=0,row=0)
output=Text(window,width=100,height=25,background="pink")
output.grid(column=15,row=15)
def show():
    L='The new database is :'+"\n" 
    for i in Math:
        L=L+str(i)+":"+str(Math[i])+"\n"
    return(L)
def action_add():
    def GO_add():
        if Book_Id.get() not in Math:
            def GO_done():
                Math.update({Book_Id.get():[Book_Name.get(),Book_Num.get(),Book_Cat.get()]})
                output.delete(0.0, END)
                output.insert(END,show())
                Label_1.destroy()
                Label_3.destroy()
                Label_8.destroy()
                Button_3b.destroy()
                Label_5.destroy()
                Button_3a.destroy()
                User_Entry_1.destroy()
                User_Entry_2.destroy()
                User_Entry_3.destroy()
                User_Entry.destroy()
            Label_1=ttk.Label(window,text="Enter the name of the new book : ",background="purple",foreground="white")
            Label_1.grid(column=0,row=5)
            Label_3=ttk.Label(window,text="Enter the num of new book : ",background="purple",foreground="white")
            Label_3.grid(column=0,row=6)
            Label_8=ttk.Label(window,text="Enter the Cat of the new book : ",background="purple",foreground="white")
            Label_8.grid(column=0,row=7)
            User_Entry_1=Entry(window,width=32,textvariable=Book_Name)
            User_Entry_1.grid(column=1,row=5)
            User_Entry_2=Entry(window,width=32,textvariable=Book_Num)
            User_Entry_2.grid(column=1,row=6)
            User_Entry_3=Entry(window,width=32,textvariable=Book_Cat)
            User_Entry_3.grid(column=1,row=7)
            Button_3b=ttk.Button(window,text="SUBMIT",command=GO_done)
            Button_3b.grid(column=2,row=8)
        else:
            output.delete(0.0, END)
            output.insert(END,"The book is already present in the database")
            Label_5.destroy()
            Button_3a.destroy()
            User_Entry.destroy()
    Label_5=ttk.Label(window,text="Enter the id of the book to be Added : ",background="purple",foreground="white")
    Label_5.grid(column=0,row=4)
    User_Entry=Entry(window,width=32,textvariable=Book_Id)
    User_Entry.grid(column=1,row=4)
    Button_3a=ttk.Button(window,text="SUBMIT",command=GO_add)
    Button_3a.grid(column=2,row=4)
Button_3=ttk.Button(window,text="ADD",command=action_add)
Button_3.grid(column=0,row=2)
def action_del():
    def GO_del():
        if Book_Id.get() in Math:
            del Math[Book_Id.get()]
            output.delete(0.0, END)
            output.insert(END,show())
            User_Entry.destroy()
            Label_4.destroy()
            Button_2b.destroy()
        else:
            output.delete(0.0, END)
            output.insert(END,"That book is not present in the  database")
            User_Entry.destroy()
            Label_4.destroy()
            Button_2b.destroy()
    Label_4=ttk.Label(window,text="Enter the id of the book to be deleated : ",background="purple",foreground="white")
    Label_4.grid(column=0,row=4)
    User_Entry=Entry(window,width=32,textvariable=Book_Id)
    User_Entry.grid(column=1,row=4)
    Button_2b=ttk.Button(window,text="SUBMIT",command=GO_del)
    Button_2b.grid(column=2,row=4)
Button_2=ttk.Button(window,text="DELETE",command=action_del)
Button_2.grid(column=1,row=2)
def action_upp():
    def GO_upp():
        if Book_Id.get() in Math:
            def GO_done():
                output.delete(0.0, END)
                Math.update({Book_Id.get():[Book_Name.get(),Book_Num.get(),Book_Cat.get()]})
                output.insert(END,show())
                Label_1.destroy()
                Label_3.destroy()
                Label_8.destroy()
                Label_5.destroy()
                Button_3b.destroy()
                User_Entry_1.destroy()
                User_Entry_2.destroy()
                User_Entry_3.destroy()
                User_Entry.destroy()
                Button_3a.destroy()
            Label_1=ttk.Label(window,text="Enter the new name of the book : ",background="purple",foreground="white")
            Label_1.grid(column=0,row=5)
            Label_3=ttk.Label(window,text="Enter the new num of book : ",background="purple",foreground="white")
            Label_3.grid(column=0,row=6)
            Label_8=ttk.Label(window,text="Enter the new Cat : ",background="purple",foreground="white")
            Label_8.grid(column=0,row=7)
            User_Entry_1=Entry(window,width=32,textvariable=Book_Name)
            User_Entry_1.grid(column=1,row=5)
            User_Entry_2=Entry(window,width=32,textvariable=Book_Num)
            User_Entry_2.grid(column=1,row=6)
            User_Entry_3=Entry(window,width=32,textvariable=Book_Cat)
            User_Entry_3.grid(column=1,row=7)
            Button_3b=ttk.Button(window,text="SUBMIT",command=GO_done)
            Button_3b.grid(column=2,row=8)
        else:
            output.delete(0.0, END)
            output.insert(END,"The entered book is not there in the data base to be updated")
            Label_5.destroy()
            Button_3a.destroy()
            User_Entry.destroy()
    Label_5=ttk.Label(window,text="Enter the id of the book to be Updated : ",background="purple",foreground="white")
    Label_5.grid(column=0,row=4)
    User_Entry=Entry(window,width=32,textvariable=Book_Id)
    User_Entry.grid(column=1,row=4)
    Button_3a=ttk.Button(window,text="SUBMIT",command=GO_upp)
    Button_3a.grid(column=2,row=4)
Button_3=ttk.Button(window,text="UPDATE",command=action_upp)
Button_3.grid(column=2,row=2)
def action_search():
    def GO_id():
        count=0
        for i in Math:
            if i==Book_Id.get():
                output.delete(0.0, END)
                output.insert(END,"The is found--   "+str(i)+":"+str(Math[i]))
                count=count+1
        if count == 0:
            output.delete(0.0, END)
            output.insert(END,"The book is not ther in the Library")
        Label_5.destroy()
        User_Entry.destroy()
        Button_2b.destroy()
    Label_5=ttk.Label(window,text="Enter the id of the book to be Search : ",background="purple",foreground="white")
    Label_5.grid(column=0,row=4)
    User_Entry=Entry(window,width=32,textvariable=Book_Id)
    User_Entry.grid(column=1,row=4)
    Button_2b=ttk.Button(window,text="SUBMIT",command=GO_id)
    Button_2b.grid(column=2,row=4)
Button_2=ttk.Button(window,text="SEARCH",command=action_search)
Button_2.grid(column=3,row=2)
def action_plot():
    var1=tkinter.IntVar()
    Checkbutton(window, text="  PI graph", variable=var1).grid(row=3, column=4)
    var2=tkinter.IntVar()
    Checkbutton(window, text="Line Graph", variable=var2).grid(row=4, column=4)
    def adis():
        Button_4a.destroy()
        if var1.get()==0 and var2.get()==1:
            XX=[]
            YY=[]
            for i in Math:
                XX.append(i)
                YY.append(Math[i][1])
            plt.plot(XX,YY) 
            plt.xlabel('Book_Id')
            plt.ylabel('Nom_of_Books') 
            plt.show()
        elif var2.get()==0 and var1.get()==1:
            XX=[]
            YY=[]
            ZZ=[]
            ZC=[]
            co=0
            for i in Math:
                co=co+1
                if len(Math)%2==0:
                    if co%2==0:
                        ZZ.append("b")
                        ZC.append(0.1)
                    else:
                        ZZ.append("g")
                        ZC.append(0.0)
                else:
                    if co==0:
                        ZZ.append("b")
                        ZC.append(0.0)
                    elif co==1:
                        ZZ.append("g")
                        ZC.append(0.1)
                    elif co==2:
                        ZZ.append("y")
                        ZC.append(0.2)
                    else:
                        co=1
                        ZZ.append("b")
                        ZC.append(0.0)
                XX.append(i)
                YY.append(Math[i][1])
            plt.title('Here is ur graph')
            activities = XX
            slices = YY
            colors = ZZ 
            plt.pie(slices, labels = activities, colors=colors,startangle=90, shadow = True, explode =ZC,radius = 1.2, autopct = '%1.1f%%') 
            plt.legend() 
            plt.show()
        else:
            output.delete(0.0, END)
            output.insert(END,"dont select both")
    Button_4a=ttk.Button(window,text="SUBMIT",command=adis)
    Button_4a.grid(column=4,row=5)
Button_4=ttk.Button(window,text="PLOT",command=action_plot)
Button_4.grid(column=4,row=2)
def action_show():
    output.delete(0.0, END)
    L='The new database is :'+"\n" 
    for i in Math:
        L=L+str(i)+":"+str(Math[i])+"\n"
    output.insert(END,L)
Button_2=ttk.Button(window,text="SHOW",command=action_show)
Button_2.grid(column=5,row=2)
def action_exit():
    window.destroy()
Button_5=ttk.Button(window,text="EXIT",command=action_exit)
Button_5.grid(column=6,row=2)
window.mainloop()

