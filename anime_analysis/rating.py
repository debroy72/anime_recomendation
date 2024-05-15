import pandas as pd
import matplotlib.pyplot as plt

# Load the anime dataset
anime_data = pd.read_csv('animes.csv')

# Visualize the distribution of ratings (scores)
plt.figure(figsize=(10, 6))
plt.hist(anime_data['score'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Distribution of Ratings (Scores)')
plt.grid(True)
plt.show()

# Explore the relationship between ratings and number of episodes using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(anime_data['episodes'], anime_data['score'], color='salmon', alpha=0.5)
plt.xlabel('Number of Episodes')
plt.ylabel('Score')
plt.title('Relationship between Ratings and Number of Episodes')
plt.grid(True)
plt.show()

# Group similar genres into broader categories
anime_data['genre_category'] = anime_data['genre'].apply(lambda x: 'Action' if 'Action' in x else
                                                         'Comedy' if 'Comedy' in x else
                                                         'Drama' if 'Drama' in x else
                                                         'Fantasy' if 'Fantasy' in x else
                                                         'Other')

# Plot the relationship between ratings and genre category using a box plot
plt.figure(figsize=(12, 8))
anime_data.boxplot(column='score', by='genre_category', vert=False, figsize=(12, 8))
plt.xlabel('Score')
plt.ylabel('Genre Category')
plt.title('Relationship between Ratings and Genre Category')
plt.grid(True)
plt.show()
