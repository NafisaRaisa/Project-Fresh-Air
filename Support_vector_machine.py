# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# Load the dataset (replace 'your_dataset.csv' with the actual file name)
data = pd.read_csv('modified_result_file.csv')


# Print the list of column names to identify the correct ones to drop
#print(data.columns)

# Adjust the column names based on the printed output
columns_to_drop = ['GeoType', 'GeoID', 'GeoRank', 'Geography']  # Update with correct column names

# Drop irrelevant columns for modeling
data = data.drop(columns_to_drop, axis=1)

# Identify categorical columns
categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

# One-hot encode categorical columns
data = pd.get_dummies(data, columns=categorical_columns)

# Define features (X) and target variable (y)
X = data.drop(['Percent_Obesity', 'Mean mcg/m3'], axis=1)
y = data['Estimated annual rate per 10,000']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the SVM regressor
svm_regressor = SVR(kernel='linear', C=1.0)

# Perform cross-validation
cv_scores = cross_val_score(svm_regressor, X, y, cv=5, scoring='neg_mean_squared_error')

# Train the model on the full training set
svm_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_regressor.predict(X_test)

# Evaluate the model on the test set
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Cross-Validation Mean Squared Error (MSE): {-cv_scores.mean()}')
print(f'Mean Squared Error (MSE) on Test Set: {mse}')
print(f'R-squared (R2) on Test Set: {r2}')


