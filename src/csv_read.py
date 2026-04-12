import csv  # Import the CSV module to read the file.

# Open the file in read mode ('r') from the specified path.
with open("../data/raw/orders.csv", "r") as f:
    # Create a reader object to iterate over lines in the given CSV file.
    reader = csv.reader(f)
    # Loop through each row in the CSV file.
    for row in reader:
        print(row)  # Print each row as a list.