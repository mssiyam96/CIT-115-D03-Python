#Constants for commission rate and currency formatting
COMMISSION_RATE = 0.03
CURRENCY_FORMAT = "${:,.2f}"

#Float Input
#validation using Python error handling (try-except)and ensures the value is positive and non-zero.

def getFloatInput(prompt_text):
    
    while True:
        try:
            #Get input
            value_str = input(prompt_text)
            
            input_value = float(value_str)
            
            #Check if positive and non-zero
            if input_value > 0:
                return input_value
            else:
                print("Error: Sales value must be positive and non-zero.")
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

#Getting the median and Calculates the median of a sorted list

def getMedian(sales_list):

    list_count = len(sales_list)
    if list_count == 0:
        return 0.0
        
    # Odd number of entries
    if list_count % 2 != 0:
        median_index = list_count // 2
        return sales_list[median_index]
    
    # Even number of entries
    else:
        index_upper = list_count // 2
        index_lower = index_upper - 1
        return (sales_list[index_lower] + sales_list[index_upper]) / 2.0


#Main Function

def main():
    print("--- BDJ Real Estate Sales Analyzer ---")
    sales_entries = []
    
    property_count = 1
    
    #Data Entry Loop
    
    while True:

#Get the sales price using the required validation function
        prompt = f"Enter Property Sale value {property_count}: "
        sales_price = getFloatInput(prompt)
        sales_entries.append(sales_price)

        #Prompt user to continue/exit and validate 'Y' or 'N'
        while True:
            continue_input = input("Enter another value Y or N: ").strip().upper()
            if continue_input in ('N', 'Y'):
                break
            else:
                print("Error: Please enter 'Y' to continue or 'N' to exit.")
        
        if continue_input == 'N':
            break
        
        #Increment the counter for the next property
        
        property_count += 1

    #Check for empty list
    if not sales_entries:
        print("\nNo sales entries were recorded. Exiting.")
        return

    
    #Sort the list
    sales_entries.sort()
    
    #Calculate the statistics
    total_sales = sum(sales_entries)
    list_count = len(sales_entries)
    min_sales = sales_entries[0]
    max_sales = sales_entries[-1]
    average_sales = total_sales / list_count
    median_sales = getMedian(sales_entries) # Call the required median function
    commission = total_sales * COMMISSION_RATE


    
    print("="*40)
    #Loop through the sorted sales list and print with property numbers
    # We use enumerate to get both the index (i) and the sales value
    for i, sales in enumerate(sales_entries):
        # i + 1 gives the property number (since enumerate starts at 0)
        print(f"Property {i + 1}: {CURRENCY_FORMAT.format(sales)}")
    

    print(f"Minimum Sales Value: {CURRENCY_FORMAT.format(min_sales)}")
    print(f"Maximum Sales Value: {CURRENCY_FORMAT.format(max_sales)}")
    print(f"Total Sales Value: {CURRENCY_FORMAT.format(total_sales)}")
    print(f"Average Sales Value: {CURRENCY_FORMAT.format(average_sales)}")
    print(f"Median Sales Value: {CURRENCY_FORMAT.format(median_sales)}")
    
    print(f"Total Commission ({COMMISSION_RATE*100:.0f}%): {CURRENCY_FORMAT.format(commission)}")
    print("="*40)

# Execute the main function
if __name__ == "__main__":
    main()
