#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
from scipy.signal import find_peaks, butter, filtfilt
import matplotlib.pyplot as plt


# In[18]:


# 1. Read the ECG Data
df = pd.read_csv('ECG1.csv')
ecg_signal = df['Shimmer_89F4_ECG_LA_RA_24BIT_LPF_CAL'].values 


# In[19]:


# 2. Preprocess the Data
# Bandpass filter parameters
lowcut = 0.5
highcut = 50.0
fs = 250.0  # Sample rate, replace with actual value
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
# Butterworth filter
b, a = butter(1, [low, high], btype='band')
filtered_signal = filtfilt(b, a, ecg_signal)


# In[20]:


# 3. Derivative Filter to highlight QRS complex
# Implement derivative filter

diff_signal = np.diff(filtered_signal, n=1)


# In[21]:


# 4. Squaring
squared_signal = np.square(filtered_signal)


# In[22]:


# 5. Moving Window Integration

# Simple moving window integration
window_size = int(0.150 * fs)  # 150 ms window size, adjust based on your sampling rate (fs)
integrated_signal = np.convolve(squared_signal, np.ones(window_size)/window_size, mode='same')


# In[23]:


# 6. Thresholding and Decision Rule
# Implement adaptive thresholding
# Find peaks in the integrated signal
peaks, _ = find_peaks(integrated_signal, height=0.6*np.max(integrated_signal))  # Example threshold

# Adaptive thresholding could be implemented here, adjusting the threshold based on signal and noise levels


# In[24]:


# 7. Post-processing
# Refine QRS detection
# Simple post-processing to remove closely spaced peaks
min_distance = int(0.200 * fs)  # Minimum distance between QRS complexes, e.g., 200 ms
final_peaks = [peaks[0]]  # Initialize with the first peak
for peak in peaks[1:]:
    if peak - final_peaks[-1] > min_distance:
        final_peaks.append(peak)


# In[25]:


# Visualization of results
plt.figure(figsize=(10, 6))
plt.plot(ecg_signal, label='Filtered ECG Signal')
plt.plot(final_peaks, ecg_signal[final_peaks], 'ro', label='Detected QRS Peaks')
plt.title('QRS Detection')
plt.legend()
plt.show()


# In[ ]:




