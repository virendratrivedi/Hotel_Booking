#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# ### Loading the dataset 

# In[2]:


df=pd.read_csv('hotel_booking.csv')


# ### Exploratory Data Analysis and Data Cleaning

# In[3]:


df.sample(8)


# In[4]:


df.shape


# In[5]:


df.columns


# ## Drop Personal Information column

# In[6]:


df=df.drop(['name', 'email','phone-number','credit_card'], axis=1)


# In[7]:


df.info()


# In[8]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[9]:


df.describe(include='object')


# In[10]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*60)


# In[11]:


df.isnull().sum()


# In[12]:


df=df.drop(['company', 'agent'], axis=1)


# In[13]:


df.dropna(inplace=True)


# In[14]:


df.isnull().sum()


# In[15]:


df.describe()


# In[16]:


df['adr'].plot(kind='box')  ## Outlier 


# In[17]:


df=df[df['adr']<5000]


# ### Data Analysis and Visualizations

# In[18]:


cancelled_per = df['is_canceled'].value_counts(normalize=True)
cancelled_per


# In[19]:


plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not Cancel','cencel'],df['is_canceled'].value_counts(),width=0.7)


# In[20]:


plt.figure(figsize=(10,8))
ax1=sns.countplot(data=df,x='hotel',hue='is_canceled',)
plt.xlabel('Hotel')
plt.title('Resrvation stats in different hotel',size=20)
plt.ylabel('Number of Reservation')


# In[21]:


resort_hotel = df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[22]:


city_hotel = df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[23]:


df.columns


# In[24]:


resort_hotel=resort_hotel.groupby('reservation_status_date')['adr'].mean()
city_hotel=city_hotel.groupby('reservation_status_date')['adr'].mean()


# In[25]:


plt.figure(figsize=(20,8))
plt.title('average daily rate in City and Resort hotel',size=30)
plt.plot(resort_hotel.index,resort_hotel.values,label='Resort Hotel')
plt.plot(city_hotel.index,city_hotel.values,label='City Hotel')
plt.legend(fontsize=20)


# In[26]:


df['months']=df['reservation_status_date'].dt.month
plt.figure(figsize=(15,7))
ax1 = sns.countplot(data=df,x='months',hue='is_canceled')
plt.legend(['not cencel','cencel'])
plt.ylabel('Number of Resevation')
plt.title('Reservation staus per month',size=25)


# ### Plot average daily rate fo reach month

# In[27]:


plt.figure(figsize=(15,7))
plt.title('ADR per month',size=25)
sns.barplot('months','adr',data=df[df['is_canceled']==1].groupby('months')[['adr']].sum().reset_index())

plt.show()


# In[28]:



df.columns


# In[35]:


df.head(2)


# ### Country Basis 

# In[29]:


canceled_data=df[df['is_canceled']==1]
top_10_country=canceled_data['country'].value_counts()[:10]


# In[30]:


plt.figure(figsize=(15,7))
plt.title('Tope 10 Country with reservation cencel')
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()


# In[31]:


top_10_country.index


# In[32]:


df['market_segment'].value_counts()


# In[33]:


df['market_segment'].value_counts(normalize=True)*100


# In[34]:


canceled_data['market_segment'].value_counts(normalize=True)*100


# ### Which price is high cancel or non cancel 

# In[50]:


canceled_df_adr=canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace=True)
canceled_df_adr.sort_values('reservation_status_date',inplace=True)

not_canceled_data=df[df['is_canceled']==0]
not_canceled_df_adr=not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace=True)
not_canceled_df_adr.sort_values('reservation_status_date',inplace=True)


# In[56]:


plt.figure(figsize=(20,6))
plt.title('Average Daily Rate',size=30)
plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'],label='not cancelled')
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'],label='cancelled')
plt.legend()


# In[57]:


canceled_df_adr=canceled_df_adr[(canceled_df_adr['reservation_status_date']>'2016') & (canceled_df_adr['reservation_status_date']<'2017-09')]
not_canceled_df_adr=not_canceled_df_adr[(not_canceled_df_adr['reservation_status_date']>'2016') & (not_canceled_df_adr['reservation_status_date']<'2017-09')]


# In[58]:


plt.figure(figsize=(20,6))
plt.title('Average Daily Rate',size=30)
plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'],label='not cancelled')
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'],label='cancelled')
plt.legend()


# In[ ]:




