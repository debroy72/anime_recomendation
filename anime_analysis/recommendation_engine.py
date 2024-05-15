# recommendation_engine.py

import pandas as pd

def load_data():
    try:
        data = pd.read_csv('animes.csv')  # Ensure the correct file name
    except FileNotFoundError:
        print("Error: The dataset file was not found.")
        exit()

    # Assuming the dataset has these columns, adjust if necessary
    expected_columns = ['uid', 'title', 'genre', 'synopsis']
    missing_columns = [col for col in expected_columns if col not in data.columns]
    if missing_columns:
        print(f"Error: The dataset is missing the following columns: {missing_columns}")
        exit()

    # Separate the data into ratings and anime metadata
    anime = data[['uid', 'title', 'genre', 'synopsis']].drop_duplicates().reset_index(drop=True)

    # If 'rating' column exists in your dataset, use it; otherwise, we can use a dummy 'ratings' DataFrame
    if 'rating' in data.columns:
        ratings = data[['uid', 'rating']]
    else:
        # If 'rating' is not available, we can simulate it for demonstration purposes
        data['rating'] = data.get('score', pd.Series([8.0] * len(data)))  # Assuming 'score' is available
        ratings = data[['uid', 'rating']]

    return anime, ratings

def recommend_for_new_user(preferred_genres, num_recommendations=5):
    anime, ratings = load_data()
    
    # Filter anime based on preferred genres
    filtered_anime = anime[anime['genre'].str.contains('|'.join(preferred_genres), case=False, na=False)]
    
    # Calculate popularity (average rating or number of ratings)
    anime_ratings = ratings.groupby('uid').agg({'rating': ['mean', 'count']}).reset_index()
    anime_ratings.columns = ['uid', 'mean_rating', 'rating_count']
    
    # Merge with filtered anime to get popularity metrics
    filtered_anime = pd.merge(filtered_anime, anime_ratings, on='uid')
    
    # Rank anime by mean rating and rating count
    filtered_anime = filtered_anime.sort_values(by=['mean_rating', 'rating_count'], ascending=False)
    
    # Return top recommendations
    return filtered_anime.head(num_recommendations).to_dict('records')
