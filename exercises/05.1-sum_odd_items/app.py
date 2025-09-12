my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(my_list):
    total = 0
    for number in my_list:
        if number % 2 != 0:
            total += number
    return total
print(sum_odds(my_list))