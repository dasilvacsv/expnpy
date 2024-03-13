
accounts = {"USDT": 0, "VES": 0, "Internet": 0}

def add_account(account_name, initial_balance=0):
    accounts[account_name] = initial_balance

def add_transaction(from_account, to_account, amount):
    if amount <= accounts[from_account]:
        accounts[from_account] -= amount
        accounts[to_account] += amount
    else:
        print("Insufficient balance")

def view_balances():
    for account, balance in accounts.items():
        print(f"{account}: {balance}")

while True:
    action = input("What would you like to do? (add, view, add_account, quit): ")
    if action == "add":
        from_account = input("Enter the from account: ")
        to_account = input("Enter the to account: ")
        amount = float(input("Enter the amount: "))
        add_transaction(from_account, to_account, amount)
    elif action == "view":
        view_balances()
    elif action == "add_account":
        account_name = input("Enter the name of the new account: ")
        initial_balance = float(input("Enter the initial balance of the new account: "))
        add_account(account_name, initial_balance)
    elif action == "quit":
        break
