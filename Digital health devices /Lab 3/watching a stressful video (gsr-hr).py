import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('WATCHIBG A VIDEO TO INDUCE ANXIETY(raw).csv')

x_axis = data['Shimmer_86BB_TimestampSync_Unix_CAL']

# Plot the unfiltered GSR-HR data
plt.figure(figsize=(9, 5))
plt.subplot(3, 1, 1)
plt.plot(data['Shimmer_86BB_PPGtoHR_CAL'], label='unfiltered GSR-HR')
plt.title('Unfiltered GSR-HR Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')  # Add y-axis label

# Plot the filtered GSR-HR data
plt.subplot(3, 1, 2)
plt.plot(data['Shimmer_86BB_PPGtoHR_LPF_CAL'], label='Filtered GSR-HR')
plt.title('Filtered GSR-HR Data')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')  # Add y-axis label

# Show the plot
plt.tight_layout()
plt.show()

