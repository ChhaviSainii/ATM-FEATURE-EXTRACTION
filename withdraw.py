import tkinter as tk
from tkinter import messagebox
from database import check_balance,add_history,update

def withdraw_cash(name):          # function to create separate gui for withdraw
    root=tk.Toplevel()               # mini child window
    root.title("Withdraw window") 
    root.geometry("350x350")     
    root.config(bg= "#2b2b2b")   
    root.resizable(False,False) 


   # Header line
    tk.Label(root,text="Withdraw Money",font=("Helvetica", 16, "bold"),fg="white",bg="#1a1a1a",pady=10).pack(fill="x")

     # Input             
    tk.Label(root,text="Enter Amount",font=("Arial", 12),fg="white",bg="#2b2b2b").pack(pady=10)  # box contain text, font of text,background(bg) and foreground(fg) color with the vertical space between them is 10
    amt=tk.Entry(root)  #input 
    amt.pack()


    def withdraw(): # fn with contains logic
        amountt=int(amt.get())  # fetch the input
        current=check_balance(name)  #using check_balance fn in dB retrive balance
        if current<amountt:
            messagebox.showerror("ERROR!!! ","Insufficient balance")   #show erroe if current is less than withdraw method
        else:
            update(name,current-amountt)     # update the new amount after withdraw
            messagebox.showinfo("SUCCESS...",f"{amountt} get withdraw")
            add_history(name,f"Wthdraw:{amountt}")  # add to the history
    btn = tk.Button(root,text="WITHDRAW",width=20,bg="#0080ff",fg="white",font=("Arial", 12, "bold"),bd=4,relief="raised",command=withdraw)  # creat a withdraw button which command to call the fn withdraw after clocking 
    btn.pack(pady=20)

    # Hover Effect
    btn.bind("<Enter>", lambda e: e.widget.config(bg="#004080"))  # when mouse point to the button it changes its color 
    btn.bind("<Leave>", lambda e: e.widget.config(bg="#0080ff"))  # resent again to "#0080ff" blue



