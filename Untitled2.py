#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


review = pd.read_excel('D:/h2/f1.xlsx')


# In[2]:


review['SA_TIME'] = review['SA_TIME'].map(lambda x: str(x)[:-1])
review


# In[4]:


r_2 = pd.read_excel('D:/h2/f2.xlsx')


# In[5]:


review = review.drop(review.index[0:16])


# In[6]:


review.drop(review[review['SA_ITEM_NO'] == 6269969100051].index, inplace = True)


# In[7]:


r_2.drop(r_2[r_2['SA_ITEM_NO'] == 6269969100051].index, inplace = True)


# In[8]:


review["GN_NAME"] = np.nan


# In[9]:


def products(i,j,k):
    return review.loc[(review.PROD_GROUP == i) & (review.PROD_DEP == j) & (review.PROD_ITEM == k)]


# In[10]:


for k in [2]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 1) & (review.PROD_ITEM == k), 'GN_NAME'] = 'rice'
    
for k in [3, 5, 6, 7, 8, 11, 12]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 1) & (review.PROD_ITEM == k), 'GN_NAME'] = 'beans'
            
for k in [11]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 2) & (review.PROD_ITEM == k), 'GN_NAME'] = 'pasta & vermicelli'
    
for k in [6,4,7,1,5,3,10,14,12]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 2) & (review.PROD_ITEM == k), 'GN_NAME'] = 'grains'
    
for k in [1]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 3) & (review.PROD_ITEM == k), 'GN_NAME'] = 'cooking oil'
    
for k in [2, 3]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 4) & (review.PROD_ITEM == k), 'GN_NAME'] = 'sugar & sugar loaf'
    
for k in [1, 2, 5, 3, 4, 12]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 5) & (review.PROD_ITEM == k), 'GN_NAME'] = 'tea & coffee'
    
review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 6), 'GN_NAME'] = 'meat & fish'
    
review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 7), 'GN_NAME'] = 'dairy'
    
for k in [3, 4]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 8) & (review.PROD_ITEM == k), 'GN_NAME'] = 'canned food'
    
for k in [3, 6, 1]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 9) & (review.PROD_ITEM == k), 'GN_NAME'] = 'jam'
    
review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 10), 'GN_NAME'] = 'soft drinks'
    
review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 11), 'GN_NAME'] = 'herbs & distillates'
    
    
for k in [16, 26]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'pastes'
        
for k in [43]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'pasta & vermicelli'
    
for k in [2, 21, 14, 28]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'pickles'
    
for k in [7, 17, 60, 43, 35, 29, 19, 22, 25, 31, 20, 9]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'spices'
    
for k in [55, 24, 11, 5, 45, 64, 6, 38]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'flavors'
    
for k in [8, 10, 39]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'baking'
    
for k in [23, 36, 37, 32, 58]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 12) & (review.PROD_ITEM == k), 'GN_NAME'] = 'dried vegetable'
    
review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 13), 'GN_NAME'] = 'dried goods'

for k in [38]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 14) & (review.PROD_ITEM == k), 'GN_NAME'] = 'dried goods'
    
for k in [66, 42, 44]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 14) & (review.PROD_ITEM == k), 'GN_NAME'] = 'baking'
    
for k in [6,56,65,12,57,47,20,70,18,17,7,53,15,1,2,5,41,23,3,8,34,29,22]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 14) & (review.PROD_ITEM == k), 'GN_NAME'] = 'biscuits'
    
for k in [31, 69, 59, 28, 26, 72, 62, 39]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 14) & (review.PROD_ITEM == k), 'GN_NAME'] = 'snacks'
    
for k in [51, 43]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 14) & (review.PROD_ITEM == k), 'GN_NAME'] = 'grains'
    
for k in [35, 20, 29]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 15) & (review.PROD_ITEM == k), 'GN_NAME'] = 'breakfast'
    
for k in [36]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 15) & (review.PROD_ITEM == k), 'GN_NAME'] = 'dried goods'
    
for k in [30]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 15) & (review.PROD_ITEM == k), 'GN_NAME'] = 'baking'
    
for k in [33]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 15) & (review.PROD_ITEM == k), 'GN_NAME'] = 'biscuits'
    
for k in [25]:
    review.loc[(review.PROD_GROUP == 1) & (review.PROD_DEP == 15) & (review.PROD_ITEM == k), 'GN_NAME'] = 'snacks'
    


