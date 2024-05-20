#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1-import libraires 
import sys
import pandas as pd
import sklearn


# #Q2 
# Keras is a high-level neural networks library, written in Python and capable of running on top of either TensorFlow or Theano. It was developed with a focus on enabling fast experimentation and being able to go from idea to result with the least possible delay a key to doing good research. Keras was initially developed as part of the research effort of project ONEIROS (Open-ended Neuro-Electronic Intelligent Robot Operating System).
# 
# -Allows for easy and fast prototyping (through total modularity, minimalism, and extensibility).
# 
# -Supports both convolutional networks and recurrent networks, as well as combinations of the two.
# 
# -Supports arbitrary connectivity schemes (including multi-input and multi-output training).
# 
# -Runs seamlessly on CPU and GPU

# #Q3
# TensorFlow is an open-source machine learning library developed by the Google Brain team. It is one of the most popular and widely used frameworks for building and training machine learning models, especially deep learning models. TensorFlow provides a comprehensive set of tools and libraries for numerical computation, data flow graphs, and machine learning across a range of tasks. some of the major attributes include:
# 
# 1 Versatility: TensorFlow can be applied to a wide range of tasks, but it particularly excels in training and deploying deep neural networks.
# 
# 2 Data Tools: TensorFlow provides tools for data consolidation, cleaning, and preprocessing. You can work with standard datasets, scalable data pipelines, and preprocessing layers to prepare your data effectively.
# 
# 3 Responsible AI: The library includes tools to uncover and eliminate bias in your data, ensuring fair and ethical outcomes from your machine learning models.
# 
# 4 Ecosystem: TensorFlow offers an entire ecosystem built on its core framework. You can explore pre-trained models, fine-tune them, and track development using tools like Model Analysis and TensorBoard.
# 
# 5 Deployment Options:
# On-Device: Run models on mobile devices, edge computing devices, and even microcontrollers using TensorFlow Lite.
# 
# In the Browser: Use TensorFlow.js to perform machine learning directly in web browsers.
# 
# In the Cloud: Deploy production-ready ML pipelines for training and inference using TFX.

# #Q4
# Keras serves as the high-level API for the TensorFlow platform.Keras leverages TensorFlow’s scalability and cross-platform capabilities, allowing the running of  models on GPUs, TPUs, browsers, or mobile devices.
# 
# In 2017, the developers of Keras and TensorFlow collaborated to bring Keras into the TensorFlow project. Since TensorFlow version 2.0, Keras has been included as the official high-level API for building and training deep learning models within the TensorFlow framework. 
# 
# This integration allows users to combine the simplicity of Keras with the flexibility and scalability of TensorFlow, offering a powerful platform for developing and deploying machine learning and deep learning applications.

# In[2]:


get_ipython().system('pip install tensorflow')


# In[3]:


#importing keras 
import keras


# In[4]:


#print versionof libraries
print ('Python:{}'. format(sys.version))
print ('pd:{}' .format(pd.__version__))
print ('sklearn:{}' .format(sklearn.__version__))
print ('keras:{}'. format(keras.__version__))


# In[5]:


#Task 3
#load a txt file
df = pd.read_table('Autism-Child-Data.txt', delimiter=',')


# In[6]:


#entering deleted attributes
names=['A1_Score',
      'A2_Score',
      'A3_Score',
      'A4_Score',
      'A5_Score',
      'A6_Score',
      'A7_Score',
      'A8_Score',
      'A9_Score',
      'A10_Score',
      'age',
      'gender',
      'ethnicity',
      'jundice',
      'family_hist_autism',
       'contry_of_res',
       'used_app_before',
       'result',
       'age_desc',
       'relation',
       'class']
       


# In[7]:


#reading data using pandas 
data = pd.read_table('Autism-Child-Data.txt', sep=',', names=names)


# In[8]:


#task 4
print ('Shape of Dataframe: {}'.  format(data.shape))
print (data.loc[0])


# #Q5
# Patient [0]does not have a family historyof autism 

# In[9]:


print (data.loc[21])


# #Q6 Patient [21] ethnicity is unknown or missing

# In[10]:


#task 5 Print out records of the first thirteen patients 
first_thirteen_patients = data.loc[range(1, 14)]
print(first_thirteen_patients)


# In[11]:


# task 6
# Use describe() to generate statistics
summary_statistics = data.describe()

# Print the DataFrame with count, mean, std, min, max, and percentiles
print(summary_statistics)


# In[12]:


#task 7 obtaining data types from dataset
data.dtypes


# #Q7 
# For most data types, pandas uses NumPy arrays as the concrete objects contained with a Index, Series, or DataFrame.
# 
# For some data types, pandas extends NumPy’s type system
# 
# In pandas, the term "object" refers to the dtype (data type) that can represent a variety of data structures, including strings or mixed types (i.e., columns with different types of data). The object dtype is a catch-all for columns that don't fit into a more specific category like int, float, datetime, etc.
# 
# When you see a column or Series with dtype "object" in pandas, it typically means that the data in that column is not purely numerical or has a mix of data types. This can include strings, mixed types, or even more complex Python objects.

# In[13]:


#Data Processing
#Q8 Drop unwanted columns 
data = data.drop(['result', 'age_desc'], axis=1)


# In[14]:


data.loc [ :12]


# In[15]:


#task 9 splitting dataframe into X and Y
x = data.drop(['class'], axis= 1)
y = data['class']


# In[16]:


# Using loc[] to check the DataFrame
x.loc[:]


# In[17]:


#Task 10 one-hot encoding for X converting values to categorical variables and showing the dummy value 
X = pd.get_dummies(x)
 


# In[18]:


X.columns.values


# In[19]:


X.loc[7]


# In[20]:


