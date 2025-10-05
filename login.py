import tkinter as tk
from tkinter import messagebox
import atm_gui
from database import login

root = tk.Tk()
root.title("ATM Machine")

#  Square & fixed window
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#2b2b2b")  # Dark grey/black background

# Top Frame (still can use pack, it's separate)
top_frame = tk.Frame(root, bg="#1a1a1a", pady=20)
top_frame.pack(fill="x")
tk.Label(top_frame, text="Welcome to ATM", font=("Helvetica", 18, "bold"),
         fg="white", bg="#1a1a1a").pack()

# Middle Frame - ALL grid
middle_frame = tk.Frame(root, bg="#2b2b2b", pady=20)
middle_frame.pack(fill="both", expand=True)

# Name row
tk.Label(middle_frame, text="Name", font=("Arial",12), bg="#2b2b2b",
         fg="white", bd=2, relief="groove", width=8).grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(middle_frame, font=("Arial",12), bd=3, relief="groove", width=20)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# PIN row
tk.Label(middle_frame, text="PIN", font=("Arial",12), bg="#2b2b2b",
         fg="white", bd=2, relief="groove", width=8).grid(row=1, column=0, padx=10, pady=10, sticky="e")
pin_entry = tk.Entry(middle_frame, font=("Arial",12), bd=3, relief="groove", show="*", width=20)
pin_entry.grid(row=1, column=1, padx=10, pady=10)

# Login function
def login_to_account():
    name = name_entry.get()
    pin = pin_entry.get()
    if login(name, pin):
        root.destroy()
        atm_gui.main_menu(name)
    else:
        messagebox.showerror("Error", "Invalid Name or PIN")

# Button with hover
def on_enter(e): e.widget['bg'] = "#004080"
def on_leave(e): e.widget['bg'] = "#0080ff"

login_btn = tk.Button(middle_frame, text="Login", width=20, bg="#0080ff",
                      fg="white", font=("Arial",12,"bold"), bd=4, relief="raised",
                      command=login_to_account)
login_btn.grid(row=2, column=0, columnspan=2, pady=20)
login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

root.mainloop()
