import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length should be at least 4."
            )
            return

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters

        if var_numbers.get():
            characters += string.digits

        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror(
                "Error",
                "Select at least one character type."
            )
            return

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid password length."
        )


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("550x450")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
)
title_label.pack(pady=20)

# Length
length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12),
    bg="#f4f6f8"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20
)
length_entry.pack(pady=10)

# Checkboxes
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(
    root,
    text="Include Letters",
    variable=var_letters,
    bg="#f4f6f8"
)
letters_check.pack()

numbers_check = tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=var_numbers,
    bg="#f4f6f8"
)
numbers_check.pack()

symbols_check = tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=var_symbols,
    bg="#f4f6f8"
)
symbols_check.pack()

# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#3498db",
    fg="white",
    font=("Arial", 12, "bold")
)
generate_button.pack(pady=15)

# Password Output
password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=35,
    justify="center"
)
password_entry.pack(pady=10)

# Copy Button
copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#2ecc71",
    fg="white",
    font=("Arial", 12, "bold")
)
copy_button.pack(pady=10)

# Footer
footer_label = tk.Label(
    root,
    text="Developed by Sai Sowmya Pamuru",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="gray"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()