# In[11]:


for k in [16, 11, 2, 55, 65, 37, 19, 13, 52, 49, 45, 14]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 1) & (review.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'
    
for k in [7, 61, 22, 44, 38, 35, 8, 15, 31, 17, 10, 3, 24, 21, 6, 18, 43, 58]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 1) & (review.PROD_ITEM == k), 'GN_NAME'] = 'detergents'
    
for k in [18, 3, 100, 7, 19, 9, 30, 1, 61, 70, 2, 4, 13, 32, 20, 51, 35]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 2) & (review.PROD_ITEM == k), 'GN_NAME'] = 'plastic households '
    
for k in [16, 14, 27, 36, 11, 69, 28, 5, 66, 55, 17, 94, 29, 86]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 2) & (review.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'
    
for k in [79, 99]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 2) & (review.PROD_ITEM == k), 'GN_NAME'] = 'cosmetics'    

for k in [20, 22, 19, 56, 40, 63, 16]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 3) & (review.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'   

for k in [8, 1, 14, 9, 11, 51, 29, 46, 45, 69, 54, 4, 44, 42, 30, 36, 28, 7, 43, 50,10,38,52,13,34,31,3,39]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 3) & (review.PROD_ITEM == k), 'GN_NAME'] = 'cosmetics'
    
for k in [6, 5]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 4) & (review.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'
    
for k in [42, 20, 12, 21, 25, 2, 26, 22, 17, 32, 45, 31, 1, 23, 4]:
    review.loc[(review.PROD_GROUP == 2) & (review.PROD_DEP == 4) & (review.PROD_ITEM == k), 'GN_NAME'] = 'cosmetics'


# In[12]:


review.loc[(review.PROD_GROUP == 3) & (review.PROD_DEP == 2) , 'GN_NAME'] = 'frouit & vegetbles'
review.loc[(review.PROD_GROUP == 3) & (review.PROD_DEP == 1) , 'GN_NAME'] = 'frouit & vegetbles'
review.loc[(review.PROD_GROUP == 3) & (review.PROD_DEP == 7) , 'GN_NAME'] = 'pickles'
review.loc[(review.PROD_GROUP == 3) & (review.PROD_DEP == 14) , 'GN_NAME'] = 'fast foods '


# In[13]:


review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 5), 'GN_NAME'] = 'Kitchen appliances'

for k in [84,22,39,1,106,24,63,129,78,53,82,75,71,123,21,62,57,31,74,69,41,61,34,73,77,46,20,94,119,14,13,93,51,121,114,126,36,106]:
    review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 8) & (review.PROD_ITEM == k), 'GN_NAME'] = 'households'
    
for k in [97,98,25,8,76,50,102,72,26,70,2,6,108,55,35,128,23,40,107,11,28,91,27,55,88,64,48,99,32,60,17,10,66,58,49,45,80,130]:
    review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 8) & (review.PROD_ITEM == k), 'GN_NAME'] = 'Kitchen appliances'
    
for k in [28, 11]:
    review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 4) & (review.PROD_ITEM == k), 'GN_NAME'] = 'electeronics'

review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 1), 'GN_NAME'] = 'home appliances'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 7), 'GN_NAME'] = 'Kitchen appliances'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 6), 'GN_NAME'] = 'Kitchen appliances'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 12), 'GN_NAME'] = 'households'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 9), 'GN_NAME'] = 'Kitchen appliances'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 2), 'GN_NAME'] = 'home appliances'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 18), 'GN_NAME'] = 'Kitchen appliances'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 15), 'GN_NAME'] = 'car spares'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 13), 'GN_NAME'] = 'households'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 21), 'GN_NAME'] = 'car spares'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 19), 'GN_NAME'] = 'households'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 16), 'GN_NAME'] = 'sporty'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 16), 'GN_NAME'] = 'households'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 3), 'GN_NAME'] = 'mobile accessories'
review.loc[(review.PROD_GROUP == 4) & (review.PROD_DEP == 11), 'GN_NAME'] = 'households'



# In[14]:


review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 2), 'GN_NAME'] = 'Stationery'
review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 7), 'GN_NAME'] = 'toy'
review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 5), 'GN_NAME'] = 'toy'
review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 3), 'GN_NAME'] = 'book & CD'
review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 4), 'GN_NAME'] = 'book & CD'
review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 6), 'GN_NAME'] = 'toy'
review.loc[(review.PROD_GROUP == 5) & (review.PROD_DEP == 1), 'GN_NAME'] = 'Stationery'


