#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning

# In[2]:


import pandas as pd


# ## Book Data

# In[31]:


# Import Book data into a Pandas dataframe
book_dataframe = pd.read_csv("./Sample data/03_Library Systembook.csv")
book_dataframe.head(50)


# In[32]:


# Review Book data
book_dataframe.info()


# In[53]:


# Remove columns with missing Id or Book name
book_df = book_dataframe.dropna(subset=["Id","Books"])
book_df


# In[60]:


# Check data types
book_df.info()


# In[62]:


# Convert Book Returned column to date
book_df.loc[:, "Book Returned"] = pd.to_datetime(book_df["Book Returned"])
book_df["Book Returned"].dtype



# In[65]:


# Remove double quotes around the Book checkout dates
book_df.loc[:, "Book checkout"] = book_df["Book checkout"].str.strip('"')

# Update Book checkout date for Book checkout is 32/05/2023
book_df.loc[book_df["Book checkout"] == "32/05/2023", "Book checkout"] = "31/05/2023"
book_df[book_df["Book checkout"] == "32/05/2023"]


# In[155]:


# Convert Book chceckout column to date
book_df["Book checkout"] = pd.to_datetime(book_df["Book checkout"], format="%d/%m/%Y")
# book_df.loc[:, "Book checkout"] = pd.to_datetime(book_df["Book checkout"], format="%d/%m/%Y")
book_df["Book checkout"].dtype
# book_df


# In[159]:


# Convert Book Returned column to date
book_df["Book Returned"] = pd.to_datetime(book_df["Book Returned"], format="%d/%m/%Y")
# book_df.loc[:, "Book Returned"] = pd.to_datetime(book_df["Book Returned"], format="%d/%m/%Y")
book_df["Book Returned"].dtype
# book_df


# In[74]:


# Remove time and keep date only
book_df.loc[:, "Book checkout"] = pd.to_datetime(book_df["Book checkout"]).dt.date
book_df.loc[:, "Book Returned"] = pd.to_datetime(book_df["Book Returned"]).dt.date
book_df


# In[88]:


# Find duplicate records
book_df[book_df.duplicated(subset=["Books"], keep=False)]


# In[89]:


# Drop duplicate records
book_df = book_df.drop_duplicates(subset=["Books"])


# In[ ]:


# Convert float id values to int
# book_df.loc[:, ["Id", "Customer ID"]] = book_df[["Id", "Customer ID"]].astype("Int64")    # Didn't work

book_df["Customer ID"] = book_df[["Customer ID"]].astype("Int64")     # Run this first
book_df.loc[:, ["Customer ID"]] = book_df[["Customer ID"]].astype("Int64")    # Run this second
book_df["Id"] = book_df[["Id"]].astype("Int64")     # Run this first 
book_df.loc[:, ["Id"]] = book_df[["Id"]].astype("Int64")  # Run this second



# In[160]:


book_df


# In[161]:


book_df.info()


# ## Customer Data

# In[145]:


# Import Customers data into a Pandas dataframe
customers_dataframe = pd.read_csv("./Sample data/03_Library Systemcustomers.csv")
customers_dataframe


# In[146]:


# Review Customers data types
customers_dataframe.info()


# In[147]:


# Drop null values
customers_df = customers_dataframe.dropna(subset=["Customer ID"])
customers_df


# In[150]:


# Convert float Customer id values to int
customers_df["Customer ID"] = customers_df[["Customer ID"]].astype("Int64")
customers_df.loc[:, ["Customer ID"]] = customers_df[["Customer ID"]].astype("Int64")


# In[151]:


customers_df


# In[152]:


customers_df.info()


# ## Load cleaned data into new csv files

# In[ ]:


# book_df.to_csv("./Cleaned data/03_Library Systembook_cleaned.csv", index=False)


# In[ ]:


# customers_df.to_csv("./Cleaned data/03_Library Systemcustomers_cleaned.csv", index=False)

