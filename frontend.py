import tkinter
import backend

def view_command():
    lis1.delete(0,tkinter.END)
    for row in backend.view():
        lis1.insert(tkinter.END,row)

def search_command():
    lis1.delete(0,tkinter.END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
        lis1.insert(tkinter.END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    lis1.delete(0,tkinter.END)
    lis1.insert(tkinter.END,(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))
    
def delete_command():
    backend.delete(title_text.get())
    lis1.delete(0,tkinter.END)
    view_command()
    
    
window=tkinter.Tk()

window.wm_title("Amir's bookstore")
#LABELS
l1=tkinter.Label(window,text="Title")
l1.grid(row=0,column=0)

l2=tkinter.Label(window,text="Year")
l2.grid(row=1,column=0)

l3=tkinter.Label(window,text="Author")
l3.grid(row=0,column=2)

l2=tkinter.Label(window,text="ISBN")
l2.grid(row=1,column=2)

#ENTRY
title_text=tkinter.StringVar()
e1=tkinter.Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

year_text=tkinter.StringVar()
e2=tkinter.Entry(window,textvariable=year_text)
e2.grid(row=1,column=1)

author_text=tkinter.StringVar()
e3=tkinter.Entry(window,textvariable=author_text)
e3.grid(row=0,column=3)

ISBN_text=tkinter.StringVar()
e4=tkinter.Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

#BUTTONS
b1=tkinter.Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=tkinter.Button(window,text="Search All",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=tkinter.Button(window,text="Add",width=12,command=add_command)
b3.grid(row=4,column=3)

b5=tkinter.Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=tkinter.Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

#LIST BOX
lis1=tkinter.Listbox(window,height=6,width=35)
lis1.grid(row=2,column=0,rowspan=6,columnspan=2)

sc1=tkinter.Scrollbar(window)
sc1.grid(row=2,column=2,rowspan=6)

#CONFIGURE
lis1.configure(yscrollcommand=sc1.set)
sc1.configure(command=lis1.yview)

window.mainloop()