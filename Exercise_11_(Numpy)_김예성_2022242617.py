#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip3')


# In[3]:


get_ipython().system(' pip3 install numpy')


# In[4]:


import numpy as np


# In[5]:


a = np.arange(6)


# In[6]:


type(a)


# In[7]:


a


# In[8]:


a2 = a[np.newaxis, :]


# In[9]:


a[:]


# In[10]:


a2 = a[np.newaxis, :]


# In[11]:


a2


# In[12]:


a2.shape


# In[13]:


a.shape


# In[14]:


a = []


# In[15]:


a = [0,1,2,3,4,5]


# In[16]:


a


# In[17]:


a[0]


# In[18]:


a[3]


# In[19]:


a[1]


# In[20]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[21]:


print(a[0])


# In[22]:


a


# In[23]:


a[0,1]


# In[24]:


a[1]


# In[25]:


a[2]


# In[26]:


a[0]


# In[27]:


[[0., 0., 0.],
 [1., 1., 1.]]


# In[28]:


import numpy as np
a = np.array([1,2,3])


# In[29]:


a = np.array([1,2,3])


# In[30]:


a


# In[31]:


a


# In[32]:


np.zeros(2)


# In[33]:


np.zeros(10)


# In[34]:


np.ones(10)


# In[35]:


np.empty(2)


# In[36]:


np.arange(2,9,2)


# In[37]:


np.arange(2,8,2)


# In[38]:


np.arange(2,99,2)


# In[39]:


np.linspace(0,10, num=5)


# In[40]:


x = np.ones(2, dtype=np.int64)


# In[41]:


x


# In[42]:


type(x)


# In[43]:


type(a)


# In[44]:


arr = np.array([2,1,5,3,7,4,6,8])


# In[45]:


arr


# In[46]:


arr


# In[47]:


np.sort(arr)


# In[48]:


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])


# In[49]:


np.concatenate((a,b)) #데이터를 합치고 싶을때 사용


# In[50]:


x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])


# In[51]:


np.concatenate((x,y),axis=0)


# In[52]:


array_example = np.array([[[0,1,2,3],
                         [4,5,6,7]],
                        
                        [[0,1,2,3],
                         [4,5,6,7]],
                         
                         [[0,1,2,3],
                         [4,5,6,7]]])


# In[53]:


array_example.ndim


# In[54]:


array_example.size


# In[55]:


array_example.shape


# In[57]:


print(a)


# In[61]:


data = np.array([1,2])
ones = np.ones(2,dtype = int)
data + ones


# In[62]:


data - ones


# In[63]:


data * data


# In[64]:


data / data


# In[65]:


a = np.array([1,2,3,4])
a.sum()


# In[67]:


b = np.array([[1,1],[2,2]])


# In[68]:


b.sum(axis=0)


# In[69]:


b.sum(axis=1)


# In[70]:


data = np.array([1.0,2.0])
data * 1.6


# In[72]:


data.max()


# In[73]:


data.min()


# In[74]:


data.sum()


# In[75]:


a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])


# In[76]:


a.sum()


# In[77]:


a.min()


# In[78]:


a.min(axis=0)


# In[79]:


data = np.array([[1,2],[3,4],[5,6]])
data


# In[80]:


data[0,1]


# In[81]:


data[1:3]


# In[82]:


data[0:2,0]


# In[83]:


data.max()


# In[84]:


data.min()


# In[85]:


data.sum()


# In[86]:


data = np.array([[1,2],[5,3],[4,6]])
data


# In[87]:


data.max(axis=0)


# In[88]:


data.max(axis=1)


# In[89]:


data = np.array([[1,2],[3,4]])
ones = np.array([[1,1],[1,1]])
data+ones


# In[90]:


data = np.array([[1,2],[3,4],[5,6]])
ones_row = np.array([[1,1]])
data+ones_row


# In[92]:


np.ones((4,3,2))


# In[93]:


np.ones(3)


# In[94]:


np.zeros(3)


# In[98]:


rng = np.random.default_rng()
rng.random(3)


# In[99]:


np.ones((3,2))


# In[100]:


np.zeros((3,2))


# In[101]:


rng.random((3,2))


# In[102]:


rng.integers(5, size = (2,4))


# In[103]:


a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])


# In[104]:


unique_values = np.unique(a) #중복되는거는 빼고 보여달라
print(unique_values)


# In[105]:


a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])


# In[106]:


unique_values = np.unique(a_2d)
print(unique_values)


# In[107]:


unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)


# In[108]:


unique_rows, indices, occurrence_count = np.unique(
     a_2d, axis=0, return_counts=True, return_index=True)
print(unique_rows)


# In[109]:


print(indices)


# In[110]:


print(occurrence_count)


# In[111]:


data.reshape(2,3)


# In[114]:


data.reshape(3,2)


# In[116]:


arr = np.arange(6).reshape((2,3))
arr


# In[117]:


arr.transpose()


# In[118]:


arr.T


# In[119]:


arr = np.array([1,2,3,4,5,6,7,8])


# In[120]:


reversed_arr = np.flip(arr)


# In[121]:


print('Reversed Array:' , reversed_arr)


# In[122]:


arr_2d = np.array([[1,2,3,4,], [5,6,7,8],[9,10,11,12]])


# In[123]:


reversed_arr = np.flip(arr_2d)
print(reversed_arr)


# In[124]:


reversed_arr_colums = np.flip(arr_2d, axis=1)
print(reversed_arr_colums)


# In[125]:


arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)


# In[126]:


arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)


# In[127]:


x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[128]:


x.flatten()


# In[129]:


a1 = x.flatten()
a1[0] = 99
print(x)


# In[130]:


print(a1)


# In[131]:


a2 = x.ravel()
a2[0] = 98
print(x)


# In[132]:


print(a2)


# In[ ]:




