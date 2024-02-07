import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Load your CSV file
# Replace 'your_dataset.csv' with your actual CSV file name
df = pd.read_csv('/Users/nafisaraisa/Documents/Project_Fresh_Air/data_cleaning/modified_result_file.csv')

# Assuming the target variable is in the 'target_column' column
# Replace 'target_column' with your actual target variable column name
X = df.drop(['Percent_Obesity', 'Mean mcg/m3'], axis=1, errors='ignore')  # Exclude 'Borough' if it exists
y = df['Estimated annual rate per 10,000']

# Identify non-numeric columns
non_numeric_cols = X.select_dtypes(include=['object']).columns

# Drop non-numeric columns
X = X.drop(non_numeric_cols, axis=1)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform 70/20/10 train/validation/test split
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.33, random_state=42)

# Create your model
#model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=2000, random_state=42, solver='adam', learning_rate_init=0.001)
model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42, solver='adam', learning_rate_init=0.1)


# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the validation set
val_predictions = model.predict(X_val)

# Evaluate the model on the validation set (you can use different metrics)
val_mse = mean_squared_error(y_val, val_predictions)
print(f"Mean Squared Error on Validation Set: {val_mse}")

# Perform cross-validation
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='neg_mean_squared_error')

# Print the cross-validation scores
print("Cross-validation scores:", cv_scores)

# Optionally, you can print the mean and standard deviation of the cross-validation scores
print(f"Mean CV Score: {abs(np.mean(cv_scores)):.2f}")
print(f"Standard Deviation CV Score: {np.std(cv_scores):.2f}")

# Make predictions on the test set
test_predictions = model.predict(X_test)

# Evaluate the model on the test set (you can use different metrics)
test_mse = mean_squared_error(y_test, test_predictions)
print(f"Mean Squared Error on Test Set: {test_mse}")


