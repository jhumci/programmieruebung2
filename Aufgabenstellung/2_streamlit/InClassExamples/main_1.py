import streamlit as st

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
current_user = st.selectbox(
    'Versuchsperson',
    options = ["Nutzer1", "Nutzer2"], key="sbVersuchsperson")



