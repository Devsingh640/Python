radius_is = int(input('Enter radius of the circle : '))

def circle_parameters(radius):
    diameter = float(2 * radius)    # calculating cube.
    circumference = float(2 * (22/7) * radius)    # calculating circumference.
    area = float((22/7) * radius * radius )
    return(diameter, circumference, area)    # returning calculated value.


d , c , a = circle_parameters(radius = radius_is)


print('\nDiameter : ', d)
print('\nCircumference : ', c)
print('\nArea : ', a)