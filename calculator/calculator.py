import tkinter
from tkinter import *
# from tkinter import messagebox  

root = Tk()

root.title(' Calculator ')

root.resizable(0,0)

root.iconbitmap('img.ico')


root.config(bg = '#95a5a6', width =root.winfo_screenwidth(), height =root.winfo_screenheight())

# ........................................................................................................

def btn_click(item):
    value = txt.get() + str(item)
    out.insert(END,item)
    
def equal():
    result = str(eval(out.get()))
    out.delete(0,END)
    out.insert(END,result)
    
    
def reset_value(event):
    out.delete(0,END)
    
def delete_value(event):
    data = out.get()
    out.delete(len(data)-1,END)
    
    

txt = StringVar()
 
# .........................................................................................................
out = Entry(root, width = 20, font = 'Times 25 bold', textvariable = txt,borderwidth='5',fg='red')
out.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20)



b1 = Button(root, text = '+',font=20,fg='#e67e22',width= 4,borderwidth='5',cursor='hand2',command=lambda:btn_click('+'))
b1.grid(row = 2, column =0,pady=5)

b2 = Button(root, text = '-',font=20,fg='#27ae60',width= 4,borderwidth='5',cursor='hand2',command=lambda:btn_click('-'))
b2.grid(row = 2, column = 1,pady=5)

b3 = Button(root, text = '*',font=20,fg='#9b59b6',width= 4,borderwidth='5',cursor='hand2',command=lambda:btn_click('*'))
b3.grid(row = 2, column = 2,pady=5)

b4 = Button(root, text = '/',font=20,fg='#55efc4',width= 4,borderwidth='5',cursor='hand2',command=lambda:btn_click('/'))
b4.grid(row = 2, column = 3,pady=5)

b5 = Button(root, text = '1',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(1))
b5.grid(row = 3, column =0,pady=5)

b6 = Button(root, text = '2',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(2))
b6.grid(row = 3, column = 1,pady=5)

b7 = Button(root, text = '3',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(3))
b7.grid(row = 3, column = 2,pady=5)

b8 = Button(root, text = '4',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(4))
b8.grid(row = 3, column = 3,pady=5)

b9 = Button(root, text = '5',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(5))
b9.grid(row = 4, column =0,pady=5)

b10 = Button(root, text = '6',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(6))
b10.grid(row = 4, column = 1,pady=5)

b11 = Button(root, text = '7',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(7))
b11.grid(row = 4, column = 2,pady=5)

b12 = Button(root, text = '8',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(8))
b12.grid(row = 4, column = 3,pady=5)

b13 = Button(root, text = '9',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(9))
b13.grid(row = 5, column = 0,pady=5)

b14 = Button(root, text = '0',font=20,fg='#f1c40f',width= 3,cursor='hand2',command=lambda:btn_click(0))
b14.grid(row = 5, column = 1,pady=5)

b15 = Button(root, text = 'delete',font=20,fg='#686de0',width= 12,borderwidth='5',cursor='hand2')
b15.bind('<Button-1>',delete_value)
b15.grid(row = 5, column =2, columnspan = 2,pady=5)


b17 = Button(root, text = 'reset',font=20,fg='#686de0',width= 12,borderwidth='5',cursor='hand2')
b17.bind('<Button-1>',reset_value)
b17.grid(row = 6, column =0, columnspan = 2,pady=5)

b18 = Button(root, text = '.',font=20,fg='#ff4d4d',width= 5,cursor='hand2',command=lambda:btn_click('.'))
b18.grid(row = 6, column = 2,pady=5)

b19 = Button(root, text = '=',font=20,fg='#686de0',width= 5,cursor='hand2',command=lambda:equal())
b19.grid(row = 6, column =3, columnspan = 1,pady=5)


root.mainloop()
