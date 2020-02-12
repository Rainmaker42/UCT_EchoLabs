'''
Python Lab 8
Write a script to create an empty list called “mylist” and perform the
    following actions on the list:
-	Add one at a time and in order the following strings:  “Mickey Mantle,”
    “Ty Cobb,” and “Babe Ruth”
1	Output the list using print and str.format() function to display the
    items of the list alphabetically by first name
2	Add “Hank Aaron” to the end of the list
3	Remove the first item in the list
4	Output the list using print and str.format() function to display
    the items of the list twice
5	Remove the last item in the list
6	Output the list
The output should be similar to the output below.

'''

#not using inputs

#myList = "Micky Mantle", "Ty Cobb", "Babe Ruth"
myList = "Micky Mantle"
myList += " Ty Cobb"
myList += " Babe Ruth "

print("The list includes: " + myList)
# print("2x: { " + myList * 2 + "]")
