#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A simple bar chart 


# In[2]:


from matplotlib import pyplot as plt


# In[4]:


year = [1950, 1960, 1970, 1980,1990,2000,2010,2020]
gpd = [300.2, 543.3, 1075.9, 2863.5,5979.6,10289.7, 14958.3,18623.4]


# In[12]:


plt.plot(year, gpd, color='red', linestyle='solid')
plt.title('Nominal GDP')
plt.ylabel("Billions of $")
plt.xlabel("Decades")
plt.show()


# In[ ]:


year_5_=[1975,1980,]


# In[ ]:





# In[ ]:





# In[13]:


#import libraries


# In[19]:


import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 
import numpy as np
import scipy as sp
import warnings
warnings.filterwarnings('ignore')


# In[20]:


df= pd.read_csv('heart.csv')


# In[21]:


df.head()


# In[22]:


df.shape


# In[23]:


df.describe()


# In[24]:


df.isnull().sum()


# In[25]:


print(df.info())


# In[26]:


plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')


# In[27]:


sns.pairplot(data=df)


# In[28]:


df.hist(figsize=(12,12), layout=(5,3))


# In[30]:


df.plot(kind='box', subplots=True ,layout=(5,3), figsize=(12,12))
plt.show()


# In[31]:


sns.catplot(data=df, x='sex', y='age',hue='target', palette='winter')


# In[33]:


sns.barplot(data=df, x='sex',y='chol', hue='target', palette='husl')


# In[34]:


plt.rcParams['figure.figsize']=(12,8)
sns.set_style('darkgrid')


# In[35]:


#Age distribution 


# In[37]:


df['age'].hist(grid=True, bins=10);
plt.title('Age Distribution')


# In[38]:


sns.distplot(df['trestbps'], bins=10)
plt.title('Resting Blood Pressure')


# In[39]:


plt.rcParams['figure.figsize']=(8,8)
sns.scatterplot(x='chol', y='trestbps', hue='sex', size=None, data=df)
plt.title('Cholesterol VS Resdting Blood Pressure')


# In[ ]:


year_by_5=[1975,1980,1985,1990,1995,2000,2005,2010,2015,2020]
total_h_exp=[12199.4,2298.4,3984]

