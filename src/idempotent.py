def transform_orders_v1(raw_orders):
    """Idempotent version of the transform_orders function."""

    transformed_orders = []
    for order in raw_orders:
        transformed_order = {
            'order_id': order['order_id'],
            'amount': float(order['amount']),
            'country': order['country'].upper(),
        }
        transformed_orders.append(transformed_order)
    return transformed_orders

# Now let's see a non-idempotent version of the transform_orders function.
# We define the list outside the function this time.
transformed_orders = []

def transform_orders_v2(raw_orders):
    """Non-idempotent version of the transform_orders function."""

    for order in raw_orders:
        transformed_order = {
            'order_id': order['order_id'],
            'amount': float(order['amount']),
            'country': order['country'].upper(),
        }
        transformed_orders.append(transformed_order)
    return transformed_orders

sample_orders = [
    {'order_id': '123', 'amount': '100', 'country': 'us'},
    {'order_id': '124', 'amount': '200', 'country': 'kr'}
]

print("v1 first:", transform_orders_v1(sample_orders))
print("v1 second:", transform_orders_v1(sample_orders))

print("v2 first:", transform_orders_v2(sample_orders))
print("v2 second:", transform_orders_v2(sample_orders))
# The second call to transform_orders_v2 will append the transformed orders again, resulting in duplicates.