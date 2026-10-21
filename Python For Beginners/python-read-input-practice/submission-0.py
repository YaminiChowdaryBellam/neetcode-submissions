def add_two_numbers() -> int:
    two_numbers = input()
    two_list = [int(num) for num in two_numbers.split(',')]
    sum = 0
    for i in range(len(two_list)):
        sum += two_list[i]
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