# In[15]:


review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 5), 'GN_NAME'] = 'bed equipment'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 11), 'GN_NAME'] = 'shoes & textile'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 1), 'GN_NAME'] = 'shoes & textile'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 4), 'GN_NAME'] = 'shoes & textile'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 2), 'GN_NAME'] = 'shoes & textile'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 10), 'GN_NAME'] = 'bag & baggage'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 9), 'GN_NAME'] = 'shoes & textile'
review.loc[(review.PROD_GROUP == 6) & (review.PROD_DEP == 3), 'GN_NAME'] = 'shoes & textile'



# In[16]:


r_2["GN_NAME"] = np.nan


# In[17]:


def products_2(i,j,k):
    return r_2.loc[(r_2.PROD_GROUP == i) & (r_2.PROD_DEP == j) & (r_2.PROD_ITEM == k)]


# In[18]:


for k in [2]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 1) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'rice'
    
for k in [1, 3, 5, 6, 7, 8, 11, 12, 4]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 1) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'beans'
            
for k in [11]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 2) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'pasta & vermicelli'
    
for k in [6,4,7,1,5,3,10,14,12]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 2) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'grains'
    
for k in [1]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 3) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'cooking oil'
    
for k in [2, 3]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 4) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'sugar & sugar loaf'
    
r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 5) , 'GN_NAME'] = 'tea & coffee'
    
r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 6) , 'GN_NAME'] = 'meat & fish'
    
r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 7) , 'GN_NAME'] = 'dairy'
    
for k in [3, 4]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 8) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'canned food'
    
for k in [3, 6, 1]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 9) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'jam'
    
r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 10) , 'GN_NAME'] = 'soft drinks'
    
r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 11) , 'GN_NAME'] = 'herbs & distillates'
    
    
for k in [16, 26]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'pastes'
    
for k in [43]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'pasta & vermicelli'
    
for k in [2, 21, 14, 28]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'pickles'
    
for k in [7, 17, 60, 43, 35, 29, 19, 22, 25, 31, 20, 9]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'spices'
    
for k in [55, 24, 11, 5, 45, 64, 6, 38]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'flavors'
    
for k in [8, 10, 39]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'baking'
    
for k in [23, 36, 37, 32, 58]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 12) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'dried vegetable'
    
for k in [10, 21, 13, 1, 36, 22, 6, 19, 12, 9, 30, 15, 7, 35, 3, 29, 37, 31, 4, 41, 24, 18, 33, 11, 17, 8]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 13) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'dried goods'
    
for k in [66, 42, 44]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 14) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'baking'
    
for k in [6,56,65,12,57,47,20,70,18,17,7,53,15,1,2,5,41,23,3,8,34,29,22]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 14) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'biscuits'
    
for k in [31, 69, 59, 28, 26, 72, 62, 39]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 14) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'snacks'

for k in [51, 43]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 14) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'grains'
    
for k in [35, 20, 29]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 15) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'breakfast'
    
for k in [36]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 15) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'dried goods'
    
for k in [30]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 15) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'baking'
    
for k in [33]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 15) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'biscuits'
    
for k in [25]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 15) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'snacks'
    
for k in [22]:
    r_2.loc[(r_2.PROD_GROUP == 1) & (r_2.PROD_DEP == 15) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'meat & fish'


# In[19]:


for k in [16, 11, 2, 55, 65, 37, 19, 13, 52, 49, 45, 14]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 1) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'
    
for k in [7, 61, 22, 44, 38, 35, 8, 15, 31, 17, 10, 3, 24, 21, 6, 18, 43, 58, 60]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 1) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'detergents'
    
for k in [18, 3, 100, 7, 19, 9, 30, 1, 61, 70, 2, 4, 13, 32, 20, 51, 35]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 2) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'plastic households '
    
for k in [16, 14, 27, 36, 11, 69, 28, 5, 66, 55, 17, 94, 29, 86, 90]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 2) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'
    
for k in [79, 99]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 2) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'cosmetics'    

for k in [20, 22, 19, 56, 40, 63, 16]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 3) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'   

for k in [8, 1, 14, 9, 11, 51, 29, 46, 45, 69, 54, 4, 44, 42, 30, 36, 28, 7, 43, 50,10,38,52,13,34,31,3,39]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 3) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'cosmetics'
    
