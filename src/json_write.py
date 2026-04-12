import json  # Import the built-in JSON module for parsing and writing JSON data.

# A dictionary object representing the data structure to be saved.
data = {
    "orders": [
        {"id": 1, "item": [{"sku": "A1", "qty": 2}]},
        {"id": 2, "item": [{"sku": "B2", "qty": 5}]}
    ]
}

# Set the target folder and file path.
# ".." moves up one level from the 'src' folder to the project root.
folder_path = "../data/raw"
file_path = f"{folder_path}/orders.json"

# Open the file in write mode ('w').
with open(file_path, 'w') as f:
    # Serialize 'data' as a JSON formatted stream to the file 'f'.
    # 'indent=2' adds visual spacing for better readability.
    json.dump(data, f, indent=2)