#!/usr/bin/env python
# coding: utf-8

# # Seaborn Notebook
# 
# I am using seaborn because it is a package that is not included in requirements.txt

# In[1]:


import seaborn as sns


# In[2]:


iris = sns.load_dataset("iris")


# In[3]:


sns.displot(data = iris, x = "sepal_length")


# ### Seaborn is cool, as well as the iris dataset
#  
# That is all folks.

# In[ ]:




