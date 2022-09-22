#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[19]:


data=np.loadtxt('E:\IITK RESOURSES\COMPUTATIONAL TOOLS FOR TE\XTRA\Assignment\ques1_data.txt',delimiter=',')
print(data[:5])


# In[26]:


n_sites=len(data)
n_sites


# In[35]:


total_yearly_traffic=np.sum(data,axis=1)
total_yearly_traffic
MAT=total_yearly_traffic/12
print(MAT[:5])


# In[41]:


max_index=total_yearly_traffic.argmax()
max_index


# In[43]:


min_index=total_yearly_traffic.argmin()
min_index


# In[45]:


max_value=total_yearly_traffic.max()
max_value


# In[46]:


min_value=total_yearly_traffic.min()
min_value


# In[52]:


traffic_volume=np.sum(data,axis=0)
print(traffic_volume)


# In[55]:


max_month_index=traffic_volume.argmax()
max_month_index


# In[56]:


min_month_index=traffic_volume.argmin()
min_month_index


# In[59]:


required_site_index=np.argwhere(total_yearly_traffic>9700)
required_site_index


# In[60]:


required_month_index=np.argwhere(traffic_volume>38000)
required_month_index


# # second

# In[62]:


import numpy as np


# In[63]:


text="Neeraj Chopra brings home the much awaited Gold First place medal for Flag of India in his debut Olympic Games. The gigantic effort made sure India has best ever medal haul in the olympics. Congratulations champ Neeraj Chopra, the whole nation is proud of you"
print(text)


# In[67]:


part_by_part=text.split()
part_by_part


# In[71]:


words_counts=len(part_by_part)
words_counts


# In[74]:


type(part_by_part)


# In[79]:


unique_word_count=len(set(part_by_part))
unique_word_count


# # complete

# In[ ]:




