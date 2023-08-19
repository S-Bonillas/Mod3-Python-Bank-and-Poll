#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Add dependences.
import os
import csv

# Select paths for file import and export.
file_import = os.path.join(".", "resources", "election_data.csv")
file_export = os.path.join(".", "Mod3_PyPoll_Analysis.txt")

# Establish starting point to track total votes.
total_votes = 0

# Establish starting points to track candidate dictionary and list.
cand_votes = {}
cand_options = []

# Establish starting point for winning candidate data.
winning_cand = ""
winning_count = 0

# Open the file to extract the data
with open(file_import) as election_data:
    reader = csv.reader(election_data)
    
    # Read the header.
    header = next(reader)
    
    # Loop through the data to...
    for row in reader:
        # ...Find the sum of total votes.
        total_votes = total_votes + 1
        
        # ...Extract candidate name from each row.
        cand_name = row[2]
        
        # If statement to extract candidate names.
        if cand_name not in cand_options:
            cand_options.append(cand_name)
        
            cand_votes[cand_name] = 0
        cand_votes[cand_name] += 1

# Prepare the data for export.
with open(file_export, "w") as txt_file:
    # Display and export first part of the findings (total votes).
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    print(election_results, end="")
    txt_file.write(election_results)
    
    # Find candidate vote numbers and percentages
    for cand in cand_votes:
        votes = cand_votes[cand]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if(votes > winning_count):
            winning_count = votes
            winning_cand = cand
        
        # Display and export the middle part of the findings (candidates and percentages)
        voter_output = f"{cand}: {vote_percentage:.3f}% ({votes})\n"
                
        print(voter_output, end="")
        txt_file.write(voter_output)

    # Display and export end of the findings (winning candidate).
    winning_cand_summary = (
        f"-------------------------\n"
        f"Winner: {winning_cand}\n"
        f"-------------------------\n"
    )
    
    print (winning_cand_summary)
    txt_file.write(winning_cand_summary)

