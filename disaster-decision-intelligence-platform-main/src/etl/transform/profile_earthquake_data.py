import pandas as pd

FILE_PATH = "data/raw/earthquakes.csv"


def profile_data(df):

    print("=" * 60)
    print("EARTHQUAKE DATA PROFILE")
    print("=" * 60)

    print(f"\nRows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names")
    print("-" * 60)
    print(df.columns.tolist())

    print("\nData Types")
    print("-" * 60)
    print(df.dtypes)

    print("\nMissing Values")
    print("-" * 60)
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print("-" * 60)
    print(df.duplicated().sum())

    print("\nStatistical Summary")
    print("-" * 60)
    print(df.describe())


def main():

    df = pd.read_csv(FILE_PATH)

    profile_data(df)


if __name__ == "__main__":
    main()