import tkinter as tk
from tkinter import messagebox
import math


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry box
        entry = tk.Entry(self.root, textvariable=self.text_input, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Define buttons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sqrt',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+'
        ]

        # Create buttons dynamically
        row = 1
        col = 0
        for button in buttons:
            if button not in ('=', 'C', 'sqrt', '^'):
                btn = tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18),
                                command=lambda b=button: self.button_click(b))
            else:
                btn = tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18),
                                command=lambda b=button: self.special_operations(b))

            btn.grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def button_click(self, button):
        if button in '0123456789.':
            self.expression += button
        else:
            self.expression += ' ' + button + ' '
        self.text_input.set(self.expression)

    def special_operations(self, operation):
        if operation == 'C':
            self.expression = ""
            self.text_input.set(self.expression)
        elif operation == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
                self.expression = ""
                self.text_input.set("")
        elif operation == 'sqrt':
            try:
                result = str(math.sqrt(float(self.expression)))
                self.text_input.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
                self.expression = ""
                self.text_input.set("")
        elif operation == '^':
            self.expression += '**'
            self.text_input.set(self.expression)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
