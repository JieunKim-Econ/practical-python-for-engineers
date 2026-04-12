def calculate_total(order):
    if "amount" not in order:
        raise TypeError("Order must contain 'amount' key") # This will raise a TypeError if the 'amount' key is missing from the order dictionary.
    return order["amount"] * 2

order = {"amont": "100"}   
total = calculate_total(order)
print(f"Total amount calculated: {total}")  