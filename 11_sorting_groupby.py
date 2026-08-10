import pandas as pd
# load dataset
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(file_url)

# Group by "time" and calculate total bill sum and average 
day_stats = df.groupby("day")["total_bill"].agg(["sum", "mean"])
day_stats.columns = ["Total Revenue", "Average Bill"]

# sort by "Total Revenue" from highest to lowest (ascending=false)
sorted_stats = day_stats.sort_values(by='Total Revenue', ascending=False)

# print results
print(round(sorted_stats, 2))
