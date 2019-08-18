print('To rotate the list in left.')
print('')

lst1 = [1, 2, 3, 4, 5, 6, 7] 
print('Old list : ', lst1)

print('')

for n in range(0, len(lst1)):
    a = lst1[n:] + lst1[:n]  

    print(a)