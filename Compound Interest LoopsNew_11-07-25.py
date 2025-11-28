#Getting Inputs for Deposits and validate them to be greater than 0 by using try-except rule

while True:
    try:
        fDeposit = float(input("Enter the Deposit(PV): "))
        if fDeposit < 0:
            print("You must enter A valid number greater than 0 ")
            continue
        if fDeposit == 0:
            print("You must enter A valid number greater than 0 ")
            continue
        break

    except ValueError:
        print("You must enter a number")

#Getting Inputs for Interest Rate and validate them to be greater than 0 by using try-except rule
        
while True:
    try:
        fInterestRatePercent = float(input("Enter the monthly Interest(r): "))
        if fInterestRatePercent < 0:
            print("You must enter A valid number greater than 0 ")
            continue
        if fInterestRatePercent == 0:
            print("You must enter A valid number greater than 0 ")
            continue
        break

    except ValueError:
        print("You must enter a number ")

#Getting Inputs for Number of Months and validate them to be greater than 0 by using try-except rule
        
while True:
    try:
        iNumMonths = float(input("Enter the month: "))
        if iNumMonths < 0:
            print("You must enter A valid number greater than 0 ")
            continue
        if iNumMonths == 0:
            print("You must enter A valid number greater than 0 ")
            continue
        break

    except ValueError:
        print("You must enter a number")
        
#Getting Inputs for Goal and validate them to be greater than or equal to 0 by using try-except rule
        
while True:
    try:
        fGoal = float(input("Enter the Goal: "))
        if fGoal < 0:
            print("You must enter A valid number greater or equals to 0 ")
            continue
        break

    except ValueError:
        print("You must enter a positive number ")


#Convert the Interest Rate from percent to decimal then convert to Monthly rate
        
fInterestRateDecimal = fInterestRatePercent / 100
fMonthlyInterestRate = fInterestRateDecimal / 12


print(f'\nMonthly interest rate: {fMonthlyInterestRate:.5f}')

#Compound the deposit over given months

print("\nCompounding Results:")
print("-----------------------------")

fBalance = fDeposit
iMonth = 1

while iMonth <= iNumMonths:
    fInterest = fBalance * fMonthlyInterestRate
    fBalance = fBalance + fInterest
    print(f'Month {iMonth}: Balance = ${fBalance:,.2f}')
    iMonth = iMonth + 1

#Predict how many months it will take to reach Goal
    
if fGoal > fDeposit:
    fPredictBalance = fDeposit
    iMonthsToGoal = 0

    while fPredictBalance < fGoal:
        fInterest = fPredictBalance * fMonthlyInterestRate
        fPredictBalance = fPredictBalance + fInterest
        iMonthsToGoal = iMonthsToGoal + 1

    print("\n----------------------------------------------")
    print(f"It will take approximately {iMonthsToGoal:,} months \n to reach your goal of ${fGoal:,.2f}")
    


#End of Program


