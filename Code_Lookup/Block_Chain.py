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
	print("4.) Run crack")
	pl()
	sp()
	sp()
	sp()


def crack_test():
	block_chain[0] = 3


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
		print("Make Your Transaction")
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

	elif user_choice_is == "4":
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
		print("Invalid Option")
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

print("All Transactions Saved")

sp()
sp()
fl()
fl()

