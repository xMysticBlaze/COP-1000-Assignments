
#Abdul Wassid
#SPC ID: 2506642

dollar_amount = int(input("enter dollar amount: "))

fifty = 0
twenty = 0
ten = 0
five = 0 
one = 0

while dollar_amount > 0:
    if dollar_amount >= 50:
        dollar_amount -= 50
        fifty += 1
    elif dollar_amount >= 20:
        dollar_amount -= 20
        twenty += 1
    elif dollar_amount >= 10:
        dollar_amount -= 10
        ten += 1
    elif dollar_amount >= 5:
        dollar_amount -= 5
        five += 1
    elif dollar_amount >= 1:
        dollar_amount -= 1
        one += 1
    else:
        break

print("Your change is:")
print(f"{fifty} fifty dollar bill(s)")
print(f"{twenty} twenty dollar bill(s)")
print(f"{ten} ten dollar bill(s)")
print(f"{five} five dollar bill(s)")
print(f"{one} one dollar bill(s)")