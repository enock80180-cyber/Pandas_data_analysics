import pandas as pd

# 1. Load the real dataset
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(file_url)

# Calculate average total Bill
avg_bill = df["total_bill"].mean()

# Calculate the total sum of tips
total_sum = df["tip"].sum()

# 4. Print the answers Clearly
print("The Average Bill: $", avg_bill)
print("The Total tip: $", total_sum)
