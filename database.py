import pandas as pd
from recipe_recommend import recipe_list, data

# Sample nested list data
recipes_data = recipe_list(data)
# Define the column names
columns = ["Recipe", "Price", "Link"]
# Create a DataFrame from the nested list
df = pd.DataFrame(recipes_data, columns=columns)
# Display the table
print(df)
