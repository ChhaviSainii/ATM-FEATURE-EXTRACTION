accounts={
    "Ravi":{ "balance": 5000, "pin": 1234, "transactions": []},    #accounts details 
    "Priya":{ "balance": 7000, "pin": 2345, "transactions": []},
    "Suresh":{"balance": 10000, "pin": 3456, "transactions": []},
    "Anita":{"balance": 3000, "pin": 4567, "transactions": []},
    "Kiran":{ "balance": 8500, "pin": 5678, "transactions": []},
    "Meena":{"balance": 12000, "pin": 6789, "transactions": []},
    "Vamsi":{ "balance": 4500, "pin": 7890, "transactions": []},
    "Rohit":{ "balance": 6000, "pin": 8901, "transactions": []},
    "Sonia":{ "balance": 9000, "pin": 9012, "transactions": []},
    "Neha":{ "balance": 11000, "pin": 1122, "transactions": []}
 }
def login(name,pin): #login function using name and pin
    if name in accounts and str(accounts[name]["pin"])==str(pin): #check for name and pin from the accounts
        return True
    return False

def check_balance(name):   
    return accounts[name]["balance"]   #return respective balance detail

def update(name, amount):
    accounts[name]["balance"]=amount  #updation of new amount

def add_history(name,record):           # add to th transaction history after every step
    accounts[name]["transactions"].append(record)

def get_history(name):
    return accounts[name]["transactions"]   #fetch all the activities 