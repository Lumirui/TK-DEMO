import tkinter as tk
count=0
window=tk.Tk()
window.title('计数器')
window.geometry('200x300')
window.resizable(False,False)
def click_on():
  global count
  count+=1
  add.config(text=count+1)
click=tk.Button(window,command=click_on,text='点我数字+1')
click.grid(row=1,column=1)
add=tk.Label(window,text=0)
add.grid(row=1,column=2)
window.mainloop()