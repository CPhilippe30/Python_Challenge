# Dependencies
import csv
import os

 # Files to load and output 
csvpath= os.path.join( "Resources", "budget_data.csv")
budget_data= os.path.join("analysis","budget_analysis.txt")

# Track various revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0


# Read the csv and convert it into a list of dictionaries
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    cvs_header= next(csvreader)

    for row in csvreader:
        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Track the revenue change
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis",
    f"----------------------------\n",
    f"Total Months: {total_months}\n",
    f"Total Revenue: ${total_revenue}\n",
    f"Average Revenue Change: ${revenue_avg}\n",
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n",
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)dsadsa
print(*output)

# Export the results to text file
