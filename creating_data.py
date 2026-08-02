import pandas as pd

# Create a small dataset
data = {
     "City": ["Amsterdam", "Almere", "Utrecht", "Rotterdam"],
     "Rent": [2100, 1450, 1760, 1600],   
     "Bedroom": [2, 3, 2, 1]
}

#  Turn it into a Pandas Table (DataFrame)
df = pd.DataFrame(data)

# Display the table
df
