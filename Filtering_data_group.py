import pandas as pd

# 1. load the dataset
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(file_url)

# 2. Group by the day and calculate the average tip for each day
avg_tip_by_day = df.groupby("day")["tip"].mean()

print(avg_tip_by_day)
