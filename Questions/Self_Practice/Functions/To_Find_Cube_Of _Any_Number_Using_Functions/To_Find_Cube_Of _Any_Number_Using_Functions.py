calculate_cube_of = int(input('Enter a number whose cube is to be calculated : '))

def cube_is(b):
    cube_value_is = (b*b*b)    # calculating cube.
    return(cube_value_is)    # returning calculated value.


cube = cube_is(b = calculate_cube_of)    # called function and passed a value to it.


print('\nCube of %d is : %d' % (calculate_cube_of, cube)) # printing result using string formatting.