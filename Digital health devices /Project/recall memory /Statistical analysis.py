import pandas as pd

# Load the dataset
data1 = pd.read_csv('GSR1.csv')
data2 = pd.read_csv('GSR2.csv')

# Calculate the average skin resistance
average_skin_resistance1 = data1['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'].mean()
average_skin_resistance2 = data2['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'].mean()

#calculate the average Heart Rate
average_Heart_Rate1 = data1['Shimmer_86BB_PPGtoHR_LPF_CAL'].mean()
average_Heart_Rate2 = data2['Shimmer_86BB_PPGtoHR_LPF_CAL'].mean()

# Calculate the average resistance from conductance
average_conductance1 = data1['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'].mean()
average_resistance_from_conductance1 = 1 / average_conductance1

average_conductance2 = data2['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'].mean()
average_resistance_from_conductance2 = 1 / average_conductance2


# Print the results
print(f"Average Skin Resistance for participant 1: {average_skin_resistance1} ohms")
print(f"Average Resistance (from Conductance) for participant 1: {average_resistance_from_conductance1} ohms")
print(f"Average Heart for participant 1: {average_Heart_Rate1} beats per minute")

print(f"Average Skin Resistance for participant 2: {average_skin_resistance2} ohms")
print(f"Average Resistance (from Conductance) for participant 2: {average_resistance_from_conductance2} ohms")
print(f"Average Heart for participant 2: {average_Heart_Rate2} beats per minute")
