import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CalcBeyond - Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.dark_mode = True
        self.memory = None
        self.result_var = tk.StringVar()

        self.entry = tk.Entry(
            root, textvariable=self.result_var, font=("Consolas", 24),
            bd=8, insertwidth=2, width=15, borderwidth=4, relief="ridge", justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        buttons = [
            "7", "8", "9", "/", "sin",
            "4", "5", "6", "*", "cos",
            "1", "2", "3", "-", "tan",
            "C", "0", ".", "+", "log",
            "M+", "MR", "√", "x²", "="
        ]

        row = 1
        col = 0

        for button in buttons:
            if button == "=":
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), bg="#4caf50", fg="white",
                          command=self.calculate).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
                col += 2
            elif button == "C":
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), bg="#f44336", fg="white",
                          command=self.clear).grid(row=row, column=col, padx=5, pady=5)
                col += 1
            else:
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
                          command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5)
                col += 1
                if col > 4:
                    col = 0
                    row += 1

        tk.Button(root, text="Toggle Theme", width=12, height=2, font=("Arial", 12),
                  command=self.toggle_theme).grid(row=row, column=0, columnspan=4, pady=10)

        self.apply_theme()

    def apply_theme(self):
        """Applies the selected theme."""
        if self.dark_mode:
            self.root.config(bg="#2b2b2b")
            self.entry.config(bg="#1c1c1c", fg="#ffffff", insertbackground="#ffffff")
        else:
            self.root.config(bg="#ffffff")
            self.entry.config(bg="#f5f5f5", fg="#000000", insertbackground="#000000")

    def toggle_theme(self):
        """Toggles between light and dark modes."""
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def on_button_click(self, button):
        """Handles button clicks."""
        try:
            if button == "C":
                self.result_var.set("")
            elif button == "M+":
                self.memory = float(self.result_var.get())
                messagebox.showinfo("Memory", "Value stored in memory!")
            elif button == "MR":
                if self.memory is not None:
                    self.result_var.set(str(self.memory))
                else:
                    messagebox.showwarning("Memory", "No value in memory!")
            elif button == "√":
                value = float(self.result_var.get())
                self.result_var.set(str(math.sqrt(value)))
            elif button == "x²":
                value = float(self.result_var.get())
                self.result_var.set(str(value ** 2))
            elif button == "sin":
                value = float(self.result_var.get())
                self.result_var.set(str(math.sin(math.radians(value))))
            elif button == "cos":
                value = float(self.result_var.get())
                self.result_var.set(str(math.cos(math.radians(value))))
            elif button == "tan":
                value = float(self.result_var.get())
                self.result_var.set(str(math.tan(math.radians(value))))
            elif button == "log":
                value = float(self.result_var.get())
                self.result_var.set(str(math.log10(value)))
            else:
                self.result_var.set(self.result_var.get() + button)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input!")

    def calculate(self):
        """Evaluates the expression in the entry field."""
        try:
            result = eval(self.result_var.get())
            self.result_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression!")

    def clear(self):
        """Clears the entry field."""
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    AdvancedCalculator(root)
    root.mainloop()
