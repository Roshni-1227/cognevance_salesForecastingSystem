import pandas as pd


FILE_PATH = "data/sample_-_superstore.xls"


def load_data(file_path):
    """Load the Orders sheet from the Superstore Excel workbook."""
    return pd.read_excel(file_path, sheet_name="Orders")


def profile_data(df):
    """Generate basic data quality and structure information."""

    print("=" * 60)
    print("SALES DATA QUALITY PROFILE")
    print("=" * 60)

    print(f"\nDataset shape: {df.shape[0]} rows x {df.shape[1]} columns")

    print("\nColumn names:")
    for column in df.columns:
        print(f"- {column}")

    print("\nMissing values:")
    missing_values = df.isnull().sum()
    print(missing_values)

    print(f"\nTotal missing values: {missing_values.sum()}")

    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate rows: {duplicate_count}")

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    print("\nDate range:")
    print(f"Start: {df['Order Date'].min().date()}")
    print(f"End:   {df['Order Date'].max().date()}")

    print("\nNumeric summary:")
    print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())

    print("\nUnique orders:", df["Order ID"].nunique())
    print("Unique customers:", df["Customer ID"].nunique())
    print("Unique products:", df["Product ID"].nunique())


if __name__ == "__main__":
    sales_data = load_data(FILE_PATH)
    profile_data(sales_data)