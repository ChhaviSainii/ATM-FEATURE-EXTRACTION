import tkinter as tk
from database import get_history
from tkinter import messagebox

def show_history(name):
    root=tk.Toplevel()
    root.title("Transaction Window")
    root.geometry("400x400")
    root.configure(bg="#2b2b2b")      # Dark grey background
    root.resizable(False, False)
    

    transactions=get_history(name)
    tk.Label(root,text="your transactions",font=("Helvetica", 16, "bold"),
        fg="white",
        bg="#1a1a1a",
        pady=10).pack(pady=10)

    if not transactions:
        messagebox.showinfo("No transactions yet")
    else:
        for transaction in transactions:
            tk.Label(root,text=transaction,anchor="w",font=("Helvetica", 16, "bold"),
        fg="white",
        bg="#1a1a1a",
        pady=10).pack(fill="x",padx=10)