for k in [6, 5]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 4) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'toiletries'
    
for k in [42, 20, 12, 21, 25, 2, 26, 22, 17, 32, 45, 31, 1, 23, 4, 47]:
    r_2.loc[(r_2.PROD_GROUP == 2) & (r_2.PROD_DEP == 4) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'cosmetics'


# In[20]:


r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 2) , 'GN_NAME'] = 'frouit & vegetbles'
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 1) , 'GN_NAME'] = 'frouit & vegetbles'
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 7) , 'GN_NAME'] = 'pickles'
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 14) , 'GN_NAME'] = 'fast foods '
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 9) , 'GN_NAME'] = 'date '
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 6) , 'GN_NAME'] = 'date '
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 8) , 'GN_NAME'] = 'dried goods'
r_2.loc[(r_2.PROD_GROUP == 3) & (r_2.PROD_DEP == 3) , 'GN_NAME'] = 'meat & fish'


# In[21]:


r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 5), 'GN_NAME'] = 'Kitchen appliances'

for k in [84,22,39,1,106,24,63,129,78,53,82,75,71,123,21,62,57,31,74,69,41,61,34,73,77,46,20,94,119,14,13,93,51,121,114,126,36,106]:
    r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 8) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'households'
    
for k in [43,90,97,98,25,8,76,50,102,72,26,70,2,6,108,55,35,128,23,40,107,11,28,91,27,55,88,64,48,99,32,60,17,10,66,58,49,45,80,130]:
    r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 8) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'Kitchen appliances'
    
for k in [28, 11]:
    r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 4) & (r_2.PROD_ITEM == k), 'GN_NAME'] = 'electeronics'

r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 1), 'GN_NAME'] = 'home appliances'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 7), 'GN_NAME'] = 'Kitchen appliances'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 6), 'GN_NAME'] = 'Kitchen appliances'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 12), 'GN_NAME'] = 'households'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 9), 'GN_NAME'] = 'Kitchen appliances'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 2), 'GN_NAME'] = 'home appliances'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 18), 'GN_NAME'] = 'Kitchen appliances'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 15), 'GN_NAME'] = 'car spares'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 13), 'GN_NAME'] = 'households'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 21), 'GN_NAME'] = 'car spares'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 19), 'GN_NAME'] = 'households'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 16), 'GN_NAME'] = 'sporty'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 16), 'GN_NAME'] = 'households'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 3), 'GN_NAME'] = 'mobile accessories'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 11), 'GN_NAME'] = 'households'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 24), 'GN_NAME'] = 'households'
r_2.loc[(r_2.PROD_GROUP == 4) & (r_2.PROD_DEP == 23), 'GN_NAME'] = 'Kitchen appliances'



# In[22]:


r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 2), 'GN_NAME'] = 'Stationery'
r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 7), 'GN_NAME'] = 'toy'
r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 5), 'GN_NAME'] = 'toy'
r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 3), 'GN_NAME'] = 'book & CD'
r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 4), 'GN_NAME'] = 'book & CD'
r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 6), 'GN_NAME'] = 'toy'
r_2.loc[(r_2.PROD_GROUP == 5) & (r_2.PROD_DEP == 1), 'GN_NAME'] = 'Stationery'


# In[23]:


r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 5), 'GN_NAME'] = 'bed equipment'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 11), 'GN_NAME'] = 'shoes & textile'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 1), 'GN_NAME'] = 'shoes & textile'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 4), 'GN_NAME'] = 'shoes & textile'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 2), 'GN_NAME'] = 'shoes & textile'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 10), 'GN_NAME'] = 'bag & baggage'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 9), 'GN_NAME'] = 'shoes & textile'
r_2.loc[(r_2.PROD_GROUP == 6) & (r_2.PROD_DEP == 3), 'GN_NAME'] = 'shoes & textile'



# In[24]:


sale = pd.concat([review, r_2])


# In[26]:


sale.reset_index(drop = True)


# In[33]:


selected_columns = ['GN_NAME', 'PROD_ITEM', 'SA_UNIT_PR']

# Create a new DataFrame with only the selected columns
selected_df = sale[selected_columns]


# Group the DataFrame by 'GN_NAME' and apply a lambda function to get unique values of 'PROD_ITEM' and corresponding 'SA_UNIT_PR'
unique_values_df = selected_df.groupby('GN_NAME').apply(lambda x: x.drop_duplicates())

