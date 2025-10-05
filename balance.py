import tkinter as tk
from database import add_history, check_balance


def check_balancee(name):
    root = tk.Toplevel()
    root.title("BALANCE")
    root.geometry("350x200")
    root.configure(bg="#2b2b2b")      # Dark background
    root.resizable(False, False)

    balance = check_balance(name)

    # Header
    tk.Label(
        root,
        text="Account Balance",
        font=("Helvetica", 16, "bold"),
        fg="white",
        bg="#1a1a1a",
        pady=15
    ).pack(fill="x")

    # Balance Display
    tk.Label(
        root,
        text=f"₹ {balance}",
        font=("Arial", 18, "bold"),
        fg="#00ff80",   # Bright green for money
        bg="#2b2b2b"
    ).pack(pady=30)

    add_history(name, f"Checked balance: ₹{balance}")
