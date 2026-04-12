def transform_orders(raw_orders):
    
    transformed_orders = []
    for order in raw_orders:
        transformed_order = {
            'order_id': order['order_id'],
            'amount': float(order['amount']),
            'country': order['country'].upper(),
        }
        transformed_orders.append(transformed_order)
    return transformed_orders