#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # initialize two variables to store the first and second elements of each tuple
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    # check if the tuples are not empty
    if tuple_a:
        # assign the first element of tuple_a to a1
        a1 = tuple_a[0]
        # check if tuple_a has more than one element
        if len(tuple_a) > 1:
            # assign the second element of tuple_a to a2
            a2 = tuple_a[1]
    if tuple_b:
        # assign the first element of tuple_b to b1
        b1 = tuple_b[0]
        # check if tuple_b has more than one element
        if len(tuple_b) > 1:
            # assign the second element of tuple_b to b2
            b2 = tuple_b[1]
    # add the corresponding elements of each tuple and return a new tuple
    return (a1 + b1, a2 + b2)
