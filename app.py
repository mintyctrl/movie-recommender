import pandas as pd
import streamlit as st

# Load the dataset
movies_df = pd.read_csv('movies.csv')

# Define the recommendation function
def get_recommendations(genre_choice, mood_keywords=[]):
    # Filter movies by genre
    genre_filtered = movies_df[movies_df['genres'].str.contains(genre_choice, case=False, na=False)]

    # Further filter by mood keywords
    if mood_keywords:
        genre_filtered = genre_filtered[genre_filtered['title'].apply(lambda title: any(keyword in title.lower() for keyword in mood_keywords))]

    # Return the top 10 results
    return genre_filtered[['title', 'genres']].head(10)

# Streamlit app interface
st.title("Movie Recommendation Tool")
st.write("Get movie recommendations based on genre and mood keywords!")

# Genre selection
genre_choice = st.selectbox("Choose a genre:", movies_df['genres'].unique())

# Mood keywords input
mood_keywords_input = st.text_input("Enter mood keywords separated by commas (e.g., happy, thrilling):")
mood_keywords = [kw.strip().lower() for kw in mood_keywords_input.split(",") if kw.strip()]

# Button to get recommendations
if st.button("Get Recommendations"):
    recommendations = get_recommendations(genre_choice, mood_keywords)
    st.write("Top Recommendations:")
    st.write(recommendations)
