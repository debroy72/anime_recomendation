import pandas as pd
import matplotlib.pyplot as plt

# Load the anime dataset
anime_data = pd.read_csv('animes.csv')

# Split the genres string into lists
anime_data['genre'] = anime_data['genre'].str.split(', ')

# Initialize an empty DataFrame for genre data
genre_data = pd.DataFrame(columns=['Genre', 'Popularity', 'Score'])

# Iterate through each row of the dataset
for index, row in anime_data.iterrows():
    genres = row['genre']
    popularity = row['popularity']
    score = row['score']
    
    # Iterate through each genre of the current anime
    for genre in genres:
        genre_data = pd.concat([genre_data, pd.DataFrame({'Genre': [genre], 'Popularity': [popularity], 'Score': [score]})])

# Calculate the average popularity and score for each genre
genre_avg_data = genre_data.groupby('Genre').mean().reset_index()

# Clean up genre names
genre_avg_data['Genre'] = genre_avg_data['Genre'].str.strip(" '[]")

# Divide genres into four groups based on their initial letter
groups = {
    'A-D': ['Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons', 'Drama', 'Ecchi', 'Fantasy'],
    'E-H': ['Game', 'Harem', 'Hentai', 'Historical', 'Horror'],
    'I-M': ['Josei', 'Kids', 'Magic', 'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery'],
    'N-Z': ['Parody', 'Police', 'Psychological', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai', 'Slice of Life', 'Space', 'Sports', 'Super Power', 'Supernatural', 'Thriller', 'Vampire']
}

# Create subplots for each group
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot each group separately
for ax, (group_name, genres) in zip(axes.flatten(), groups.items()):
    # Filter genre data based on group's genres
    group_data = genre_avg_data[genre_avg_data['Genre'].isin(genres)]
    
    # Plot only if there's data for the group
    if not group_data.empty:
        ax.barh(group_data['Genre'], group_data['Popularity'], color='skyblue', label='Average Popularity')
        ax.barh(group_data['Genre'], group_data['Score'], color='salmon', label='Average Score')
        ax.set_xlabel('Popularity / Score')
        ax.set_ylabel('Genre')
        ax.set_title(f'Genre Analysis: {group_name}')
        ax.legend()

plt.tight_layout()
plt.show()
