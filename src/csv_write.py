import csv # Import the built-in CSV module to handle CSV files.

# Prepare the data as a list of lists (Header + Data rows).
rows = [
    ["order_id", "customer", "amount", "country"], # Header row (column names)
    [1, "Alice", 120.5, "US"],
    [2, "Bob", 75.0, "KR"],
    [3, "Charlie", 200.0, "US"]
]

# Set the target folder and file path.
# ".." moves up one level from the 'src' folder to the project root.
folder_path = "../data/raw"
file_path = f"{folder_path}/orders.csv"

# Open "orders.csv" at the specified path
# 'w' for write mode, newline="" to prevent extra lines between rows.
with open(file_path, "w", newline="") as f:
    # Create a writer object to format the data as CSV.
    writer = csv.writer(f)

    # Write all rows from the list to the CSV file at once.
    writer.writerows(rows)
 