# Reset the index of the DataFrame
unique_values_df.reset_index(drop=True, inplace=True)

unique_values_df.to_excel('sش.xlsx', index=False)


# In[40]:


m_1 = review[['SA_FACTOR','GN_NAME']]


# In[31]:


m_1


# In[32]:


m_2 = r_2[['SA_FACTOR','GN_NAME']]


# In[33]:


m_2


# In[34]:


m_1['SA_FACTOR'] = m_1['SA_FACTOR'].astype('int')


# In[41]:


writer = pd.ExcelWriter('m_1.xlsx')


# In[42]:


m_1.to_excel(writer)
writer.save()


# In[100]:


m_1[pd.isnull(m_1.GN_NAME)]


# In[25]:


y = sale.loc[(sale.GN_NAME == 'beans'), 'PROD_NAME']
y.unique()


# In[13]:


y_5 = s.loc[(s.SA_ITEM_NO == 6269685200691)  , 'PROD_NAME']
y_5


# In[47]:


z = s.loc[(s.PROD_GROUP == 6) , 'PROD_DEP']
z.unique()


# In[60]:


y_1 = sale.loc[(sale.PROD_GROUP == 1) & (sale.PROD_DEP == 12)]
y_1.PROD_ITEM.value_counts()


# In[14]:


9794/730


# In[59]:


y_2 = sale.loc[(sale.PROD_GROUP == 1) & (sale.PROD_DEP == 14) & (sale.PROD_ITEM == 3), 'PROD_NAME']
y_2.unique()


# In[24]:


def mean_cat(i,j,k,d):
    return sale.loc[(sale.PROD_GROUP == i) & (sale.PROD_DEP == j) & (sale.PROD_ITEM == k)].PROD_ITEM.value_counts().sum()/d



# In[25]:





# In[55]:


23+74+55+33+12+27+43+43


# In[13]:


s.PROD_NAME.describe()


# In[14]:


y_3 = s.PROD_NAME.value_counts()
y_3


# In[ ]:





# In[ ]:


def measure(i,j):
    return s.loc[(s.PROD_GROUP == i) & (s.PROD_DEP == j)]


# In[27]:


# food group:
# grain
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 1),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 18,16,6
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 2),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 15,18,3

# Edible oils
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 3),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 30,6,6

# sugar
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 4),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 25,22,12

# tea and coffee
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 5),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 17,16,8

# protein products
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 6),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 14,14,6

# dairy 
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 7),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 12,7,7

# Canned foods
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 8),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 10,7,7

# jam
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 9),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 12,7,5

# drinks
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 10),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 32,10,10

# Distillates
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 11),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 20,7,7

# pickles
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 12),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 16,10,6

# herbs
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 13),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 20,14,5

# biscuits
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 14),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 20,7,7

# breakfasts
s.loc[(s.PROD_GROUP == 1) & (s.PROD_DEP == 15),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 26,18,6


# In[29]:


# Detergents
s.loc[(s.PROD_GROUP == 2) & (s.PROD_DEP == 1),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 20,8,5

# toiletry
s.loc[(s.PROD_GROUP == 2) & (s.PROD_DEP == 2),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 12,20,5

# cosmetics
s.loc[(s.PROD_GROUP == 2) & (s.PROD_DEP == 3),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 12,8,5
s.loc[(s.PROD_GROUP == 2) & (s.PROD_DEP == 4),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 10,6,5


# In[30]:


# fruit and vegetables
s.loc[(s.PROD_GROUP == 3) & (s.PROD_DEP == 2),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 14,14,6
s.loc[(s.PROD_GROUP == 3) & (s.PROD_DEP == 1),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 10,20,20

# Meat and poultry 
s.loc[(s.PROD_GROUP == 3) & (s.PROD_DEP == 3),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 14,14,6

# dates
s.loc[(s.PROD_GROUP == 3) & (s.PROD_DEP == 9),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 10,16,7

# processed meat
s.loc[(s.PROD_GROUP == 3) & (s.PROD_DEP == 14),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 10,20,8


# In[31]:


# households
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 8),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 22,33,14
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 5),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 25,10,10
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 7),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 13,13,13
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 6),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 17,17,5
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 13),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 25,25,8
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 18),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 12,37,21
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 9),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 27,17,12

# light group
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 4),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 11,17,6

# major households
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 1),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 30,25,23
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 2),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 42,35,33

