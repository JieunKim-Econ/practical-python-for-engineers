# Convert a list to a set for deduplication as sets don't allow duplicate values
order_id = [101, 102, 103, 101, 104, 102]
unique_order_ids = set(order_id)
print(unique_order_ids) 
# Result: {104, 101, 102, 103}