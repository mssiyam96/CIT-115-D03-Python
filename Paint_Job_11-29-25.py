import math

#Getting a float Input and confirm it should be positive and non-zero.

def getFloatInput(sPrompt):
    while True:
        try:
            sInput = input(sPrompt + ": ")
            fValue = float(sInput)
            
            if fValue > 0:
                return fValue
            else:
                print("Error: Value must be a positive, non-zero number. Please try again.")
                
        except ValueError:
            print("Error: Input must be a valid numeric value. Please try again.")


#Getting gallons needed to paint and round it up to the nearest whole number.
            
def getGallonsOfPaint(fWallArea, fFeetPerGallon):
    iTotalGallons = math.ceil(fWallArea / fFeetPerGallon)
    return iTotalGallons


# Getting the total labor hours.

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    fTotalHours = fLaborHoursPerGallon * iTotalGallons
    return fTotalHours


# Getting the total labor cost.

def getLaborCost(fTotalLaborHours, fLaborChargePerHour):
    fCost = fTotalLaborHours * fLaborChargePerHour
    return fCost

# Calculating the total paint cost.

def getPaintCost(iTotalGallons, fPaintPrice):
    fTotalPaintCost = iTotalGallons * fPaintPrice
    return fTotalPaintCost

# Sales tax calculations.

def getSalesTax(sState):
    
# Normalize input to uppercase for comparison.
    sState = sState.upper()
    
    if sState == "CT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0

# All calculated values and customer details.

def showCostEstimate(sLastName, iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxRate, fTotalCost):
    
    fTaxAmount = (fPaintCost + fLaborCost) * fTaxRate
    fGrandTotal = fPaintCost + fLaborCost + fTaxAmount

# Create the output string content
    sOutput = (
        
        f"{'*' * 30}\n"
        f"PAINT JOB ESTIMATE: {sLastName}\n"
        f"{'*' * 30}\n"
        f"Gallons of Paint:   {iGallons}\n"
        f"Labor Hours:        {fLaborHours:.1f}\n"
        f"Paint Charges:     ${fPaintCost:,.2f}\n"
        f"Labor Cost:        ${fLaborCost:,.2f}\n"
        f"Tax Amount:        ${fTaxAmount:,.2f}\n"
        f"{'-' * 30}\n"
        f"TOTAL COST:        ${fGrandTotal:,.2f}\n"
        f"{'*' * 30}\n"
    )

# Print to Screen
    print(sOutput)

# Write to File
    sFileName = f"{sLastName}_PaintJobOutput.txt"
    try:
        with open(sFileName, "w") as fileOutput:
            fileOutput.write(sOutput)
        print(f"File: {sFileName} is created")
    except IOError:
        print("Error: Could not write to file.")

# Creating a main function

def main():
    print("--- Paint Job Estimator ---\n")

# Input Variables (using getFloatInput for validation)

    fWallSqFt = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per Gallon")
    fFeetPerGallon = getFloatInput("Enter feet per Gallon")
    fLaborHoursPerGallon = getFloatInput("Enter labor hours per Gallon")
    fLaborChargePerHour = getFloatInput("Enter labor charge per hour")

# String Inputs
    sState = input("Enter the State (e.g., CT, MA): ")
    sLastName = input("Enter Customer Last Name: ")

# Perform Calculations using specific functions
    iTotalGallons = getGallonsOfPaint(fWallSqFt, fFeetPerGallon)
    
    fTotalLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    
# Passing the total calculated hours to get the cost
    fTotalLaborCost = getLaborCost(fTotalLaborHours, fLaborChargePerHour)
    
    fTotalPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    
    fTaxRate = getSalesTax(sState)
    
# Calculate base total (pre-tax) to pass to display function logic
    fBaseTotal = fTotalPaintCost + fTotalLaborCost

# Show Output and Save to File
    showCostEstimate(sLastName, iTotalGallons, fTotalLaborHours, 
                     fTotalPaintCost, fTotalLaborCost, fTaxRate, fBaseTotal)

# Run the program
if __name__ == "__main__":
    main()
