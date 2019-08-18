print('To reverse the list.')
print('')

lst1 = [10, 2, 12, 1, 14, 11] 
print('Old list : ', lst1)

lst1.sort()
print('New list ascending : ', lst1)

lst1 = sorted(lst1, reverse = True)
print('New list decending : ', lst1)

