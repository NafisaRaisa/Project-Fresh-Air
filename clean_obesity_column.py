import pandas as pd

# Read the CSV file
file_path = '/Users/nafisaraisa/Documents/Project_Fresh_Air/data_cleaning/all_result_file.csv'
df = pd.read_csv(file_path)

# Specify the column with parentheses
column_to_clean = 'Percent_Obesity'  # Replace with the actual column name

# Use str.replace with an empty string to remove everything within parentheses
df[column_to_clean] = df[column_to_clean].str.replace(r'\(.*\)', '', regex=True)

# Print the updated DataFrame
print(df)

# Specify the path for the new CSV file
output_file_path = '/Users/nafisaraisa/Documents/Project_Fresh_Air/data_cleaning/modified_result_file.csv'

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)
