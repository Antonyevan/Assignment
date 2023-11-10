# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:20:01 2023

@author: SNEHA MARTIN
"""
import pandas as pd
import matplotlib.pyplot as plt

#Function Defenition
def plot_pie_chart(data, labels, title):
    # Plotting the pie chart
    plt.figure(figsize=(6, 6))

    # Pie chart
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=['lightblue', 'lightgreen', 'lightcoral'])

    plt.title(title)

    # Display the plot
    plt.show()
    

# Read Data from csv file
covid_data = pd.read_csv("data.csv", index_col=0)

# Select data for India and USA
india_data = covid_data.loc['India']
usa_data = covid_data.loc['USA']

# Call the function for India
plot_pie_chart(india_data, labels=india_data.index, title='Covid Data India - 23 AUG 2020')

# Call the function for the USA
plot_pie_chart(usa_data, labels=usa_data.index, title='Covid Data USA - 23 AUG 2020')




