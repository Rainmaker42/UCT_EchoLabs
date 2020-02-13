'''
Write a program to:
Define four tuples that contains the strings “Duck”, “Bots”, “Are”, and “Awesome”.
Print each of the tuples out.
Define a dictionary with a key “ABC” and value “123”.
Print the key and value out.


'''

tupelAssignment = "Duck", "Bots", "Are", "Awesome"
print("{}\n{}\n{}\n{}\n".format(tupelAssignment[0], tupelAssignment[1],
                                tupelAssignment[2], tupelAssignment[3]))

dictionaryKey = {'A': 1, 'B': 2, 'C': 3}
for key, value in dictionaryKey.items():
    print(key, value)

print(dictionaryKey.keys())
