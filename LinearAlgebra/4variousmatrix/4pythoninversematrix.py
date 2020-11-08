#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np


# In[44]:


a = [input().split() for i in range(2)]
a = np.array(a)
print(a)


# In[45]:


a = a.astype(np.float64)
print(np.linalg.det(a))
if np.linalg.det(a) != 0:
    print(np.linalg.inv(a))
else:
    print("No exist")


# In[ ]:




