import os
import csv

# Path to the CSV file
election_csv = os.path.join("Resources", "election_data.csv")

# Determine the directory of the election_csv file
election_csv_directory = os.path.dirname(election_csv)

# Define the path for the analysis text file
analysis_txt_path = os.path.join("Analysis", "Election_Results.txt")

# create a dictionary for the election data
data = {
    "total_votes": 0,
    "candidates": {}
}

def calculate_election_results():
    # the total number of votes from the data dictionary
    total_votes = data["total_votes"]

    # creates a list to hold the summary of the results
    results_summary = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------",
    ]
    
    # loops though each candidate in the dictionary to calculate their vote percentage
    for candidate, votes in data["candidates"].items():
        # calculate each candidates vote percentage
        vote_percentage = (votes / total_votes) * 100
        # append the candidates results to the summary list
        results_summary.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    # identify the winner by finding the candidate with the maximum number of votes
    winner = max(data["candidates"], key=data["candidates"].get)
    # add the winner's information to the summary list
    results_summary.extend([
        "-------------------------",
        f"Winner: {winner}",
        "-------------------------"
    ])

    # combine the summary list into a single string for output
    text_file_output = "\n".join(results_summary)

    # open the output file and write the summary string to it
    with open(analysis_txt_path, "w") as file:
        file.write(text_file_output)

# read the CSV file
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)  # skip the header row

    for row in csv_reader:
        candidate_name = row[2]
        data["total_votes"] += 1
        if candidate_name not in data["candidates"]:
            data["candidates"][candidate_name] = 1 # keep count for each candidate vote total
        else:
            data["candidates"][candidate_name] += 1 # keep count for each candidate vote total


calculate_election_results()
