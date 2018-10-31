"""
A program that stores book information:
Address, Name
Order Amount, Tip Amount

User can:

View all records
Search an entry
Add entry
Update entry
Delete entries
"""

from tkinter import *
import backcode

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in backcode.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backcode.search(Address_text.get(),Name_text.get(),Order_text.get(),Tip_text.get()):
        list1.insert(END,row)
def add_command():
    backcode.insert(Address_text.get(),Name_text.get(),Order_text.get(),Tip_text.get())
    list1.delete(0,END)
    list1.insert(END,(Address_text.get(),Name_text.get(),Order_text.get(),Tip_text.get()))

def delete_command():
    backcode.delete(selected_tuple[0])

def update_command():
    backcode.update(selected_tuple[0],Address_text.get(),Name_text.get(),Order_text.get(),Tip_text.get())

window=Tk()

window.wm_title("Tip Tracker")

l1=Label(window,text="Address")
l1.grid(row=0,column=0)

l2=Label(window,text="Name")
l2.grid(row=0,column=2)

l3=Label(window,text="Order Amount")
l3.grid(row=1,column=0)

l4=Label(window,text="Tip Amount")
l4.grid(row=1,column=2)

Address_text=StringVar()
e1=Entry(window,textvariable=Address_text)
e1.grid(row=0,column=1)

Name_text=StringVar()
e2=Entry(window,textvariable=Name_text)
e2.grid(row=0,column=3)

Order_text=StringVar()
e3=Entry(window,textvariable=Order_text)
e3.grid(row=1,column=1)

Tip_text=StringVar()
e4=Entry(window,textvariable=Tip_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()