import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define parameters
num_records = 1000  # Ensure at least 1,000 rows
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Health & Beauty']
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']

# Generate data
data = {
    "Order_ID": [fake.uuid4() for _ in range(num_records)],
    "Customer_Name": [fake.name() for _ in range(num_records)],
    "Email": [fake.email() for _ in range(num_records)],
    "Product_Category": [random.choice(categories) for _ in range(num_records)],
    "Purchase_Amount": [round(random.uniform(10.0, 500.0), 2) for _ in range(num_records)],
    "Quantity": [random.randint(1, 5) for _ in range(num_records)],
    "Order_Date": [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
    "Payment_Method": [random.choice(payment_methods) for _ in range(num_records)],
    "Region": [fake.city() for _ in range(num_records)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add more rows if necessary to exceed 1,000
while len(df) < 1000:
    extra_rows = {
        "Order_ID": fake.uuid4(),
        "Customer_Name": fake.name(),
        "Email": fake.email(),
        "Product_Category": random.choice(categories),
        "Purchase_Amount": round(random.uniform(10.0, 500.0), 2),
        "Quantity": random.randint(1, 5),
        "Order_Date": fake.date_between(start_date='-2y', end_date='today'),
        "Payment_Method": random.choice(payment_methods),
        "Region": fake.city(),
    }
    df = pd.concat([df, pd.DataFrame([extra_rows])], ignore_index=True)

# Save to CSV
df.to_csv("faker_ecommerce_data.csv", index=False)

print(f"Faker dataset generated with {len(df)} rows and saved as faker_ecommerce_data.csv!")
