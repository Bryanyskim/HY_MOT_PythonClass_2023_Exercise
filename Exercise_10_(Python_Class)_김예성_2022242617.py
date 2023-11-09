#!/usr/bin/env python
# coding: utf-8

# In[24]:


result1 = 0
result2 = 0 


# In[25]:


def adder1(num):
    global result1
    result1 += num
    return result1


# In[26]:


def adder2(num):
    global result2
    result2 += num
    return result2


# In[27]:


adder1(3)


# In[28]:


adder1(4)


# In[29]:


adder2(5)


# In[30]:


adder2(3)


# In[33]:


class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


# In[34]:


cal2.adder(110)


# In[1]:


class Service : 
    secret = "지구는 40006년에 멸망한다."


# In[2]:


s = Service()


# In[3]:


s. secret


# In[4]:


s2 = Service()


# In[5]:


s2.secret


# In[6]:


Service.secret


# In[8]:


#class의 기능을 담당하는 함수는 매서드라고 한다. 


# In[48]:


class Service : 
    secret = "지구는 40006년에 멸망한다."
    
    def __init__(self,name):
        self.name = name
    
    def sum(self, a,b):
        result = a+b
        print("%s님 %s + %s = %s입니다" %(self.name, a, b, result))


# In[54]:


an = Service("셀리")


# In[55]:


#매서드는 첫번째는 self로 자기 자신을 넘기는 것이다. 자기 자신을 넘기는 것으로 이해할 수 있도록 한다. 의미를 찾아서 써 주는 것이 가독성을 높힌다. 


# In[56]:


an.sum(1,1)


# In[57]:


an = Service("박달도사")


# In[59]:


an.sum(1,1)


# In[60]:


class FourCal: 
    pass


# In[61]:


a = FourCal()


# In[63]:


print(type(a))


# In[113]:


class FourCal: 
    
    def setdata(self, first,second):
        self.first = first
        self.second = second
        
    def sum(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


# In[114]:


a = FourCal()


# In[115]:


a.setdata(4,2)


# In[116]:


a.first


# In[117]:


a.second


# In[118]:


print(a.sum())


# In[119]:


a.mul()


# In[120]:


a.sub()


# In[121]:


a.div()


# In[ ]:





# In[ ]:




