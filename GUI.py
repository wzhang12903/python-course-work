import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------
def load_data():
    try:
        df = pd.read_csv("students.csv")
        return df
    except:
        messagebox.showerror("Error", "students.csv not found!")
        return None

# -----------------------------
# Show Students
# -----------------------------
def show_students():
    df = load_data()
    if df is None:
        return

    text.delete(1.0, tk.END)
    text.insert(tk.END, "Students:\n")
    text.insert(tk.END, df.to_string(index=False))

# -----------------------------
# Show Statistics
# -----------------------------
def show_stats():
    df = load_data()
    if df is None:
        return

    avg = df["Score"].mean()
    high = df["Score"].max()
    low = df["Score"].min()

    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Average: {avg:.2f}\n")
    text.insert(tk.END, f"Highest: {high}\n")
    text.insert(tk.END, f"Lowest: {low}\n")

# -----------------------------
# Show Grades
# -----------------------------
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

def show_grades():
    df = load_data()
    if df is None:
        return

    text.delete(1.0, tk.END)
    text.insert(tk.END, "Grades:\n")

    for _, row in df.iterrows():
        grade = get_grade(row["Score"])
        text.insert(tk.END, f"{row['Name']}: {grade}\n")

# -----------------------------
# Plot Charts
# -----------------------------
def plot_scores():
    df = load_data()
    if df is None:
        return

    plt.figure()
    plt.bar(df["Name"], df["Score"])
    plt.title("Student Scores")
    plt.xlabel("Students")
    plt.ylabel("Score")
    plt.show()

# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Student Analyzer")
root.geometry("500x400")

# Buttons
btn1 = tk.Button(root, text="Show Students", command=show_students)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Show Statistics", command=show_stats)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Show Grades", command=show_grades)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Show Chart", command=plot_scores)
btn4.pack(pady=5)

# Text Area
text = tk.Text(root, height=15)
text.pack(pady=10)

# Run App
root.mainloop()
