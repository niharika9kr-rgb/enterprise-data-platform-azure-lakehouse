import random
import pandas as pd
from faker import Faker

# Create Faker object
fake = Faker("nl_NL")

# Number of customers
NUM_CUSTOMERS = 5000

# Possible values
loyalty_tiers = ["Bronze", "Silver", "Gold", "Platinum"]
countries = ["Netherlands", "Germany", "Belgium", "France"]

customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    customers.append({
        "master_customer_id": f"C{i:06d}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "gender": random.choice(["Male", "Female"]),
        "date_of_birth": fake.date_of_birth(
            minimum_age=18,
            maximum_age=80
        ),
        "city": fake.city(),
        "country": random.choice(countries),
        "registration_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "loyalty_tier": random.choice(loyalty_tiers),
        "marketing_opt_in": random.choice(["Yes", "No"])
    })

# Convert to DataFrame
df = pd.DataFrame(customers)

# Save dataset
df.to_csv(
    "datasets/master/master_customers.csv",
    index=False
)

print(f"{len(df)} master customers generated successfully!")