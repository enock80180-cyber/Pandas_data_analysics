import pandas as pd

# 1. Recreate dataset
data = {
    "City": ["Amsterdam", "Almere", "Utrecht", "Rotterdam"],
    "Rent": [2100, 1450, 1760, 1600],
    "Bedroom":[2, 3, 2, 1]
}
df = pd.DataFrame(data)
print(df)

# 2. Calculate total sum of all the rent
total_rent = df["Rent"].sum()

# 3.Print the results
print("\nThe total combine rent is:", total_rent)
