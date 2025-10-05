# ATM-FEATURE-EXTRACTION
🏦 ATM GUI System (Python + Tkinter)

An ATM Machine Simulation built with Python Tkinter for GUI and a custom database module for managing accounts.
It provides basic ATM functionalities like Login, Balance Check, Deposit, Withdraw, and Transaction History.

✨ Features

🔐 Login System (Account name based)

💰 Check Balance in real-time

➕ Deposit Cash with instant update

➖ Withdraw Cash with balance check

📜 Transaction History tracking

🎨 Attractive Tkinter GUI (square-shaped windows, labels with input fields)

🛠️ Tech Stack

Python 3

Tkinter (GUI)

Custom Database (Python dictionary / file / SQLite as backend)

📂 Project Structure
ATM-GUI/
│── database.py       # Handles account storage, balance update, history
│── atm_gui.py        # Main ATM GUI file
│── login.py          # Login window
│── balance.py        # Balance check window
│── deposit.py        # Deposit cash window
│── withdraw.py       # Withdraw cash window
│── history.py        # Transaction history window
│── README.md         # Project Documentation

🚀 How to Run

Clone this repository:

git clone https://github.com/YourUsername/ATM-GUI.git
cd ATM-GUI


Make sure Python is installed (python --version).

Run the main file:

python atm_gui.py
