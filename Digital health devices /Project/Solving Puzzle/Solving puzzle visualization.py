import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV files
data1 = pd.read_csv('GSR1.csv')  # Make sure the filename is correct (assuming 'GSR.csv' without the extra space)
data2 = pd.read_csv('ECG1.csv')
data3 = pd.read_csv('GSR2.csv')
data4 = pd.read_csv('ECG2.csv')

# Adjusting figsize
plt.figure(figsize=(15, 8))

# Adjusting the space between plots
plt.subplots_adjust(hspace=0.6)

# Plotting the GSR DATA for participant 1
plt.subplot(4, 1, 1)
plt.plot(data1['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'], label='Skin_Conductance', color='yellow', alpha=0.7)
plt.plot(data1['Shimmer_86BB_PPGtoHR_LPF_CAL'], label='PPGtoHR', color='green', alpha=0.7)
plt.plot(data1['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'], label='Skin_Resistance', color='orange', alpha=0.7)
plt.plot(data1['Shimmer_86BB_PPG_IBI_LPF_CAL'], label='PPG_IBI', color='brown', alpha=0.7)
plt.title('Participant 1 GSR')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('GSR Readings')

# Plotting the ECG DATA for participant 1
plt.subplot(4, 1, 2)
plt.plot(data2['Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL'], label='ECGtoHR_LA_RA', color='brown', alpha=0.7)
plt.plot(data2['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'], label='ECGtoHR_LL_LA', color='orange', alpha=0.7)
plt.plot(data2['Shimmer_89F4_ECGtoHR_LL_RA_LPF_CAL'], label='ECGtoHR_LL_RA', color='green', alpha=0.7)
plt.plot(data2['Shimmer_89F4_ECGtoHR_Vx_RL_LPF_CAL'], label='ECGtoHR_Vx_RL', color='yellow', alpha=0.7)


plt.title('Participant 1 ECG')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('ECG Readings')

# Plotting the GSR DATA for participant 2
plt.subplot(4, 1, 3)
plt.plot(data3['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'],  label='Skin_Conductance', color='yellow', alpha=0.7)
plt.plot(data3['Shimmer_86BB_PPGtoHR_LPF_CAL'], label='PPGtoHR', color='green', alpha=0.7)
plt.plot(data3['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'], label='Skin_Resistance', color='orange', alpha=0.7)
plt.plot(data3['Shimmer_86BB_PPG_IBI_LPF_CAL'], label='PPG_IBI', color='brown', alpha=0.7)
plt.title('Participant 2 GSR')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('GSR Readings')

# Plotting the ECG DATA for participant 2
plt.subplot(4, 1, 4)
plt.plot(data4['Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL'], label='ECGtoHR_LA_RA', color='brown', alpha=0.7)
plt.plot(data4['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'], label='ECGtoHR_LL_LA', color='orange', alpha=0.7)
plt.plot(data4['Shimmer_89F4_ECGtoHR_LL_RA_LPF_CAL'], label='ECGtoHR_LL_RA', color='green', alpha=0.7)
plt.plot(data4['Shimmer_89F4_ECGtoHR_Vx_RL_LPF_CAL'], label='ECGtoHR_Vx_RL', color='yellow', alpha=0.7)


plt.title('Participant 2 ECG')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('ECG Readings')

plt.show()  # Show the plot
