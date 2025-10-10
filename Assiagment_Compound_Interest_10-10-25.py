
#Defining the values

Principal_Investment = float(input('Enter the starting Principal Investment(PV): '))
Interest_Rate = float(input('Enter the annual Interest Rate(r): '))

Compounding = float(input('How many times per year is the Interest Compounded(m)? '))
Number_of_Period = float(input('For How many years will be the Number of Periods(t)? '))

#Convert the Interest Rate from percent to decimal
rate = float(Interest_Rate/100)

#Formula FV = PV * (1 + r/m)** mt

Future_Value = float(Principal_Investment * (1.0 + rate / Compounding) ** (Number_of_Period * Compounding))

#output
print(f"At the end of {Number_of_Period} years you will have $ {Future_Value:,.2f}")
