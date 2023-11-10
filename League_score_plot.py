# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:45:22 2023

@author: - aa23aan
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

#Function Defenition
def League_score(data):
        #select years 
        data['Year'] = data['Year'].astype(int)
        
        # Creation of playerdata
        player1 = data[data['Player Names'] == 'Lionel Messi']
        player2 = data[data['Player Names'] == 'Cristiano Ronaldo']
        
        #selecting goals scored by corresponding players
        year = data['Year'].unique()
        year = year.astype(int)
        player1_goals = player1[player1['Year'].isin(year)][['Year','Goals']]
        player2_goals = player2[player2['Year'].isin(year)][['Year','Goals']]
        
        #Plotting
        plt.figure(figsize=(10,6))
        plt.plot(player1_goals['Year'],player1_goals['Goals'], 
                 label = "Lionel Messi", color = 'darkblue')
        plt.plot(player2_goals['Year'],player2_goals['Goals'], 
                 label = "Cristiano Ronaldo", color = 'red')
        
        #Giving title and labels
        plt.title('Messi - Ronaldo Goal Scoring Comaprison (2016 - 2020)')
        plt.xlabel('Year')
        plt.ylabel('Goals')
        plt.xticks(np.arange(min(year)-1,max(year))+1)
        plt.legend()
        
        plt.show()

#Read CSV file        
data = pd.read_csv('League_score.csv')
League_score(data)

