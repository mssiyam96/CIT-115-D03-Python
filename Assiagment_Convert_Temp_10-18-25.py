#Constants declaration
F_BOIL = 212.0
C_BOIL = 100.0

#Welcome Message
print("Welcome to the Temperature Converter by Siyam:")
print("\n\n")


#Temparature input
fTemperature = float(input("Please enter the temperature (e.g. 68.5 or 39): "))


#Unit input
sUnit = input("Is the temperature F for Fahrenheit or C for Celsius? ")

#Calculation

#Check if the unit is valid
if sUnit not in ('F', 'C', 'f', 'c'):
    print("You must enter a F/f or C/c")

else:
#Process of Fahrenheit (F) conversion
 if sUnit == 'F' or sUnit == 'f':
    #Check for upper limit
    if fTemperature > F_BOIL:
        print(f'Temp can not be > {F_BOIL:.0f}')
    else:
        #Formula Celsius: C = (5/9) * (F - 32)
        fConvertedTemp = (5.0 / 9.0) * (fTemperature - 32.0)
        
        #Output result of Celsius
        print(f'The Celsius equivalent is: {fConvertedTemp:.1f}')

 #Process of Celsius (C) conversion
 elif sUnit == 'C' or sUnit == 'c':
    #Check for upper limit
    if fTemperature > C_BOIL:
        print(f'Temp can not be > {C_BOIL:.0f}')
    else:
        #Formula Fahrenheit: F = (9/5) * C + 32
        fConvertedTemp = ((9.0 / 5.0) * fTemperature) + 32.0
        
        #Output result of Fahrenheit
        print(f'The Fahrenheit equivalent is: {fConvertedTemp:.1f}')

