# routes.py
from flask import Blueprint, request, jsonify
from controllers import add_account, add_transaction, get_all_accounts

api = Blueprint('api', __name__)

@api.route('/add_account', methods=['POST'])
def add_account_route():
    data = request.get_json()
    add_account(data['name'], data.get('balance', 0))
    return jsonify({'message': 'New account created.'}), 201

@api.route('/add_transaction', methods=['POST'])
def add_transaction_route():
    data = request.get_json()
    success = add_transaction(data['from'], data['to'], data['amount'])
    if success:
        return jsonify({'message': 'Transaction completed.'}), 200
    else:
        return jsonify({'message': 'Insufficient balance.'}), 400

@api.route('/view_balances', methods=['GET'])
def view_balances_route():
    accounts = get_all_accounts()
    return jsonify({'accounts': [{ 'name': a.name, 'balance': a.balance } for a in accounts]}), 200