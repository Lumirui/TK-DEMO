# Tkinter 知识点总结

> 示例代码来源：辞职信 GUI 程序

---

## 1. 基础框架

```python
import tkinter as tk                    # 导入 tkinter 模块
root = tk.Tk()                          # 创建主窗口
root.mainloop()                         # 进入事件循环（必须放在最后）
```

---

## 2. 窗口设置

| 方法 / 属性 | 说明 | 示例 |
|---|---|---|
| `geometry()` | 设置窗口大小和位置 | `root.geometry('宽x高+X坐标+Y坐标')` |
| `title()` | 设置窗口标题 | `root.title('辞职信')` |

> `'520x500+100+100'` → 宽 520px，高 500px，距屏幕左边 100px，距屏幕上边 100px

---

## 3. Frame（框架）

- 用于**分组/容器化管理**控件，方便布局
- 必须用 `pack()` / `place()` / `grid()` 将其放置到父容器中才能显示

```python
frame1 = tk.Frame(root)    # 创建但不显示
frame1.pack()              # 显示 frame1（此处原代码被注释掉了）
frame2 = tk.Frame(root)    # 另一个 frame
frame2.pack()              # 显示 frame2
```

---

## 4. Label（标签）

```python
tk.Label(父容器, text='文本', font=字号, padx=内边距X, pady=内边距Y, fg='文字颜色', bd=边框宽度, height=高度, anchor=对齐).pack()
```

| 参数 | 说明 |
|---|---|
| `text` | 显示的文字 |
| `font` | 字体（可用数字 `24` 或元组 `('黑体',18)` |
| `fg` / `foreground` | 文字颜色 |
| `padx` / `pady` | 水平/垂直内边距 |
| `bd` / `borderwidth` | 边框宽度（`0` = 无边框） |
| `height` | 高度（⚠️ 若是 Label 且非图片，单位为**文本行数**；若是图片则为像素） |
| `anchor` | 对齐方式（`tk.N`=北/上，`tk.S`=南/下，`tk.CENTER`=居中 等） |

---

## 5. PhotoImage（图片显示）

```python
img = tk.PhotoImage(file='图片文件.png')     # 加载图片（支持 PNG / GIF）
Label_img = tk.Label(frame1, image=img)      # 通过 Label 显示图片
Button(frame1, image=img)                    # 也可以通过 Button 显示图片
```

⚠️ **注意**：图片对象必须保存在**不会被垃圾回收**的变量中（如全局变量或实例属性），否则图片不显示。

---

## 6. Button（按钮）

```python
tk.Button(父容器, image=图片, text='文本', bd=边框, command=回调函数)
```

| 参数 | 说明 |
|---|---|
| `image` | 按钮上的图片 |
| `text` | 按钮上的文字 |
| `bd` | 边框宽度（`0` = 无边框） |
| `command` | 点击时触发的函数（如 `root.quit` 退出程序） |

---

## 7. 布局管理器：`pack()`

- **盒式排列**，沿一个方向依次堆放
- `side` 参数：`tk.LEFT`（向左）、`tk.RIGHT`、`tk.TOP`（默认）、`tk.BOTTOM`
- `anchor` 参数：在分配空间内的对齐方式

```python
tk.Label(frame1, text='...').pack(side=tk.LEFT, anchor=tk.N)
```

---

## 8. 布局管理器：`place()`

- **精确/相对定位**，不受其他控件影响
- `relx` / `rely`：相对坐标（`0.0` ~ `1.0`，相对于父容器的百分比）
- `anchor`：锚点对齐

```python
btn.place(relx=0.3, rely=0.8, anchor=tk.CENTER)   # 位于父容器 30% 宽、80% 高 处
btn.place(relx=0.9, rely=0.8)                      # 位于父容器 90% 宽、80% 高 处
```

---

## 9. 重要对比速查

| 特性 | `pack()` | `place()` | `grid()` |
|---|---|---|---|
| 定位方式 | 顺序堆叠 | 精确坐标 / 相对定位 | 行列网格 |
| 适用场景 | 简单线性布局 | 精确位置控制 | 表格/表单布局 |

---

## 10. 常见小坑

1. **`frame1.pack()` 被注释掉了** → frame1 及其全部子控件都不会显示在窗口中
2. **图片变量作用域**：`img`、`yesimg`、`noimg` 必须保持在全局/实例作用域，否则被回收后图片消失
3. **`height=300` 在 Label 中**：如果显示的是文本，单位是**行数**（300 行非常高）；如果是图片才是像素
4. **混合布局**：同一个父容器内**不能混用** `pack()` 和 `grid()`，但 `pack()` 和 `place()` 可以混用（如本例）
