import pandas as pd

# Load master customer data
master_df = pd.read_csv("datasets/master/master_customers.csv")

# Select 4000 random customers
website_df = master_df.sample(
    n=4000,
    random_state=42
).reset_index(drop=True)

# Create Website Customer IDs
website_df["customer_id"] = [
    f"WC{i:06d}"
    for i in range(1, len(website_df) + 1)
]

# Keep only Website columns
website_df = website_df[
    [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "city",
        "country",
        "registration_date",
        "marketing_opt_in"
    ]
]

# Save Website dataset
website_df.to_csv(
    "datasets/website/customers_website.csv",
    index=False
)

print(f"{len(website_df)} Website customers generated successfully!")