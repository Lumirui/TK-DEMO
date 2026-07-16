import tkinter as tk
import time
# 创建主窗口
root = tk.Tk()
root.title("时钟")
# 创建标签来显示时间
time_label = tk.Label(root, font=('Helvetica', 48), fg='black')
time_label.pack(pady=20)
# 更新时间的函数
def update_time():
   current_time = time.strftime('%H:%M:%S')
   time_label.config(text=current_time)
   root.after(1000, update_time) # 每隔1秒更新一次
# 调用更新时间的函数并运行主循环
update_time()
root.mainloop()