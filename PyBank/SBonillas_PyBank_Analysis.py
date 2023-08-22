#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Add dependencies.
import os
import csv

# Select paths for inputs and outputs.
file_open = os.path.join(".", "Resources", "budget_data.csv")
file_export = os.path.join(".", "Mod3_PyBank_Analysis.txt")

# Defining variables
total_months = 0
total_net = 0

net_change_list = []

greatest = ["", 0]
least = ["", 9999999999999999999]

#Read the csv file and convert to a list.
with open(file_open) as financial_data:
    reader = csv.reader(financial_data)
           
    # Define the header.
    header = next(reader)
    
    # Define values for the analysis.
    first_row = next(reader)
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    total_months += 1
    
    for row in reader:
        # Determine the totals.
        total_months += 1
        total_net += int(row[1])
        
        # Calculate the net change.
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
                        
        #Calculate the largest increase.
        if(net_change > greatest[1]):
            greatest[0] = row[0]
            greatest[1] = net_change
        
        #Calculate the largest decrease.
        if(net_change < least[1]):
            least[0] = row [0]
            least[1] = net_change
            
# Calculate the monthly average.          
net_monthly_average = sum(net_change_list)/ len(net_change_list) 

# Display Requested Results.  Added comma separators and decimal places as necessary (for aesthetics).
output = (
    f"----------------------\n"
    f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $ {total_net:,.2f}\n"
    f"Average Change: $ {net_monthly_average:,.2f}\n"
    f"Largest Increase in Profits: {greatest[0]} ($ {greatest[1]:,.2f})\n"
    f"Largest Decrease in Profits: {least[0]} ($ {least[1]:,.2f})\n"
    f"----------------------\n"
)

# Print results to terminal.
print(output)

# Export the results to a text file.
with open (file_export, "w") as txt_file:
    txt_file.write(output)

