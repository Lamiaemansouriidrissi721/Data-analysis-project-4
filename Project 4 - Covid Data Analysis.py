#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd 


# In[40]:


import matplotlib.pyplot as plt 


# In[41]:


import seaborn as sns 


# In[42]:


data=pd.read_csv(r"C:\Users\kumak\Desktop\selfstudy\Python\Dataset  Project 4 - Covid Data Analysis.csv")
data


# In[43]:


#before jumping to  work its imoportant to delete  the null values.


# In[44]:


data.dtypes #3 object values and two int , like the previous codes iwill have to addin the code the type of this coloumns


# In[45]:


data.isnull().sum() #it seems like only state coloumn thqt hqve  181 null value i whether have choice to aplly it for all or just that specific couloumn


# In[46]:


object_columns = data.select_dtypes(include=['object','float64']).columns
data[object_columns] = data[object_columns].fillna('Unknown')


# In[47]:


data.isnull().sum() #it seems liken the data is all clean now


# In[48]:


sns.heatmap(data.isnull())
plt.show


# In[49]:


#Q. 1) Show the number of Confirmed, Deaths and Recovered cases in each Region.


# In[50]:


data


# In[51]:


#its about extracting  3 coloumns:
grouped = data.groupby('Region').agg({'Confirmed': 'sum', 'Deaths': 'sum','Recovered':'sum'})
grouped


# In[ ]:


#data.groupby('Region')['Confirmed','Recovered'].sum().sort_values()
#data.groupby('Region')['Confirmed','Recovered'].sum()


# In[52]:


#Q. 2) Remove all the records where the Confirmed Cases is Less Than 10.


# In[55]:


filtered_data = data[data['Confirmed'] >= 10]

filtered_data 


# In[ ]:


#Q. 3) In which Region, maximum number of Confirmed cases were recorded ?


# In[58]:


grouped = data.groupby('Region').agg({'Confirmed': 'max'})
grouped
grouped.sort_values(by='Confirmed', ascending=False)


# In[60]:


region_with_max_confirmed = grouped['Confirmed'].idxmax()
region_with_max_confirmed 


# In[70]:


data.groupby('Region').agg({'Deaths': 'min'}).sort_values(by='Deaths', ascending=False)


# In[ ]:


#Q. 5) How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020 ?


# In[75]:


india_data = data[(data['Date'] <= '4/29/2020') & (data['Region'] == 'India')].agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
})
india_data 


# In[ ]:


#Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order.


# In[88]:


data.sort_values(by='Confirmed',ascending=True)


# In[101]:


#Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.*
data.sort_values(by='Recovered',ascending=False)


# In[ ]:


#  visualise the number of death by region in a line plot


# In[107]:


x=data['Region']
y=data['Deaths']
# Create a line plot
plt.figure(figsize=(30,10))
plt.plot(x , y, marker='o')

# Adding titles and labels
plt.title('Number of Deaths by Region')
plt.xlabel('Regions')
plt.ylabel('Number of Deaths')

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show() #the vis is absolutely not readable hence its better to see slice by slice


# In[116]:


# Filtering data for Germany and Netherlands
filtered_data = data[data['Region'].isin(['Germany', 'Netherlands'])]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Region'], filtered_data['Deaths'], marker='o')

# Adding titles and labels
plt.title('Number of Deaths in Germany and Netherlands')
plt.xlabel('Region')
plt.ylabel('Number of Deaths')

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
#iwant to filter it by date but this data seems to caputre only the season of april 29 .2020


# In[ ]:


# it would be ebtter if i focus on one region like US and compare the number confirmed vs recovered


# In[131]:


#FIRST STEP is to extrac the data :
# Filtering data for the 'US' region
us_data = data[data['Region'] == 'US']

# Extracting confirmed and recovered values
confirmed_cases = us_data['Confirmed'].sum()


confirmed_cases


# In[132]:


recovered_cases = us_data['Recovered'].sum()
recovered_cases


# In[135]:


# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(['Confirmed', 'Recovered'], [confirmed_cases, recovered_cases], color=['blue', 'green'])

# Adding titles and labels
plt.title('Confirmed vs Recovered Cases in the US')
plt.ylabel('Number of Cases')

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:


# its seems like they have lots of confirmed cases than the recovered  


# In[139]:


us_data = data[data['Region'] == 'Canada']

# Extracting confirmed and recovered values
confirmed_c = us_data['Confirmed'].sum()


confirmed_c


# In[137]:


Recovered_c = us_data['Recovered'].sum()
Recovered_c 


# In[144]:


# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(['Confirmed (US)', 'Recovered (US)', 'Confirmed (Canada)', 'Recovered (Canada)'],
        [confirmed_cases, recovered_cases, confirmed_c, Recovered_c],
        color=['blue', 'green', 'blue', 'green'])

# Adding titles and labels
plt.title('Confirmed vs Recovered Cases in the US and Canada')
plt.ylabel('Number of Cases')

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()


# In[147]:


# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(['Confirmed (US)', 'Recovered (US)', 'Confirmed (Canada)', 'Recovered (Canada)'],
         [confirmed_cases, recovered_cases, confirmed_c, Recovered_c],
         marker='o')

# Adding titles and labels
plt.title('Confirmed vs Recovered Cases in the US and Canada')
plt.xlabel('Cases')
plt.ylabel('Number of Cases')

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()



# In[ ]:




