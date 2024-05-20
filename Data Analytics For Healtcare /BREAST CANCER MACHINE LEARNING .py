#!/usr/bin/env python
# coding: utf-8

# # objective of h=the project: To examine how to use  machine larming to help detect breast cancer through. SVmand KNM models

# In[1]:


#import libraries 


# In[2]:


import sys
import scipy 
import numpy
import matplotlib
import pandas 
import sklearn 


# In[3]:


#prtint versions of the libraries


# In[8]:


print ('Python:{}'. format(sys.version))
print ('scipy:{}' .format(scipy.__version__))
print ('numpy:{}' .format(numpy.__version__))
print ('matplotlib:{}' .format(matplotlib.__version__))
print ('pandas:{}' .format(pandas.__version__))
print ('sklearn:{}' .format(sklearn.__version__))



# In[9]:


"""import packages in the specific ways. that we will be using them in the project"""


# In[16]:


import numpy as np 
from sklearn import preprocessing 
#import the KNN for neighbors
from sklearn.neighbors import KNeighborsClassifier
#import support vector classifier from support vector machine(SVM)
from sklearn.svm import SVC
#import model selection which allows us to use both KNMand svc in one step 
from sklearn import model_selection 
#import train test split from sklearn model selection
from sklearn.model_selection import train_test_split
#we neeed to obtain some metrics 
from sklearn.metrics import classification_report, accuracy_score
#we can explore data visualization in pandas, before. doing actualmachine learning 
from pandas.plotting import scatter_matrix
#we can use matplotlib for visualization as well
import matplotlib.pyplot as plt 
#wecan importa all pandas to handle datasets 
import pandas as pd



# In[17]:


#A note about depracted packages.Some packages get old, replaced or discontinued  


# # Import or upload dataset

# In[35]:


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"


# In[36]:


names = ['id', 'clump_thickness', 'uniform_cell_size', 'uniform_cell_shape', 'marginal_adhesion', 
         'single_epithelial_size', 'bare_nuclei', 'bland-chromatin', 'normal_nucleoli', 'mitosis', 'class']
#create dataframe
df = pd.read_csv(url, names=names)


# In[37]:


#Data preprocessing 
#Examine whether the dataset has missing data 


# In[38]:


df.replace('?', -99999, inplace=True)
print(df.axes)


# In[39]:


print(df.shape)


# In[41]:


print(df.loc[6])


# In[43]:


df.head(7)


# In[45]:


print(df.loc[6])
print(df.describe())


# In[51]:


df.hist(figsize =(20,20))
plt.show()


# In[50]:


scatter_matrix(df, figsize = (20,20))
plt.show()


# In[52]:


#Create the training dataset. To do this we define them as x and y datasets


# In[57]:


x = np.array(df.drop(['class'], axis=1))
y = np.array(df['class'])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[58]:


#Testing options
speed = 8 
scoring ='accuracy'


# In[63]:


#define models is to train 
models = []
models.append(('KNN', KNeighborsClassifier(n_neighbors =5)))
models.append(('SVM', SVC()))


# In[ ]:





# In[ ]:




