'''
Python Lab 7
DECLARE and ASSIGN variable for first name
DECLARE and ASSIGN variable for last name
DECLARE and ASSIGN variable for full name which is concatenated first and last names
Print the full name
Print the initials using first and last name variables
Print the initials using the full name variable
Print letters 2-6 of the full name variable
Print the last 5 letters of the full name variable
Print the first name twice followed by the last name twice

'''

firstName = "James"
lastName = "Smith"
fullName = firstName+lastName
fullNameWithSpace = firstName + " " + lastName

print(fullName)
print("{} {}".format(firstName[:1], lastName[:1]))
print("{} {}".format(fullNameWithSpace.split()[0], fullNameWithSpace.split()[1]))
print("{} {}".format(fullName[:1], fullName[5:6]))
print("{}".format(fullName[1:6]))
print("{}".format(fullName[-5:]))
print("{}{}".format(firstName*2, lastName*2))



