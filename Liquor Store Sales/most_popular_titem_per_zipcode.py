# The first task at hand is to get the most popular item in each zipcode for 2016-2019. Following
# will be a comprehensive method for data cleaning and extraction utilizing Python Pandas library and plotly for
# visualization in the end.

import pandas as pd
import numpy as np

df = pd.read_csv('finance_liquor_sales.csv')


# Check for missing values and data inconsistency

print(df.info())
# and or
print(df.isnull().sum())

#  We can see that there are missing values in the store_location, county_number, county, category and category_name columns. To avoid introducing bias in our data analysis,
# it is best to drop all rows with missing values.

df.dropna(inplace=True)

# This will ensure that our dataset has non-null values.

print(df.isnull().sum()) # no missing values detected

# reset the index

df = df.reset_index(drop=True)

# Check for data inconsistency

    # date needs to be converted to datetime data type

df['date'] = pd.to_datetime(df['date'])

    # additionally, we will convert the zip_code data type to int64 since the zip_code doesn't have to be a float number

df['zip_code'] = df['zip_code'].astype(np.int64)


# save the new formatted dataset into csv

df.to_csv('cleaned_finance_liquor_sales.csv', index=False) # we can specify the path that we want our data to be saved.
                                                                     # i.e (r'C:\Users\User1\Desktop\cleaned_finance_liquor_sales.csv')

# Filter the DataFrame for years between 2016 and 2019

filtered_df = df[(df['date'].dt.year >= 2016) & (df['date'].dt.year <= 2019)]

# save the new formatted dataset into csv

filtered_df.to_csv(r'C:\Users\User1\Desktop\filtered_finance_liquor_sales.csv', index=False)


# To get the most popular items per zip_code we have to group by two columns, zip_code
# and item_number (since there might be duplicate values for both cases) and sum the bottles_sold

grouped_df = filtered_df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
print(grouped_df)


# Now we can visualize the data. I went with plotly.express as it gives me
# more in depth analysis and control over the properties of the graph.

import plotly.graph_objects as go
import plotly.express as px

# Create a Plotly figure
fig = go.Figure()

# Add a scatter trace
fig.add_trace(
    go.Scatter(
        x=grouped_df.index,  # Adding 1 to start index from 1 instead of 0
        y=grouped_df['bottles_sold'],
        mode='markers',
        marker=dict(
            size=grouped_df['bottles_sold'],
            sizemode='area',
            sizeref=2.0 * max(grouped_df['bottles_sold'])/(50.**2),  # Adjust marker size
            color=grouped_df.index,  # Color based on index value
            colorscale='Viridis',  # Choose a colorscale
            colorbar=dict(
                title='Index',
                tickvals=df.index[0:61:10]),# Add a colorbar
            showscale=True,  # Show the colorscale
        ),
        text=grouped_df.apply(lambda row: f"bottles_sold: {row['bottles_sold']}<br>"
                                  f"zip_code: {row['zip_code']}<br>"
                                  f"item_number: {row['item_number']}",
                        axis=1),  # Hovertext,
        hoverinfo='text',
    )
)

# Customize layout
fig.update_layout(
    title='Most Popular Items',
    title_x=0.5,
    xaxis_title='Zipcode',
    yaxis_title='Bottles Sold',
    width=800,
    height=600
)

# Show the figure
fig.show()



