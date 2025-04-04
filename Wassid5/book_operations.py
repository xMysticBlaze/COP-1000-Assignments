# Author: ChatGPT
# SPC ID#: XYZ123

def compute_subtotal(price, quantity):
    """
    Compute and return the subtotal for a book purchase.
    
    :param price: Price of the book
    :param quantity: Quantity of books being purchased
    :return: Subtotal amount
    """
    subtotal = price * quantity
    print(f"Subtotal for this purchase: ${subtotal:.2f}")
    return subtotal
