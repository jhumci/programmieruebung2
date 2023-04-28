#%%

message = "Hello!"

print(message)

#%%

message = message +  " World!"

print(message)
# %%
import my_first_module

print(my_first_module.answer_of_everything())
# %%

result = 1	

for x in [1, 4, 5, 7, 0, 8]:
    result = result / x
    print(x)
# %%

import numpy as np

np.random.rand()
# %%

import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Simulate 10 seconds of ECG Signal (recorded at 250 samples / second)
ecg_signal = nk.ecg_simulate(duration=10, sampling_rate=250)

# Automatically process the (raw) ECG signal
signals, info = nk.ecg_process(ecg_signal, sampling_rate=250)

# Plot the signal
signals["ECG_Raw"].plot()
# %%
