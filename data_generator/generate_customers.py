import csv
import random
from datetime import datetime, timedelta

# Sample data
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Sophia",
    "James", "Charlotte", "Lucas", "Mia", "Ethan"
]

last_names = [
    "Johnson", "Smith", "Brown", "Taylor", "Wilson",
    "Anderson", "Thomas", "Martin", "White", "Moore"
]

countries = [
    "Netherlands",
    "Germany",
    "USA",
    "India"
]

today = datetime.today()

# Store all customer records
rows = []

# Generate 1000 customers
for i in range(1, 1001):

    customer_id = f"WC{i:06d}"

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    email = (
        first_name.lower()
        + "."
        + last_name.lower()
        + str(i)
        + "@retailmart.com"
    )

    phone = "+31 6 " + str(random.randint(10000000, 99999999))

    country = random.choice(countries)

    registration_date = (
        today - timedelta(days=random.randint(1, 730))
    ).strftime("%Y-%m-%d")

    marketing_opt_in = random.choice(["Yes", "No"])

    rows.append([
        customer_id,
        first_name,
        last_name,
        email,
        phone,
        country,
        registration_date,
        marketing_opt_in
    ])

# Write the data to a CSV file
with open(
    "datasets/website/customers_website.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    # Header row
    writer.writerow([
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "country",
        "registration_date",
        "marketing_opt_in"
    ])

    # Data rows
    writer.writerows(rows)

print("Website customer dataset generated successfully!")