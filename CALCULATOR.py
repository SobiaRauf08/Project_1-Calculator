import tkinter as tk
from tkinter import messagebox

# Main click handler
def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            entry.delete(0, tk.END)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Hover Effects
def on_enter(e):
    e.widget["bg"] = "#707070"

def on_leave(e):
    btn = e.widget
    text = btn.cget("text")
    btn["bg"] = color_map.get(text, "#3a3a3a")

# Color map for different buttons
color_map = {
    "/": "#6a1b9a",
    "*": "#6a1b9a",
    "-": "#6a1b9a",
    "+": "#6a1b9a",
    "=": "#43a047",
    "C": "#e53935"
}

# App setup
root = tk.Tk()
root.title("Professional Calculator")
root.geometry("350x500")
root.resizable(0, 0)
root.configure(bg="#2c2f33")

# Entry field
entry = tk.Entry(root, font=("Segoe UI", 26), bd=0, bg="#1e2124", fg="white", justify="right")
entry.pack(fill=tk.BOTH, padx=20, pady=20, ipady=15)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root, bg="#2c2f33")
    frame.pack(expand=True, fill="both", padx=10, pady=5)
    for char in row:
        bg_color = color_map.get(char, "#3a3a3a")
        btn = tk.Button(
            frame, text=char, font=("Segoe UI", 18),
            fg="white", bg=bg_color, activebackground="#888888", activeforeground="white",
            relief="flat", bd=0
        )
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", click)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

root.mainloop()

