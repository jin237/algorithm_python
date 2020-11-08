#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np


# In[50]:


v = list()
w = list()


# In[51]:


for i in range(3):
    vbec = int(input())
    v.append(vbec)
for i in range(3):
    wbec = int(input())
    w.append(wbec)


# In[52]:


print(v)
print(w)


# In[53]:


v = np.array(v)
w = np.array(w)


# In[54]:


print(np.dot(v, w))


# In[56]:


print(np.sum(v*w))


# In[64]:


import math
normv = math.sqrt(np.dot(v, v))
print(normv)
print("√",np.dot(v, v))


# In[58]:


print(u)


# In[ ]:


print("%d/%d,%d/%d,%d/%d". v(1),np.dot(v,v)v(2),v(3))

