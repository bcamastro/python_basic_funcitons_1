#countdown: takes a number, and returns a list counting down from that number to 0
def countdown(x):
    numbers = [x]
    while x> 0:
        x = x-1
        numbers.append(x)
#    print(numbers)
    return numbers
countdown(10)

#Print and Return - Create a function that will receive a list with two numbers.
#Print the first value and return the second.
def print_and_return(lst):
    if len(lst) != 2:
        print("error list must be 2 values")
    else:
        print(lst[0])
        return(lst[1])
print_and_return([2,4])
    
#First Plus Length - Create a function that accepts a list and returns the 
#sum of the first value in the list plus the list's length.
def first_plus_length (fplus):
    f_plus_l = fplus[0]+len(fplus)
#    print(f_plus_l)
    return (f_plus_l)
first_plus_length([100,2,300,4,9854972135])

"""This Length, That Value - Write a function that accepts two integers 
as parameters: size and value. The function should create and return a 
list whose length is equal to the given size, and whose values are all 
the given value."""

def length_and_value(s,v):
    landv = []
    while s > 0:
        landv.append(v)
        s = s-1
#    print(landv)
    return(landv)
length_and_value(7,5)

"""Values Greater than Second - Write a function that accepts a list and 
creates a new list containing only the values from the original list that 
are greater than its 2nd value. Print how many values this is and then return 
the new list. If the list has less than 2 elements, have the function return False"""

def values_greater_than_second(vallst):
    new_vallst = []
    if len(vallst) < 2:
        return(False)
    else:
        for x in vallst:
            if x > vallst[1]:
                new_vallst.append(x)
        print(len(new_vallst))
#        print(new_vallst)
    return new_vallst

values_greater_than_second([5,5,1,2,3,4,6,7,8,9,10])