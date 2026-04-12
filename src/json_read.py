import json  # Import the JSON module to facilitate data deserialization.

# Open the JSON file in read-only mode to access stored data.
with open("../data/raw/orders.json", 'r') as f:
    # Deserialize the JSON file content back into a Python dictionary (state recovery).
    data = json.load(f)

# Initialize a list to hold the flattened data structure.
rows = [] 

# Iterate through the top-level 'orders' list.
for order in data["orders"]: 
    # Extract nested 'item' data from each order to flatten the hierarchy.
    for item in order["item"]: 
        # Create a "flat record" by mapping parent 'id' with child 'sku' and 'qty'.
        rows.append({ 
            "id": order["id"], 
            "sku": item["sku"],  
            "qty": item["qty"]
        })

# Print the resulting list of flat dictionaries.
print(rows)
# Result: [{'id': 1, 'sku': 'A1', 'qty': 2}, {'id': 2, 'sku': 'B2', 'qty': 5}]