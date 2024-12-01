import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
        result_label.config(text=f"Result: {result:.2f}", fg="green")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))
        result_label.config(text="Result: Error", fg="red")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  


title_label = tk.Label(root, text="Calculator", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333333")
title_label.pack(pady=20)


frame_inputs = tk.Frame(root, bg="#f0f8ff")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Enter first number:", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
entry1.grid(row=0, column=1, pady=5)

tk.Label(frame_inputs, text="Enter second number:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
entry2.grid(row=1, column=1, pady=5)


frame_buttons = tk.Frame(root, bg="#f0f8ff")
frame_buttons.pack(pady=20)

btn_style = {"font": ("Arial", 12, "bold"), "bg": "#87ceeb", "fg": "#ffffff", "width": 10, "relief": "raised"}
tk.Button(frame_buttons, text="Add", command=lambda: calculate("add"), **btn_style).grid(row=0, column=0, padx=10, pady=5)
tk.Button(frame_buttons, text="Subtract", command=lambda: calculate("subtract"), **btn_style).grid(row=0, column=1, padx=10, pady=5)
tk.Button(frame_buttons, text="Multiply", command=lambda: calculate("multiply"), **btn_style).grid(row=1, column=0, padx=10, pady=5)
tk.Button(frame_buttons, text="Divide", command=lambda: calculate("divide"), **btn_style).grid(row=1, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#333333")
result_label.pack(pady=20)

footer_label = tk.Label(root, text="Created by: Pranav Jadhav", font=("Arial", 10), bg="#f0f8ff", fg="#999999")
footer_label.pack(pady=10)

root.mainloop()



