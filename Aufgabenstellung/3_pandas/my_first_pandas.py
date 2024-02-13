# %% https://github.com/jhumci/BLT_BDS/blob/main/1_Visualisierung_und_Datenbanken.ipynb
import pandas as pd

#%%

pd.read_csv("..\data\ekg_data\01_Ruhe.txt")
# %%

pd.read_csv(r"..\data\ekg_data\01_Ruhe.txt")
# %%

df = pd.read_csv(r"..\data\ekg_data\01_Ruhe.txt", sep="\t", header=None)


# %%

df.columns = ["Messwerte in mV","Zeit in ms"]

df
# %%

sample_df = df.head(2000)

# %%
sample_df.plot()
# %%

sample_df.plot(x= "Zeit in ms", y="Messwerte in mV")
# %%

sample_df.mean()

# %%

sample_df.min()


# %%

sample_df.max()


# %%

sample_df.describe()

# %%

# %%
import plotly.express as px


fig = px.line(sample_df, x= "Zeit in ms", y="Messwerte in mV")
fig.show()

#%%


import seaborn as sns

sns.lineplot(x= "Zeit in ms", y="Messwerte in mV",data = sample_df)

# %%

sample_df.where(sample_df["Zeit in ms"] >16000)

# %%


sample_df[sample_df["Zeit in ms"] >16000]
# %%

sample_df["Name"] = "Julian"
# %%

for index, observation in sample_df.iterrows():
    print(observation)
    break


# %%


for index, observation in sample_df.iterrows():
    print(observation["Messwerte in mV"])
    if observation["Messwerte in mV"] > 300:
        print(index)

# %%

high_values = []

for index, observation in sample_df.iterrows():
    print(observation["Messwerte in mV"])
    if observation["Messwerte in mV"] > 300:
        print(index)
        high_values.append(index)

# %%
