import tkinter as tk
from tkinter import messagebox
from random import random
root=tk.Tk()
root.geometry('500x500+100+100')
root.title('辞职信')
frame1=tk.Frame(root)
frame1.pack()
tk.Label(frame1,text='尊敬的各位领导',font=24,padx=30,pady=30).pack(side=tk.LEFT,anchor=tk.N)
img=tk.PhotoImage(file='gaoci.png')
Label_img=tk.Label(frame1,image=img,padx=30,pady=30,bd=0)
Label_img.pack(side=tk.LEFT,anchor=tk.N)
tk.Label(frame1,text='辞职人:小王',height=25,font=24,padx=30,pady=30,anchor=tk.S).pack(side=tk.LEFT)
yesimg=tk.PhotoImage(file='yes.png')
noimg=tk.PhotoImage(file='no.png')
yes_btn=tk.Button(frame1,image=yesimg,bd=0)
no_btn=tk.Button(frame1,image=noimg,bd=0)
yes_btn.place(relx=0.3,rely=0.8,anchor=tk.CENTER)
no_btn.place(relx=0.7,rely=0.8,anchor=tk.CENTER)
frame2=tk.Frame(root)
# frame2.pack()
tk.Label(frame2,
        text='老板大人，臣告退了这一退，\n可能就是一辈子了\n！！！！٩(๑>◡<๑)۶ ！！！！',
        font=('黑体',18),
        justify=tk.LEFT,
        height=300,
        fg='red',
        padx=50
        ).pack()
tk.Button(frame2,text='退出',command=root.quit).place(relx=0.9,rely=0.8)
def on_exit():
  messagebox.showwarning(title='提示',message='此路不通')
root.protocol('WM_DELETE_WINDOW',on_exit)
def move(event):
  no_btn.place(relx=random(),rely=random(),anchor=tk.CENTER)
no_btn.bind('<Enter>',move)
def sure():
  frame1.pack_forget()
yes_btn.config(command=sure)
root.mainloop()