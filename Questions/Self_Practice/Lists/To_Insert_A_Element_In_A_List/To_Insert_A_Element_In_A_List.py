print('To insert a new elements in a list.')
print('')

insert_this = int(input('Enter a number that has to be inserted in a list : '))
print('')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Orignal list is : ', a)
print('')

a.append(insert_this)
print('New list is : ', a)
