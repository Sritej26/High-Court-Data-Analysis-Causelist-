import pandas as pd
import os
import seaborn as sns
import numpy as np
import datetime
from datetime import timedelta
import re
import matplotlib.pyplot as plt

os.chdir("C:/Users/Sritej. N/Downloads")
stats=pd.read_csv("jaipur2.csv")

y=stats['DATE'].values
stats=stats.drop(stats.columns[8],axis=1)
stats['NUM_TYPE']=stats[['CASE_TYPE','CASE_NO']].agg('-'.join,axis=1)
x1=stats['NUM_TYPE'].values
c=0
dates=[]
Dict={}
for i in x1:
    p=[]
    Dict[i] = p
    

for i in range(len(x1)):
    Dict[x1[i]].append(y[i])
        
datetimeFormat='%Y_%m_%d'    
s=0
Dict1={}
diff={}
t=0
for i,j in Dict.items():  
       t+=len(j)
    
    
for i,j in Dict.items():
    Dict1[i] = np.sort(j)

t=0

# =============================================================================
# ind=[]
# l='ek'
# for i in y:   
#     i=str(i)
#     result = i.startswith("HON'BLE")
#     if(result==True):
#         ind.append(t)
#     t+=1
# 
# =============================================================================



for i,j in Dict1.items():
    list=[]
    if(len(j)>1):
        for k in range(len(j)-1):
            list.append(datetime.datetime.strptime(Dict1[i][k+1],datetimeFormat).date()-datetime.datetime.strptime(Dict1[i][k],datetimeFormat).date())
            diff[i]=list    


for i,j in diff.items():
    if(len(j)==0):
        t+=1

t1=0
for i,j in Dict1.items():
    if(len(j)==1):
        t1+=1


        
#types1 = [type(k) for k in diff.keys()]

diff1={}
for i,j in diff.items():
    list1=[]
    for k in range(len(j)):
        list1.append(j[k].days)
    diff1[i]=list1

diff2={}
for i,j in diff1.items():
    count1=0
    for k in j:
        count1=count1+k
    diff2[i]=count1/len(j)
 
x=stats["CASE_TYPE"].value_counts()
x.plot()

ct=stats["CASE_TYPE"].unique()
avg={}
for i in ct:
    list3=[]
    for j,k in diff2.items():
        result=j.startswith(i)
        if(result==True):
            list3.append(k)
    avg[i]=list3
            
avg1={}
avgofavg=[]
for i,j in avg.items():
    count2=0
    if(len(j)>0):
        for k in j:
            count2=count2+k
        avg1[i]=count2/len(j) 
        avgofavg.append(count2/len(j) )
  
aog=np.sort(avgofavg)
aag = np.sort(aog)[::-1]

plt.plot(aag)
    
   
stats['COURTROOM'].value_counts().plot('bar')
# plt.scatter(stats['COURTROOM'],stats['CASE_TYPE'])

stats=stats.dropna(subset=['JUDGE'])        
j = {}
for i in stats.values[:,:]:
    if i[6] not in j:
        j[i[6]] = []
        j[i[6]].append(i[1]+'-'+i[2])
    else:
        j[i[6]].append(i[1]+'-'+i[2])
        
jud = {}
nj = []
for i,k in j.items():
    z = []
    s=0
    p=0
    for ii in k:
        if ii not in diff2:
            z.append(ii)
        else:
            s = s+diff2[ii]
            p+=1
    if p == 0:
       nj.append(i)
       continue
    jud[i] = s/p
jd={}
from collections import OrderedDict
import operator

jd = OrderedDict(sorted(jud.items(), key=lambda x: x[1]))
jr= dict(sorted(jud.items(), key=operator.itemgetter(1),reverse=True))

nl=[]
for i in nj:
    for k in j[i]:
        nl.append(k)      



plt.bar(jr.keys(),jr.values())

   
plt.bar(avg1.keys(),avg1.values())    

stats['ROOM_TYPE']=stats[['CASE_TYPE','COURTROOM']].agg('-'.join,axis=1)
x=stats['ROOM_TYPE'].value_counts()  
ctr={}
for i in ct :
    for j in range(len(x)):
        if(x.index[j].startswith(i)):
            ctr[x.index[j]]=x[j]
            break
  
plt.bar(ctr.keys(),ctr.values())


stats[["year", "month", "day"]] = stats["DATE"].str.split("_", expand=True)

stats_2015 = stats.loc[stats['year'] == '2015']
# stats_2015 = stats.loc[stats['year'] == '2016']
# stats_2015 = stats.loc[stats['year'] == '2017']
# stats_2015 = stats.loc[stats['year'] == '2018']
# stats_2015 = stats.loc[stats['year'] == '2019']

stats_2015_9 = stats_2015.loc[stats_2015['month'] == '09']

judges ={}
for i in stats_2015['JUDGE'].unique():
    data = stats_2015.loc[stats_2015['JUDGE'] == i]
    count = data["DATE"].unique()
    avg = len(data)/len(count)
    judges[i] = avg
            
            
            
          