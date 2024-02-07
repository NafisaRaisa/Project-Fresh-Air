import pandas as pd


# Read CSV files
file1 = pd.read_csv('/Users/nafisaraisa/Downloads/Asthma.csv')
file2 = pd.read_csv('/Users/nafisaraisa/Downloads/obesity.csv')

# Get the values of columns GeoID and Time from file1 and file2
column_geo_id_values_file1 = file1['GeoID']
column_time_values_file1 = file1['Time']

column_time_values_file2 = file2['Time']
column_geo_id_values_file2 = file2['GeoID']
column_m_values_file2 = file2['Number']
column_n_values_file2 = file2['Percent']

# Create an empty dataframe to accumulate results
result_df = pd.DataFrame()

# Loop through each value in column GeoID of file1
for index, value_file1_geo_id in enumerate(column_geo_id_values_file1):
    # Check if the value is present in any cell of column GeoID of file2
    if any(value_file1_geo_id == value_file2_geo_id for value_file2_geo_id in column_geo_id_values_file2):
        # Get the corresponding values in columns Time, M, and N for the matched row in file2
        value_file1_time = column_time_values_file1.iloc[index]
        matching_rows_file2 = file2[(file2['GeoID'] == value_file1_geo_id) & (file2['Time'] == value_file1_time)]

        # Check if a match is found in file2
        if not matching_rows_file2.empty:
            # Add the matching rows to the result dataframe
            result_df = pd.concat([result_df, file1.iloc[[index]].assign(
                Number_Obesity=matching_rows_file2['Number'].values[0],
                Percent_Obesity=matching_rows_file2['Percent'].values[0]
            )], ignore_index=True)

# Save the final result to a CSV file
result_df.to_csv('Final_merged_file.csv', index=False)
