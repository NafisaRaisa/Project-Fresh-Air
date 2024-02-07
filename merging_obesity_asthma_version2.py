import pandas as pd


# Read CSV files
file1 = pd.read_csv('/Users/nafisaraisa/Downloads/Asthma.csv')
file2 = pd.read_csv('/Users/nafisaraisa/Downloads/obesity.csv')

# Get the values of columns GeoID, GeoType, and Time from file1 and file2
column_geo_id_values_file1 = file1['GeoID']
column_geo_type_values_file1 = file1['GeoType']
column_time_values_file1 = file1['Time']

column_time_values_file2 = file2['Time']
column_geo_id_values_file2 = file2['GeoID']
column_geo_type_values_file2 = file2['GeoType']
column_m_values_file2 = file2['Number']
column_n_values_file2 = file2['Percent']

# Create an empty dataframe to store the results
result_df = pd.DataFrame()

# Loop through each value in column GeoID of file1
for index, value_file1_geo_id in enumerate(column_geo_id_values_file1):
    # Check if the value is present in any cell of column GeoID, GeoType, and Time of file2
    match_condition = (
        (value_file1_geo_id == column_geo_id_values_file2) &
        (column_geo_type_values_file1.iloc[index] == column_geo_type_values_file2) &
        (column_time_values_file1.iloc[index] == column_time_values_file2)
    )

    if any(match_condition):
        # Get the corresponding values in columns Time, M, and N for the matched row in file2
        value_file1_time = column_time_values_file1.iloc[index]
        matching_rows_file2 = file2[
            (column_geo_id_values_file2 == value_file1_geo_id) &
            (column_geo_type_values_file2 == column_geo_type_values_file1.iloc[index]) &
            (column_time_values_file2 == value_file1_time)
        ]

        # Check if a match is found in file2
        if not matching_rows_file2.empty:
            # Create a new dataframe with all columns from the corresponding row of file1
            temp_result_df = file1.iloc[[index]].copy()

            # Add new columns with values from columns M and N of file2 using .loc
            temp_result_df.loc[:, 'Number_Obesity'] = matching_rows_file2['Number'].values[0]
            temp_result_df.loc[:, 'Percent_Obesity'] = matching_rows_file2['Percent'].values[0]

            # Append the temporary result to the overall result dataframe
            result_df = result_df.append(temp_result_df, ignore_index=True)

# Save the result to a new CSV file
result_df.to_csv('result_file.csv', index=False)
