# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:30:39 2023

@author: - aa23aan
"""

import matplotlib.pyplot as plt
import pandas as pd

#Function defenition
def plot_goals_comparison(data, year, top_n=10):
    # Filter data for the specified year
    df_year = data[data['Year'] == year]

    # Select the top goal scorers based on the "Goals" column
    top_scorers = df_year.nlargest(top_n, 'Goals')

    # Select relevant columns for the bar chart
    top_scorers_subset = top_scorers[['Player Names', 'Shots', 'OnTarget']]

    # Plotting the stacked bar chart
    plt.figure(figsize=(12, 8))

    # Plot Shots
    plt.bar(top_scorers_subset['Player Names'], top_scorers_subset['Shots'],
            label='Shots', color='Brown')

    # Plot On Target on top of Shots
    plt.bar(top_scorers_subset['Player Names'], top_scorers_subset['OnTarget'], 
            bottom=top_scorers_subset['Shots'],
            label='On Target', color='lightcoral')

    # Adding labels and title
    plt.xlabel('Player Names')
    plt.ylabel('Count')
    plt.title('Comparison of Shots and On Target '
              'for Top 10 Goal Scorers 2016')
    plt.xticks(rotation=90)

    # Adding legend
    plt.legend()

    # Display the plot
    plt.show()


# Read CSV file
df = pd.read_csv('League_score.csv')
# Specifying the year and calling the function
plot_goals_comparison(df, year=2016)


