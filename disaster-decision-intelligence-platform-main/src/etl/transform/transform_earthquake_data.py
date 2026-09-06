import pandas as pd

INPUT_FILE = "data/raw/earthquakes.csv"
OUTPUT_FILE = "data/processed/earthquakes_processed.csv"


def transform_data():

    df = pd.read_csv(INPUT_FILE)

    # --------------------------
    # Remove duplicate records
    # --------------------------
    df.drop_duplicates(inplace=True)

    # --------------------------
    # Remove rows with missing magnitude
    # --------------------------
    df.dropna(subset=["magnitude"], inplace=True)

    # --------------------------
    # Convert Unix timestamp to datetime
    # --------------------------
    df["time"] = pd.to_datetime(df["time"], unit="ms")
    df["updated"] = pd.to_datetime(df["updated"], unit="ms")

    # --------------------------
    # Rename columns
    # --------------------------
    df.rename(columns={
        "mag": "magnitude"
    }, inplace=True)

    # --------------------------
    # Create Date column
    # --------------------------
    df["date"] = df["time"].dt.date

    # --------------------------
    # Create Hour column
    # --------------------------
    df["hour"] = df["time"].dt.hour

    # --------------------------
    # Save cleaned dataset
    # --------------------------
    df.to_csv(OUTPUT_FILE, index=False)

    print("Transformation Completed")
    print(df.head())
    print()
    print(f"Processed Records : {len(df)}")


if __name__ == "__main__":
    transform_data()