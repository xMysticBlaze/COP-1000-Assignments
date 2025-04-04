
# Abdul Wassid
# SPC ID: 2506642

# Pseudocode:


eligible_for_membership = True
age = int(input("Enter your age: "))
if age < 18:
  eligible_for_membership = False
elif eligible_for_membership:
    sessions = int(input("Enter the number of personal training sessions attended: "))
    base_fee = 200
    membership_cost = 200
    young_member_fee = 50
    first_session_cost = 40
    second_session_cost = 70
    additional_sessions_cost = 100
    total_session_cost = 0

    if age < 25:
      membership_cost += young_member_fee

    if sessions == 1:
        total_session_cost += first_session_cost
    if sessions == 2:
        total_session_cost += first_session_cost + second_session_cost
    if sessions >= 3:
        total_session_cost += first_session_cost + second_session_cost + additional_sessions_cost*(sessions-2)

    membership_cost += total_session_cost

    print(f"the base membership cost: ${base_fee:,.2f}")
    print(f"your young member fee is: ${young_member_fee:,.2f}")
    print(f"your personsal training cost is: ${total_session_cost:,.2f}")
    print(f"your total cost is: ${membership_cost:,.2f}")

if not eligible_for_membership:
  print("you are too young for a membership")