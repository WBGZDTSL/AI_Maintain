from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import json
from datetime import date
from collections import OrderedDict
import cufflinks as cf
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import seaborn as sns
import plotly.express as px
# %matplotlib inline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#%%
data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

# df = pd.DataFrame(
#     OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
# )
#%%
df = pd.read_excel(r"C:\Users\jweiban\PycharmProjects\Git-base\AI Maintain\chiller_data_preprocessed_v1.1.xlsx", header=0, sheet_name='Sheet3',
                   index_col=None)
# px.bar(df,x='year',y='pop')
#
# df_tips= px.data.tips()
px.bar(df,
       x='Predict_End_date',
       y='Part Code',
       color='Chiller',
       title='Data Chart'
       # labels={'Part Code':'Tip Amount','day':'Day of the Week'}
       )
#%%
file = open(r'C:/Users/jweiban/OneDrive - Johnson Controls/Desktop/work/Mass/file.txt','w')
#%%
file.write("123")
#%%
num=1
string= "1"
num2=int(string)
word="friends"
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
#%%
phone_number="1386-666-0006"
hiding_number= phone_number.replace(phone_number[:9],'*'*9)

search='168'
num_a='1386-168-0006'
num_b='1681-222-0006'
c=num_a.find(search)
print(search + 'is at' + str(num_a.find(search)+1) + 'to' + str(num_a.find(search)+len(search)) + 'of num_a')
#%%
print('{} a word she can get what she {} for'.format("with","came"))
#%%
def fahrenheit_converter(C):
    fahrenheit = C*9/5+32
    return str(fahrenheit)+"℉"
C2F=fahrenheit_converter(66)
#%%
def Weight_Conversion(A):
    Weight_Kilogram= A/1000
    return str (Weight_Kilogram)+"Kg"
#%%
def hypotenuse_calculation(a,b):
    hypotenuse= (a**2+b**2)**(1/2)
    return "Thd right triangle third side\'s length is " + str(hypotenuse)
c= hypotenuse_calculation(3,4)
#%%
def trapezoid_area(base_up,base_down,height=6):
    return (1/2)*(base_up+base_down)*height
trapezoid_area(height=2,base_up=3,base_down=6)
#%%
def flashlight(battery1,battery2):
    return "light!"
num1=600
num2=600
flashlight(num1,num2)
#%%
file=open('C:/Users/jweiban/OneDrive - Johnson Controls/Desktop/work/Mass/file.txt','w')
file.write("777")
file.close()
#%%
def text_creat(name,msg):
    desktop_path='C:/Users/jweiban/OneDrive - Johnson Controls/Desktop/work/Mass/'
    full_path=desktop_path+name+".txt"
    file=open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
text_creat("lll","HHHH")
#%%
def text_filter(word,consored_word='lame',changed_word='Awesome'):
    return word.replace(consored_word,changed_word)

text_filter('Python is lame!')
#%%
def consored_text_create(name,msg):
    clean_msg= text_filter(msg)
    text_creat(name,clean_msg)
#%%
a= "42"
b=42
#%%
True > False
#%%
ablum=[]
ablum=['Black Star','David Bowie',25,True]
ablum.append("new song")
ablum[0]
'Black Star' in ablum
#%%
the_Eddie='Eddie'
name='Eddie'
the_Eddie == name
the_Eddie is name
#%%
bool(0)
bool(None)
bool([])
bool('')
bool(False)
#%%
def account_login():
    password = input('password: ')
    if password == "12345":
        print('Login success!')
    else:
        print("Wrong password or invalid input!")
        account_login()
account_login()
#%%
password_list=["*#*#","12345"]
def account_login():
    password=input("Password: ")
    password_correct = password= password_list[-1]
    password_reset = password = password_list[0]
    if password_correct:
        print("Login Success!")
    elif password_reset:
        new_password=input("New_password: ")
        password_list.append(new_password)
        print("Your password has changed successfully!")
        account_login()
    else:
        print("Wrong password or invalid input!")
        account_login()
#%%
# for i in [1,2,3,5]:
#     print(i)
for num in range(1,11):
    print(str(num) + " + 1 = " ,num+1 )
#%%
songlist=['Holy Diver','Thunderstruck','Rebel Rebel']
for song in songlist:
    if song == songlist[0]:
