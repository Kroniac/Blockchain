blockchain = []

def get_last_transaction_value():
  return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
  blockchain.append([last_transaction, transaction_amount])

def return_transaction_value():
  user_input = float(input('Your transaction amount: '))
  return user_input

def return_user_choice():
  user_input = float(input('Your choice: '))
  return user_input

def print_blockchain_elements():
  for block in blockchain:
    print('Outputting Block')
    print(block)

tx_amount = return_transaction_value()
add_value(tx_amount)

while True:
  print('Please choose')
  print('1: Add a new transaction block')
  print('2: Output the blockchain blocks')
  user_choice = return_user_choice()
  if user_choice == 1:
    tx_amount = return_transaction_value()
    add_value(tx_amount, get_last_transaction_value())
  else:
    print_blockchain_elements()




