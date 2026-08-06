import pandas as pd

# 1. Real DATASET URL
file_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Pull the data into panda
df = pd.read_csv(file_url)

# Get the Data
print(df)
