my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(my_function):
    max_number = my_function[0]

    for number in my_function:
        if number > max_number:
            max_number = number

    return max_number

print(max_integer(my_list))