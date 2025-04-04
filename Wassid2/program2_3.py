
#Abdul Wassid
#SPC ID: 2506642

widget_price = 54.99
widget_amount = int(input("how many widgets do you want to buy? "))
sales_tax = 0.09
shipping = 1
total_cost = widget_amount*widget_price
total_tax = total_cost*sales_tax
total_shipping = widget_amount*shipping
entire_cost = total_cost + total_tax + total_shipping

print()
print("R E C E I P T")
print()
print(f"Widgets base cost is: ${total_cost:,.2f} ({widget_amount:,} @  ${widget_price})")
print()
print(f"shipping and handling: ${total_shipping:,}")
print(f"tax: ${total_tax:,.2f}")
print()
print(f"the total cost is ${entire_cost:,.2f}")