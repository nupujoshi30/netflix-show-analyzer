# %% Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# %% Load the dataset
df = pd.read_csv("C:\\Users\\Dell\\Downloads\\LINKEDLN\\Netflix Show Analyzer\\netflix_titles.csv")

# %% Initial Inspection
# View shape and columns
print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)

# Check basic info
print("\nData Types:\n", df.dtypes)

# See first few rows
print("\nFirst few rows:\n", df.head())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# %% Clean 'date_added' column
# Strip spaces and convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='mixed', errors='coerce')

# Create new columns for year and month
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

print("\nValid dates:", df['date_added'].notnull().sum())
print("Invalid or missing dates:", df['date_added'].isnull().sum())

# %% Remove Duplicates
df.drop_duplicates(inplace=True)
print("\nShape after removing duplicates:", df.shape)


#movies vs TV shows count
import seaborn as sns
import matplotlib.pyplot as plt

# %% Plot: Movie vs TV Show Count
# Count of content type
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='pastel')
plt.title("Distribution of Content Type on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# %% Plot: Netflix Content Added Over the Years

# Remove rows with missing year
year_counts = df['year_added'].dropna().value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o', color='coral')
plt.title("Netflix Content Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.tight_layout()
plt.show()

# %% Plot: Top 10 Countries with Most Netflix Titles

# Drop missing countries
top_countries = df['country'].dropna().value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
plt.title("Top 10 Countries with Most Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

# Save the plot (fix path!)
plt.savefig(r"C:\Users\Dell\Downloads\LINKEDLN\Netflix Show Analyzer\output\top_countries_netflix.png")
plt.show()

# %% Plot: Top 10 Genres on Netflix

from collections import Counter

# Step 1: Flatten all genres into a list
all_genres = []
for genre_list in df['listed_in'].dropna():
    all_genres.extend([genre.strip() for genre in genre_list.split(',')])

# Step 2: Count the top 10 genres
genre_counts = Counter(all_genres).most_common(10)
genres, counts = zip(*genre_counts)

# Step 3: Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=list(counts), y=list(genres), palette='magma')
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()

# Save the plot
plt.savefig("C:/Users/Dell/Downloads/LINKEDLN/Netflix Show Analyzer/output/top_netflix_genres.png")
plt.show()
