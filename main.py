import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load CSV
df = pd.read_csv('USvideos.csv')
print("Data shape:", df.shape)
print(df.head())
print(df.describe())
print("Unique categories:", df['category_id'].nunique())

# Top 10 video categories by views
top_categories = df.groupby('category_id')['views'].sum().sort_values(ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
top_categories.plot(kind='bar')
plt.title("Top 10 Video Categories by Views")
plt.xlabel("Category ID")
plt.ylabel("Total Views")
plt.tight_layout()
plt.show()

# WordCloud for trending video titles
text = " ".join(title for title in df['title'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Trending Keywords in YouTube Titles")
plt.show()
