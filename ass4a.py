import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

results=requests.get("https://api.data.gov.in/resource/b9cfed4c-a1a2-4f7a-affa-88a8e1a2149c?api-key=579b464db66ec23bdd00000135dcc3f6deb14ba8558e186acfabc286&format=json&offset=0&limit=1000")

data_set=results.json()['records']

dict1={}
for i in data_set:
    age=int(i.get('age'))
    gender=i.get('gender')
    sample_result=i.get('sample_result')
    if age in dict1:
        if sample_result=="Positive":
            dict1[age]=dict1[age]+1 
    else:
        dict1[age]=0
        if sample_result=="Positive":
            dict1[age]=dict1[age]+1
            

dict4={}
for i in data_set:
    age=int(i.get('age'))
    gender=i.get('gender')
    result=i.get('result')
    if age in dict4:
        if result=="Death":
            dict4[age]=dict4[age]+1 
    else:
        dict4[age]=0
        if result=="Death":
            dict4[age]=dict4[age]+1


dict2={}
for i in sorted(dict1):
    dict2[i]=dict1[i]


dict5={}
for i in sorted(dict4):
    dict5[i]=dict4[i]
    

dict3={"1-10": 0,"11-20": 0,"21-30": 0,"31-40": 0,"41-50": 0,"51-60": 0,"61-70": 0,"71-80": 0,"81-90": 0}
for i in dict2.keys():
    if i<11 and i>=1:
        dict3["1-10"]=dict2[i]+dict3["1-10"]
    elif i>=11 and i<=20:
        dict3["11-20"]=dict2[i]+dict3["11-20"]
    elif i>=21 and i<=30:
        dict3["21-30"]=dict2[i]+dict3["21-30"]
    elif i>=31 and i<=40:
        dict3["31-40"]=dict2[i]+dict3["31-40"]
    elif i>=41 and i<=50:
        dict3["41-50"]=dict2[i]+dict3["41-50"]
    elif i>=51 and i<=60:
        dict3["51-60"]=dict2[i]+dict3["51-60"]
    elif i>=61 and i<=70:
        dict3["61-70"]=dict2[i]+dict3["61-70"]
    elif i>=71 and i<=80:
        dict3["71-80"]=dict2[i]+dict3["71-80"]
    else:
        dict3["81-90"]=dict2[i]+dict3["81-90"]
        


ages=list(dict3.keys())
ages2=list(dict2.keys())
num_of_patient1=list(dict3.values())
num_of_patient2=list(dict2.values())
num_of_deaths=list(dict5.values())

num_of_patient1=np.array(num_of_patient1)
num_of_patient2=np.array(num_of_patient2)
num_of_deaths=np.array(num_of_deaths)
ratio=num_of_deaths/num_of_patient2

fig1=plt.figure(1)                                                                                                                #plot figure
ax1=fig1.add_subplot(1,1,1)                                      
fig2=plt.figure(2)                                                                                                                #plot figure
ax2=fig2.add_subplot(1,1,1)

ax1.bar(ages,num_of_patient1)
ax1.set_xlabel("age group")
ax1.set_ylabel("number of patients")
ax1.set_title("No. of covid infected people based on age in surat")
print(ages2)
print(ratio)
print(len(ages2))
print(len(ratio))
ax2.scatter(ages2,ratio)
ax2.set_xlabel("ages(in years)")
ax2.set_ylabel("Ratio of deaths w.r.t. no. of cases")
ax2.set_title("Ratio of deaths w.r.t. no. of cases based on age in surat")

plt.show()