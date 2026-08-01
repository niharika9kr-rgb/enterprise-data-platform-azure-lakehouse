from datetime import datetime, timedelta
import random
import pandas as pd

rows = []

start_date = datetime.today() - timedelta(days=730)

for i in range(731):

    current_date = start_date + timedelta(days=i)

    rows.append({
        "exchange_date": current_date.strftime("%Y-%m-%d"),
        "EUR": 1.0000,
        "USD": round(random.uniform(1.05, 1.20), 4),
        "GBP": round(random.uniform(0.82, 0.95), 4)
    })

df = pd.DataFrame(rows)

df.to_csv(
    "datasets/reference/exchange_rates.csv",
    index=False
)

print(
    f"{len(df)} exchange rates generated."
)