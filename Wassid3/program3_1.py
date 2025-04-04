
# Abdul Wassid
# SPC ID: 2506642

# Pseudocode:
# 1. Get the number of days and the day type (weekday/weekend) from the user.
# 2. Calculate the rental cost based on the provided rates.
# 3. Apply the discount if the rental is 7 or more days.
# 4. Display the calculated cost in currency format.

weekday_lenght = int(input("how many weekdays did you rent for? "))
weekend_lenght = int(input("how many weekend days did you rend for? "))

weekday_cost = 135
weekend_cost = weekday_cost*1.5
total_weekday_cost = weekday_cost*weekday_lenght
total_weekend_cost = weekend_cost*weekend_lenght 
discount = 50
total_days = weekday_lenght + weekend_lenght
total_cost = total_weekday_cost + total_weekend_cost
discount_check = False

if total_days >= 7:
    total_cost -= 50
    discount_check = True

print(f"your regular cost is: ${total_weekday_cost:,.2f}")
print(f"your weekend cost is: ${total_weekend_cost:,.2f}")
if discount_check == True:
    print(f"discount: ${discount:,.2f}")
else:
    print("discount: $0.00")
print(f"your total cost is: ${total_cost:,.2f}")
