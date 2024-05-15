import pandas as pd

# Load the dataset into a pandas DataFrame
anime_data = pd.read_csv('animes.csv')

# Explore the structure of the dataset
print("Dataset Information:")
print(anime_data.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(anime_data.head())

# Check for missing values
print("\nMissing Values:")
print(anime_data.isnull().sum())

# Summary statistics for numeric columns
print("\nSummary Statistics for Numeric Columns:")
print(anime_data.describe())

# Unique values in categorical columns
print("\nUnique Values in Categorical Columns:")
print("Genre:", anime_data['genre'].unique())
# Repeat for other categorical columns as needed

# Explore specific features
print("\nExplore Specific Features:")
print("Sample Synopsis:")
for i, synopsis in enumerate(anime_data['synopsis'].sample(5)):
    print(f"Synopsis {i+1}: {synopsis}")
# Repeat for other features of interest
