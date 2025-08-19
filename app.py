import streamlit as st 
import pickle 
import pandas as pd
import requests


def fetch_poster(movie_id): 
    response = requests.get(
    'https://api.themoviedb.org/3/movie/{}?api_key=9f51560555a6780d1168b61401879469'.format(movie_id)
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
                            
                            




def recommend(movie): 
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list: 
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch Poster from API 
        recommended_movies_posters.append(fetch_poster(movie_id ))
        
    return recommended_movies,recommended_movies_posters




with open("movie_list.pkl", "rb") as file:
    movies_list  = pickle.load(file)
    
with open("similarity.pkl", "rb") as file1:
    similarity  = pickle.load(file1)
    
movies = pd.DataFrame(movies_list)

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('How would you like to be contacted?', movies['title'].values)

if st.button('Recommend'): 
    names, posters = recommend(selected_movie_name)
    
    # Display Posters 
    
    col1, col2, col3, col4, col5 = st.columns(5)
     
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
        
        
    col6, col7, col8, col9, col10 = st.columns(5)
     
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
    