# Constants for Grades
fA_PLUS = 97.0
fA = 94.0
fA_MINUS = 90.0
fB_PLUS = 87.0
fB = 84.0
fB_MINUS = 80.0
fC_PLUS = 77.0
fC = 74.0
fC_MINUS = 70.0
fD_PLUS = 67.0
fD = 64.0
fD_MINUS = 60.0


#Ask for Name
sPersonName = input("Enter the Student's name for the Grade Calculation: ")

#Ask for 4 Test Scores
iTest1 = int(input("Enter Test 1(whole number): "))
iTest2 = int(input("Enter Test 2(whole number): "))
iTest3 = int(input("Enter Test 3(whole number): "))
iTest4 = int(input("Enter Test 4(whole number): "))

#Prompt for Drop Lowest Option
#Convert input to uppercase immediately for concise comparison
sDropLowest = input("Do you wish to Drop the lowest Grade (Y or N)? ").upper()

#Check for Negative Test Scores
# Use logical OR for efficient checking of all four variables in one statement.
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    exit() # Stop the program

#Check Drop Lowest Input (Must be Y or N)
    
if sDropLowest != 'Y' and sDropLowest != 'N':
    print("Enter Y or N to Drop the Lowest Grade.")
    exit() # Stop the program


#Calculate total sum once
iTotalSum = iTest1 + iTest2 + iTest3 + iTest4 

if sDropLowest == 'Y':
    #Determine the Lowest Score
    
    #Initialize iLowestScore to the first test score
    iLowestScore = iTest1
    
    #Use sequential IF statements to update the lowest score (more efficient than nested IF/ELIF)
    if iTest2 < iLowestScore:
        iLowestScore = iTest2
        
    if iTest3 < iLowestScore:
        iLowestScore = iTest3
        
    if iTest4 < iLowestScore:
        iLowestScore = iTest4
        
    #Calculating the average by subtracting the lowest and dividing by 3.0
    fAverage = (iTotalSum - iLowestScore) / 3.0
    
else: #Drop Lowest must be 'N' due to prior validation
    #Average of 4 test scores
    fAverage = iTotalSum / 4.0

#Determine Letter Grade (checking from highest to lowest)

if fAverage >= fA_PLUS:
    sLetterGrade = "A+"
elif fAverage >= fA: 
    sLetterGrade = "A"
elif fAverage >= fA_MINUS: 
    sLetterGrade = "A-"
elif fAverage >= fB_PLUS: 
    sLetterGrade = "B+"
elif fAverage >= fB: 
    sLetterGrade = "B"
elif fAverage >= fB_MINUS: 
    sLetterGrade = "B-"
elif fAverage >= fC_PLUS: 
    sLetterGrade = "C+"
elif fAverage >= fC: 
    sLetterGrade = "C"
elif fAverage >= fC_MINUS: 
    sLetterGrade = "C-"
elif fAverage >= fD_PLUS: 
    sLetterGrade = "D+"
elif fAverage >= fD: 
    sLetterGrade = "D"
elif fAverage >= fD_MINUS: 
    sLetterGrade = "D-"
else: 
    sLetterGrade = "F" #59.9 or less
    
#Output Results (Formatted to 1 decimal position)

print("-" * 35)
print("GRADE ANALYZER RESULTS")
print("-" * 35)
print(f"{sPersonName}'s Calculated Average Score: {fAverage:.1f}")
print(f'Final Letter Grade: {sLetterGrade}')
print("-" * 35)
