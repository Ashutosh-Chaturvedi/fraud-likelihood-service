import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


NUMERIC_FEATURES = [
    "amount",
    "account_age_days",
    "num_transactions_last_24h",
    "avg_transaction_amount_7d",
]

CATEGORICAL_FEATURES = [
    "transaction_type"
]

BOOLEAN_FEATURES = [
    "is_international"
]

TARGET = "is_fraud"


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def build_preprocessor() -> ColumnTransformer:
    numeric_transformer = "passthrough"

    categorical_transformer = OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, NUMERIC_FEATURES),
            ("cat", categorical_transformer, CATEGORICAL_FEATURES),
            ("bool", "passthrough", BOOLEAN_FEATURES),
        ]
    )

    return preprocessor


def split_features_labels(df: pd.DataFrame):
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    return X, y


def train_val_split(X, y, test_size=0.2, random_state=42):
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
