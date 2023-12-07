#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique = set()
    for num in my_list:
        if num not in unique:
            unique.add(num)
            sum += num
    return sum
