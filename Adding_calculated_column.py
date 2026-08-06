import pandas as pd

# 1. Recreate dataset
data = {
    "City": ["Amsterdam", "Almere", "Utrecht", "Rotterdam"],
    "Rent": [2100, 1450, 1760, 1600],
    "Bedroom":[2, 3, 2, 1]
}
df = pd.DataFrame(data)

# 2. Divide Rent bt Bedroom to create a new column
df["Rent_per_bed"] = df["Rent"]/df["Bedroom"]

print(df)
