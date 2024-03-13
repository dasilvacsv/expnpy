# controllers.py
from models import db, Account

def add_account(name, balance=0):
    new_account = Account(name=name, balance=balance)
    db.session.add(new_account)
    db.session.commit()

def add_transaction(from_account_name, to_account_name, amount):
    from_account = Account.query.filter_by(name=from_account_name).first()
    to_account = Account.query.filter_by(name=to_account_name).first()
    if from_account.balance >= amount:
        from_account.balance -= amount
        to_account.balance += amount
        db.session.commit()
        return True
    else:
        return False

def get_all_accounts():
    return Account.query.all()