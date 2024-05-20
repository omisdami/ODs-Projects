#!/usr/bin/env python
# coding: utf-8

# # Part A: Illustrative Cases

# In[1]:


def calculate_bmi(weight, height, weight_unit='kg', height_unit='m'):
    
    if weight_unit == 'lb':
        weight_kg = weight * 0.453592
    else:
        weight_kg = weight

    if height_unit == 'cm':
        height_m = height /100
    else:
        height_m = height

    bmi = weight_kg / height_m ** 2
    return bmi




# In[2]:


#Patient 1
weight_input= 130 * 0.453592
height_input= 165.1/100

bmi_result = calculate_bmi(weight_input, height_input)
print(f"BMI is: {bmi_result}")


# In[3]:


#Patient 2
weight_input= 114 * 0.453592
height_input= 165/ 100

bmi_result = calculate_bmi(weight_input, height_input)
print(f"BMI is: {bmi_result}")


# In[4]:


#Patient 3
weight_input= 145 * 0.453592
height_input= 171/100

bmi_result = calculate_bmi(weight_input, height_input)
print(f"BMI is: {bmi_result}")


# In[5]:


#Patient 4
weight_input= 55
height_input= 150

bmi = weight_input / height_input ** 2
print(bmi)


# # MEDICATION LIST

# In[6]:


formulary = ["epirubicin", "florouracil", "cyclophodphamide", "doceetaxel 155mg IV", "erlotinib 150mg", "oxaliplatin","leucovorin", "fluorouracil"]


# In[7]:


for medication in formulary:
    print(f"{medication} is Prescribed")


# # oncology unit admissions

# In[8]:


oncology_unit_admissions = {
    "Patient 1" : "Room 26-A",
    "Patient 2" : "Room 26-B",
    "Patient 3" : "Room 267",
    "Patient 4" : "Room 28-A"
}
print (f"Admitted as follows {oncology_unit_admissions}")


# In[9]:


def bmi_status(calculate_bmi):
 if bmi_status < 18.5:
    return 'Underweight'
 elif 18.5 <= bmi < 25:
    return 'Normal weight'
 elif 25 <= bmi < 30: 
        return 'overweight'
 else: return'Obese'


# In[ ]:





# # Part B: Wisconsin Breast Cancer Dataset

# In[10]:


import pandas as pd

file_path = 'data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

print("Columns for the first five rows:")
print(df.head())

print("\nColumns for the last five rows:")
print(df.tail())


# In[11]:


import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import scipy as sp
import warnings
warnings.filterwarnings('ignore')


# In[12]:


df['diagnosis'].hist(grid=True, bins=10);
plt.title('BAR CHART')


# In[15]:


file_path = 'data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Select columns of specific data types (float64 and int64)
numeric_columns = df.select_dtypes(include=['float64', 'int64'])

# Create a correlation matrix
correlation_matrix = numeric_columns.corr()

plt.figure(figsize=(20,20))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()


# # Part C: Canadian Institute for Health Information National Health Expenditures Data Table

# In[17]:


file_path = 'cihi_nhex_data.xlsx'


# In[18]:


# Read the Excel sheet into a DataFrame
df = pd.read_excel(file_path)


# In[19]:


#  Data for 5 years interval for hospitals
years = list(range(1975, 2021, 5))
hospital_expenditure = [5454.9,9334.4,16260.3,22768.5,24231.5,29615.4,41218.0,56256.5,63811.1,74637.5]


# In[20]:


# Line plot for total health expenditure by use of funds for hospitals
plt.figure(figsize=(10, 6))
plt.plot(years, hospital_expenditure, marker='o', linestyle='-', color='black')
plt.title('Total Health Expenditure for Hospitals')
plt.xlabel('Years')
plt.ylabel('Millions of $')
plt.grid(True)
plt.show()


# In[24]:


#  Data for 5 years interval for hospitals
years = list(range(1975, 2021, 5))
physicians_expenditure = [1839.9,3287.5,6045.7,9178.8,10615.6,13220.9,18556.6,27403.1,34346.5,39094.5]



# In[35]:


# Bar chart for total health expenditure by use of funds for physicians
plt.figure(figsize=(10, 6))
colors = ['violet', 'red', 'orange', 'yellow' 'green']  # Define the. list of colors
plt.bar(years, physicians_expenditure, color=colors, edgecolor='black')  # Added edgecolor for better visibility
plt.title('Total Health Expenditure for Physicians')
plt.xlabel('Years')
plt.ylabel('Millions of $')
plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')  # Added linestyle and alpha for grid aesthetics
plt.xticks(years)  # Set x-axis ticks to match the years
plt.show()


# In[ ]:





# In[ ]:




