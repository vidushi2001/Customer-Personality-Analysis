#importing libraries
import numpy as np
import pandas as pd

#importing the datset and forming a dataframe
data = pd.read_csv('/content/Book1.csv')
df = pd.DataFrame(data)
df.head()
#checking for null values and data types 
df.info()

#importing libraries for visualisation
import matplotlib.pyplot as plt
import seaborn as sns

#calculating present age from year of birth
df['Present Age'] = 2000 - df['Year_Birth'] + 21
avg_age = sum(list(df['Present Age']))/len(df['Present Age'])
print(avg_age)
#plotting age on graph to get an idea of age dynamic of customers
sns.set(rc={'figure.figsize':(15,5)})
sns.countplot(x = df['Present Age'],data=df)

#attempt to study the response rate of all the campaigns launched by company
df['TotalPurchaseThroughCampaign'] = df['AcceptedCmp2'] + df['AcceptedCmp3'] + df['AcceptedCmp4'] + df['AcceptedCmp5']  + df['AcceptedCmp1'] + df['Response']
df['TotalPurchaseThroughCampaign'].head()
sns.heatmap(data = df[['AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','AcceptedCmp1','Response','TotalPurchaseThroughCampaign']].corr(),annot = True)

#calculating percentage of purchases through each campaign
count = 0
for i in df['AcceptedCmp3']:
  if i == 1:
    count = count+1
print((count/2240)*100)    

count = 0
for i in df['AcceptedCmp1']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['AcceptedCmp2']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['AcceptedCmp4']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['AcceptedCmp5']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

count = 0
for i in df['Response']:
  if i == 1:
    count = count+1
print((count/2240)*100) 

#pie chart depicting the education level of customers
plt.figure(figsize=(10,7))
l,a = list(set(data["Education"])),[]
for i in range(len(l)):
    a.append(data["Education"].to_list().count(l[i]))
    l[i] = l[i]+" ("+str(a[i]*100/len(data["Education"])) + " %)"
plt.pie(a,labels=l, radius=2)
plt.show()

#relation between education and number of kids
sns.displot(x="Education",y="Kidhome",data=data)

#relation between education and response to the campaign
sns.displot(x="Education",y="Response",data=data)

#heatmap
sns.set(rc={'figure.figsize':(25,20)})
hm = sns.heatmap(data = df.corr(),annot=True)

#relation between in store purchases and income
sns.set(rc={'figure.figsize':(5,5)})
sns.heatmap(df[['Income','NumStorePurchases']].corr(),annot=True)
