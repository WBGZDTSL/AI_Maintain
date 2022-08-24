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
import random
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
    tries=3
    while tries>0:
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
            tries=tries-1
            print(tries,"times left")
    else:
        print("Your account has been suspened")

#%%
# for i in [1,2,3,5]:
#     print(i)
for num in range(1,11):
    print(str(num) + " + 1 = " ,num+1 )
#%%
songlist=['Holy Diver','Thunderstruck','Rebel Rebel']
for song in songlist:
    if song == songlist[0]:
        print(song," -Dio")
    elif   song == songlist[1]:
        print(song, " -AC/DC")
    else:
        print(song, " -David Bowie")
#%%
for i in range(1,10):
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))
#%%
count=0
while True:
    print("Repeat this line!")
    count = count +1
    if count == 5:
        break
#%%
a_list=[1,2,3]
print(sum(a_list))
point1= random.randrange(1,7)
point2= random.randrange(1,7)
point3= random.randrange(1,7)
#%%
def roll_dice(numbers=3,points=None):
    print('<<<< ROLL THE DICE!>>>>')
    if points is None:
        points=[]
    while numbers>0:
        point = random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return "Big "
    elif isSmall:
        return  "small"

def start_game():
    print("<<<< GAME START>>>>")
    choices = ['Big','Small']
    your_choices = input('Big or Small: ')
    if your_choices in choices:
        points=roll_dice()
        total=sum(points)
        youWin= your_choices == roll_result(total)
        if youWin:
            print('The points are ',points,'You win !')
        else:
            print('The points are ',points,'You lose !')
    else:
        print('Invalid Words!')
        start_game()

#%%List Introduce
Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

all_in_list= [1,
              1.0,
              'a word',
              print(1),
              True,
              [1,2],

              (1,2),
              {'key':'value'}
]

fruit = ['pineapple','pear']
fruit.insert(6,'grape')
print(fruit)

fruit[0:0] = ['Orange']
fruit.remove('grape')
fruit[0]='Grapefruit'
del fruit[0:2]
#%% Dictionary
NASDAQ_code= {
    'BAIDU':"Baidu",
    'SINA': 'Sina',
    # 'YOKU':'Youku'
}
NASDAQ_code['YOUKU']= 'Youku'
NASDAQ_code.update({'FB':'Bacebook','TSLA':'Tesla'})
del NASDAQ_code['FB']
#%% Tuple
letters = ('a','b','c','d','e','f')
letters[0]
#%% Set
a_set={1,2,3,5}
a_set.add(4)
a_set.discard(1)
#%%
num_list = [6,2,7,4,1,3,5]
a1=sorted(num_list)
a_reversed_order=sorted(num_list,reverse=True)
del num
#%%
for a,b in zip(num,str):
    print(b,'is',a)

#%%comprehension
a= [i**2 for i in range(4)]
c= [j+1 for j in range(1,10)]
k= [n for n in range(1,10) if n%2 == 0]
z= [letter.lower() for letter in "ABCDEFGHIJKLMN"]
#%%
for num,z in enumerate(z):
    print(z,' is ',num+1)
#%% Class
class CocaCola():
    # formula = ['caffeine','sugar','water','soda']
# coke_for_me = CocaCola()
# coke_for_you =CocaCola()
# coke_for_you.formula
# coke_for_china = CocaCola()
# coke_for_china.local_logo = '可口可乐'
#     def __init__(self):
#         self.local_logo = '可口可乐'
#     def __init__(self):
#         for element in self.formula:
#             print('Coke has {}!'.format(element))
#
#     def drink(self):
#         print('Energy!')

# coke = CocaCola()
# print(coke.local_logo)
    calories    = 140
    sodium      = 45
    total_card  = 39
    caffeine    = 34
    ingredients =  [

    ]
