
# Name:Abdul Wassid
# SPC ID#:2506642

# Pseudocode:
# 1. Prompt the user for the number of different books.
# 2. Initialize a total amount to 0.
# 3. For each book:
#    a. Prompt user for title.
#    b. Prompt user for ISBN.
#    c. Prompt user for price.
#    d. Prompt user for quantity.
#    e. Call compute_subtotal function and add the returned value to the total amount.
# 4. Print the total amount.

import book_operations

def main():
    total_amount = 0.0
    
    num_books = int(input("Enter the number of different books being purchased: "))

    for _ in range(num_books):
        title = input("Enter the title of the book: ")
        isbn = input("Enter the ISBN number of the book: ")
        price = float(input("Enter the price of the book: $"))
        quantity = int(input("Enter the quantity being purchased: "))

        total_amount += book_operations.compute_subtotal(price, quantity)

    print(f"\nThe total amount for all purchases is: ${total_amount:.2f}")

if __name__ == "__main__":
    main()
