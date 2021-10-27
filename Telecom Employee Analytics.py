#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
pd.set_option('max_columns',1000)
pd.set_option('display.max_rows', None)


# In[ ]:


#Reading excel file
df = pd.read_excel('employee_data.xlsx')


# In[ ]:


#Getting unique ranks 
df[df['Assignment Status']=='ACTIVE'].Grade.unique()


# In[ ]:


#defining years 
years = [2019,2020,2021]


# In[ ]:


#making new columns for better understanding
for year in years: 
    df['start_male.'+str(year)] = ((df['Hire Date'] < pd.Timestamp(year,1,1)) & ((df['Last Working Date'] > pd.Timestamp(year,1,1)) | (df['Last Working Date'].isnull())) & (df['Gender']=='MALE')).astype(int)
    df['end_male.'+str(year)] =   ((df['Hire Date'] < pd.Timestamp(year,12,31)) & ((df['Last Working Date'] > pd.Timestamp(year,12,31)) | (df['Last Working Date'].isnull())) & (df['Gender']=='MALE')).astype(int)
    df['resignation_male.'+str(year)] = ((df['HR Status'] == 'RESIGNATION') & (df['Last Working Date'].dt.year == year)& (df['Gender']=='MALE')).astype(int)
    df['termination_male.'+str(year)] = ((df['HR Status'] == 'TERMINATION') & (df['Last Working Date'].dt.year == year)& (df['Gender']=='MALE')).astype(int)
    df['start_female.'+str(year)] = ((df['Hire Date'] < pd.Timestamp(year,1,1)) & ((df['Last Working Date'] > pd.Timestamp(year,1,1)) | (df['Last Working Date'].isnull())) & (df['Gender']=='FEMALE')).astype(int)
    df['end_female.'+str(year)] =   ((df['Hire Date'] < pd.Timestamp(year,12,31)) & ((df['Last Working Date'] > pd.Timestamp(year,12,31)) | (df['Last Working Date'].isnull())) & (df['Gender']=='FEMALE')).astype(int)
    df['resignation_female.'+str(year)] = ((df['HR Status'] == 'RESIGNATION') & (df['Last Working Date'].dt.year == year)& (df['Gender']=='FEMALE')).astype(int)
    df['termination_female.'+str(year)] = ((df['HR Status'] == 'TERMINATION') & (df['Last Working Date'].dt.year == year)& (df['Gender']=='FEMALE')).astype(int)
   


# In[ ]:


df.columns


# In[ ]:


df['resignation_female.2020'].sum()


# In[ ]:


#Getting part of string
gender_df = df.loc[:,'start_male.2019':]


# In[ ]:


gender_df.head()


# In[ ]:


#reseting index and maing dataframe
year_gender_df = gender_df.sum().reset_index()


# In[ ]:


year_gender_df.head(3)


# In[ ]:


year_gender_df.columns = ['action', 'count']


# In[ ]:


year_gender_df


# In[ ]:


year_gender_df['year'] = year_gender_df['action'].apply(lambda x: x.split('.')[-1])
year_gender_df['gender'] = year_gender_df['action'].apply(lambda x: x.split('.')[0])
year_gender_df['gender'] = year_gender_df['gender'].apply(lambda x: x.split('_')[-1])
year_gender_df


# In[ ]:


year_gender_df


# In[ ]:


#spliting on . and storing in new column
year_gender_df['dimension'] = year_gender_df['action'].apply(lambda x: x.split('.')[-2])


# In[ ]:


year_gender_df


# In[ ]:


#pivoting the data for better visual understaning
pivot_df = pd.pivot(data = year_gender_df, index = 'year', columns = 'dimension',values = 'count')


# In[ ]:


pivot_df

