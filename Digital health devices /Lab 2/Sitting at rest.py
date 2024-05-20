import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('SITTING AT REST(cleaned).csv')

x_axis = data['Shimmer_89C7_TimestampSync_Unix_CAL']

# Plot the accelerometer data
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(data['Shimmer_89C7_Accel_LN_X_CAL'], label='X')
plt.plot(data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Y')
plt.plot(data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Z')
plt.title('Sitting at Rest(Accelerometer Unfiltered Data)')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')  # Add y-axis label

# Plot the gyroscope data
plt.subplot(3, 1, 2)
plt.plot(data['Shimmer_89C7_Gyro_X_CAL'], label='X')
plt.plot(data['Shimmer_89C7_Gyro_Y_CAL'], label='Y')
plt.plot(data['Shimmer_89C7_Gyro_Z_CAL'], label='Z')
plt.title('Sitting at Rest(Gyroscope Unfiltered Data)')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')  # Add y-axis label

# Plot the magnetometer data
plt.subplot(3, 1, 3)
plt.plot(data['Shimmer_89C7_Mag_X_CAL'], label='X')
plt.plot(data['Shimmer_89C7_Mag_Y_CAL'], label='Y')
plt.plot(data['Shimmer_89C7_Mag_Z_CAL'], label='Z')
plt.title('Sitting at Rest(Magnetometer Unfiltered Data)')
plt.legend()
plt.xlabel('Timestamp')  # Add x-axis label
plt.ylabel('Sensor Readings')  # Add y-axis label

# Show the plot
plt.tight_layout()
plt.show()

