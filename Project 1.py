#!/usr/bin/env python
# coding: utf-8

# In[1]:


name=input('Enter Name of Student:')
std=input('Enter Standard:')
div=input('Enter Divion:')
rollno=int(input('Enter Roll No:'))


# Subject Marks Out of 100

# In[2]:


math=int(input('Enter Maths Marks:'))
science=int(input('Enter Science Marks:'))
Eng=int(input('Enter English Marks:'))


# # Percentage Scored

# In[3]:


percent=float(((math+science+Eng)/300)*100)
print(percent)


#  Displaying All Details

# In[4]:


print("Name:",name +'\n'+'Standard:',std + '\n'+ 'Division:',div + '\n' + 'Roll No.:',rollno )
print("Maths Marks:",str(math) + '\n'+ "Science marks:",str(science) +'\n'+"English Marks:",str(Eng) )
print("Percentage Scored:",str(percent)  + ' %')


# In[ ]:




