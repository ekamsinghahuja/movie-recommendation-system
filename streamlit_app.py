import streamlit as st
import pickle
import requests
import pandas
import numpy 

new = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('sim.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    li=[]
    recommended_movie_posters = []
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        li.append(new.iloc[i[0]].title)
        movie_id = new.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return li,recommended_movie_posters
movies_list = new['title'].values
        
st.title('Movie Dekho')

option = st.selectbox('Movie u Like',movies_list)


if st.button('Recommend'):
    li,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(li[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(li[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(li[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(li[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(li[4])
        st.image(recommended_movie_posters[4])