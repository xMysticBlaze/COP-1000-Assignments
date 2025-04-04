# 
# Abdul Wassid
# SPC ID: 2506642

# Pseudocode:
# 1. Get three quiz scores from the user.
# 2. Determine the lowest score among the three using nested if statements.
# 3. Display the lowest score.

score1 = int(input("Enter score for quiz 1: "))
score2 = int(input("Enter score for quiz 2: "))
score3 = int(input("Enter score for quiz 3: "))

if score1 <= score2 and score1 <= score3:
    lowest_score = score1
elif score2 <= score1 and score2 <= score3:
    lowest_score = score2
else:
    lowest_score = score3

print(f"the scores provided are: {score1}, {score2}, and {score3}.")
print(f"The lowest score is: {lowest_score}") 