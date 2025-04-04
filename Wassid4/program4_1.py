
# Name:Abdul Wassid SPC ID:2506642

# Initialize variables
savings_goal = int(input("Enter your weekly savings goal: "))
total_saved = 0
days_saved = 0

# Use a while loop to accept and process saved amounts each day
while True:
    saved_amount = int(input("Enter the amount saved for the day (enter 0 to stop): "))
    
    # Check if the user wants to stop saving
    if saved_amount == 0:
        break
    
    total_saved += saved_amount
    days_saved += 1

# Calculate the difference between the savings goal and total saved
difference = total_saved - savings_goal

# Determine if the goal was met, exceeded, or missed
if difference == 0:
    result = "met"
elif difference > 0:
    result = "exceeded"
else:
    result = "missed"

# Output the results
print(f"Number of days saved: {days_saved}")
print(f"Total saved: ${total_saved}")
print(f"You {result} your savings goal by ${abs(difference)}.")
