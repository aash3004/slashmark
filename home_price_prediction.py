import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb

# Step 1: Data Collection
# Assume you have a dataset named 'housing_data.csv' with columns for income, schools, hospitals, crime rates, and home prices
data = pd.read_csv('kc_house_data.csv')

# Step 2: Data Preprocessing
# Handle missing values, encode categorical variables, scale numerical features, split data into training and testing sets
X = data[['floors', 'bedrooms', 'bathrooms', 'condition']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Feature Engineering (if needed)

# Step 4: Model Training
xgb_model = xgb.XGBRegressor()
xgb_model.fit(X_train, y_train)

# Step 5: Model Evaluation
y_pred = xgb_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# You can also print other evaluation metrics like RMSE, R-squared

# Step 6: Prediction
# Assume new_data is a DataFrame containing new observations with features: income, schools, hospitals, crime rates
new_data = pd.DataFrame({'floors': [2], 'bedrooms': [3], 'bathrooms': [3], 'condition': [3]})
predicted_price = xgb_model.predict(new_data)
print("Predicted Home Price:", predicted_price)
