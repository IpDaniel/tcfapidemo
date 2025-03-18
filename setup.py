import pandas as pd
import os

# Create database directory if it doesn't exist
os.makedirs('database', exist_ok=True)

# Sample data for products
products_data = {
    'product_id': [1, 2, 3, 4, 5],
    'seller_id': [1, 1, 2, 2, 3],
    'name': ['Gaming Laptop', 'Wireless Mouse', 'Smartphone', 'Tablet', 'Headphones'],
    'price': [1299.99, 29.99, 699.99, 349.99, 159.99],
    'description': [
        'High-performance gaming laptop with RTX 3080',
        'Ergonomic wireless mouse with long battery life',
        'Latest model smartphone with 5G capability',
        '10-inch tablet with HD display',
        'Noise-cancelling Bluetooth headphones'
    ]
}
products_df = pd.DataFrame(products_data)
products_df.to_excel('database/products.xlsx', index=False)

# Sample data for customers
customers_data = {
    'customer_id': [1, 2, 3],
    'name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'email': ['john@example.com', 'jane@example.com', 'bob@example.com'],
    'password': ['hashed_password1', 'hashed_password2', 'hashed_password3']
}
customers_df = pd.DataFrame(customers_data)
customers_df.to_excel('database/customers.xlsx', index=False)

# Sample data for sellers
sellers_data = {
    'seller_id': [1, 2, 3],
    'name': ['Tech Store', 'Electronics Hub', 'Audio Shop'],
    'email': ['tech@store.com', 'electronics@hub.com', 'audio@shop.com'],
    'password': ['hashed_password1', 'hashed_password2', 'hashed_password3']
}
sellers_df = pd.DataFrame(sellers_data)
sellers_df.to_excel('database/sellers.xlsx', index=False)

# Sample data for finances (just cash records)
finances_data = {
    'transaction_id': [1, 2, 3, 4],
    'date': ['2024-03-15', '2024-03-15', '2024-03-16', '2024-03-16'],
    'type': ['sale', 'sale', 'sale', 'sale'],
    'customer_id': [1, 2, 1, 3],
    'product_id': [1, 3, 2, 5],
    'quantity': [1, 1, 2, 1],
    'amount': [1299.99, 699.99, 59.98, 159.99],
    'cash_balance': [1299.99, 1999.98, 2059.96, 2219.95]
}
finances_df = pd.DataFrame(finances_data)
finances_df.to_excel('database/finances.xlsx', index=False)

print("Sample data has been created in the database directory.")
