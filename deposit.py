import tkinter as tk
from tkinter import messagebox
from database import check_balance, add_history, update

def deposit_cash(name):  # deposit gui
    root = tk.Toplevel()  # child  window 
    root.title("Deposit Window")
    root.geometry("350x220")
    root.configure(bg="#2b2b2b")      # Dark grey background
    root.resizable(False, False)        # make the geometry fix

    # Header
    tk.Label(root,text="Deposit Money",font=("Helvetica", 16, "bold"),fg="white",bg="#1a1a1a",pady=10).pack(fill="x")

    # Input Label
    tk.Label(root,text="Enter Amount",font=("Arial", 12),fg="white",bg="#2b2b2b").pack(pady=15)

    amt = tk.Entry(root, font=("Arial", 12), bd=3, relief="groove")
    amt.pack(pady=5)

    def deposit():   #deposit logic
        try:
            amount = int(amt.get())     #fetch the amount
            if amount <= 0:
                raise ValueError    
            current = check_balance(name)
            update(name, current + amount)   
            messagebox.showinfo("Success", f"₹{amount} deposited successfully!")
            add_history(name, f"Deposited ₹{amount}")
            root.destroy()  # close window after deposit
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount.")

    # Styled Button
    btn = tk.Button(
        root,
        text="DEPOSIT",
        width=20,
        bg="#0080ff",
        fg="white",
        font=("Arial", 12, "bold"),
        bd=4,
        relief="raised",
        command=deposit
    )
    btn.pack(pady=20)

    # Hover Effect
    btn.bind("<Enter>", lambda e: e.widget.config(bg="#004080"))
    btn.bind("<Leave>", lambda e: e.widget.config(bg="#0080ff"))
