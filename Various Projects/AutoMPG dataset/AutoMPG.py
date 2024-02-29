# In the automotive dataset, which contains information about various
# car models, we will perform basic exploratory data analysis create a plot
# of weight vs mpg.

        # importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

        # load the dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df = pd.read_csv(url, names=column_names, delim_whitespace=True)  # the CSV file values are separated by spaces

        # find any inconsistencies or missing data

print(df.isna().sum())
print(df.dtypes)


        # clean the dataset

df['horsepower'].replace('?', np.nan, inplace=True)     #replace any '?' with NaN values
df['horsepower'] = df['horsepower'].astype(float)
df.dropna(inplace=True)     # removes any NaN values

        # perform basic statistics and print the details

print(df.describe())


        # we can also print the correlation matrix of the DataFrame if we
        # want to see how each column is related to every other column


correlation_matrix = df.drop('car_name', axis=1).corr()
print(correlation_matrix)


            # Visualize with Scatter Plot the weight vs mpg

plt.scatter(df["weight"], df["mpg"])
plt.xlabel('Weight')
plt.ylabel('Miles Per Gallon')
plt.title('Weight vs. MPG')
plt.show()

            # Alternatively, for a more aesthetically pleasing graph


import plotly.graph_objects as go

# Create a Plotly figure
fig = go.Figure()

# Add a scatter trace
fig.add_trace(
    go.Scatter(
        x=df["weight"],
        y=df["mpg"],
        mode='markers',
        marker=dict(
            size=df["mpg"],
            sizemode="area",
            sizeref=2.0 * max(df["mpg"])/(20.**2),  # Adjust marker size
            color=df["weight"],
            colorbar=dict(
                title='Weight Values'
            ),
        ),
        text=df.apply(lambda row: f"weight: {row['weight']}<br>"
                                  f"mpg: {row['mpg']}<br>",
                        axis=1),  # Hovertext
        hoverinfo='text',
    )
)

# Customize layout
fig.update_layout(
    title='Weight Vs MPG',
    title_x=0.5,
    xaxis_title='Weight (lb)',
    yaxis_title='Miles Per Gallon',
    width=800,
    height=600,
    xaxis=dict(
        title=dict(
            text='Weight (lb)',
            font=dict(size=18)  # Adjust x axis font size
        )
    ),
    yaxis=dict(
        title=dict(
            text='Miles Per Gallon',
            font=dict(size=18)  # Adjust x axis font size
        )
    )
)

