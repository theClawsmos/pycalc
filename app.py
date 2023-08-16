import tkinter as tk

def button_click(number):
    current = entry_var.get()
    entry_var.set(current + str(number))

def backspace():
    current = entry_var.get()
    entry_var.set(current[:-1])

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        expression = entry_var.get().replace("*", "*")  # Corrected multiplication symbol
        result = eval(expression)
        if result.is_integer():
            result = int(result)
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

root = tk.Tk()

root.geometry("300x600")
root.title("Calculator")
root.resizable(False, False)  # Prevent window resizing

canvas = tk.Canvas(root, width=300, height=600, bg="#000000")
canvas.pack()

entry_var = tk.StringVar()  # Variable to store the entry text
entry = tk.Entry(root, textvariable=entry_var, font=("Star Jedi", 20), bd=0, justify="right", bg="#111111", fg="#ffffff")
canvas.create_window(150, 70, window=entry, width=280)

buttons = [
    ("7", 50, 150), ("8", 150, 150), ("9", 250, 150),
    ("4", 50, 220), ("5", 150, 220), ("6", 250, 220),
    ("1", 50, 290), ("2", 150, 290), ("3", 250, 290),
    (".", 50, 360), ("0", 150, 360), ("Back", 250, 360),
    ("+", 50, 430), ("-", 150, 430), ("*", 250, 430),  # Changed multiplication label to "*"
    ("C", 50, 500), ("Equal", 150, 500)
]

for label, x, y in buttons:
    if label == "Back":
        button = tk.Button(root, text=label, font=("Star Jedi", 16), command=backspace, bd=0, bg="#222222", fg="#ffffff")
    elif label == "C":
        button = tk.Button(root, text=label, font=("Star Jedi", 16), command=clear_entry, bd=0, bg="#222222", fg="#ffffff")
    elif label == "Equal":
        button = tk.Button(root, text=label, font=("Star Jedi", 16), command=calculate, bd=0, bg="#3333cc", fg="#ffffff")
    else:
        button = tk.Button(root, text=label, font=("Star Jedi", 16), command=lambda label=label: button_click(label), bd=0, bg="#111111", fg="#ffffff")
    canvas.create_window(x, y, window=button, width=80, height=60)

root.mainloop()
