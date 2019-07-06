def sp():
	print(" ")


def fl():
	print("######################################################################################")


def dl():
	print("......................................................................................")


def kl():
	print("======================================================================================")


def pl():
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


sp()
sp()
fl()
fl()
print("                      WELCOME TO YOUR BIT-COIN TRANSFER PORTAL")
fl()
sp()
sp()


block_chain = []  


def print_users_available_options():
	pl()
	print("TO PROCEED SELECT FROM THE LISTED OPTIONS")
	pl()
	sp()
	print("1.) To Print Last Transaction")
	print("2.) Create New Transaction")
	print("3.) Exit")
	pl()
	sp()
	sp()
	sp()


def choice_input():

	dl()
	user_choice = input("Select : ")
	return user_choice

def block_chain_print():	
	print(block_chain)	

def get_last_block_chain_amount():
	return block_chain[-1]

def adding_value_to_block_chain(last_tx, append_a_new_amount):
	block_chain.append([last_tx, append_a_new_amount])


def success_transaction():
	print("Transaction Completed")


if block_chain == []:

	kl()
	print("Make Your First Transaction")
	kl()
	sp()
	first_tx_amount = float(input("Enter Your First Transaction Amount : ")) 
	print("Amount Entered :",first_tx_amount)
	block_chain.append(first_tx_amount)
	success_transaction()
	sp()
	kl()
	sp()
	sp()
	sp()

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
		print("Make Your First Transaction")
		kl()
		sp()
		tx_amount = float(input("Enter Your Transaction Amount : "))
		print("Amount Entered :",tx_amount)
		adding_value_to_block_chain(last_tx = get_last_block_chain_amount(), append_a_new_amount = tx_amount)
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
		print("Exit")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
		break
		
	else:
		kl()
		sp()
		print("Invalid Option")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

print("All Transactions Saved")

sp()
sp()
fl()
fl()

