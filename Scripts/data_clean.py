import pandas as pd


## Book Data

# Import Book data into a Pandas dataframe
book_dataframe = pd.read_csv("./Sample data/03_Library Systembook.csv")

# Remove columns with missing Id or Book name
book_df = book_dataframe.dropna(subset=["Id","Books"])

# Convert Book Returned column to date
book_df.loc[:, "Book Returned"] = pd.to_datetime(book_df["Book Returned"])
# book_df["Book Returned"].dtype

# Remove double quotes around the Book checkout dates
book_df.loc[:, "Book checkout"] = book_df["Book checkout"].str.strip('"')

# Update Book checkout date for Book checkout is 32/05/2023
book_df.loc[book_df["Book checkout"] == "32/05/2023", "Book checkout"] = "31/05/2023"
# book_df[book_df["Book checkout"] == "32/05/2023"]

# Convert Book chceckout column to date
book_df["Book checkout"] = pd.to_datetime(book_df["Book checkout"], format="%d/%m/%Y")
# book_df["Book checkout"].dtype
# book_df

# Convert Book Returned column to date
book_df["Book Returned"] = pd.to_datetime(book_df["Book Returned"], format="%d/%m/%Y")
# book_df["Book Returned"].dtype

# Remove time and keep date only
book_df.loc[:, "Book checkout"] = pd.to_datetime(book_df["Book checkout"]).dt.date
book_df.loc[:, "Book Returned"] = pd.to_datetime(book_df["Book Returned"]).dt.date

# Find duplicate records
# book_df[book_df.duplicated(subset=["Books"], keep=False)]

# Drop duplicate records
book_df = book_df.drop_duplicates(subset=["Books"])

# Convert float id values to int
# book_df.loc[:, ["Id", "Customer ID"]] = book_df[["Id", "Customer ID"]].astype("Int64")    # Didn't work

book_df["Customer ID"] = book_df[["Customer ID"]].astype("Int64")
book_df["Id"] = book_df[["Id"]].astype("Int64")

# Add load duration column to book dataframe
def loan_duration(df):
    return df['Book Returned'] - df['Book checkout']
book_df['Loan duration'] = loan_duration(df=book_df)



### Customer Data

# Import Customers data into a Pandas dataframe
customers_dataframe = pd.read_csv("./Sample data/03_Library Systemcustomers.csv")
customers_dataframe

# Drop null values
customers_df = customers_dataframe.dropna(subset=["Customer ID"])

# Convert float Customer id values to int
customers_df["Customer ID"] = customers_df[["Customer ID"]].astype("Int64")

