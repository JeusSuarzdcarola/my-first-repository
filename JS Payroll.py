salary = 0
numDependents = 0
stateTax = 0
FederalTax = 0
dependentDeduction = 0
totalWithholding = 0
takehomePay = 0

#input from user
salary = float(input("Please enter your salary amount: "))
numDependents = float(input("Please enter your number of dependents: "))

# calculate stateTax here.
stateTax = salary * .065
print("State Tax: $" + str(stateTax))

#Calculate federalTax here
FederalTax = salary * .28
print("Federal Tax: $" + str(FederalTax))

#Calculate dependant Deduction here.
dependentDeduction = (salary * .025) * numDependents
print("Dependent Deduction: $" + str(dependentDeduction))

# Calculate totalwithholding here.
totalWithholding = stateTax + FederalTax + dependentDeduction

# Calculate takehomePay here.
takehomePay = salary - totalWithholding

print("Salary: $" + str(salary))
print("take Home Pay: $" + str(takehomePay))