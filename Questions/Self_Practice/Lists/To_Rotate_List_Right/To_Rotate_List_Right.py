print('To rotate the list in right.')
print('')

lst1 = [1, 2, 3, 4, 5, 6, 7] 
l = len(lst1)
print('Old list : ', lst1)

print('')

for n in range(0, len(lst1)):
    lst1 = lst1[l-1:] + lst1[:l-1]  
    print(lst1)