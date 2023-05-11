# %%

import pandas as pd
import plotly.express as px

def read_my_csv():
    df = pd.read_csv(r"..\data\ekg_data\01_Ruhe.txt", sep="\t", header=None)

    df.columns = ["Messwerte in mV","Zeit in ms"]
    return df


# %%

def make_plot(df):

    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

#%% Test

#df = read_my_csv()
#fig = make_plot(df)

#fig.show()

# %%
