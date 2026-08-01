import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


ORDERS_PATH = Path("datasets/orders/orders.csv")
OUTPUT_PATH = Path("datasets/payments/payments.csv")


def generate_payment_date(order_date: str, late: bool = False) -> str:
    order_dt = datetime.strptime(order_date, "%Y-%m-%d")

    delay_days = random.randint(2, 7) if late else random.randint(0, 1)

    return (order_dt + timedelta(days=delay_days)).strftime("%Y-%m-%d")


def generate_payments(orders_df: pd.DataFrame) -> pd.DataFrame:
    payments = []

    for payment_number, order in enumerate(
        orders_df.itertuples(index=False),
        start=1,
    ):
        if order.order_status == "Cancelled":
            payment_status = random.choices(
                ["Failed", "Not Attempted"],
                weights=[70, 30],
                k=1,
            )[0]

        elif order.order_status == "Refunded":
            payment_status = "Refunded"

        elif order.order_status == "Pending":
            payment_status = random.choices(
                ["Pending", "Failed"],
                weights=[75, 25],
                k=1,
            )[0]

        else:
            payment_status = random.choices(
                ["Successful", "Failed"],
                weights=[97, 3],
                k=1,
            )[0]

        payment_method = random.choices(
            [
                "Credit Card",
                "Debit Card",
                "PayPal",
                "Bank Transfer",
                "Digital Wallet",
            ],
            weights=[35, 25, 15, 15, 10],
            k=1,
        )[0]

        is_late = random.random() < 0.05

        if payment_status == "Successful":
            payment_amount = float(order.total_amount)
        elif payment_status == "Refunded":
            payment_amount = -float(order.total_amount)
        elif payment_status == "Pending":
            payment_amount = float(order.total_amount)
        else:
            payment_amount = 0.0

        payments.append(
            {
                "payment_id": f"PAY{payment_number:08d}",
                "order_id": order.order_id,
                "payment_method": payment_method,
                "payment_status": payment_status,
                "payment_amount": round(payment_amount, 2),
                "currency": order.currency,
                "payment_date": generate_payment_date(
                    order_date=order.order_date,
                    late=is_late,
                ),
                "late_arrival_flag": "Y" if is_late else "N",
            }
        )

    return pd.DataFrame(payments)


def main() -> None:
    if not ORDERS_PATH.exists():
        raise FileNotFoundError(
            f"Orders file not found: {ORDERS_PATH}"
        )

    orders_df = pd.read_csv(ORDERS_PATH)
    payments_df = generate_payments(orders_df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    payments_df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print(f"{len(payments_df)} payments generated successfully!")
    print(f"Saved to: {OUTPUT_PATH}")

    print("\nPayments by status:")
    print(payments_df["payment_status"].value_counts())

    print("\nLate-arriving payments:")
    print(payments_df["late_arrival_flag"].value_counts())


if __name__ == "__main__":
    main()