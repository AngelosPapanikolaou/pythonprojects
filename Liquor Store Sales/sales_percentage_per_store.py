# We are tasked to compute the sales percentage we have to group
# by store_name and sale_dollars and sum the sale_dollars for each store,
# then we simply divide by the total sales * 100

import pandas as pd
import numpy as np


grouped_df = ((filtered_df.groupby('store_name')['sale_dollars'].sum() / filtered_df['sale_dollars'].sum()) * 100).reset_index()
grouped_df['sale_dollars'] = grouped_df['sale_dollars'].round(2)
print(grouped_df)



# Get the top 15 stores. It's optional, for better visualization purposes.

sorted_df = grouped_df.sort_values('sale_dollars', ascending=False).head(15)
print(sorted_df)

# Sort back to ascending for the graph

final_df = sorted_df.sort_values('sale_dollars', ascending = True)
print(final_df)



# Visualize using a bar graph

import plotly.graph_objects as go
import plotly.express as px

fig = px.bar(final_df, x='sale_dollars', y='store_name',
             color='sale_dollars',
             orientation='h',
             text = 'sale_dollars',
             hover_data={'store_name': True, 'sale_dollars': True},
             labels={'sales_percentage': '% Sales'})

# Customize layout and traces
fig.update_traces(textposition = 'outside')

fig.update_layout(title='Top Stores by Sales',
                  title_x=0.55,
                  xaxis_title='% Sales',
                  yaxis_title='Store Name',
                  height=600,
                  width=1300)

# Show the plot
fig.show()














