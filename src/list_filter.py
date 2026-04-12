orders = [
    {"order_id":1, "country":"US"},
    {"order_id":2, "country":"KR"},
    {"order_id":3, "country":"KR"}
]

kr_order = [] # Create a empty list

for order in orders:
    if order["country"] == "KR":
        kr_order.append(order)

print(kr_order) 
#[{'order_id': 2, 'country': 'KR'}, {'order_id': 3, 'country': 'KR'}]