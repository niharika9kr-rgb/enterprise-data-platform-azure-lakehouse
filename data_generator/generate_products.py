import random
from pathlib import Path

import pandas as pd


CATEGORY_CONFIG = {
    "Electronics": {
        "products": [
            "Laptop",
            "Monitor",
            "Keyboard",
            "Mouse",
            "Tablet",
            "Smartphone",
            "Headphones",
        ],
        "brands": ["Apple", "Samsung", "Sony", "LG", "Lenovo", "Dell"],
        "price_range": (25, 2200),
    },
    "Clothing": {
        "products": [
            "T-Shirt",
            "Jeans",
            "Jacket",
            "Sneakers",
            "Dress",
        ],
        "brands": ["Nike", "Adidas", "Puma", "Zara", "H&M"],
        "price_range": (15, 350),
    },
    "Home": {
        "products": [
            "Chair",
            "Desk",
            "Coffee Machine",
            "Vacuum Cleaner",
            "Dining Table",
        ],
        "brands": ["IKEA", "Philips", "Bosch", "Dyson", "Siemens"],
        "price_range": (30, 1500),
    },
    "Sports": {
        "products": [
            "Football",
            "Yoga Mat",
            "Running Shoes",
            "Dumbbells",
            "Fitness Tracker",
        ],
        "brands": ["Nike", "Adidas", "Puma", "Reebok", "Garmin"],
        "price_range": (10, 700),
    },
    "Beauty": {
        "products": [
            "Perfume",
            "Shampoo",
            "Face Cream",
            "Lipstick",
            "Body Lotion",
        ],
        "brands": ["L'Oreal", "Nivea", "Dove", "Maybelline", "Garnier"],
        "price_range": (5, 250),
    },
}

NUM_PRODUCTS = 1000
OUTPUT_PATH = Path("datasets/products/products.csv")


def generate_products() -> pd.DataFrame:
    products = []
    category_names = list(CATEGORY_CONFIG.keys())

    for product_number in range(1, NUM_PRODUCTS + 1):
        category = random.choice(category_names)
        config = CATEGORY_CONFIG[category]

        product_name = random.choice(config["products"])
        brand = random.choice(config["brands"])
        minimum_price, maximum_price = config["price_range"]

        products.append(
            {
                "product_id": f"P{product_number:06d}",
                "product_name": product_name,
                "category": category,
                "brand": brand,
                "unit_price": round(
                    random.uniform(minimum_price, maximum_price),
                    2,
                ),
                "currency": random.choice(["EUR", "USD", "GBP"]),
                "active_flag": random.choices(
                    ["Y", "N"],
                    weights=[85, 15],
                    k=1,
                )[0],
            }
        )

    return pd.DataFrame(products)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    products_df = generate_products()
    products_df.to_csv(OUTPUT_PATH, index=False)

    print(f"{len(products_df)} products generated successfully!")
    print(f"Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()