# car spares parts
s.loc[(s.PROD_GROUP == 4) & (s.PROD_DEP == 15),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 18,40,10


# In[32]:


# stationary
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 2),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 21,11,5
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 1),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 21,14,2

# CDs
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 4),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 12,14,2

# toys
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 6),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 29,28,8

# books and puzzles
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 3),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 30,22,1

# tools
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 7),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 28,14,14
s.loc[(s.PROD_GROUP == 5) & (s.PROD_DEP == 5),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 28,14,14


# In[33]:


# apparels
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 2),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 22,15,2
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 4),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 22,15,2
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 11),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 22,15,2
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 3),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 22,15,2
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 1),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 22,15,2

# footwear
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 9),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 24,15,5

# Bedding 
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 5),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 16,36,26

# bags and luggage
s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 6),['PROD_HIGHT','PROD_WIDTH','PROD_DEPTH']] = 42,30,10


# In[19]:


y_4 = s.loc[(s.PROD_GROUP == 6) & (s.PROD_DEP == 5) & (s.prod_item == 3)]
y_4.mean()
            


# In[21]:


y_2 = s.loc[(s.prod_group == 1) & (s.prod_cat == 1) & (s.prod_item == 5)]
y_2.prod_name.value_counts().sum()/720


# In[29]:


sale


# In[30]:


def mean_cat(i,j,k,d):
    return sale.loc[(sale.PROD_GROUP == i) & (sale.PROD_DEP == j) & (sale.PROD_ITEM == k)].PROD_ITEM.value_counts().sum()/d



# In[24]:


mean_cat(1,1,5,720)


# In[39]:


s.loc[(s.prod_group == 1)]['prod_cat'].values


# In[ ]:





# In[26]:


d=730
for i in range(1,7):
    for j in set(sale.loc[(sale.PROD_GROUP == i)]['PROD_DEP'].values):
        for k in set(sale.loc[(sale.PROD_GROUP == i)& (sale.PROD_DEP == j)]['PROD_ITEM'].values):
            print('i: ',i,'j: ',j,'k: ',k)
            a=mean_cat(i,j,k,d)
            print(a)


# In[27]:


# define function
def mean_cat(i,k,d):
    return sale.loc[(sale.GN_NAME == i) &  (sale.PROD_ITEM == k)].PROD_ITEM.value_counts().sum()/d

# set value for d
d = 730

# initialize an empty list to store the results
results = []

# loop over i, j, and k and compute the mean
for i in range(1,7):
    for j in set(sale.loc[(sale.PROD_GROUP == i)]['PROD_DEP'].values):
        for k in set(sale.loc[(sale.PROD_GROUP == i)& (sale.PROD_DEP == j)]['PROD_ITEM'].values):
            # compute the mean
            mean_value = mean_cat(i, j, k, d)
            # append the result to the list
            results.append((i, j, k, mean_value))

# create a pandas dataframe from the results
df = pd.DataFrame(results, columns=['PROD_GROUP', 'PROD_DEP', 'PROD_ITEM', 'mean_value'])

# round the mean_value column to two decimal places
df['mean_value'] = df['mean_value'].round(2)

# save the dataframe to an Excel file
df.to_excel('output.xlsx', index=False)


# In[30]:


# define function
def mean_cat(i,k,d):
    return sale.loc[(sale.GN_NAME == i) & (sale.PROD_ITEM == k)].PROD_ITEM.value_counts().sum()/d

# set value for d
d = 730

# initialize an empty list to store the results
results = []

# loop over i and k and compute the mean
for i in set(sale['GN_NAME'].values):
    for k in set(sale.loc[sale.GN_NAME == i]['PROD_ITEM'].values):
        # compute the mean
        mean_value = mean_cat(i, k, d)
        # append the result to the list
        results.append((i, k, mean_value))

# create a pandas dataframe from the results
df = pd.DataFrame(results, columns=['GN_NAME', 'PROD_ITEM', 'mean_value'])

# round the mean_value column to two decimal places
df['mean_value'] = df['mean_value'].round(2)

# save the dataframe to an Excel file
df.to_excel('c_rate.xlsx', index=False)


# In[29]:


s['prod_cat'].values


# In[48]:


.27777777*720


# In[6]:


o = set(range(1,11))


# In[ ]:




