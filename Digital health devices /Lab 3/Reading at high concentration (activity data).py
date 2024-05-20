import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('READING AT HIGH CONC(raw).csv')

x_axis = data['Shimmer_86BB_TimestampSync_Unix_CAL']

# Plot the GSR Range data
plt.figure(figsize=(12, 8))
plt.subplot(6, 1, 1)
plt.plot(data['Shimmer_86BB_GSR_Range_CAL'], label='Unfiltered GSR Range')
plt.plot(data['Shimmer_86BB_GSR_Range_LPF_CAL'], label='Filtered GSR Range')
plt.title('GSR Range Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')  # Add y-axis label

# Plot the Skin Conductance Data
plt.subplot(6, 1, 2)
plt.plot(data['Shimmer_86BB_GSR_Skin_Conductance_CAL'], label='Unfiltered Skin Conductance')
plt.plot(data['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'], label='Filtered Skin Conductance')
plt.title('Skin Conductance Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')

# Plot the Skin Resistance Data
plt.subplot(6, 1, 3)
plt.plot(data['Shimmer_86BB_GSR_Skin_Resistance_CAL'], label='Unfiltered Skin Resistance')
plt.plot(data['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'], label='Filtered Skin Resistance')
plt.title('Skin Resistance Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')

# Plot the PPG A13 Data
plt.subplot(6, 1, 4)
plt.plot(data['Shimmer_86BB_PPG_A13_CAL'], label='Unfiltered PPG A13')
plt.plot(data['Shimmer_86BB_PPG_A13_LPF_CAL'], label='Filtered PPG A13')
plt.title('PPG A13 Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')

# Plot the PPG IBI Data
plt.subplot(6, 1, 5)
plt.plot(data['Shimmer_86BB_PPG_IBI_CAL'], label='Unfiltered PPG IBI')
plt.plot(data['Shimmer_86BB_PPG_IBI_LPF_CAL'], label='Filtered PPG IBI')
plt.title('PPG IBI Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')

# Plot the GSR-HR Data
plt.subplot(6, 1, 6)
plt.plot(data['Shimmer_86BB_PPGtoHR_CAL'], label='Unfiltered GSR-HR')
plt.plot(data['Shimmer_86BB_PPGtoHR_LPF_CAL'], label='Filtered GSR-HR')
plt.title('GSR-HR Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')

# Show the plot
plt.tight_layout()
plt.show()


