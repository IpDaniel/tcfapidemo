import pandas as pd
import os
from typing import Dict, Any, Optional

def get_product_by_id(product_id: int) -> Optional[Dict[str, Any]]:
    """
    Retrieve product information by product ID.
    Returns None if product not found.
    """
    try:
        df = pd.read_excel('database/products.xlsx')
        product = df[df['product_id'] == product_id]
        if product.empty:
            return None
        return product.iloc[0].to_dict()
    except Exception as e:
        print(f"Error retrieving product: {e}")
        return None

def add_product(seller_id: int, name: str, price: float, description: str) -> bool:
    """
    Add a new product to the database.
    Returns True if successful, False otherwise.
    """
    try:
        df = pd.read_excel('database/products.xlsx')
        new_product_id = df['product_id'].max() + 1
        new_product = {
            'product_id': new_product_id,
            'seller_id': seller_id,
            'name': name,
            'price': price,
            'description': description
        }
        df = pd.concat([df, pd.DataFrame([new_product])], ignore_index=True)
        df.to_excel('database/products.xlsx', index=False)
        return True
    except Exception as e:
        print(f"Error adding product: {e}")
        return False

def register_customer(name: str, email: str, password: str) -> Optional[int]:
    """
    Register a new customer.
    Returns the new customer_id if successful, None otherwise.
    """
    try:
        df = pd.read_excel('database/customers.xlsx')
        # Check if email already exists
        if email in df['email'].values:
            print("Email already registered")
            return None
            
        new_customer_id = df['customer_id'].max() + 1
        new_customer = {
            'customer_id': new_customer_id,
            'name': name,
            'email': email,
            'password': password  # Note: In a real application, this should be hashed
        }
        df = pd.concat([df, pd.DataFrame([new_customer])], ignore_index=True)
        df.to_excel('database/customers.xlsx', index=False)
        return new_customer_id
    except Exception as e:
        print(f"Error registering customer: {e}")
        return None

def purchase_product(customer_id: int, product_id: int, quantity: int = 1) -> bool:
    """
    Process a product purchase.
    Returns True if successful, False otherwise.
    """
    try:
        # Load necessary dataframes
        products_df = pd.read_excel('database/products.xlsx')
        finances_df = pd.read_excel('database/finances.xlsx')
        
        # Get product details
        product = products_df[products_df['product_id'] == product_id]
        if product.empty:
            print("Product not found")
            return False
            
        # Calculate transaction details
        price = product.iloc[0]['price']
        total_amount = price * quantity
        new_transaction_id = finances_df['transaction_id'].max() + 1
        current_balance = finances_df['cash_balance'].iloc[-1] if not finances_df.empty else 0
        new_balance = current_balance + total_amount
        
        # Create new transaction
        new_transaction = {
            'transaction_id': new_transaction_id,
            'date': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'type': 'sale',
            'customer_id': customer_id,
            'product_id': product_id,
            'quantity': quantity,
            'amount': total_amount,
            'cash_balance': new_balance
        }
        
        # Update finances
        finances_df = pd.concat([finances_df, pd.DataFrame([new_transaction])], ignore_index=True)
        finances_df.to_excel('database/finances.xlsx', index=False)
        return True
    except Exception as e:
        print(f"Error processing purchase: {e}")
        return False
