import pickle
import streamlit as st
import streamlit.components.v1 as stc
import requests
from PIL import Image

def recommend(original_title):
    index = new_df[new_df['original_title'] == original_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    recommended_book_posters = []
    recommended_book_authors = []
    recommended_book_ratings = []
    for i in distances[1:7]:
        books_id = new_df.iloc[i[0]].image_url
        recommended_book_posters.append(books_id)
        recommended_book_names.append(new_df.iloc[i[0]].original_title)
        recommended_book_authors.append(new_df.iloc[i[0]].authors)
        recommended_book_ratings.append(new_df.iloc[i[0]].average_rating)

    return recommended_book_names,recommended_book_posters,recommended_book_authors,recommended_book_ratings

# Mengubah background image
st.markdown(
    """
    <style>
          /* Gambar background untuk perangkat seluler */
        @media (max-width: 767px) {
            .stApp {
                background-image: url("https://i.imgur.com/Ay46iln.png");
                background-size: 100% 100%;
                background-repeat: no-repeat;
            }
        }

        /* Gambar background untuk desktop */
        @media (min-width: 768px) {
            .stApp {
                background-image: url("https://i.imgur.com/MIQKt3H.png");
                background-size: 100% 100%;
                background-repeat: no-repeat;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

title = Image.open('bgbooktitle.png')
st.image(title)
st.subheader('  ')

new_df = pickle.load(open('book_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

book_list = new_df['original_title'].values
selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    book_list
)

if st.button('Show Recommendation'):
    recommended_book_names,recommended_book_posters,recommended_book_authors,recommended_book_ratings = recommend(selected_book)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader(recommended_book_names[0])
        st.text(recommended_book_authors[0])
        st.caption(':star2: '+(recommended_book_ratings[0]))
        st.image(recommended_book_posters[0])
    with col1:
        st.subheader(recommended_book_names[1])
        st.text(recommended_book_authors[1])
        st.caption(':star2: '+(recommended_book_ratings[1]))
        st.image(recommended_book_posters[1])

    with col2:
        st.subheader(recommended_book_names[2])
        st.text(recommended_book_authors[2])
        st.caption(':star2: '+(recommended_book_ratings[2]))
        st.image(recommended_book_posters[2])
    with col2:
        st.subheader(recommended_book_names[3])
        st.text(recommended_book_authors[3])
        st.caption(':star2: '+(recommended_book_ratings[3]))
        st.image(recommended_book_posters[3])
        
    with col3:
        st.subheader(recommended_book_names[4])
        st.text(recommended_book_authors[4])
        st.caption(':star2: '+(recommended_book_ratings[4]))
        st.image(recommended_book_posters[4])
    with col3:
        st.subheader(recommended_book_names[5])
        st.text(recommended_book_authors[5])
        st.caption(':star2: '+(recommended_book_ratings[5]))
        st.image(recommended_book_posters[5])
