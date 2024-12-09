import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Load the dataset
sensor_data = pd.read_csv("sensor_data.csv")  # Replace with the correct path to your file

# Prepare data
X = sensor_data[['Temperature (°C)', 'Pressure (hPa)']]  # Features
y_humidity = sensor_data['Humidity (%)']  # Target variable (humidity)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_humidity, test_size=0.2, random_state=42)

# Function to fit and evaluate polynomial regression for a range of degrees
def optimize_polynomial_regression(X_train, y_train, X_test, y_test, max_degree=5):
    results = []
    for degree in range(1, max_degree + 1):
        # Create a pipeline with polynomial features and linear regression
        model = Pipeline([
            ('poly_features', PolynomialFeatures(degree=degree)),
            ('linear_regression', LinearRegression())
        ])
        # Fit the model
        model.fit(X_train, y_train)
        # Predict on test data and calculate mean squared error
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        results.append((degree, mse))
    return results

# Optimize polynomial degree for humidity prediction
humidity_results = optimize_polynomial_regression(X_train, y_train, X_test, y_test, max_degree=5)

# Find the best degree
best_degree, best_mse = min(humidity_results, key=lambda x: x[1])

print("Optimal Polynomial Degree for Humidity Prediction:", best_degree)
print("Mean Squared Error at Optimal Degree:", best_mse)
