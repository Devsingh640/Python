##########################################################################################################
# GLOBAL VARIABLES
##########################################################################################################


block_chain = []  
open_transactions = []
owner = "OM DEV SINGH"
userauth = "admin"
passauth = "admin@123"


##########################################################################################################
# UI IMPROVEMENT PRINT FUNCTIONS
##########################################################################################################


def sp():
	print(" ")


def fl():
	print("#"*100)


def dl():
	print("."*100)


def kl():
	print("="*100)


def pl():
	print("+"*100)


def print_users_available_options():
	pl()
	print("TO PROCEED SELECT FROM THE LISTED OPTIONS")
	pl()
	sp()
	print("1.) To Print Last Transaction")
	print("2.) To Create Open Transactions")
	print("3.) To print Open Transactions")
	print("4.) Exit")
	print("5.) Run crack")
	pl()
	sp()
	sp()
	sp()


def choice_input():
	dl()
	user_choice = input("Select : ")
	return user_choice


def success_transaction():
	print("Transaction Completed")


def block_chain_print():	
	print(block_chain)


def open_transactions_print():	
	print(open_transactions)


def access_deny():	
	print("Access Deny")


def access_grant():	
	print("Access Granted")
	

##########################################################################################################
# SECURITY RELATED FUNCTIONS
##########################################################################################################


def crack_test():
	block_chain[0] = 3


def user_login_in():
	while True:
		""" 
			:username: username enter by the user for login.
			:password: password entered by the user for login.
		"""
		sp()
		kl()
		username = input("Enter UserName : ")
		password = input("Enter Password : ")
		kl()
		sp()
		if userauth == username and password == passauth:
			access_grant()
			break
		else:
			access_deny()
			continue


def crack_detection_system():	
	block_index = 0
	is_valid = True
	
	for block in block_chain:
		if block_index == 0:
			block_index += 1
			continue

		elif block[0] == block_chain[block_index - 1]:
			print(block_index)
			print(block[0])
			print(block_chain[block_index])
			print(block_chain[block_index - 1])
			is_valid = True
		
		else:	
			is_valid = False
			print("Chain Had Been Compromised")
			break
		block_index += 1
	return is_valid


##########################################################################################################
# FUNCTIONS
##########################################################################################################


def user_input_to_open_a_transaction():
	""" 
		:tx_sender:    who will send coins for now set to default ie OM.
		:tx_recipient: who will get coins.
		:tx_amount:    no. of coins send in a transaction.
	"""
	tx_sender    = owner
	tx_recipient = input("Enter Recipients Name : ")
	tx_amount    = float(input("Enter Transaction Amount : "))
	return (tx_sender, tx_recipient, tx_amount)	   # sending data in tuple.


def get_last_block_chain_amount():
	return block_chain[-1]


def adding_value_to_open_transactions(this):
	open_transactions.append(this)


def adding_value_to_block_chain(last_tx, append_a_new_amount):
	block_chain.append([last_tx, append_a_new_amount])


def add_transactions(sender, recipient, amount=1.0):
	""" 
		:sender:    who will send coins.
		:recipient: who will get coins.
		:amount:    no. of coins send in a transaction default is set to 1.0.
	"""
	transaction =   { 
						'sender':    sender,
						'recipient': recipient,
						'amount':    amount
					}

	adding_value_to_open_transactions(this = transaction)
	

def mine_block():
	pass


##########################################################################################################
# MAIN PROGRAM
##########################################################################################################

user_login_in()

sp()
sp()
fl()
fl()
print("                      WELCOME TO YOUR BIT-COIN TRANSFER PORTAL")
fl()
sp()
sp()

# START OF WHILE LOOP.
while True:
	print_users_available_options()
	user_choice_is = choice_input()

	if user_choice_is == "1":
		kl()
		sp()
		block_chain_print()
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "2":
		kl()
		print("Make Your Transaction")
		kl()
		sp()
		tx_data = user_input_to_open_a_transaction()	# imported tuple here which contain multiple dats.
		tx_sender , tx_recipient, tx_amount = tx_data	# opened tupled and used its data
		print("Senders Name   : ",tx_sender)
		print("Recipient Name : ",tx_recipient)
		print("Amount Entered : ", tx_amount)
		add_transactions(sender = tx_sender, recipient = tx_recipient, amount = tx_amount)		
		success_transaction()
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "3":
		kl()
		sp()
		open_transactions_print()
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
	
	elif user_choice_is == "4":
		kl()
		sp()
		print("Exit")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
		break

	elif user_choice_is == "5":
		kl()
		sp()
		crack_test()
		print("CRACKRD")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
				
	else:
		kl()
		sp()
		print("Invalid Input")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
		
	if not crack_detection_system():
		print("Chain Had Been Compromised")
		break

	else:
		continue
# END OF WHILE LOOP.

print("All Transactions Saved")
sp()
sp()
fl()
fl()

##########################################################################################################
# END OF PROGRAM
##########################################################################################################