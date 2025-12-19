import tkinter as tk

# دالة لإضافة الرقم أو العملية
def click_button(value):
    entry.insert(tk.END, value)

# دالة لحساب الناتج
def calculate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# دالة لمسح الشاشة
def clear(event=None):
    entry.delete(0, tk.END)

# التعامل مع ضغط الكيبورد
def key_press(event):
    if event.char.isdigit() or event.char in '+-*/.':
        click_button(event.char)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    elif event.keysym.upper() == 'C':
        clear()

# نافذة رئيسية
root = tk.Tk()
root.title("iPhone Style Calculator")
root.geometry("360x500")
root.configure(bg="#1c1c1c")
root.bind("<Key>", key_press)

# شاشة العرض
entry = tk.Entry(root, font=('Helvetica', 32), bd=0, bg="#1c1c1c", fg="white", justify='right')
entry.pack(fill='both', ipadx=8, pady=20, padx=10)

# أزرار
buttons = [
    ['C', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '='],
    ['1', '2', '3', '.'],
    ['0']
]

btn_frame = tk.Frame(root, bg="#1c1c1c")
btn_frame.pack(expand=True, fill='both')

for r, row in enumerate(buttons):
    row_frame = tk.Frame(btn_frame, bg="#1c1c1c")
    row_frame.pack(expand=True, fill='both')
    for c, char in enumerate(row):
        if char == '=':
            b = tk.Button(row_frame, text=char, bg="#ff9500", fg="white", font=('Helvetica', 24),
                          bd=0, relief='ridge', command=calculate)
        elif char == 'C':
            b = tk.Button(row_frame, text=char, bg="#ff3b30", fg="white", font=('Helvetica', 24),
                          bd=0, relief='ridge', command=clear)
        elif char in ['+', '-', '*', '/']:
            b = tk.Button(row_frame, text=char, bg="#ff9500", fg="white", font=('Helvetica', 24),
                          bd=0, relief='ridge', command=lambda x=char: click_button(x))
        else:
            b = tk.Button(row_frame, text=char, bg="#333333", fg="white", font=('Helvetica', 24),
                          bd=0, relief='ridge', command=lambda x=char: click_button(x))
        b.pack(side='left', expand=True, fill='both', padx=5, pady=5)

root.mainloop()