# Project-Fresh-Air
Analyzing the relationship among air-quality, obesity, and asthma using data mining and machine learning techniques 


Step 1 Extracting Data:
Data on average obesity, air quality and astha rate were extracted from government website in 3 different csv file. From those 3 datastes, we created a dataset containing information about time, GeoType, GeoRank, Geography, GeoID, Annual asthma rate out of 10,000, age-adjusted asthma rate out of 10,000, number of asthma cases, number of obesity cases, percent of obesity, 90%,10% and mean air quality data using the script "merging_all3_files.py". The resulitng dataste contained 61 rows. 

Step 2 Data Cleaning: Missing and non-numerical data on certain columns were deleted as they were very few compared to the dataset. The Percent_Obesity column of the dataset which previously contained both the mean and range of obesity percentage were replaced by the percent_obesity column containing only the average and not the range. The script "clean_obesity_column.py" was used to clean the Percent_Obesity column of the dataset.

Step 3 Finding Correlation among the variables: Using the script "corr_matrices.py", a correlation matrice was created for "Percent_Obesity" "Annual Asthma rate" and "Mean Air Quality". Below is the matrice:

<img width="690" alt="Screenshot 2023-11-30 at 12 43 46 AM" src="https://github.com/NafisaRaisa/Project-Fresh-Air/assets/96096118/a656fce6-8198-430f-9f95-adb3ac8a26cf">


Step 4 Scaling: The varibles were scaled in order to ensure that all features contribute equaly to the training of the model. 

Step 5 Predictive Modeling: Used Neural Network(MLPRegressor) to create a predictive model. Did a 70% training, 20%testing, and 10% evaluation test set. After experimenting with different iteration and learning rates, we decided that iteration=10,000 and learning_rate=0.1 currently gives the lowest mean square error. Therefore the current model is built with those values. Cross validation was perfomed to enhance the performance of the model. The script "neural_network.py" was used to create the predictive model.


<img width="649" alt="neural_network_results" src="https://github.com/NafisaRaisa/Project-Fresh-Air/assets/96096118/3e994082-1db2-4bee-9b5d-ee744d44593f">

In addition to the Neural Network, we also implemented the Support Vector Machine to build a predictive model using the script "Support_vector_machine.py". Support vector machine shows more promising results than Neural Network for our data. Below is the result
<img width="437" alt="Screenshot 2023-12-21 at 5 04 38 AM" src="https://github.com/NafisaRaisa/Project-Fresh-Air/assets/96096118/882c4973-67dc-447a-be6d-041a3dc3b8ed">