#Task 11 one-hot encoding for Y  converting values to categorical variables and showing the dummy value 
Y = pd.get_dummies(y)
Y.columns.values


# In[21]:


Y.loc[7]


# In[22]:


#splitting the datasetinto training and testing datsets 
#task 12
from sklearn import model_selection 

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = 0.2, random_state=42)

# print the shape of the datasets
print (X_train.shape)
print (X_test.shape)
print (Y_train.shape)
print (Y_test.shape)


# #Q9 
# 
# The test size is a crucial parameter when splitting datasets into training and testing sets in machine learning. It plays a pivotal role in model evaluation, helping assess a model's generalization performance on new, unseen data. Adequate test size is essential for detecting overfitting, optimizing hyperparameters, and avoiding data leakage. A larger test set provides a more robust and reliable estimate of a model's performance, ensuring that the evaluation metrics are less susceptible to random variability. Striking the right balance in test size is crucial, as it influences the trade-off between having sufficient data for training and obtaining a trustworthy evaluation of a model's ability to generalize to real-world scenarios. Cross-validation techniques can complement this process by mitigating performance variability across different train-test splits.

# In[23]:


#setting up a neural network using keras
#task 13 importing the layers and models needed to set up thhe model 

from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# #Q10
# 
# Sequential:
# Sequential is a linear stack of layers in Keras. It allows for the creation of models layer by layer in a step-by-step fashion. Each layer has weights that correspond to the layer that follows it. This is the most straightforward way to build a neural network in Keras.
# 
# Dense:
# Dense is a type of layer in Keras that represents a fully connected layer. It means that each neuron in the layer is connected to every neuron in the preceding layer. The Dense layer is often used for the output layer in a neural network, especially for classification problems.
# 
# Adam:
# Adam is an optimization algorithm commonly used for training deep learning models. It is an extension to stochastic gradient descent (SGD) and combines ideas from Adagrad and RMSprop. Adam adjusts the learning rates of each parameter individually, allowing for adaptive learning rates and efficient optimization.
# For the most accurate and up-to-date information, please refer to the official documentation for TensorFlow and Keras by following the provided links.

# In[25]:


#task 14 defining the function to set up the keras model 

def create_model (): 
    #set up the model 
    model = Sequential ([
    (Dense(8, input_dim=X_train.shape[1], kernel_initializer='normal', activation='relu')),
    (Dense(4, kernel_initializer='normal', activation = 'relu')),
    (Dense(2, activation='sigmoid'))
    ])
    return model

#task 16 creating model 
model = create_model()

#task 15 compiling the model by defining an optimizer and specifing a learning rate

#complie the model, define an optimizer and specify a learning rate 

adam = Adam (learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics =['accuracy'])


print(model.summary())



  


# In[26]:


print (X_train)


# In[27]:


print ("shape of X_train:", X_train.shape)


# In[28]:


print (Y_train)


# In[32]:


#converting to float 32
#Training and testing the neural network 
#task 17 fitting the model to the training data

X_train = X_train.astype('float32')
Y_train = Y_train.astype('float32')

model.fit(X_train, Y_train, epochs=50, batch_size=10, verbose= 1)


# #Q11
# In machine learning, particularly in the context of training neural networks, defining the number of epochs and batch size are crucial hyperparameters that influence the training process. Let's break down the need for defining epochs and batch size:
# 
# Epochs:
# An epoch represents one complete pass through the entire training dataset during the training phase.
# Training a model involves adjusting its parameters based on the error (or loss) it incurs on the training data. Multiple passes through the dataset allow the model to learn from the data and improve its performance.
# However, training for too many epochs can lead to overfitting, where the model becomes too specialized on the training data and performs poorly on new, unseen data.
# Batch Size:
# The batch size refers to the number of training examples utilized in one iteration. In each iteration, the model's parameters are updated based on the average error computed over the examples in the current batch.
# Different batch sizes have different effects on the training process. A smaller batch size may lead to a more frequent update of the model parameters, providing a more stochastic and noisy learning process. On the other hand, a larger batch size may offer a more stable and averaged gradient but requires more memory.
# The choice of batch size is also related to the computational resources available. Larger batch sizes might require more memory, and if the batch size is too large for the available resources, it can lead to out-of-memory errors.
# 
# #Q12
# In Keras, the verbose parameter is used to control the amount of information printed during the training and evaluation of a model. It is commonly used when fitting or evaluating a model using methods such as fit() or evaluate(). The verbose parameter takes integer values, and its purpose is to adjust the level of logging or output displayed on the console during the training or evaluation process.
# 
# #Q13
#  The accuracy increased progresively and became 100%b before the first 50 epochs while the loss had an initial lower figure before spiking up and slowly regressing.The accuracy result is however for the training. data.
# 

# In[34]:


#task 18 generating classification and accuracy reports 

from sklearn.metrics import classification_report, accuracy_score
import numpy as np

#converting X_test into float32
X_test = X_test.astype('float32')

predictions =np.argmax(model.predict(X_test),axis=1)
predictions


# In[37]:


#prediction results, accuracy score and classification report
print('Prediction Results. for Neural Network')
print(accuracy_score(Y_test[['YES']],predictions))
print(classification_report(Y_test[['YES']],predictions))


# #Q14
#  Precision is a measure of how many predicted positive instances are actually positive. In this case, it's 97% for the False class and 90% for the True class
#  
#  #Q15
#  Recall also called sensitivity measures how many actual positive instances were correctly predicted. It's 95% for both False and True classes.
# 
# #Q16
# F1-score is the harmonic mean of precision and recall. It is a balance between precision and recall. It's 96% for False and 93% for True class.
# 
# #Q17
# The support score is the number of actual occurrences of the class in the specified dataset.  In this case, it's 39 for False and 20 for the True class.
# 

# In[ ]:




