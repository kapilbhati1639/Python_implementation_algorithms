#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


def slowfib(n):
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowfib(n-1)+slowfib(n-2)

    
    


# In[10]:


slowfib(25)


# In[31]:


def fastfib(n):
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 1
        b = 0
        for i in range(2,n+1):
            t = a 
            a = a+b
            b = t
    return a
        
        


# In[43]:


n = 37
slowfib(n)


# In[44]:


fastfib(n)

