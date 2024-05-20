#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries 


# In[17]:


import sys
import scipy 
import numpy
import matplotlib
import pandas 
import sklearn
import seaborn


# In[3]:


#prtint versions of the libraries


# In[4]:


print ('Python:{}'. format(sys.version))
print ('scipy:{}' .format(scipy.__version__))
print ('numpy:{}' .format(numpy.__version__))
print ('matplotlib:{}' .format(matplotlib.__version__))
print ('pandas:{}' .format(pandas.__version__))
print ('sklearn:{}' .format(sklearn.__version__))



# In[18]:


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


# In[6]:


# Load the data from the CSV files
data = pd.read_csv('ECG1.csv')


# In[7]:


#Data preprocessing 
#Examine whether the dataset has missing data 


# In[8]:


data.replace('?', -99999, inplace=True)
print(data.axes)


# In[9]:


print(data.shape)


# In[10]:


print(data.describe())


# In[11]:


data.hist(figsize =(20,20))
plt.show()


# In[25]:


sns.boxplot(x='Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL', y='Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL',hue='Shimmer_89F4_TimestampSync_Unix_CAL', palette='seismic', data=data)


# In[26]:


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


# In[27]:


# Statistical features for the 'Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL' column
LL_LA_electrode = data['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL']
mean_LL_LA_electrode = LL_LA_electrode.mean()
variance_LL_LA_electrode = LL_LA_electrode.var()
skewness_LL_LA_electrode = skew(LL_LA_electrode)
kurtosis_LL_LA_electrode = kurtosis(LL_LA_electrode)

# Frequency-based features: FFT on 'Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'
fft_LL_LA_electrode = fft(LL_LA_electrode.to_numpy())
fft_abs_LL_LA_electrode = np.abs(fft_LL_LA_electrode)
dominant_frequency_amplitude = np.max(fft_abs_LL_LA_electrode)


scaler = MinMaxScaler()
# Ensuring to drop the timestamp column before normalization and keeping the rest of the dataset
normalized_data = scaler.fit_transform(data.iloc[:, 1:])  # Dropping the timestamp for normalization

# Creating a DataFrame from the normalized data for easier analysis
normalized_data_df = pd.DataFrame(normalized_data, columns=data.columns[1:])

statistical_features = {
    "Mean LL_LA_electrode": mean_LL_LA_electrode,
    "Variance LL_LA_electrode": variance_LL_LA_electrode,
    "Skewness LL_LA_electrode": skewness_LL_LA_electrode,
    "Kurtosis LL_LA_electrode": kurtosis_LL_LA_electrode,
    "Dominant Frequency Amplitude": dominant_frequency_amplitude
}

# Returning statistical features and a summary of the normalized data for review
normalized_summary = normalized_data_df.describe().to_dict()

(statistical_features, normalized_summary)





# In[28]:


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


# In[29]:


# Step 2: Feature Extraction within Each Window
def extract_features(window):
    features = {}
    
    features['mean'] = window['Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL'].mean()
    features['variance'] = window['Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL'].var()
    
    features['mean'] = window['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'].mean()
    features['variance'] = window['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL'].var()
    
    features['mean'] = window['Shimmer_89F4_ECGtoHR_LL_RA_LPF_CAL'].mean()
    features['variance'] = window['Shimmer_89F4_ECGtoHR_LL_RA_LPF_CAL'].var()
    
    features['mean'] = window['Shimmer_89F4_ECGtoHR_Vx_RL_LPF_CAL'].mean()
    features['variance'] = window['Shimmer_89F4_ECGtoHR_Vx_RL_LPF_CAL'].var()
    
    
    return features
    


# In[31]:


# Define features and target
X = data.drop('Shimmer_89F4_ECGtoHR_LA_RA_LPF_CAL', axis=1)  # Features
y = data['Shimmer_89F4_ECGtoHR_LL_LA_LPF_CAL']  # Target variable

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


# In[32]:


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




