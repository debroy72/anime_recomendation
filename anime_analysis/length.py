import pandas as pd
import matplotlib.pyplot as plt

# Load the anime dataset
anime_data = pd.read_csv('animes.csv')

# Data Preparation
# Drop rows with missing values in the 'episodes', 'popularity', and 'score' columns
anime_data.dropna(subset=['episodes', 'popularity', 'score'], inplace=True)

# Season Length Calculation
# For simplicity, assume each entry in the dataset represents a single season
# The number of episodes is considered as the length of the season

# Analysis
# Scatter plot of season length vs. popularity
plt.figure(figsize=(10, 6))
plt.scatter(anime_data['episodes'], anime_data['popularity'], color='skyblue', alpha=0.5)
plt.xlabel('Number of Episodes in Season')
plt.ylabel('Popularity')
plt.title('Season Length vs. Popularity')
plt.grid(True)
plt.show()

# Scatter plot of season length vs. score
plt.figure(figsize=(10, 6))
plt.scatter(anime_data['episodes'], anime_data['score'], color='salmon', alpha=0.5)
plt.xlabel('Number of Episodes in Season')
plt.ylabel('Score')
plt.title('Season Length vs. Score')
plt.grid(True)
plt.show()
