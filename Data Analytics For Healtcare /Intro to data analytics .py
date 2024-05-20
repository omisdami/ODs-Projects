#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Introduction to summary and correlation


# In[3]:


num_hosp =[100,49,23,24,33,45,13,67,23,73,23,44,88,34,53,65,43,67,23,83,63,49,98,34]


# In[5]:


from collections import  Counter
import matplotlib.pyplot as plt


# In[7]:


hosp_counts = Counter (num_hosp)
xs= range(101)
ys= [hosp_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,101,0,5])
plt.title("Bar Chart of Hospitalization Counts")
plt.xlabel("# of Hospitalizations")
plt.ylabel("# of hospitals")
plt.show()


# In[8]:


num_points= len(num_hosp)
print(num_points)


# In[9]:


largest_value = max(num_hosp)
smallest_value= min(num_hosp)
print(largest_value)
print(smallest_value)


# In[11]:


sorted_values= sorted(num_hosp)
smallest_values= sorted_values[0]


# In[12]:


print(smallest_value)


# In[14]:


nth_value= sorted_values[6]
print(nth_value)


# In[16]:


second_smallest_value= sorted_values[1]
second_largest_value= sorted_values[-2]
print(second_smallest_value)
print(second_largest_value)


# # CENTRAL TENDENCES

# In[19]:


import statistics 


# In[20]:


x= statistics.mean(num_hosp)
print("Mean value is :", x)


# In[21]:


hosp_med= statistics.median(num_hosp)
print(hosp_med)


# In[42]:


hosp_quant1= statistics.quantiles(num_hosp, n=4, method = 'exclusive')
print(hosp_quant1)


# In[28]:


import numpy as np


# In[29]:


hosp_quant50= np.quantile(num_hosp, .50)
print(hosp_quant50)


# In[30]:


hosp_quant75= np.quantile(num_hosp, .75)
print(hosp_quant75)


# In[31]:


hosp_quant90= np.quantile(num_hosp, .90)
print(hosp_quant90)


# In[32]:


hosp_mode= statistics.mode(num_hosp)
print(hosp_mode)


# # DISPERSION 

# In[37]:


range_hosp = max(num_hosp)- min(num_hosp)
print(range_hosp)


# In[38]:


x = range(11)
for n in x:
    print(n)


# In[40]:


import math 


# In[43]:


statistics.variance(num_hosp)


# In[44]:


std_hosp= statistics.stdev(num_hosp)
print(std_hosp)


# In[48]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy as sp
import warnings
warnings.filterwarnings('ignore')


# In[49]:


df= pd.read_csv('heart.csv')


# In[51]:


plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')


# In[52]:


gen= pd.crosstab(df['sex'], df['target'])
print(gen)


# In[54]:


gen.plot(kind='bar', stacked=True, color=['red','black'], grid=False)


# In[61]:


temp= pd.crosstab(index=df['sex'],
                  columns=[df['thal']], 
                  margins=True) 
temp


# In[62]:


temp.plot(kind='bar', stacked=True)
plt.show()


# In[63]:


sns.boxplot(x='sex', y='chol', hue='target', palette='seismic', data=df)


# In[64]:


sns.countplot(x='cp', hue='sex', data=df, palette='BrBG')


# In[ ]:




