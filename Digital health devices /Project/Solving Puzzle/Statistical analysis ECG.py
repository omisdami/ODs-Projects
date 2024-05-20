import pandas as pd

# Load the dataset
data1 = pd.read_csv('ECG1.csv')
data2 = pd.read_csv('ECG2.csv')
# Calculate the average Heart Rate
average_Heart_Rate1 = data1['Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL'].mean()
average_Heart_Rate2 = data1['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'].mean()
average_Heart_Rate3 = data1['Shimmer_89F4_ECGtoHR_LL_RA_LPF_CAL'].mean()
average_Heart_Rate4 = data1['Shimmer_89F4_ECGtoHR_Vx_RL_LPF_CAL'].mean()

average_Heart_Rate5 = data2['Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL'].mean()
average_Heart_Rate6 = data2['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'].mean()
average_Heart_Rate7 = data2['Shimmer_89F4_ECGtoHR_LL_RA_LPF_CAL'].mean()
average_Heart_Rate8 = data2['Shimmer_89F4_ECGtoHR_Vx_RL_LPF_CAL'].mean()



# Print the results
print(f"Average Heart Rate for participant 1.1: {average_Heart_Rate1} beats per minute")
print(f"Average Heart Rate for participant 1.2: {average_Heart_Rate2} beats per minute")
print(f"Average Heart Rate for participant 1.3: {average_Heart_Rate3} beats per minute")
print(f"Average Heart Rate for participant 1.4: {average_Heart_Rate4} beats per minute")





print(f"Average Heart Rate for participant 2.1: {average_Heart_Rate5} beats per minute")
print(f"Average Heart Rate for participant 2.2: {average_Heart_Rate6} beats per minute")
print(f"Average Heart Rate for participant 2.3: {average_Heart_Rate7} beats per minute")
print(f"Average Heart Rate for participant 2.4: {average_Heart_Rate8} beats per minute")
