#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libraries 


# In[84]:


import sys
import scipy 
import numpy
import matplotlib
import pandas 
import sklearn
import seaborn


# In[5]:


#prtint versions of the libraries


# In[6]:


print ('Python:{}'. format(sys.version))
print ('scipy:{}' .format(scipy.__version__))
print ('numpy:{}' .format(numpy.__version__))
print ('matplotlib:{}' .format(matplotlib.__version__))
print ('pandas:{}' .format(pandas.__version__))
print ('sklearn:{}' .format(sklearn.__version__))



# In[85]:


import numpy as np 
import seaborn as sns
from sklearn import preprocessing 
from sklearn import model_selection 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt  
import pandas as pd
from scipy.stats import skew, kurtosis
from scipy.fft import fft
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# In[8]:


# Load the data from the CSV files
data = pd.read_csv('GSR1.csv')


# In[9]:


#Data preprocessing 
#Examine whether the dataset has missing data 


# In[11]:


data.replace('?', -99999, inplace=True)
print(data.axes)


# In[12]:


print(data.shape)


# In[15]:


print(data.describe())


# In[16]:


data.hist(figsize =(20,20))
plt.show()


# In[86]:


sns.boxplot(x='Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL', y='Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL',hue='Shimmer_86BB_TimestampSync_Unix_CAL', palette='seismic', data=data)


# In[41]:


# Display basic information about the dataset for review
data_info = {
    "head": data.head(),
    "description": data.describe(),
    "info": data.info()
}

# Since we cannot directly execute data.info(), we gather necessary info manually
info_details = {
    "columns": data.columns.tolist(),
    "shape": data.shape,
    "missing_values": data.isnull().sum().to_dict()
}

data_info["details"] = info_details

data_info


# In[48]:


# Statistical features for the 'Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL' column
gsr_conductance = data['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL']
mean_conductance = gsr_conductance.mean()
variance_conductance = gsr_conductance.var()
skewness_conductance = skew(gsr_conductance)
kurtosis_conductance = kurtosis(gsr_conductance)

# Frequency-based features: FFT on 'Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'
fft_conductance = fft(gsr_conductance.to_numpy())
fft_abs_conductance = np.abs(fft_conductance)
dominant_frequency_amplitude = np.max(fft_abs_conductance)


scaler = MinMaxScaler()
# Ensuring to drop the timestamp column before normalization and keeping the rest of the dataset
normalized_data = scaler.fit_transform(data.iloc[:, 1:])  # Dropping the timestamp for normalization

# Creating a DataFrame from the normalized data for easier analysis
normalized_data_df = pd.DataFrame(normalized_data, columns=data.columns[1:])

statistical_features = {
    "Mean Conductance": mean_conductance,
    "Variance Conductance": variance_conductance,
    "Skewness Conductance": skewness_conductance,
    "Kurtosis Conductance": kurtosis_conductance,
    "Dominant Frequency Amplitude": dominant_frequency_amplitude
}

# Returning statistical features and a summary of the normalized data for review
normalized_summary = normalized_data_df.describe().to_dict()

(statistical_features, normalized_summary)





# In[49]:


# Statistical features for the 'Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL' column
gsr_resistance = data['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL']
mean_resistance = gsr_resistance.mean()
variance_resistance = gsr_resistance.var()
skewness_resistance = skew(gsr_resistance)
kurtosis_resistance = kurtosis(gsr_resistance)

# Frequency-based features: FFT on 'Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'
fft_resistance = fft(gsr_resistance.to_numpy())
fft_abs_resistance = np.abs(fft_resistance)
dominant_frequency_amplitude = np.max(fft_abs_resistance)


scaler = MinMaxScaler()
# Ensuring to drop the timestamp column before normalization and keeping the rest of the dataset
normalized_data = scaler.fit_transform(data.iloc[:, 1:])  # Dropping the timestamp for normalization

# Creating a DataFrame from the normalized data for easier analysis
normalized_data_df = pd.DataFrame(normalized_data, columns=data.columns[1:])

statistical_features = {
    "Mean resistance": mean_resistance,
    "Variance resistance": variance_resistance,
    "Skewness resistance": skewness_resistance,
    "Kurtosis resistance": kurtosis_resistance,
    "Dominant Frequency Amplitude": dominant_frequency_amplitude
}

# Returning statistical features and a summary of the normalized data for review
normalized_summary = normalized_data_df.describe().to_dict()

(statistical_features, normalized_summary)



# In[55]:


# Step 1: Segmenting Data into Time Windows

window_size = 60  # in seconds, adjust according to your dataset's sampling rate
overlap_size = 30  # in seconds
start = 0  # Starting index of the window
end = window_size  # Ending index of the window
windows = []  # To store the segmented windows

while end <= len(data):
    windows.append(data.iloc[start:end])
    start += window_size - overlap_size
    end = start + window_size




# In[72]:


# Step 2: Feature Extraction within Each Window
def extract_features(window):
    features = {}
    
    features['mean'] = window['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'].mean()
    features['variance'] = window['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'].var()
    features['mean'] = window['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'].mean()
    features['variance'] = window['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'].var()
    return features
    
   



# In[78]:


# Step 3: Combining Different Physiological Signals into Composite Features
# This step involves domain-specific knowledge to create meaningful combinations

composite_features = []
for window in windows:
    composite_feature = {}
    
    #to get conductance_heart_rate_ratio
    composite_feature['conductance_heart_rate_ratio'] = window['Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL'].mean() / window['Shimmer_86BB_PPGtoHR_LPF_CAL'].mean()
    composite_features.append(composite_feature)
    
      #to get conductance_heart_rate_ratio
    composite_feature['resistance_heart_rate_ratio'] = window['Shimmer_86BB_GSR_Skin_Resistance_LPF_CAL'].mean() / window['Shimmer_86BB_PPGtoHR_LPF_CAL'].mean()
    composite_features.append(composite_feature)
   
    print(composite_feature)
  


# In[81]:


# Define features and target
X = data.drop('Shimmer_86BB_GSR_Skin_Conductance_LPF_CAL', axis=1)  # Features
y = data['Shimmer_86BB_PPGtoHR_LPF_CAL']  # Target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the model for regression
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)

# Evaluate the model using RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f}")

# Feature Importance
feature_importances = pd.DataFrame(rf.feature_importances_,
                                   index = X_train.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances)


# In[82]:


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Predictions on the test set
y_pred = rf.predict(X_test)

# Calculating performance metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Adjusted R-squared
n = len(y_test)  # Number of observations
p = X_test.shape[1]  # Number of features
adjusted_r2 = 1 - (1-r2)*(n-1)/(n-p-1)

# Printing the metrics
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R-squared: {r2:.2f}")
print(f"Adjusted R-squared: {adjusted_r2:.2f}")


# In[ ]:




