'''
Python Lab 18 while loop

'''


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


userInput = input("How many iterations? ")
sequenceGenerator = 1

while int(userInput) > sequenceGenerator:
    print(Fibonacci(sequenceGenerator))
    sequenceGenerator += 1
