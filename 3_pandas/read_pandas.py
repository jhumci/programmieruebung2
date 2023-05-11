# %%

import pandas as pd

def read_csv():
    df = pd.read_csv(r"..\data\ekg_data\01_Ruhe.txt", sep="\t", header=None)
    # %%
    df.columns = ["Messwerte in mV","Zeit in ms"]
    return df

