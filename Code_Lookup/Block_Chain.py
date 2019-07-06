sp()
sp()
fl()
fl()
print("                      WELCOME TO YOUR BIT-COIN TRANSFER PORTAL")	#Welcome message to portal.
fl()
fl()
sp()
sp()

block_chain = []  #Initially empty list.

def sp():
	print(" ")


def fl():
	print("*************************************************************************************")


def print_users_available_options():
	print("TO PROCEED SELECT FROM BELOW OPTIONS")
	print("1.) To print last transaction")
	print("2.) Create new transaction")
	print("3.) Exit")
	print(" ")


def choice_input():
	user_choice = int(input("Choice : "))
	return user_choice

def block_chain_print():	#Print function for list.
	print(block_chain)	#This will be called to print the block list.


def get_last_block_chain_amount():	#Get function for last element element of block chain.
	return block_chain[-1]	#When called this will send last block chain value stored.


def adding_value_to_block_chain(last_tx, append_a_new_amount):	#Append function for list ie to add value to a list.
	block_chain.append([last_tx, append_a_new_amount])	#This will be called to append value to a block chain list, the value will be appended along with the last stored value of block chain list.


def success_transaction():
	print("Transaction Completed")


if block_chain == []:  #Checking weather the list is empty or not, if empty ask for the fist value.
	print(" ")
	print(" ")
	print("This Is Your First Transaction")
	print(" ")
	first_tx_amount = float(input("Enter Your First Transaction Amount : "))  #Asking for the first value of list.
	
	print("Amount Entered :",first_tx_amount)
	block_chain.append(first_tx_amount)  #Calling append function to add the user entered value to list.
	success_transaction() 

	print(" ")
	print(" ")

while True:
	print_users_available_options()
	
	user_choice_is = choice_input()

	if user_choice_is == 1:
		block_chain_print()  #Calling the print function to print list.
		print(" ")
		print(" ")

	elif user_choice_is == 2:
		tx_amount = float(input("Enter your transfer amount : "))	#Asking the for more transfer value:
		print("Amount entered :",tx_amount)
		adding_value_to_block_chain(last_tx = get_last_block_chain_amount(), append_a_new_amount = tx_amount)	#Calling append function to add the user entered value to list sending entered value. 
		success_transaction()
		print(" ")
		print(" ")

	elif user_choice_is == 3:
		print("Exit")
		break
		
	else:
		print("Invalid Choice")

print("All Transactions Saved")
print(" ")
print(" ")
print("*************************************************************************************")
print("*************************************************************************************")

