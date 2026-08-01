import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


NUM_ORDERS = 50_000

PRODUCTS_PATH = Path("datasets/products/products.csv")
WEBSITE_CUSTOMERS_PATH = Path("datasets/website/customers_website.csv")
MOBILE_CUSTOMERS_PATH = Path("datasets/mobile/customers_mobile.csv")
STORE_CUSTOMERS_PATH = Path("datasets/store/customers_store.csv")
OUTPUT_PATH = Path("datasets/orders/orders.csv")


def load_source_data() -> tuple[pd.DataFrame, dict[str, list[str]]]:
    products_df = pd.read_csv(PRODUCTS_PATH)

    website_customers = pd.read_csv(WEBSITE_CUSTOMERS_PATH)
    mobile_customers = pd.read_csv(MOBILE_CUSTOMERS_PATH)
    store_customers = pd.read_csv(STORE_CUSTOMERS_PATH)

    customer_ids = {
        "Website": website_customers["customer_id"].dropna().tolist(),
        "Mobile": mobile_customers["mobile_customer_id"].dropna().tolist(),
        "Store": store_customers["store_customer_id"].dropna().tolist(),
    }

    return products_df, customer_ids


def random_order_date() -> str:
    today = datetime.today()
    order_date = today - timedelta(days=random.randint(0, 730))

    return order_date.strftime("%Y-%m-%d")


def generate_orders(
    products_df: pd.DataFrame,
    customer_ids: dict[str, list[str]],
) -> pd.DataFrame:
    orders = []

    source_weights = {
        "Website": 50,
        "Mobile": 30,
        "Store": 20,
    }

    source_names = list(source_weights.keys())
    source_probabilities = list(source_weights.values())

    product_records = products_df.to_dict("records")

    for order_number in range(1, NUM_ORDERS + 1):
        source_system = random.choices(
            source_names,
            weights=source_probabilities,
            k=1,
        )[0]

        customer_id = random.choice(customer_ids[source_system])
        product = random.choice(product_records)

        quantity = random.randint(1, 5)
        unit_price = float(product["unit_price"])

        gross_amount = quantity * unit_price

        discount_rate = random.choices(
            [0.00, 0.05, 0.10, 0.15, 0.20],
            weights=[50, 20, 15, 10, 5],
            k=1,
        )[0]

        discount_amount = round(gross_amount * discount_rate, 2)
        taxable_amount = gross_amount - discount_amount

        tax_rate = 0.21
        tax_amount = round(taxable_amount * tax_rate, 2)

        total_amount = round(
            taxable_amount + tax_amount,
            2,
        )

        order_status = random.choices(
            ["Completed", "Pending", "Cancelled", "Refunded"],
            weights=[80, 10, 5, 5],
            k=1,
        )[0]

        orders.append(
            {
                "order_id": f"ORD{order_number:08d}",
                "customer_id": customer_id,
                "source_system": source_system,
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": unit_price,
                "currency": product["currency"],
                "discount_amount": discount_amount,
                "tax_amount": tax_amount,
                "total_amount": total_amount,
                "order_status": order_status,
                "order_date": random_order_date(),
            }
        )

    return pd.DataFrame(orders)


def main() -> None:
    if not PRODUCTS_PATH.exists():
        raise FileNotFoundError(
            f"Products file not found: {PRODUCTS_PATH}"
        )

    products_df, customer_ids = load_source_data()

    orders_df = generate_orders(
        products_df=products_df,
        customer_ids=customer_ids,
    )

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    orders_df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print(f"{len(orders_df)} orders generated successfully!")
    print(f"Saved to: {OUTPUT_PATH}")

    print("\nOrders by source system:")
    print(orders_df["source_system"].value_counts())

    print("\nOrders by status:")
    print(orders_df["order_status"].value_counts())


if __name__ == "__main__":
    main()