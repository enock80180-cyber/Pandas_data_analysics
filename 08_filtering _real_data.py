import pandas as pd

# 1. load the dataset
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(file_url)

# 2. Filter for total bill greater than $40
big_bills = df[df["total_bill"] > 40]

# 3. Print the filtered table
print(big_bills) 

# 4. Count how many tables had bills over 40$
print("\nThe total bills over 40$ is", len(big_bills))
