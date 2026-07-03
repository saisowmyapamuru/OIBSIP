import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Please enter positive values."
            )
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"

        elif bmi < 25:
            category = "Normal Weight"
            color = "green"

        elif bmi < 30:
            category = "Overweight"
            color = "orange"

        else:
            category = "Obese"
            color = "red"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}",
            fg=color
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter numeric values only."
        )


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x450")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 22, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
)
title_label.pack(pady=20)

# Weight
weight_label = tk.Label(
    root,
    text="Enter Weight (kg)",
    font=("Arial", 12),
    bg="#f4f6f8"
)
weight_label.pack()

weight_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
weight_entry.pack(pady=10)

# Height
height_label = tk.Label(
    root,
    text="Enter Height (m)",
    font=("Arial", 12),
    bg="#f4f6f8"
)
height_label.pack()

height_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
height_entry.pack(pady=10)

# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    width=15
)
calculate_button.pack(pady=10)

# Clear Button
clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    font=("Arial", 12, "bold"),
    bg="#7f8c8d",
    fg="white",
    width=15
)
clear_button.pack()

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#f4f6f8"
)
result_label.pack(pady=25)

# BMI Guide
guide_label = tk.Label(
    root,
    text="Underweight <18.5 | Normal 18.5-24.9 | Overweight 25-29.9 | Obese ≥30",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="gray"
)
guide_label.pack(pady=10)

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