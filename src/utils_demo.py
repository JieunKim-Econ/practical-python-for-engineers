from utils.transform import transform_orders # Importing the transform_orders function from the utils.transform module.

data = [
    {'order_id': '123', 'amount': '100', 'country': 'us'},
    {'order_id': '124', 'amount': '200', 'country': 'kr'}
]

result = transform_orders(data)
print(result)