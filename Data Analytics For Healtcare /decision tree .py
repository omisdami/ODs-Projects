#!/usr/bin/env python
# coding: utf-8

# In[18]:


from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
X,y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

tree.plot_tree(clf)
[...]


# In[13]:


import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree 

X, y = load_iris(return_X_y=True)

#Create an instance for the model 
clf = DecisionTreeClassifier(max_depth =5)

#Train the model on the data 
clf.fit(X,y)

fn=['sepal length(cm)', 'sepal width(cm)', 'petal lenth(cm)', 'petal width(cm)']
cn=['setosa', 'versicolor', 'virginca']

#set the api = 300 TO MAKE THE IMAGE CLEANER THAN THE DEFAULT

fig,axes= plt.subplots(nrows=1, ncols=1, figsize=(4,4), dpi=300)

tree.plot_tree(clf,
               feature_names = fn, 
               class_names = cn,
               filled = True);
               


# In[ ]:




