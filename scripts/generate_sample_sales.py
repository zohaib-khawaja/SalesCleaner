import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurable parameters
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 1, 1)
products = ['Widget A', 'Widget B', 'Widget C']
price_range = {'Widget A': (1.5, 2.5), 'Widget B': (2.5, 3.5), 'Widget C': (1.0, 2.0)}
num_records = 1000  # Adjust as needed

# Generate synthetic data
records = []
for _ in range(num_records):
    date = start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days))
    product = np.random.choice(products)
    price = round(np.random.uniform(*price_range[product]), 2)
    quantity = np.random.randint(1, 100)  # Adjust max quantity as per your context
    records.append((date, product, quantity, price))

# Convert to DataFrame
sales_data = pd.DataFrame(records, columns=['date', 'product_name', 'quantity', 'price'])

# Show sample data
print(sales_data.head())

# Save or insert into your database
# For saving to CSV
sales_data.to_csv('synthetic_sales_data.csv', index=False)