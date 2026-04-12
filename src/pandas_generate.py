import pandas as pd

df = pd.DataFrame({ # Create a DataFrame with some missing values
    "order_id": range(1,11),
    "amount": [100, None, 200, 250, None, 350, 400, 450, None, 550],
    "country": ["uS", "kR", None, "De", "Fr", "iT", "Kr", "aU", "jP", None]
})

print("Original DataFrame:")
print (df)

df.to_csv("data/raw/raw_orders.csv", index=False) # Save the DataFrame to a CSV file without the index
