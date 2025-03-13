
# This program calculates an employee's productive bonus.
# """

# Intitialize variables here.
BONUS_1 = 50.00
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

employeeName = input("Enter employee's name: ")
shiftString = input("Enter number of shifts: ")
transactString = input("Enter number of Transactions: ")
dollarString = input("Enter transactions dollar value: ")

numShifts = float(shiftString)
numTransactions = float(transactString)
dollarValue = float(dollarString)
# write your code here
ProductivityScore = (dollarValue/numTransactions)/numShifts
if ProductivityScore <= 30:
    bonus =BONUS_1
elif ProductivityScore >= 31 and ProductivityScore <= 69:
    bonus = BONUS_2
elif ProductivityScore >= 70 and ProductivityScore <= 199:
    bonus = BONUS_3
elif ProductivityScore >= 200:
    bonus = BONUS_4


#Output.
print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))

