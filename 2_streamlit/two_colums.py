import streamlit as st
import read_data
from PIL import Image


with st.container():
    st.write("# EKG APP")

left_column, right_column = st.columns(2)


with left_column:

    person_names = read_data.get_person_list(read_data.load_person_data())

    st.write("## Versuchsperson auswählen")

    # Session State also supports the attribute based syntax
    if 'current_user' not in st.session_state:
        st.session_state.current_user = 'None'

    # Anlegen des Session State. Bild, wenn es kein Bild gibt
    if 'picture_path' not in st.session_state:
        st.session_state.picture_path = '../data/pictures/none.jpg'



    st.session_state.current_user = st.selectbox(
        'Versuchsperson',
        options = person_names, key="sbVersuchsperson")

    st.write("Der Name ist: ", st.session_state.current_user) 

    if st.session_state.current_user in person_names:
        st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]


    st.write("Der Pfad ist: ", st.session_state.picture_path) 


# Or even better, call Streamlit functions inside a "with" block:
with right_column:


    image = Image.open("../" + st.session_state.picture_path)
    st.image(image, caption=st.session_state.current_user)
