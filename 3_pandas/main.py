import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot


# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik

st.write("# My Plot")

df = read_my_csv()
fig = make_plot(df)

st.plotly_chart(fig)