def add(*list_of_numbers):
    sum = 0

    for number in list_of_numbers:
        sum = sum + number

    # print("Sum:", sum)


add(3, 5)
add(4, 5, 6, 7)
add(1, 2, 3, 5, 6)
# Chicken Monkey


num = range(1, 101)
for i in num:
    if (i % 5 == 0 and i % 7 == 0):
        print('ChickenMonkey', i)
    elif (i % 5 == 0):
        print('Chicken', i)
    elif (i % 7 == 0):
        print('Monkey', i)
    else:
        print(i)
