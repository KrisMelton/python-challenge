import os
import csv

# Path to the CSV file
bank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Path to the CSV file
analysis_txt_path = os.path.join("Analysis", "Election_Results.txt")

# Store the data from the CSV File
data = {
    "months": [],
    "profits_losses": [],
    "changes": []
}

def calculate():

    total_months = len(data["months"]) # Find the total months
    total_amount = sum(data["profits_losses"]) # Calulates the total amount errand 

    # Calculate changes in Profit/Losses
    for i in range(1, len(data["profits_losses"])): # Starting the row on 1
        change = data["profits_losses"][i] - data["profits_losses"][i - 1] # Taking the row it on and the 1 above 
        data["changes"].append(change)

    average_change = sum(data["changes"]) / len(data["changes"]) # Average change
    great_increase = max(data["changes"]) # Find the highest change
    great_decrease = min(data["changes"]) # Find the lowest change

     # Find corresponding months for greatest increase and decrease
    increase_index = data["changes"].index(great_increase) + 1
    decrease_index = data["changes"].index(great_decrease) + 1

    great_increase_months = data["months"][increase_index]
    great_decrease_months = data["months"][decrease_index]

    # What the text file should look like
    text_file_output = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: {total_amount}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {great_increase_months} ({great_increase})\n"
        f"Greatest Decrease in Profits: {great_decrease_months} ({great_decrease})\n"
    )
    # Write a text file to location of the csv file
    with open(analysis_txt_path, "w") as file:
        file.write(text_file_output)


# Read the CSV file
with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        data["months"].append(row[0])
        data["profits_losses"].append(int(row[1]))

calculate()