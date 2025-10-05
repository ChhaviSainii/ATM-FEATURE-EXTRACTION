import tkinter as tk
import balance, withdraw, deposit, transaction

def main_menu(name):
    root = tk.Tk()
    root.title("ATM MENU")
    root.geometry("500x500")        # Fixed square window
    root.resizable(False, False)    # Prevent resizing
    root.configure(bg="#2b2b2b")    # Dark grey/black background

    # ---- Top Frame (Header) ----
    top_frame = tk.Frame(root, bg="#1a1a1a", pady=20)
    top_frame.pack(fill="x")
    tk.Label(
        top_frame,
        text=f"Welcome, {name}",font=("Helvetica", 18, "bold"),fg="white",bg="#1a1a1a").pack()

    # ---- Middle Frame (Buttons) ----
    middle_frame = tk.Frame(root, bg="#2b2b2b", pady=20)
    middle_frame.pack(fill="both", expand=True)

    # 🔹 Common Button Style
    def styled_button(text, cmd):
        btn = tk.Button(middle_frame,text=text,width=20,bg="#0080ff",fg="white",font=("Arial", 12, "bold"),bd=4,relief="raised",command=cmd)
        btn.pack(pady=12)

        # Hover effects
        btn.bind("<Enter>", lambda e: e.widget.config(bg="#004080"))
        btn.bind("<Leave>", lambda e: e.widget.config(bg="#0080ff"))
        return btn

    # ---- ATM Menu Buttons ----
    styled_button("Check Balance", lambda: balance.check_balancee(name))
    styled_button("Withdraw", lambda: withdraw.withdraw_cash(name))
    styled_button("Deposit", lambda: deposit.deposit_cash(name))
    styled_button("Transaction History", lambda: transaction.show_history(name))
    styled_button("Exit", root.destroy)

    root.mainloop()

