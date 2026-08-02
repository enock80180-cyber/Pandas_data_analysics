import pandas as pd

# Create a small dataset
data = {
     "City": ["Amsterdam", "Almere", "Utrecht", "Rotterdam"],
     "Rent": [2100, 1450, 1760, 1600],   
     "Bedroom": [2, 3, 2, 1]
}

#  Turn it into a Pandas Table (DataFrame)
df = pd.DataFrame(data)

# Filter : Show  cities where Rent is UNDER 1700 EUR
cheap_cities = df[df["Rent"] < 1700]
print("----AFFORDABLE CITIES----")
print(cheap_cities)
