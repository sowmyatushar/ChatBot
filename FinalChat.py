# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:11:59 2020

@author: sowmi
"""


######to divide the chat transcripts to 4 different files1, files2, files3,files4###
import glob

outlines = []
all_files = glob.glob("*.text")
with open('output1.text ', 'w') as outfile:  #change to file 2, file 3, file4
    for i in range(len(all_files)):                 # Declare an empty list
        with open(all_files[i], "rb") as outfile:
            for outline in outfile:
                outlines.append(outline)
         
############
            
converted_list =[]
for element in outlines:
    converted_list.append(element.strip())
    
with open('output1.text', 'w') as filehandle:
    filehandle.writelines("%s\n" % converted_list for converted_list in converted_list)

##########################################

import pandas as pd
#run code within ################# 4 times with changed file names
###change file name as file1.xlsx , file2.xlsx , file3.xlsx, file4.xlsx.
data = pd.read_excel(r"file1.xlsx")

#creating required lists and variables
Timestamp=[]
Unread=[]
Visitor_ID=[]
Visitor_Name=[]
Visitor_Email=[]
Visitor_Notes=[]
address=[]
User_Agent=[]
Platform=[]
Browser=[]
Country_Code=[]
Country_Name=[]
Region=[]
City=[]
total_msg = []

#loop is used for parsing the data to required attribute
#itertuples is used to iterate content of particular rows
for row in data.itertuples(index=True, name='Pandas'):
    a = ((str(getattr(row, "Column1"))).split(': '))

    if a[0] == 'Timestamp' and a[1] != "":
        Timestamp.append(a[1])
    elif a[0] == 'Timestamp' and a[1] == "":
        Timestamp.append("NA")

    elif a[0] == 'Unread:false':
        Unread.append("False")
    elif a[0] == 'Unread:true':
        Unread.append("True")
    elif a[0] == 'Unread:':
        Unread.append("NA")

    elif a[0] == 'Visitor ID' and a[1] != "":
        Visitor_ID.append(a[1])
    elif a[0] == 'Visitor ID' and a[1] == "":
        Visitor_ID.append("NA")

    elif a[0] == 'Visitor Name' and a[1] != "":
        Visitor_Name.append(a[1])
    elif a[0] == 'Visitor Name' and a[1] == "":
        Visitor_Name.append("NA")

    elif a[0] == 'Visitor Email' and a[1] != "":
        Visitor_Email.append(a[1])
    elif a[0] == 'Visitor Email' and a[1] == "":
        Visitor_Email.append("NA")

    elif a[0] == 'Visitor Notes' and a[1] != "":
        Visitor_Notes.append(a[1])
    elif a[0] == 'Visitor Notes' and a[1] == "":
        Visitor_Notes.append("NA")

    elif a[0] == 'IP' and a[1] != "":
        address.append(a[1])
    elif a[0] == 'IP' and a[1] == "":
        address.append("NA")

    elif a[0] == 'Country Code' and a[1] != "":
        Country_Code.append(a[1])
    elif a[0] == 'Country Code' and a[1] == "":
        Country_Code.append("NA")

    elif a[0] == 'Country Name' and a[1] != "":
        Country_Name.append(a[1])
    elif a[0] == 'Country Name' and a[1] == "":
        Country_Name.append("NA")

    elif a[0] == 'Region' and a[1] != "":
        Region.append(a[1])
    elif a[0] == 'Region' and a[1] == "":
        Region.append("NA")

    elif a[0] == 'City' and a[1] != "":
        City.append(a[1])
    elif a[0] == 'City' and a[1] == "":
        City.append("NA")

    elif a[0] == 'User Agent' and a[1] != "":
        User_Agent.append(a[1])
    elif a[0] == 'User Agent' and a[1] == "":
        User_Agent.append("NA")

    elif a[0] == 'Platform' and a[1] != "":
        Platform.append(a[1])
    elif a[0] == 'Platform' and a[1] == "":
        Platform.append("NA")

    elif a[0] == 'Browser' and a[1] != "":
        Browser.append(a[1])
    elif a[0] == 'Browser' and a[1] == "":
        Browser.append("NA")
    else :
        total_msg.append(a)

emp = [" " for i in range(len(total_msg))]
message = [" " for i in range(len(total_msg))]
count = 0

#loop for parsing content of the message
for msg in total_msg:
    if msg[0] != '================================================================================' and len(msg) >= 2 and msg[0][0]=='(':
        emp[count] = (msg[0].split(') ')[1])
        message[count] += " " + msg[1]
    elif msg[0] != '================================================================================':
        if len(msg) < 2:
            message[count] += " " + msg[0]
        else:
            message[count] += " " + msg[0] + msg[1]
    elif msg[0] == '================================================================================':
        count += 1


emp = emp [0:count]
message = message [0:count]   


#####################parsing for 2nd file############

#run code within ################# 3 times with changed file names
######################################################################################################
#change file name as combined1.xlsx , combined2.xlsx , combined3.xlsx 
data = pd.read_excel(r"file2.xlsx")

#loop is used for parsing the data to required attribute
#itertuples is used to iterate content of particular rows
for row in data.itertuples(index=True, name='Pandas'):
    a = ((str(getattr(row, "Column1"))).split(': '))

    if a[0] == 'Timestamp' and a[1] != "":
        Timestamp.append(a[1])
    elif a[0] == 'Timestamp' and a[1] == "":
        Timestamp.append("NA")

    elif a[0] == 'Unread:false':
        Unread.append("False")
    elif a[0] == 'Unread:true':
        Unread.append("True")
    elif a[0] == 'Unread:':
        Unread.append("NA")

    elif a[0] == 'Visitor ID' and a[1] != "":
        Visitor_ID.append(a[1])
    elif a[0] == 'Visitor ID' and a[1] == "":
        Visitor_ID.append("NA")

    elif a[0] == 'Visitor Name' and a[1] != "":
        Visitor_Name.append(a[1])
    elif a[0] == 'Visitor Name' and a[1] == "":
        Visitor_Name.append("NA")

    elif a[0] == 'Visitor Email' and a[1] != "":
        Visitor_Email.append(a[1])
    elif a[0] == 'Visitor Email' and a[1] == "":
        Visitor_Email.append("NA")

    elif a[0] == 'Visitor Notes' and a[1] != "":
        Visitor_Notes.append(a[1])
    elif a[0] == 'Visitor Notes' and a[1] == "":
        Visitor_Notes.append("NA")

    elif a[0] == 'IP' and a[1] != "":
        address.append(a[1])
    elif a[0] == 'IP' and a[1] == "":
        address.append("NA")

    elif a[0] == 'Country Code' and a[1] != "":
        Country_Code.append(a[1])
    elif a[0] == 'Country Code' and a[1] == "":
        Country_Code.append("NA")

    elif a[0] == 'Country Name' and a[1] != "":
        Country_Name.append(a[1])
    elif a[0] == 'Country Name' and a[1] == "":
        Country_Name.append("NA")

    elif a[0] == 'Region' and a[1] != "":
        Region.append(a[1])
    elif a[0] == 'Region' and a[1] == "":
        Region.append("NA")

    elif a[0] == 'City' and a[1] != "":
        City.append(a[1])
    elif a[0] == 'City' and a[1] == "":
        City.append("NA")

    elif a[0] == 'User Agent' and a[1] != "":
        User_Agent.append(a[1])
    elif a[0] == 'User Agent' and a[1] == "":
        User_Agent.append("NA")

    elif a[0] == 'Platform' and a[1] != "":
        Platform.append(a[1])
    elif a[0] == 'Platform' and a[1] == "":
        Platform.append("NA")

    elif a[0] == 'Browser' and a[1] != "":
        Browser.append(a[1])
    elif a[0] == 'Browser' and a[1] == "":
        Browser.append("NA")
    else :
        total_msg.append(a)

emp = [" " for i in range(len(total_msg))]
message = [" " for i in range(len(total_msg))]
count = 0

#loop for parsing content of the message
for msg in total_msg:
    if msg[0] != '================================================================================' and len(msg) >= 2 and msg[0][0]=='(':
        emp[count] = (msg[0].split(') ')[1])
        message[count] += " " + msg[1]
    elif msg[0] != '================================================================================':
        if len(msg) < 2:
            message[count] += " " + msg[0]
        else:
            message[count] += " " + msg[0] + msg[1]
    elif msg[0] == '================================================================================':
        count += 1


emp = emp [0:count]
message = message [0:count] 

###############file3 parsing #########  

data = pd.read_excel(r"file3.xlsx")

#loop is used for parsing the data to required attribute
#itertuples is used to iterate content of particular rows
for row in data.itertuples(index=True, name='Pandas'):
    a = ((str(getattr(row, "Column1"))).split(': '))

    if a[0] == 'Timestamp' and a[1] != "":
        Timestamp.append(a[1])
    elif a[0] == 'Timestamp' and a[1] == "":
        Timestamp.append("NA")

    elif a[0] == 'Unread:false':
        Unread.append("False")
    elif a[0] == 'Unread:true':
        Unread.append("True")
    elif a[0] == 'Unread:':
        Unread.append("NA")

    elif a[0] == 'Visitor ID' and a[1] != "":
        Visitor_ID.append(a[1])
    elif a[0] == 'Visitor ID' and a[1] == "":
        Visitor_ID.append("NA")

    elif a[0] == 'Visitor Name' and a[1] != "":
        Visitor_Name.append(a[1])
    elif a[0] == 'Visitor Name' and a[1] == "":
        Visitor_Name.append("NA")

    elif a[0] == 'Visitor Email' and a[1] != "":
        Visitor_Email.append(a[1])
    elif a[0] == 'Visitor Email' and a[1] == "":
        Visitor_Email.append("NA")

    elif a[0] == 'Visitor Notes' and a[1] != "":
        Visitor_Notes.append(a[1])
    elif a[0] == 'Visitor Notes' and a[1] == "":
        Visitor_Notes.append("NA")

    elif a[0] == 'IP' and a[1] != "":
        address.append(a[1])
    elif a[0] == 'IP' and a[1] == "":
        address.append("NA")

    elif a[0] == 'Country Code' and a[1] != "":
        Country_Code.append(a[1])
    elif a[0] == 'Country Code' and a[1] == "":
        Country_Code.append("NA")

    elif a[0] == 'Country Name' and a[1] != "":
        Country_Name.append(a[1])
    elif a[0] == 'Country Name' and a[1] == "":
        Country_Name.append("NA")

    elif a[0] == 'Region' and a[1] != "":
        Region.append(a[1])
    elif a[0] == 'Region' and a[1] == "":
        Region.append("NA")

    elif a[0] == 'City' and a[1] != "":
        City.append(a[1])
    elif a[0] == 'City' and a[1] == "":
        City.append("NA")

    elif a[0] == 'User Agent' and a[1] != "":
        User_Agent.append(a[1])
    elif a[0] == 'User Agent' and a[1] == "":
        User_Agent.append("NA")

    elif a[0] == 'Platform' and a[1] != "":
        Platform.append(a[1])
    elif a[0] == 'Platform' and a[1] == "":
        Platform.append("NA")

    elif a[0] == 'Browser' and a[1] != "":
        Browser.append(a[1])
    elif a[0] == 'Browser' and a[1] == "":
        Browser.append("NA")
    else :
        total_msg.append(a)

emp = [" " for i in range(len(total_msg))]
message = [" " for i in range(len(total_msg))]
count = 0

#loop for parsing content of the message
for msg in total_msg:
    if msg[0] != '================================================================================' and len(msg) >= 2 and msg[0][0]=='(':
        emp[count] = (msg[0].split(') ')[1])
        message[count] += " " + msg[1]
    elif msg[0] != '================================================================================':
        if len(msg) < 2:
            message[count] += " " + msg[0]
        else:
            message[count] += " " + msg[0] + msg[1]
    elif msg[0] == '================================================================================':
        count += 1


emp = emp [0:count]
message = message [0:count]

################file4 parsing##############


data = pd.read_excel(r"file4.xlsx")

#loop is used for parsing the data to required attribute
#itertuples is used to iterate content of particular rows
for row in data.itertuples(index=True, name='Pandas'):
    a = ((str(getattr(row, "Column1"))).split(': '))

    if a[0] == 'Timestamp' and a[1] != "":
        Timestamp.append(a[1])
    elif a[0] == 'Timestamp' and a[1] == "":
        Timestamp.append("NA")

    elif a[0] == 'Unread:false':
        Unread.append("False")
    elif a[0] == 'Unread:true':
        Unread.append("True")
    elif a[0] == 'Unread:':
        Unread.append("NA")

    elif a[0] == 'Visitor ID' and a[1] != "":
        Visitor_ID.append(a[1])
    elif a[0] == 'Visitor ID' and a[1] == "":
        Visitor_ID.append("NA")

    elif a[0] == 'Visitor Name' and a[1] != "":
        Visitor_Name.append(a[1])
    elif a[0] == 'Visitor Name' and a[1] == "":
        Visitor_Name.append("NA")

    elif a[0] == 'Visitor Email' and a[1] != "":
        Visitor_Email.append(a[1])
    elif a[0] == 'Visitor Email' and a[1] == "":
        Visitor_Email.append("NA")

    elif a[0] == 'Visitor Notes' and a[1] != "":
        Visitor_Notes.append(a[1])
    elif a[0] == 'Visitor Notes' and a[1] == "":
        Visitor_Notes.append("NA")

    elif a[0] == 'IP' and a[1] != "":
        address.append(a[1])
    elif a[0] == 'IP' and a[1] == "":
        address.append("NA")

    elif a[0] == 'Country Code' and a[1] != "":
        Country_Code.append(a[1])
    elif a[0] == 'Country Code' and a[1] == "":
        Country_Code.append("NA")

    elif a[0] == 'Country Name' and a[1] != "":
        Country_Name.append(a[1])
    elif a[0] == 'Country Name' and a[1] == "":
        Country_Name.append("NA")

    elif a[0] == 'Region' and a[1] != "":
        Region.append(a[1])
    elif a[0] == 'Region' and a[1] == "":
        Region.append("NA")

    elif a[0] == 'City' and a[1] != "":
        City.append(a[1])
    elif a[0] == 'City' and a[1] == "":
        City.append("NA")

    elif a[0] == 'User Agent' and a[1] != "":
        User_Agent.append(a[1])
    elif a[0] == 'User Agent' and a[1] == "":
        User_Agent.append("NA")

    elif a[0] == 'Platform' and a[1] != "":
        Platform.append(a[1])
    elif a[0] == 'Platform' and a[1] == "":
        Platform.append("NA")

    elif a[0] == 'Browser' and a[1] != "":
        Browser.append(a[1])
    elif a[0] == 'Browser' and a[1] == "":
        Browser.append("NA")
    else :
        total_msg.append(a)

emp = [" " for i in range(len(total_msg))]
message = [" " for i in range(len(total_msg))]
count = 0

#loop for parsing content of the message
for msg in total_msg:
    if msg[0] != '================================================================================' and len(msg) >= 2 and msg[0][0]=='(':
        emp[count] = (msg[0].split(') ')[1])
        message[count] += " " + msg[1]
    elif msg[0] != '================================================================================':
        if len(msg) < 2:
            message[count] += " " + msg[0]
        else:
            message[count] += " " + msg[0] + msg[1]
    elif msg[0] == '================================================================================':
        count += 1


emp = emp [0:count]
message = message [0:count]



##############################################



a=Timestamp
b=Unread
c=Visitor_ID
d=Visitor_Name
e=Visitor_Email
f=City
g=Country_Code
h=Country_Name
i=Visitor_Notes
j=User_Agent
k=Browser
l=Platform
m=Region
n=address
o=total_msg
p=emp
q= message




dictionary={'Timestamp':a,'Unread':b,'Visitor_ID':c,'Visitor_Name':d,'Visitor_Email':e,'City':f,'Country_code':g,'Country_Name':h,'Visitor_Notes':i,'User_Agent':j,'Browser':k,'Platform':l,'Region':m,'address':n}

#dictionary1={'Unread':b,'total_msg':o,'emp':p,'msg':q}

dictionary1={'Unread':b,'emp':p,'message':q,'total_msg':o}

df=pd.DataFrame({ key:pd.Series(value) for key, value in dictionary.items() })
 
df_msg=pd.DataFrame({key:pd.Series(value) for key, value  in dictionary1.items() })           

df1=df.to_csv('structureddata.csv', index=True)

df2=df_msg.to_csv('Chat_msg.csv', index=True)




## impporting final structured file..Visualization purpose./TAbleau##
data=pd.read_csv('tpose3.csv')

data.columns
data.shape
data.isnull().sum()

## checking percentage of missing values..##
percent_missing = data.isnull().sum() * 100 / len(data) 
print(percent_missing) ## visitor_notes=100%,email=99.32%##

ratio = data['Unread'].value_counts()
print(ratio)


#########################Visualization#####################

import matplotlib.pylab as plt
labels=['False','True']
size=[127703,121]
colors=['green','red']
explode=(0.2,0)
plt.pie(size,explode=explode,labels=labels, colors=colors,shadow=True)
plt.title('False & True Ratio')
plt.show()




from bokeh.models import ColumnDataSource, HoverTool, Panel
from bokeh.models.widgets import Tabs

rcParams['figure.figsize'] = 16, 7
sns.barplot(x=data['City'], y=data['Country_Code'], errwidth=0,palette="PuBuGn_d")
plt.title('City wise data')
       

plt.rcParams['figure.figsize'] = (15, 8)
sns.countplot(data['weekday_name'], palette = 'rainbow')
plt.title('Distribution of Spending Score', fontsize = 14)
plt.show()




###############################importing the text msg file...#################################################################
import string
from nltk.corpus import stopwords
from textblob import Word


data1=pd.read_csv('chat_logic.csv')

data1.isna().sum()

data1.fillna("empty", inplace = True) 

##Converting all review into Lowercase..###
data1['message']= data1['message'].apply(lambda x: " ".join(word.lower() for word in x.split()))

## removing punctuation from review..#
import string
data1['message']=data1['message'].apply(lambda x:''.join([i for i in x  if i not in string.punctuation]))

## removing all stopwords(english)....###
stop_words=stopwords.words('english')

data1['message']=data1['message'].apply(lambda x: " ".join(word for word in x.split() if word not in stop_words))

# Lemmatization
data1['message']=data1['message'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

##Freqently occuring words..###
freq = pd.Series(' '.join(data1['message']).split()).value_counts()[:20]
print(freq)
freq = list(freq.index)
data1['message']=data1['message'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))

### Rare word removal..##
rare_freq = pd.Series(' '.join(data1['message']).split()).value_counts()[-50:]
data1['message']=data1['message'].apply(lambda x: " ".join(x for x in x.split() if x not in rare_freq))

##spelling correction..###
from textblob import TextBlob
"""data1['message']=data1['message'].apply(lambda x: str(TextBlob(x).correct()))"""

## Removing specific words which dont have much significance..##
n_req= ['nan','you','we','a','for','u','your','to','We','on','id','hi','just','by','connecting','the','Notes','of','be','how','may','you?','Hello'
        'for','will','is','in','okay','guidewire','etc','donxe2x80x99t','like']

data1['message']=data1['message'].apply(lambda x: " ".join(word for word in x.split() if word not in n_req))

### After cleanning data most frequect words..##
freq_400 = pd.Series(' '.join(data1['message']).split()).value_counts()[:400]
print(freq_400)

freq_400_str=freq_400.to_string() ## convert it into string for using Wordcloud..##

tst_lst=data1.message     
str_msg = " ".join([str(i) for i in tst_lst]) 
text=str_msg.split()

from collections import Counter
counter= Counter(text)
top_50= counter.most_common(50)
print(top_50)

###############.....Finding Unique Words from the entire corpus...##################
len(set(text))

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))
# This function takes in your text and your mask and generates a wordcloud. 
def generate_wordcloud(freq_400_str, mask):
    word_cloud = WordCloud(width =600, height =600, background_color='black', stopwords=STOPWORDS, mask=mask).generate(freq_400_str)
    plt.figure(figsize=(7,6),facecolor = 'black', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
#Run the following to generate your wordcloud
generate_wordcloud(freq_400_str, mask)

with open('positive-words.txt',"r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]


# loading Negative words for generating positive word cloud
with open("negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

negwords = negwords[37:]


################## negative word cloud###################
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in text if w in negwords])

from wordcloud import WordCloud
from PIL import Image
apple = np.array(Image.open("4.jpg"))

wordcloud= WordCloud(width=5000,
                     height=5000,max_font_size =1000,mask=apple,
                     background_color='black'
                     ).generate(ip_neg_in_neg )

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

mask = np.array(Image.open(requests.get('http://pngimg.com/uploads/dislike/dislike_PNG2.png', stream=True).raw))
# This function takes in your text and your mask and generates a wordcloud. 
def generate_wordcloud(ip_neg_in_neg, mask):
    word_cloud = WordCloud(width =2000, height =2000, background_color='black', stopwords=STOPWORDS, mask=mask).generate(ip_neg_in_neg)
    plt.figure(figsize=(7,6),facecolor = 'black', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

generate_wordcloud(ip_neg_in_neg, mask)    

############## Positive word cloud#############
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in text if w in poswords])

apple = np.array(Image.open("66.png"))
wordcloud_pos_in_pos = wordcloud= WordCloud(width= 3000,
                     height=3000,max_font_size =1000,mask=apple,
                     background_color='black'
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


## Generating Bi-gram.....##
import nltk
bigrm = list(nltk.bigrams(text))
bigrm_series=pd.Series(bigrm).astype(str).value_counts()[:30]
print(bigrm_series)
bigrm_series.plot(kind='bar',cmap='pink')

##Generating Tri-Gram....####
trigrm = list(nltk.trigrams(text))
trigrm_series=pd.Series(trigrm).astype(str).value_counts()[:40]
print(trigrm_series)
trigrm_series.plot(kind='bar',cmap='prism')

## Finding sentiments of conversation..##

data1['polarity'] = data1['message'].apply(lambda x: TextBlob(x).sentiment.polarity)

df_senti= pd.DataFrame({'emp':data1['emp'] ,'polarity': data1['polarity']})
df_11=df_senti.to_csv("sentiment.csv", index=False)


###########################Visualization###############################################

sns.countplot(data=data, x = 'Browser')
sns.countplot(data=data, x = 'Platform')
sns.countplot(data=data, x = 'Region')

from datetime import date, time, datetime

data.Timestamp=pd.to_datetime(data.Timestamp,dayfirst=True)

data['month'] = data['Timestamp'].dt.month

data['day'] = data['Timestamp'].dt.day

data['week'] = data['Timestamp'].dt.week

data['time'] = data['Timestamp'].dt.hour

df_timme=data.to_csv('data_time.csv', index=False) # for chat files..##

Final=pd.read_csv('final_useable.csv')
p = sns.countplot(data=Final, x = 'Day')
p = sns.countplot(data=Final, x = 'Month')

Reg = list(data.Region)
Reg_series=pd.Series(Reg).astype(str).value_counts()[:10]
print(Reg_series)
Reg_series.plot(kind='bar',cmap='prism')

Ci = list(data.City)
Ci_series=pd.Series(Ci).astype(str).value_counts()[:10]
print(Ci_series)
Ci_series.plot(kind='bar',cmap='ocean')



Cou = list(data.Country_Name)
Cou_series=pd.Series(Cou).astype(str).value_counts()[:10]
print(Cou_series)
Cou_series.plot(kind='bar',cmap='summer')

bm = list(data.Platform)
bm_series=pd.Series(bm).astype(str).value_counts()[:6]
print(bm_series)
bm_series.plot(kind='bar',cmap='pink')


brw = list(data.Browser)
b_series=pd.Series(brw).astype(str).value_counts()
print(b_series)
bm_series.plot(kind='bar',cmap='rainbow')





from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
from plotly import tools
import plotly.tools as tls
init_notebook_mode(connected=True)


import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

########### Topic Modelling....####### Latent Dirichlet allocation (LDA)....######

import re
import scipy as sp
import sys
from nltk.corpus import stopwords
from gensim.models import ldamodel
import gensim.corpora;
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.preprocessing import normalize
from pprint import pprint

data_text = data1[['message']]

from nltk import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
stop.update(['href','br'])
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

for idx in range(len(data_text)):
    data_text.iloc[idx]['message'] = [word for word in tokenizer.tokenize(data_text.iloc[idx]['message'].lower()) if word not in stop]


train_data= [value[0] for value in data_text.iloc[0:].values]
num_topics = 5

id2word = gensim.corpora.Dictionary(train_data)
corpus = [id2word.doc2bow(text) for text in train_data]
lda = ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics)

def get_lda_topics(model, num_topics):
    word_dict = {};
    for i in range(num_topics):
        words = model.show_topic(i, topn =20);
        word_dict['Topic # ' + '{:02d}'.format(i+1)] = [i[0] for i in words];
    return pd.DataFrame(word_dict)

imp_topic=get_lda_topics(lda, num_topics)

df_model=imp_topic.to_csv("topic_actual_conv.csv", index=False)


# Print the Keyword in the 5 topics
pprint(lda.print_topics())
doc_lda = lda[corpus]

###Compute Perplexity..##
print('\nPerplexity: ', lda.log_perplexity(corpus))  # a measure of how good the model is. lower the better.
## -5.3097689561841825..##

###Compute Coherence Score using c_v
from gensim.models.coherencemodel import CoherenceModel
coherence_model_lda = CoherenceModel(model=lda, texts=train_data, dictionary=id2word, coherence='c_v')
coherence_lda= coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda) ###0.8588374728797747

# Visualize the topics
import pyLDAvis.gensim
import pickle 
import pyLDAvis
pyLDAvis.enable_notebook()
plot = pyLDAvis.gensim.prepare(lda,corpus,id2word)
# Save pyLDA plot as html file
pyLDAvis.save_html(plot, 'LDA_11.html')
plot

### plotting the graph between coherence vaalue vs no. of topic....
from gensim.models.ldamodel import LdaModel
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model= LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
        model_list.append(model)
        coherencemodel =CoherenceModel(model=lda, texts=train_data, dictionary=id2word, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values

model_list, coherence_values = compute_coherence_values(dictionary=id2word, corpus=corpus, texts=train_data, start=4, limit=32, step=4)
# Show graph
import matplotlib.pyplot as plt
limit=32; start=4; step=4;
x = range(start, limit, step)
plt.plot(x, coherence_values,color='r')
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()



###### unsupervised to supervised learning....##############
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import sklearn.metrics as metrics

## Model CatBoost....#####
from catboost import CatBoostClassifier
cb=CatBoostClassifier
X=data1.message
y=data1.Target_interest

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

y_pred = model.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))##98%


confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

print(classification_report(y_test,y_pred))



## Using Logistic regression Model ..###

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.metrics import accuracy_score
le=LabelEncoder()

data1['Target_interest'] = le.fit_transform(data1['Target_interest'])
X=data1.message
y=data1.Target_interest

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

logreg = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', LogisticRegression(n_jobs=1, C=1.0)),
               ])

model=logreg.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
 #### Accuracy of the model is 98%...###

print(classification_report(y_test,y_pred))
# confusion Matrix...##
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)



######### Using Naive Bays Classifier...###########################################
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd
X= data1.message
y=data1.Target_interest

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 42)

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])

model=nb.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test,y_pred))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))###97.79

confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)








