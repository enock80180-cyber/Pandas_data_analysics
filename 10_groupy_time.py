import pandas as pd
# load dataset
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(file_url)

# Group by "time" and calculate total bill sum and average 
meal_stats = df.groupby("time")["total_bill"].agg(["sum", "mean"])

# Rename the 2 generated colums
meal_stats.columns = ["Total Revenue", "Average bill"]

print(round(meal_stats, 2))
