#!/usr/bin/env python
# coding: utf-8

# In[8]:


for i in range(1,4):
   print(i)


# In[9]:


for i in range(1,4):
    print(i+100)


# In[10]:


a = []
for i in [1,2,3]:
    a.append(i)
    print(i)


# In[11]:


print(a)


# In[1]:


b = [i+1 for i in [1,2,3]]


# In[2]:


b


# In[3]:


def calcul(i):
    c = i*2*3+i
    return c


# In[4]:


b = [calcul(i) for i in [1,2,3]]


# In[5]:


b


# In[6]:


[i+1 for i in [1,2,3] if i%2==0]


# In[8]:


a = [ ]
for i in [1,2,3]:
    if i%2==0 : 
        a.append(i+1)


# In[9]:


a


# In[10]:


number_list = [number for number in range(1,6)]    


# In[11]:


number_list


# In[12]:


number_list = [number-1 for number in range(1,6)]    


# In[13]:


number_list


# In[14]:


a_list = [number for number in range(1,6) if number % 2 == 1]


# In[15]:


a


# In[16]:


sentence = ['I','Love','Python','Soooo','Much!!!!']


# In[17]:


[word.lower() for word in sentence]


# In[20]:


[word for word in sentence if len(word) <6]

word.upper()
# In[21]:


word = python


# In[22]:


word = 'python'


# In[23]:


word.upper


# In[24]:


word.upper()


# In[25]:


word.lower()


# In[26]:


sentence


# In[27]:


sentence.upper()


# In[28]:


[word.upper() for word in sentence]


# In[29]:


[(x, x**2,x**3) for x in range(10)]


# In[34]:


rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row,col)


# In[41]:


rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
       print (cell)


# In[42]:


[(i,j) for i in range(5) for j in range(i)]


# In[43]:


word = 'letter'


# In[45]:


word.upper()


# In[47]:


word.count('e')

word.len
# In[50]:


len(word)


# In[51]:


letter_counts = {letter : word.count(letter) for letter in word}


# In[52]:


word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}


# In[54]:


letter_counts


# In[55]:


set('letters')


# In[56]:


word


# In[57]:


set(word)


# In[58]:


word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)}


# In[59]:


letter_counts


# In[63]:


days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts): 
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)


# In[64]:


import math


# In[65]:


math.sqrt(16)


# In[67]:


pip install scikit-learn


# In[1]:


get_ipython().system(' pip3 intall numpy')


# In[2]:


get_ipython().system(' pip3 install numpy')


# In[1]:


get_ipython().system(' pip3 install pandas')


# In[2]:


get_ipython().system(' pip3 install seaborn')


# In[3]:


get_ipython().system(' pip3 install matplotlib')


# In[4]:


get_ipython().system(' pip3 install scipy')


# In[5]:


get_ipython().system(' pip3 install scikit-learn')


# In[6]:


import numpy as np


# In[7]:


a = np.array([1,2])


# In[8]:


a


# In[9]:


a = 1
b = 1

c = a+b

print(c)


# In[10]:


def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) !=type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a,b)
    return result
if __name__== "__main__" :
    print(safe_sum('a',1))
    print(safe_sum(1,1))
    print(sum(10,1.45))


# In[ ]:




