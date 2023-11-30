
import pandas as pd

# Read CSV files
file1 = pd.read_csv('/Users/nafisaraisa/Downloads/Asthma.csv')
file2 = pd.read_csv('/Users/nafisaraisa/Downloads/obesity.csv')
file3 = pd.read_csv('/Users/nafisaraisa/Documents/Project_Fresh_Air/data_cleaning/year_output_file.csv')  # Add the path to your third file

# Get the values of columns GeoID, GeoType, and Time from file1 and file2
column_geo_id_values_file1 = file1['GeoID']
column_geo_type_values_file1 = file1['GeoType']
column_time_values_file1 = file1['Time']

column_time_values_file2 = file2['Time']
column_geo_id_values_file2 = file2['GeoID']
column_geo_type_values_file2 = file2['GeoType']
column_m_values_file2 = file2['Number']
column_n_values_file2 = file2['Percent']

column_time_values_file3 = file3['Time']
column_geo_id_values_file3 = file3['GeoID']
column_geo_type_values_file3 = file3['GeoType']
column_m_values_file3 = file3['10th percentile mcg/m3']
column_n_values_file3 = file3['90th percentile mcg/m3']
column_k_values_file3 = file3['Mean mcg/m3']

# Create an empty dataframe to store the results
result_df = pd.DataFrame()

# Loop through each value in column GeoID of file1
for index, value_file1_geo_id in enumerate(column_geo_id_values_file1):
    # Check if the value is present in any cell of column GeoID, GeoType, and Time of file2
    match_condition_file2 = (
        (value_file1_geo_id == column_geo_id_values_file2) &
        (column_geo_type_values_file1.iloc[index] == column_geo_type_values_file2) &
        (column_time_values_file1.iloc[index] == column_time_values_file2)
    )

    # Check if the value is present in any cell of column GeoID, GeoType, and Time of file3
    match_condition_file3 = (
        (value_file1_geo_id == column_geo_id_values_file3) &
        (column_geo_type_values_file1.iloc[index] == column_geo_type_values_file3) &
        (column_time_values_file1.iloc[index] == column_time_values_file3)
    )

    if any(match_condition_file2) and any(match_condition_file3):
        # Get the corresponding values in columns Number and Percent for the matched rows in file2 and file3
        value_file1_time = column_time_values_file1.iloc[index]
        matching_rows_file2 = file2[
            (column_geo_id_values_file2 == value_file1_geo_id) &
            (column_geo_type_values_file2 == column_geo_type_values_file1.iloc[index]) &
            (column_time_values_file2 == value_file1_time)
        ]
        matching_rows_file3 = file3[
            (column_geo_id_values_file3 == value_file1_geo_id) &
            (column_geo_type_values_file3 == column_geo_type_values_file1.iloc[index]) &
            (column_time_values_file3 == value_file1_time)
        ]

        # Check if matches are found in file2 and file3
        if not matching_rows_file2.empty and not matching_rows_file3.empty:
            # Create a new dataframe with all columns from the corresponding row of file1
            temp_result_df = file1.iloc[[index]].copy()

            # Add new columns with values from columns Number and Percent of file2
            temp_result_df['Number_Obesity'] = matching_rows_file2['Number'].values[0]
            temp_result_df['Percent_Obesity'] = matching_rows_file2['Percent'].values[0]

            # Add new columns with values from columns 10th percentile mcg/m3, 90th percentile mcg/m3, and Mean mcg/m3 of file3
            temp_result_df['10th percentile mcg/m3'] = matching_rows_file3['10th percentile mcg/m3'].values[0]
            temp_result_df['90th percentile mcg/m3'] = matching_rows_file3['90th percentile mcg/m3'].values[0]
            temp_result_df['Mean mcg/m3'] = matching_rows_file3['Mean mcg/m3'].values[0]

            # Append the temporary result to the overall result dataframe
            #result_df = result_df.append(temp_result_df, ignore_index=True)
            result_df = pd.concat([result_df, temp_result_df], ignore_index=True)

# Save the result to a new CSV file
result_df.to_csv('all_result_file_1.csv', index=False)


