import streamlit as st

if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

person_names = ["User1", "User2"]

def callback_function():
    # Logging Message
    print(f"The user has changed to {st.session_state.current_user}")
    # Manuelles wieder ausführen
    #st.rerun()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson", on_change = callback_function)

