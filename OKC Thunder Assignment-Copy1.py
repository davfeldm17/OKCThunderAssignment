#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd
import numpy as np
import math


# In[101]:


shots_data=pd.read_csv('shots_data.csv')
shots_data


# In[102]:


shots_data['2PT']=np.where(((np.abs(shots_data['x'])<=22) & (shots_data['y']<=7.8) |
                            ((shots_data['y']>7.8)&(np.sqrt(shots_data['x']**2 + shots_data['y']**2)<=23.75))),1,0)
shots_data['NC3']=np.where((shots_data['y']>7.8) & (np.sqrt(shots_data['x']**2 + shots_data['y']**2)>23.75),1,0)
shots_data['C3']=np.where((shots_data['y']<=7.8) & (np.abs(shots_data['x'])>22),1,0)
shots_data


# In[103]:


shots_data['2PTmakeA']=np.where((shots_data['team']=='Team A')&(shots_data['fgmade']==1)&(shots_data['2PT']),1,0)
shots_data['NC3makeA']=np.where((shots_data['team']=='Team A')&(shots_data['fgmade']==1)&(shots_data['NC3']),1,0)
shots_data['C3makeA']=np.where((shots_data['team']=='Team A')&(shots_data['fgmade']==1)&(shots_data['C3']),1,0)
shots_data['2PTmakeB']=np.where((shots_data['team']=='Team B')&(shots_data['fgmade']==1)&(shots_data['2PT']),1,0)
shots_data['NC3makeB']=np.where((shots_data['team']=='Team B')&(shots_data['fgmade']==1)&(shots_data['NC3']),1,0)
shots_data['C3makeB']=np.where((shots_data['team']=='Team B')&(shots_data['fgmade']==1)&(shots_data['C3']),1,0)
shots_data


# In[104]:


shots_data['team'].value_counts()


# In[105]:


percent_stats=shots_data.groupby(['team'])['fgmade','2PT','NC3','C3','2PTmakeA','NC3makeA','C3makeA',
                                           '2PTmakeB','NC3makeB','C3makeB'].sum().reset_index()
percent_stats['FGA']=percent_stats['2PT']+percent_stats['NC3']+percent_stats['C3']
percent_stats


# In[106]:


percent_stats['2PTshot%']=(percent_stats['2PT'])/percent_stats['FGA']
percent_stats['NC3shot%']=(percent_stats['NC3'])/percent_stats['FGA']
percent_stats['C3shot%']=(percent_stats['C3'])/percent_stats['FGA']
percent_stats


# In[107]:


percent_stats['2PTeFG%']=(percent_stats['2PTmakeA']+percent_stats['2PTmakeB'])/percent_stats['2PT']
percent_stats['NC3eFG%']=1.5*(percent_stats['NC3makeA']+percent_stats['NC3makeB'])/percent_stats['NC3']
percent_stats['C3eFG%']=1.5*(percent_stats['C3makeA']+percent_stats['C3makeB'])/percent_stats['C3']
percent_stats


# In[108]:


percent_stats=percent_stats[['team','2PTshot%','NC3shot%','C3shot%','2PTeFG%','NC3eFG%','C3eFG%']]
percent_stats


# In[ ]:





# In[ ]:




