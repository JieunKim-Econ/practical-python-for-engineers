import pandas as pd

df = pd.read_csv("data/raw/raw_orders.csv")
print("Dataframe with missing values:")
print(df)

df["amount"] = df["amount"].fillna(0) # Fill missing values in the 'amount' column with 0
df["amount"] = df["amount"].astype(int) # Convert the 'amount' column to integer type 
df["country"] = df["country"].str.upper() # Convert country names to uppercase
df["country"] = df["country"].fillna("UNKNOWN") # Fill missing values in the 'country' column with "UNKNOWN"

print("\nDataframe after cleaning:")
print(df)

country_summary = (   
    df.groupby("country")
    .agg(
        total_orders=("order_id", "count"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean")
    )  
    # df.groupby("country", as_index=False)["amount"]
    #.agg(["sum", "mean", "count"])  
    # .rename(columns={"sum": "total_amount", "mean": "average_amount", "count": "order_count"}) 
)
print("\nCountry summary:")
print(country_summary)  

df["running_total"] = df["amount"].cumsum() # Add a new column for the running total of the 'amount' column
print("\nDataframe with running total:")
print(df)