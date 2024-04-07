import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def fetch_sales_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    data['date'] = pd.to_datetime(data['date'])
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    return data.drop(['date', 'product_name'], axis=1)

def train_model(data):
    X = data[['month', 'year', 'price']]  # predictors
    y = data['quantity']  # target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    return model

def predict_sales(model, month, year, price):
    return model.predict([[month, year, price]])[0]

# Main execution function
def main():
    file_path = 'synthetic_sales_data.csv'
    sales_data = fetch_sales_data(file_path)
    processed_data = preprocess_data(sales_data)
    model = train_model(processed_data)
    # Example prediction
    predicted_quantity = predict_sales(model, 5, 2023, 2.5)
    print(f"Predicted sales quantity: {predicted_quantity}")

if __name__ == "__main__":
    main()