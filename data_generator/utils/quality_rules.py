import random

import pandas as pd


def add_missing_values(
    dataframe: pd.DataFrame,
    column: str,
    count: int,
    random_state: int,
) -> pd.DataFrame:
    """Set a fixed number of values in one column to null."""
    result = dataframe.copy()

    indexes = result.sample(
        n=min(count, len(result)),
        random_state=random_state,
    ).index

    result.loc[indexes, column] = pd.NA
    return result


def add_invalid_emails(
    dataframe: pd.DataFrame,
    column: str,
    count: int,
    random_state: int,
) -> pd.DataFrame:
    """Replace valid emails with intentionally invalid formats."""
    result = dataframe.copy()

    indexes = result.sample(
        n=min(count, len(result)),
        random_state=random_state,
    ).index

    invalid_patterns = [
        "invalid.email",
        "missing-at-symbol.com",
        "customer@",
        "@retailmart.com",
        "customer@@example.com",
    ]

    for index in indexes:
        result.at[index, column] = random.choice(invalid_patterns)

    return result


def add_extra_spaces(
    dataframe: pd.DataFrame,
    column: str,
    count: int,
    random_state: int,
) -> pd.DataFrame:
    """Add leading and trailing spaces to selected values."""
    result = dataframe.copy()

    indexes = result.sample(
        n=min(count, len(result)),
        random_state=random_state,
    ).index

    for index in indexes:
        value = result.at[index, column]
        if pd.notna(value):
            result.at[index, column] = f"  {value}  "

    return result


def add_mixed_case(
    dataframe: pd.DataFrame,
    column: str,
    count: int,
    random_state: int,
) -> pd.DataFrame:
    """Apply inconsistent casing to selected string values."""
    result = dataframe.copy()

    indexes = result.sample(
        n=min(count, len(result)),
        random_state=random_state,
    ).index

    for position, index in enumerate(indexes):
        value = result.at[index, column]

        if pd.isna(value):
            continue

        text = str(value)

        if position % 3 == 0:
            result.at[index, column] = text.upper()
        elif position % 3 == 1:
            result.at[index, column] = text.lower()
        else:
            result.at[index, column] = text.swapcase()

    return result


def add_duplicate_records(
    dataframe: pd.DataFrame,
    count: int,
    random_state: int,
) -> pd.DataFrame:
    """Append exact duplicate rows to the dataset."""
    duplicates = dataframe.sample(
        n=min(count, len(dataframe)),
        random_state=random_state,
    ).copy()

    return pd.concat(
        [dataframe, duplicates],
        ignore_index=True,
    )