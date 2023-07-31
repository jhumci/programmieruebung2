import pandas as pd
import matplotlib.pyplot as plt


# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen
## Als Attribut Pandas Dataframe df_ekg speichern
    def __init__(self, path):

        # definiere Überschriften
        column_names = ["Amplitude in [mV]" ,"Time in [ms]"]
        self.df_ekg = pd.read_csv(path, sep="\t", header=0, names= column_names)

    def find_peaks(self):        
        # erstelle eine liste mit den Daten
        np_array = self.df_ekg["Amplitude in [mV]"].values

        # Liste peaks, die den index der peaks speichern
        peaks = []

        # erstellt einen laufindex vom 1. bis zum
        # vor-letzten element der liste
        for index in range(1,len(np_array)-1):
            #print("index ist:", index)
            #print("wert ist:", np_array[index])
            vorgaenger = np_array[index-1]
            nachfolger = np_array[index+1]
            kandidat = np_array[index]

            #  vergleiche die drei Werte
            # wenn Kadidat höher als beide anderen

            if kandidat > nachfolger and kandidat >vorgaenger:
                # dann füge es einer liste hinzu
                peaks.append(index)
        # Erstelle Dataframe

        self.df_peaks = pd.DataFrame(peaks, columns=["Indizes"])

    def estimate_hr(self):
        # Zuerst gibt es keine HR
        self.heat_rate = None
        # Nach Blick in die Daten: nur jeder zweite Peak ist eine R-Zacke
        number_r_zacken = self.df_peaks.size / 2
        # Daten sind mit f=1000 Hz aufgezeichnet worden. 1 Beobachtung ist 1 ms
        dauer_singal_in_min = self.df_ekg.size / 1000 / 60

        self.heat_rate  = number_r_zacken / dauer_singal_in_min


    # Erstellen eines Plots
    def plot_time_series(self):
        # Same like above, but now with subplots() 
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.df_ekg["Time in [ms]"], self.df_ekg["Amplitude in [mV]"])
        self.ax.set_xlabel("Zeit in ms")
        self.ax.set_ylabel("Spannung in mV")

    def find_absolutes(self):
        self.df_peaks["Höhe in mV"] = self.df_ekg.iloc[self.df_peaks["Indizes"].values]["Amplitude in [mV]"].values
        self.df_peaks["Time in ms"] = self.df_ekg.iloc[self.df_peaks["Indizes"].values]["Time in [ms]"].values

    def calc_distance(self):
        self.df_peaks["Abstand Vorgänger in ms"] =  self.df_peaks["Time in ms"].diff(1)
        self.df_peaks["Abstand Nachfolger in ms"] =  self.df_peaks["Time in ms"].diff(-1)

    def find_dominaz(self):
        dominanzs = [0]
        for idx in range(self.df_peaks.index.min()+1,self.df_peaks.index.max()):
            #print(idx)
            index_des_peaks = int(self.df_peaks.iloc[idx]["Indizes"])
            index_des_vorangegangenen_peaks = int(self.df_peaks.iloc[idx-1]["Indizes"])
            #print(index_des_vorangegangenen_peaks)
            index_des_nachfolgenden_peaks = int(self.df_peaks.iloc[idx+1]["Indizes"])
            #print(index_des_nachfolgenden_peaks)

            lokales_min_vor = self.df_ekg.iloc[index_des_vorangegangenen_peaks:index_des_peaks].min()
            lokales_min_nach = self.df_ekg.iloc[index_des_peaks:index_des_nachfolgenden_peaks].min()
            
            lokales_min_amplitude = (lokales_min_nach["Amplitude in [mV]"] + lokales_min_vor["Amplitude in [mV]"])/2
            dominanz = self.df_peaks.iloc[idx]["Höhe in mV"] - lokales_min_amplitude
            dominanzs.append(dominanz)

        dominanzs.append(dominanz)
        dominanzs[0] = dominanzs[1]

        self.df_peaks["Dominanz in mV"] = dominanzs

    def resample(self,time):
        pass
#%%
"""
my_peakfinder = EKGdata(r"data\ekg_data\01_Ruhe_short.txt")
my_peakfinder.df_ekg
my_peakfinder.plot_time_series()
my_peakfinder.fig
my_peakfinder.find_peaks()
my_peakfinder.df_peaks
my_peakfinder.estimate_hr()
my_peakfinder.heat_rate
my_peakfinder.find_absolutes()
my_peakfinder.calc_distance()
my_peakfinder.find_dominaz()
my_peakfinder.df_peaks

#%%
my_peakfinder.df_peaks["Abstand Vorgänger in ms"].hist()
#%%

#my_peakfinder.df_peaks.boxplot(column = "Höhe in mV")
my_peakfinder.df_peaks["Höhe in mV"].hist()
#%%
my_peakfinder.df_peaks.boxplot(column = "Dominanz in mV")


# %%

my_peakfinder.df_peaks[""]
#%%


my_peakfinder.df_peaks["Höhe in mV"]
# %%
"""