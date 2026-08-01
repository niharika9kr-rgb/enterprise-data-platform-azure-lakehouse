import pandas as pd

from utils.quality_rules import (
    add_duplicate_records,
    add_extra_spaces,
    add_invalid_emails,
    add_missing_values,
    add_mixed_case,
)

# Load master customer dataset
master_df = pd.read_csv("datasets/master/master_customers.csv")

# ============================================
# WEBSITE
# ============================================

website = master_df.sample(
    n=4000,
    random_state=42
).copy()

website["customer_id"] = [
    f"WC{i:06d}"
    for i in range(1, len(website) + 1)
]

website = website[
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

website = add_missing_values(
    website,
    column="email",
    count=40,
    random_state=401,
)

website = add_missing_values(
    website,
    column="phone",
    count=30,
    random_state=402,
)

website = add_invalid_emails(
    website,
    column="email",
    count=20,
    random_state=403,
)

website = add_extra_spaces(
    website,
    column="first_name",
    count=20,
    random_state=404,
)

website = add_mixed_case(
    website,
    column="last_name",
    count=20,
    random_state=405,
)

website = add_duplicate_records(
    website,
    count=20,
    random_state=406,
)

website.to_csv(
    "datasets/website/customers_website.csv",
    index=False
)

print(f"Website: {len(website)} customers")

# ============================================
# MOBILE
# ============================================

mobile = master_df.sample(
    n=3500,
    random_state=100
).copy()

mobile["mobile_customer_id"] = [
    f"MB{i:06d}"
    for i in range(1, len(mobile) + 1)
]

mobile = mobile.rename(
    columns={
        "first_name": "fname",
        "last_name": "lname",
        "email": "email_address",
        "phone": "mobile_number",
        "registration_date": "signup_date"
    }
)

mobile = mobile[
    [
        "mobile_customer_id",
        "fname",
        "lname",
        "email_address",
        "mobile_number",
        "city",
        "country",
        "signup_date"
    ]
]

mobile = add_missing_values(
    mobile,
    column="email_address",
    count=60,
    random_state=501,
)

mobile = add_missing_values(
    mobile,
    column="mobile_number",
    count=35,
    random_state=502,
)

mobile = add_invalid_emails(
    mobile,
    column="email_address",
    count=15,
    random_state=503,
)

mobile = add_extra_spaces(
    mobile,
    column="fname",
    count=25,
    random_state=504,
)

mobile = add_mixed_case(
    mobile,
    column="lname",
    count=25,
    random_state=505,
)

mobile = add_duplicate_records(
    mobile,
    count=15,
    random_state=506,
)

mobile.to_csv(
    "datasets/mobile/customers_mobile.csv",
    index=False
)

print(f"Mobile: {len(mobile)} customers")

# ============================================
# CRM
# ============================================

crm = master_df.sample(
    n=2800,
    random_state=200
).copy()

crm["crm_customer_id"] = [
    f"CRM{i:06d}"
    for i in range(1, len(crm) + 1)
]

crm = crm[
    [
        "crm_customer_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "loyalty_tier",
        "marketing_opt_in"
    ]
]

crm = add_missing_values(
    crm,
    column="email",
    count=50,
    random_state=601,
)

crm = add_missing_values(
    crm,
    column="phone",
    count=40,
    random_state=602,
)

crm = add_invalid_emails(
    crm,
    column="email",
    count=15,
    random_state=603,
)

crm = add_mixed_case(
    crm,
    column="first_name",
    count=20,
    random_state=604,
)

crm = add_duplicate_records(
    crm,
    count=10,
    random_state=605,
)

crm.to_csv(
    "datasets/crm/customers_crm.csv",
    index=False
)

print(f"CRM: {len(crm)} customers")

# ============================================
# STORE POS
# ============================================

store = master_df.sample(
    n=2000,
    random_state=300
).copy()

store["store_customer_id"] = [
    f"ST{i:06d}"
    for i in range(1, len(store) + 1)
]

# Create full name
store["full_name"] = (
    store["first_name"] + " " + store["last_name"]
)

store = store[
    [
        "store_customer_id",
        "full_name",
        "phone",
        "city"
    ]
]

store = add_missing_values(
    store,
    column="phone",
    count=50,
    random_state=701,
)

store = add_extra_spaces(
    store,
    column="full_name",
    count=30,
    random_state=702,
)

store = add_mixed_case(
    store,
    column="full_name",
    count=30,
    random_state=703,
)

store = add_duplicate_records(
    store,
    count=10,
    random_state=704,
)

store.to_csv(
    "datasets/store/customers_store.csv",
    index=False
)

print(f"Store: {len(store)} customers")