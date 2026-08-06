import pandas as pd

# 1. load the dataset
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(file_url)

# 2. Divide tip by the total_bil,then multiply by 100(no asterisks needed)
df["tip_pic"] = df["tip"].div(df["total_bill"]).mul(100)

# 3.Calculate the overall average tip
avg_tip_pic = df["tip_pic"].mean()

# 4.Print the results rounded to 2 decimal places
print("\nAverage Tip Percentage:" , round(avg_tip_pic, 2), "%")
