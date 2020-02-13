'''
Python lab 19 for loop

'''

differentAnimals = "tiger", "lion", "cheetah", "panther", "mountain lion"
for animal in differentAnimals:
    print("{}".format(animal))

x = 0
incrementingNumber = 0
for x in range(0, 6):
    incrementingNumber += 10
    print(incrementingNumber)
