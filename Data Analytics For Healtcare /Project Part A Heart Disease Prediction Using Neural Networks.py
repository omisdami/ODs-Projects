#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Task 1
#Import libraries and print out the versions
import sys
import numpy as np
import pandas as pd
import sklearn
import keras
import matplotlib.pyplot as plt
import seaborn as sns



# In[14]:


get_ipython().system('pip install tensorflow')


# In[13]:


#print versionof libraries
print ('Python:{}'. format(sys.version))
print ('pd:{}' .format(pd.__version__))
print ('sklearn:{}' .format(sklearn.__version__))
print(f"Seaborn version: {sns.__version__}")
print ('keras:{}'. format(keras.__version__))


# In[15]:


#Task 2: Importing additional packages needed to plot scatterplot matrix
from pandas.plotting import scatter_matrix


# In[27]:


# Task 3: Import the heart disease dataset
df = pd.read_csv('processed.cleveland.data')


# In[17]:


# Task 4: Print the shape of the data frame
print(f"Shape of DataFrame: {df.shape}")


# In[18]:


# Task 5: Print out records of the first fifteen patients
print(df.head(15))


# In[19]:


# Task 6: Print out records of the last 25 patients
print(df.tail(25))


# In[20]:


# Task 7: Obtain more exploratory information about the data using the describe function
print(df.describe())


# In[21]:


# Task 8: Obtain datatypes in the dataset
print(df.dtypes)


# In[22]:


# Check for missing values
print(df.isna())


# In[31]:


# Check for missing data across the entire DataFrame
missing_data_check = df.isnull().sum()

missing_data_check


# In[52]:


# Replace missing values across all columns with 'N/A'
df.fillna('N/A', inplace=True)

# Show a sample to confirm changes
print(df.sample(7))


# In[53]:


# Task 10: Remove missing data by dropping rows with non-number values
df.dropna(inplace=True)


# In[54]:


# Check for missing data across the entire DataFrame
missing_data_check = df.isnull().sum()

missing_data_check


# In[56]:


#crosschecking the dataset
print(df)


# In[58]:


# Convert all columns to numeric, coercing errors to NaN
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


# In[60]:


# Drop rows with NaN values
df= df.dropna()

print(df)


# In[61]:


# Task 11 & 12: Reprint the shape and datatypes in the dataset
print(f"New Shape of DataFrame: {df.shape}")
print(df.dtypes)


# In[62]:


# Task 13: Use the describe function to reprint characteristics of the dataset
print(df.describe())


# In[63]:


# Task 14: Plot histograms of each variable in the dataset
df.hist(figsize=(12, 10))
plt.show()


# In[64]:


from sklearn import model_selection
from sklearn.model_selection import train_test_split


# In[68]:


# Task 15: Split the dataset
X = df.drop('num', axis=1) 
y = df['num']  

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the resulting datasets to verify the split
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[69]:


# Task 16: Convert the data into categorical labels
y_train_categorical = to_categorical(y_train)
y_test_categorical = to_categorical(y_test)
print(f"Shape of y_train_categorical: {y_train_categorical.shape}")
print(y_train_categorical[:12])


# In[70]:


# Task 17: Train the neural network by defining a create_model() function
def create_model():
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(64, activation='relu'),
        Dense(y_train_categorical.shape[1], activation='softmax')
    ])
    return model

model = create_model()


# In[71]:


# Task 18: Compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())


# In[72]:


# Task 19: Convert the data into two (binary) classes
Y_train_binary = np.where(y_train > 0, 1, 0)
Y_test_binary = np.where(y_test > 0, 1, 0)
print(Y_train_binary[:30])


# In[73]:


# Task 20: Create a new model for the binary data
def create_binary_model():
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')  # Change for binary classification
    ])
    return model

binary_model = create_binary_model()


# In[74]:


# Task 21: Compile the binary model
binary_model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
print(binary_model.summary())


# In[75]:


# Task 22: Train both models (assuming training steps are included here)
model.fit(X_train, y_train_categorical, epochs=10, batch_size=10, validation_split=0.2)
binary_model.fit(X_train, Y_train_binary, epochs=10, batch_size=10, validation_split=0.2)

# Make predictions with the categorical model
categorical_pred = model.predict(X_test)
categorical_pred = np.argmax(categorical_pred, axis=1)
print(categorical_pred)


# In[76]:


# Task 23: Generate classification report and accuracy scores for the binary model
binary_pred = binary_model.predict(X_test)
binary_pred = np.round(binary_pred).astype(int).flatten()
print(classification_report(Y_test_binary, binary_pred))
print(f"Accuracy Score: {accuracy_score(Y_test_binary, binary_pred)}")


# In[ ]:




