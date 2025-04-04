
# Name: Abdul Wassid SPC ID# 2506642

# Loop through numbers from 1000 to 1100 (inclusive)
for distance in range(1000, 1101):
    announcement = ""

    # Check if the number is divisible by 7 and/or 5
    if distance % 7 == 0:
        announcement += str(distance) + " Universe"
    
    if distance % 5 == 0:
        announcement += str(distance) + " Galaxy"
    
    # If the number is not divisible by 7 or 5, add "Star Explorer!"
    if not (distance % 7 == 0 or distance % 5 == 0):
        announcement = str(distance) + " Star Explorer!"

    # Output the announcement
    print(announcement)
