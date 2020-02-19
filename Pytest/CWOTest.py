def greet(str):
    return "Hello, {}.".format(str)


def sum_up(number):
    nums = len(str(number))
    total = 0
    for num in range(nums):
        total += int(str(number)[num])
    return total


def first_last(string):
    total = ""
    for string1 in string.split():
        total += string1[0] + string1[-1] + " "
    return total.strip()

def binary_words(string):
    total = ""
    for string1 in string.split():
        if len(string1) % 2 == 0:
            total += "0"
        else:
            total += "1"
    return total


def fast_food(list):
    food = []
    i = 0
    while i < list[0]:
        food.append("Burgers")
        i += 1
    i = 0
    while i < list[1]:
        food.append("Fries")
        i += 1
    i = 0
    while i < list[2]:
        food.append("Drinks")
        i += 1
    return food


def tacos(list):
    item = 0
    while item < len(list):
        if (list[item] != 'beef' and list[item] != 'cheese' and
            list[item] != 'lettuce' and list[item] != 'tomato'
            and list[item] != 'salsa'):
            stuff = list[item]
            list.remove(stuff)
            item -= 1
        item += 1
    return list


def groceries(list):
    list1 = []
    list2 = []
    list3 = []
    item = 0
    while item < len(list):
        if int((list[item])[:2]) < 33:
            list1.append((list[item])[3:])
        if int((list[item])[:2]) >= 33 and int((list[item])[:2]) <= 40:
            list2.append((list[item])[3:])
        if int((list[item])[:2]) > 40:
            list3.append((list[item])[3:])
        item += 1
    total = [list1, list2, list3]
    return total


def expand(num):
    total = ''
    count = 0
    while count < len(str(num)):
        if int(str(num)[count]) != 0:
            total += str(num)[count] + '0' * (len(str(num))-count-1)
            if len(str(num))-count-1 > 0:
                total += ' + '
        count += 1
    return total

print(expand(502))

def phone_filter(list):
    count = 0
    total = 0
    while count < len(list):
        if ((int(str(list[count])[5:6]) == 2 or int(str(list[count])[5:6]) == 3 or
            int(str(list[count])[5:6]) == 7) and
                ((int(str(list[count])[6:7]) == 7 or int(str(list[count])[6:7]) == 8 or
            int(str(list[count])[6:7]) == 9)) and (int(str(list[count])[7:8]) % 2 == 0)):
            total += 1
        count += 1
    return total


def word_sort(string):
    list = string.split()
    list = sorted(list, key=len)
    count = 0
    total = ""
    while count < len(list):
        total += list[count]
        total += " "
        count += 1
    return total.strip()


def box(num):
    X = 'X'
    S = ' '
    middle = ''
    list = []
    count = 0
    while count < num:
        if count == 0 or count == num-1:
            list.append(X*num)
        else:
            middle += X
            middle += S * (num-2)
            middle += X
            list.append(middle)
        count += 1
        middle = ''
    return list


def index_cipher(list):
    total = ''
    cipher = ''
    count = 0
    while count < len(list[0]):
        cipher += str(list[0])[count]
        count += 1

    count = 0
    while count < len(list[1]):
        total += cipher[int(str(((list[1]))[count]))]
        count += 1

    return total


def find_the_unique_number(list):
    total = 0
    count = 0
    while count < len(list):
        if list.count(list[count]) == 1:
            total = list[count]
            break
        count += 1
    return total


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


def simple_blackjack(list):
    count = 0
    found = 0
    while count < len(list):
        if list[count] == 11 and found == 0:
            list[count] = 1
            found = 1
        if list[count] > 11:
            return -1
        count += 1
    if sum(list) > 21:
        if found == 1:
            return (sum(list) + 10)
        else:
            return 0
    else:
        return sum(list)

