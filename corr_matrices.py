import pandas as pd

# Read the CSV file
file_path = '/Users/nafisaraisa/Documents/Project_Fresh_Air/data_cleaning/all_result_file.csv'
df = pd.read_csv(file_path)

# Specify numeric columns
numeric_columns = ['Percent_Obesity', 'Mean mcg/m3', 'Estimated annual rate per 10,000']

# Select only relevant columns and drop missing values
df = df[numeric_columns].dropna()

# Print remaining data
print("\nRemaining Data:")
print(df)

# Check if there is data after dropping missing values
if not df.empty:
    # Calculate the correlation matrix
    correlation_matrix = df.corr()

    # Print the correlation matrix
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
else:
    print("\nNo data available after dropping missing values.")
