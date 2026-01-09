import pandas as pd
import os
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('./logs', exist_ok=True)

### Book Data

# Add loan duration column to book dataframe
def enrich_dateDuration(colA, colB, df):
    """
    Takes the two datetime input column names and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note:
    colB>colA
    """
    df['date_delta'] = (df[colB]-df[colA]).dt.days

    #Conditional Filtering to be able to gauge eroneous loans.
    df.loc[df['date_delta'] < 0, 'valid_loan_flag'] = False
    df.loc[df['date_delta'] >= 0, 'valid_loan_flag'] = True

    return df


def save_metrics_to_csv(metrics_data, filename='./logs/cleaning_metrics.csv'):
    """Save metrics data to CSV for dashboard creation"""
    df_metrics = pd.DataFrame([metrics_data])

    # Append to existing file or create new one
    if os.path.exists(filename):
        df_metrics.to_csv(filename, mode='a', header=False, index=False)
    else:
        df_metrics.to_csv(filename, index=False)


def clean_book_data(input_file_path, output_file_path):
    start_time = datetime.now()
    
    # Import data into a Pandas dataframe
    book_df = pd.read_csv(input_file_path)
    initial_rows = len(book_df)

    # Count blank/null values before cleaning
    blank_values_before = book_df.isnull().sum().sum()

    # Remove rows with null Id or Book name
    before_null_removal = len(book_df)
    book_df = book_df.dropna(subset=["Id","Books"])
    null_rows_dropped = before_null_removal - len(book_df)

    # Drop duplicate records
    before_dedup = len(book_df)
    book_df = book_df.drop_duplicates()
    duplicates_dropped = before_dedup = len(book_df)

    # Remove leading and trailing spaces from Book name
    book_df["Books"] = book_df["Books"].str.strip()

    # Remove double quotes around the Book checkout dates
    book_df.loc[:, "Book checkout"] = book_df["Book checkout"].str.strip('"')

    ## Update Book checkout date for Book checkout is 32/05/2023
    #book_df.loc[book_df["Book checkout"] == "32/05/2023", "Book checkout"] = "31/05/2023"   # Generalise this

    # Validate dates and remove invalid records
    before_date_validation = len(book_df)

    # Try to convert dates
    book_df["Book checkout"] = pd.to_datetime(book_df["Book checkout"], format="%d/%m/%Y", errors='coerce')
    book_df["Book Returned"] = pd.to_datetime(book_df["Book Returned"], format="%d/%m/%Y", errors='coerce')

    # Remove rows where date conversion failed (NaT -  Not a Time)
    book_df = book_df.dropna(subset=["Book checkout", "Book Returned"])
    invalid_dates_removed = before_date_validation - len(book_df)

    # Convert float id values to int
    book_df["Customer ID"] = book_df[["Customer ID"]].astype("Int64")
    book_df["Id"] = book_df[["Id"]].astype("Int64")

    # Enrich dataframe
    book_df = enrich_dateDuration(df=book_df, colA='Book Returned', colB='Book checkout')

    # Count invalid rows
    invalid_loans = (book_df['date_delta'] < 0).sum()
    valid_loans = (book_df['date_delta'] >= 0).sum()

    # Calculate row metrics
    final_rows = len(book_df)
    total_dropped = initial_rows - final_rows
    retention_rate = (final_rows/initial_rows)*100

    #Calculate processing time
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    # Save metrics to CSV for dashboard
    metrics = {
        'timestamp': start_time,
        'dataset': 'books',
        'initial_rows': initial_rows,
        'final_rows': final_rows,
        'null_rows_dropped': null_rows_dropped,
        'duplicates_dropped': duplicates_dropped,
        'invalid_dates_removed': invalid_dates_removed,
        'invalid_loans': invalid_loans,
        'valid_loans': valid_loans,
        'total_dropped': total_dropped,
        'retention_rate': retention_rate,
        'blank_values_before': blank_values_before,
        'processing_time_seconds': processing_time,
        'input_file': input_file_path,
        'output_file': output_file_path
    }
    save_metrics_to_csv(metrics)

    # Write cleaned data into csv file
    book_df.to_csv(output_file_path, index=False)
    print("Book file cleaned.")



### Customer Data

def clean_customer_data(input_file_path, output_file_path):
    start_time = datetime.now()

    # Import data into a Pandas dataframe
    cust_df = pd.read_csv(input_file_path)
    initial_rows = len(cust_df)

    # Count blank/null values before cleaning
    blank_values_before = cust_df.isnull().sum().sum()

    # Drop null values
    before_null_removal = len(cust_df)
    cust_df = cust_df.dropna(subset=["Customer ID"])
    null_rows_dropped = before_null_removal - len(cust_df)

    # Convert float Customer id values to int
    cust_df["Customer ID"] = cust_df[["Customer ID"]].astype("Int64")

    # Calculate row metrics
    final_rows = len(cust_df)
    total_dropped = initial_rows - final_rows
    retention_rate = (final_rows/initial_rows)*100

    # Calculate processing time
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    # Save metrics to CSV for dashboard
    metrics = {
        'timestamp': start_time,
        'dataset': 'customers',
        'initial_rows': initial_rows,
        'final_rows': final_rows,
        'null_rows_dropped': null_rows_dropped,
        'duplicates_dropped': 0,
        'invalid_dates_removed': 0,
        'invalid_loans': 0,
        'valid_loans': 0,
        'total_dropped': total_dropped,
        'retention_rate': retention_rate,
        'blank_values_before': blank_values_before,
        'processing_time_seconds': processing_time,
        'input_file': input_file_path,
        'output_file': output_file_path
    }
    save_metrics_to_csv(metrics)

    # Write cleaned data into csv file
    cust_df.to_csv(output_file_path, index=False)
    print("Customer file cleaned.")

if __name__ == "__main__":
    clean_book_data(input_file_path="./sample_data/03_Library Systembook.csv", output_file_path="./cleaned_data/03_Library Systembook.csv")
    clean_customer_data(input_file_path="./sample_data/03_Library Systemcustomers.csv", output_file_path="./cleaned_data/03_Library Systemcustomers.csv")