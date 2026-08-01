import random
from datetime import datetime, timedelta

# Sample master data
FIRST_NAMES = [
    "Emma", "Liam", "Olivia", "Noah", "Sophia",
    "James", "Charlotte", "Lucas", "Mia", "Ethan"
]

LAST_NAMES = [
    "Johnson", "Smith", "Brown", "Taylor", "Wilson",
    "Anderson", "Thomas", "Martin", "White", "Moore"
]

COUNTRIES = [
    "Netherlands",
    "Germany",
    "Belgium",
    "France"
]

CITIES = {
    "Netherlands": ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "Belgium": ["Brussels", "Antwerp"],
    "France": ["Paris", "Lyon"]
}

LOYALTY_TIERS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

def generate_customer_id(prefix, number):
    return f"{prefix}{number:06d}"


def generate_name():
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    return first_name, last_name


def generate_email(first_name, last_name, number):
    return f"{first_name.lower()}.{last_name.lower()}{number}@retailmart.com"


def generate_phone():
    return "+31 6 " + str(random.randint(10000000, 99999999))


def generate_country_city():
    country = random.choice(COUNTRIES)
    city = random.choice(CITIES[country])
    return country, city


def generate_registration_date():
    today = datetime.today()
    random_days = random.randint(1, 730)
    return (today - timedelta(days=random_days)).strftime("%Y-%m-%d")


def generate_loyalty_tier():
    return random.choice(LOYALTY_TIERS)


def generate_marketing_opt_in():
    return random.choice(["Yes", "No"])