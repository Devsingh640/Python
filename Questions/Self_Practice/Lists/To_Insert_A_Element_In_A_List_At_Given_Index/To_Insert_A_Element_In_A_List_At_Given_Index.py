print('To insert a new elements in a list at specific index.')
print('')

insert_this = int(input('Enter a number that has to be inserted in a list : '))
insert_at = int(input('Enter valid index : '))
print('')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Orignal list is : ', a)
print('')

a.insert(insert_at, insert_this)
print('New list is : ', a)
