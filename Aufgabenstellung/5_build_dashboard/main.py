import streamlit as st
import read_person_data
import ekgdata
import matplotlib.pyplot as plt
from PIL import Image
from person import Person, get_person_data, get_person_object_by_full_name

#%% Zu Beginn

# Lade alle Personen als Objekt


# Anlegen diverser Session States
if "person_list" not in st.session_state:
    st.session_state.person_list = get_person_data()

# Selectbox Namen
if "selected_person" not in st.session_state:
    st.session_state.selected_person = "NONE"

# NEU: hier will ich die Person als Objekt haben, die gerade angezeigt wird
if "selected_person_object" not in st.session_state:
    st.session_state.selected_person_object = None


#%% Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sindst.session_state.selected_person  = st.selectbox("Wähle eine Versuchsperson", options=[person.get_full_name() for person in st.session_state.person_list])
st.session_state.selected_person  = st.selectbox("Wähle eine Versuchsperson", options=[person.get_full_name() for person in st.session_state.person_list])


st.session_state.selected_person_object = get_person_object_by_full_name(st.session_state.selected_person)

# Anzeigen eines Bilds mit Caption
st.image(st.session_state.selected_person_object.get_image(), caption=st.session_state.selected_person_object.get_full_name())


# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist


#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Per-son
current_egk_data = ekgdata.EKGdata(st.session_state.selected_person_object.ekg_tests[0])

#%% EKG-Daten als Matplotlib Plot anzeigen
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes
current_egk_data.plot_time_series()
# Zeige den Plot an
st.plotly_chart(current_egk_data.fig)

# %% Herzrate bestimmen
# Schätze die Herzrate 
#current_egk_data.estimate_hr()
# Zeige die Herzrate an
#st.write("Herzrate ist: ", int(current_egk_data.heat_rate)) 
