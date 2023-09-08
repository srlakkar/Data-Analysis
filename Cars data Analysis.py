#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ## Importing Data from Downloaded CSV File

# In[9]:


cars = pd.read_csv("/Users/srlakkar/Desktop/file.csv")
cars.head(3)


# ## Importing Data from Url directly

# In[27]:


url = "https://dz8fbjd9gwp2s.cloudfront.net/digital_products/64cb5694e4b000cf748a30c0/64d7b801fd6efd7c4587e23a/asset/1691859042457/file.csv"
cars2 = pd.read_csv(url)
cars2.head(3)


# In[28]:


cars2.shape


# ## Finding Null values in the data set. If i find any, fill the data with the mean value

# In[30]:


cars2.dropna()


# In[32]:


cars2.isnull().sum()


# In[33]:


cars2['Cylinders'] = cars2['Cylinders'].fillna(cars2['Cylinders'].mean())


# In[34]:


cars2.isnull().sum()


# ## Find Different Makes in the Data Set and occurence of each

# In[35]:


cars2.head()


# In[36]:


cars2['Make'].value_counts()


# ## Show all records where Origin is Asia or Europe

# In[39]:


cars2["Origin"].value_counts()


# In[42]:


cars2[cars2["Origin"].isin(["Asia","Europe"])]


# ## Remove records where weight > 4000

# In[43]:


cars2.head()


# In[44]:


cars2[cars2["Weight"] > 4000]


# In[45]:


cars2[~(cars2["Weight"] > 4000)]


# ## Increase all values of MPG City by 3, Apply function

# In[46]:


cars2.head()


# In[48]:


cars2["MPG_City"] = cars2["MPG_City"].apply(lambda x:x+3)


# In[49]:


cars2.head()


# In[ ]:




