from pandas import read_csv
import matplotlib.pyplot as plt

# Create a list to store the data for each participant
all_participant_data = []

for x in range(1, 5):
    filepath = f'{x}.csv'
    df = read_csv(filepath)
    activitiesx = df.values[:, 4]

    # Append data for the current participant to the list
    all_participant_data.append(activitiesx)

# Plot stacked histograms
plt.hist(all_participant_data, bins=20, alpha=0.7, label=['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4'])
plt.xlabel('Accelerometer')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Accelerometer Data for Participants 1 to 4')
plt.legend()
plt.show()
