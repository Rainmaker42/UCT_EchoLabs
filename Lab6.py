'''
Calculate the change due to a customer when the cost of the product and
the amount the customer tendered is given.
'''

def calculateAmountDue(productCost, amountTendered):
    "Calculates the change due"
    changeDue = amountTendered - productCost
    if changeDue < 0:
        print("NEED MOAR MONIES")
        exit
    else:
        print("The change is ${:.2f}".format(changeDue))
    return changeDue

def calculateChangeDue(changeDue):
    "Calculates the all the change and numbers"
    dollarAmount, quarterAmount, dimeAmount, nickelAmount, centAmount = 0, 0, 0, 0, 0
    while changeDue > 0:
        if changeDue - 1.0 >= 0:
            dollarAmount += 1
            changeDue -= 1
        elif changeDue - 0.25 >= 0:
            quarterAmount += 1
            changeDue -= 0.25
        elif changeDue - 0.1 >= 0:
            dimeAmount += 1
            changeDue -= 0.1
        elif changeDue - 0.05 >= 0:
            nickelAmount += 1
            changeDue -= 0.05
        elif changeDue - 0.01 >= 0:
            centAmount += 1
            changeDue -= 0.01
    print("Give back {} dollars, {} quarters, {} dimes, {} nickels, {} pennies".format(dollarAmount, quarterAmount,
                                                                                       dimeAmount, nickelAmount,
                                                                                       centAmount))

productCost = input("The cost of the product is $")
amountTendered = input("The amount tendered is $")
productCost = float(productCost)
amountTendered = float(amountTendered)
changeDue = calculateAmountDue(productCost, amountTendered)
calculateChangeDue(changeDue)



