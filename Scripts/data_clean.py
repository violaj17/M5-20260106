import pandas as pd


### Book Data

# Add load duration column to book dataframe
def dataEnrich(df):
    return df['Book Returned'] - df['Book checkout']


def clean_book_data(input_file_path, output_file_path):
    # Import data into a Pandas dataframe
    book_df = pd.read_csv(input_file_path)
    # Drop duplicate records
    book_df = book_df.drop_duplicates()
    # Remove rows with null Id or Book name
    book_df = book_df.dropna(subset=["Id","Books"])
    # Remove leading and trailing spaces from Book name
    book_df["Books"] = book_df["Books"].str.strip()
    # Remove double quotes around the Book checkout dates
    book_df.loc[:, "Book checkout"] = book_df["Book checkout"].str.strip('"')
    # Update Book checkout date for Book checkout is 32/05/2023
    book_df.loc[book_df["Book checkout"] == "32/05/2023", "Book checkout"] = "31/05/2023"   # Generalise this
    # Convert dates
    book_df["Book checkout"] = pd.to_datetime(book_df["Book checkout"], format="%d/%m/%Y")
    book_df["Book Returned"] = pd.to_datetime(book_df["Book Returned"], format="%d/%m/%Y")
    # Convert float id values to int
    book_df["Customer ID"] = book_df[["Customer ID"]].astype("Int64")
    book_df["Id"] = book_df[["Id"]].astype("Int64")
    # Enrich dataframe
    book_df['Loan duration'] = dataEnrich(df=book_df)
    # Write cleaned data into csv file
    book_df.to_csv(output_file_path, index=False)
    print("Book file cleaned.")



### Customer Data

def clean_customer_data(input_file_path, output_file_path):
    # Import data into a Pandas dataframe
    cust_df = pd.read_csv(input_file_path)
    # Drop null values
    cust_df = cust_df.dropna(subset=["Customer ID"])
    # Convert float Customer id values to int
    cust_df["Customer ID"] = cust_df[["Customer ID"]].astype("Int64")
    # Write cleaned data into csv file
    cust_df.to_csv(output_file_path, index=False)
    print("Customer file cleaned.")

if __name__ == "__main__":
    clean_book_data(input_file_path="./Sample data/03_Library Systembook.csv", output_file_path="./Cleaned data/03_Library Systembook.csv")
    clean_customer_data(input_file_path="./Sample data/03_Library Systemcustomers.csv", output_file_path="./Cleaned data/03_Library Systemcustomers.csv")