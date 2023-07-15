
import pandas as pd
import numpy as np


# /////////////
# خواندن از csv
# تغیریک  تیکه از فایل 
# csv
# به وسیله پانداس
# importing the pandas library
import pandas as pd
  
# reading the csv file
df = pd.read_csv("AllDetails.csv")
  
# updating the column value/data
# پنجمین اسم را عوض میکنه  اینی که میخوایم را میزاره
df.loc[5, 'Name'] = 'SHIV CHANDRA'

# writing into the file
df.to_csv("AllDetails.csv", index=False)
  
print(df)
# https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/


# /////////////
# ساخت جدول با پانداس
# ریختن از سه لیست
# تبدیل  از یک لیستی از تاپل ها به رکورد های جدول پانداس

# اگر سه لیست بداریم که عنصر اول هر کدوم یه 
# رکورد باشند و عنصر دوم ها یه رکورد دیگر و به همین ترتیب
X=[18,19,14,12,5]
Y=['a','b','c','d','E']
Z=['mamd','milad','javid','gali','javad']

# for x, y ,z in zip(X,Y,Z):
#     print(x,y,z)
# 18 a mamd
# 19 b milad
# 14 c javid
# 12 d gali
# 5 E javad
import  pandas as pd
# حالا اگر جدولی بسازیم که هر کدوم اینها را بهمون بده
# طبق این سر تیتر باشد
titr=['number','statue','name']

# حالا موارد را میریزیم تو یه لیست
people=[]
for x, y ,z in zip(X,Y,Z):
    people.append((x,y,z))
print(people)
# [(18, 'a', 'mamd'), (19, 'b', 'milad'), (14, 'c', 'javid'), (12, 'd', 'gali'), (5, 'E', 'javad')]

# حالا تبدیل به پانداس
# که عنصر اول بشه  ستون نمره  - عنصر دوم بشه ستون جایگاه و عنصر سوم ستون نام

df=pd.DataFrame(people,columns=titr)
print(df)
#    number statue   name
# 0      18      a   mamd
# 1      19      b  milad
# 2      14      c  javid
# 3      12      d   gali
# 4       5      E  javad

# اما چطور ای دی را حذف کنیم؟


# //////////
# تبدیل یک جدول پانداس به فایل csv
# فرض کن df بالا که پانداس است را میخوایم به سی اس وی تبدیل کنیم

df.to_csv('mamad.csv')
# ,number,statue,name
# 0,18,a,mamd
# 1,19,b,milad
# 2,14,c,javid
# 3,12,d,gali
# 4,5,E,javad

# حالا اگر میخوایم که ای دی نداشته باشه
index=False
df.to_csv('mamad.csv',index=False)



# ///////////////////////////////////////////
# تبدیل فایل سی پانداس به اکسل
df.to_excel('mamad.xls')


# ////////
# تبدیل دیکشنری به دیتافریم پانداس
# کلید ها بشن هدر و بقیه هم اعضا بشن
my_dict = {
    'name': ["a", "b", "c", "d", "e","f", "g"],
    'age': [20,27, 35, 55, 18, 21, 35],
    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]
}
import pandas as pd

df = pd.DataFrame(my_dict)

# //////
# تعریف اندیس
df = pd.DataFrame(my_dict, index=[1,2,3,4,5,6,7])


# ////////////////////
# https://blog.faradars.org/pandas-dataframe-a-lightweight-intro/


# //////////
# تبدیل پانداس به دیتابیس
# https://stackoverflow.com/questions/16476413/how-to-insert-pandas-dataframe-via-mysqldb-into-database


# /////////
# تبدیل چند لیست به جدول پانداس
# در اینجا میشد با زیپ هم انجام بشه
pandas_lists=pd.DataFrame(np.column_stack([ram,size,camera,product,Brand,Model,battery,price]),columns=['ram','size','camera','product','Brand','Model','battery','price'])
print(pandas_lists)




#       ram   size camera  ...                  Model  battery       price
# 0      128   6.43     50  ...         Redmi Note 11      5000   8800000.0
# 1      128   6.43     50  ...         Redmi Note 11      5000   8800000.0
# 2        4   1.77         ...            105 (2019)       800    599000.0
# 3      128   6.43     50  ...         Redmi Note 11      5000   8800000.0
# 4        4   1.77         ...            105 (2019)       800    599000.0
# ...    ...    ...    ...  ...                    ...      ...         ...




# //////////
# ساخت جدول روی دیتا بیسی به اسم
gushi
# با پانداس
from sqlalchemy import create_engine
engine=create_engine('mysql+mysqlconnector://root:mamad951219644002@localhost/Gushi')
# # تبدیل پانداس به دیتابیس
# اسم جدول name
df.to_sql(con=engine , name='mymobiles',if_exists='append',index=False)
#
#
# db.commit()

# اگر فارسی است از قبل بای یونیکد اش را درست کرد

# /////////

import pandas as pd
import  numpy as np
my_data=pd.read_csv('the_csv.csv',delimiter=',')

# فقط ۵ تا سطر را بده
print(my_data[0:5])
# تعداد سطر و ستون فایلمو بهم بده
print(my_data.shape)
# (19, 3)

# فقط یه ستون
# برش زدن یه ستون
x=(my_data[['sex']])
print((x[0:5]))
#    sex
# 0  161
# 1  178
# 2  178
# 3  167
# 4  165

# یه لیست تودرتو میده
# با معرفی سر ستون ها یعنی تیترها
X=(my_data[['sex','height','weight']]).values
print(X)
# [[161 78 'مرد']
#  [178 80 'مرد']
#  [178 86 'زن']
#  [167 59 'زن']]

# تغیر نوع از پانداس به نام پای
# در کار با یادگیری ماشین هم با نامپای کار میکنیم و برای تغیر ها و نمایش داده با پانداس
X=(my_data[['sex','height','weight']])
print(type(X))
# <class 'pandas.core.frame.DataFrame'>
X=(my_data[['sex','height','weight']]).values
print(type(X))
# <class 'numpy.ndarray'>

# ///////
# خواندن دیتا بیس با پانداس
# قبلا با این روش میشد
# python -m pip install --upgrade 'sqlalchemy<2.0'

import sqlalchemy
read_engine=sqlalchemy.create_engine('mysql+pymysql://root:mamad951219644002@localhost/gushi')
the_df=pd.read_sql_table('mymobiles',read_engine)
print(the_df)

# ولی الان این خطا را میده
# AttributeError: 'OptionEngine' object has no attribute 'execute'


# روش دوم
from mysql.connector import connect
import mysql
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text
engine = create_engine('mysql+pymysql://root:mamad951219644002@localhost/gushi')
conn = engine.connect()

query = text('SELECT * FROM mymobiles')
df = pd.read_sql_query(query, conn)
print(df)


# یا اوردن جدول
# gushi اسم دیتابیس هستش
engine = create_engine('mysql+pymysql://root:mamad951219644002@localhost/gushi')
conn = engine.connect()

# mymobiles اسم جدوله
df = pd.read_sql_table('mymobiles', conn)
print(df)


# اوردن کوئری
# gushi اسم دیتابیس هستش
engine = create_engine('mysql+pymysql://root:mamad951219644002@localhost/gushi')
conn = engine.connect()
query = text('SELECT * FROM mymobiles')
df = pd.read_sql_query(query, conn)
print(df)


# /////////
# ساخت جدول دیتا بیس با پانداس
# اول دیتا بیس را باید ساخته باشی
import sqlalchemy
read_engine=sqlalchemy.create_engine('mysql+pymysql://root:mamad951219644002@localhost/Mobile')
conn = read_engine.connect()
# تبدیل پانداس به دیتابیس
# این اپند اگه روشن باشه هر بار که درست میشه یه سری میچینه تهش
df.to_sql(con=conn , name='yourmobiles',if_exists='append',index=False)
# پس یاباید خاموشش کنی یا اینکه اپندشو برداری یا اگه خوبه که اضافه بشه که هیچ


# //////
# تبدیل استرینگ به اینتیجر
the_df["battery"] = the_df["battery"].astype(int)
# ValueError: invalid literal for int() with base 10: '5000mAh'
# به شرطی که همشون کاملا عدد باشند وگرنه
# اگر 5000mAh در میانه هر کدومشون باشه نمیاره
# پس از قبلش باید با رجکس یا کارهای استرینگ اونها را درست کنی

# /////////
# /////
# تبدیل دیتا بیس با پانداس به همراه ساختن پرایمر کی
group_export.to_sql(con=engine, name=example_table, if_exists='replace',
                    flavor='mysql', index=False)
with engine.connect() as con:
    con.execute('ALTER TABLE `example_table` ADD PRIMARY KEY (`ID_column`);')

# ///////
# بهمون میگه اگر خالی بودد اون خونه های خالی را بده
# این روش دونه دونه اونایی که خالی است  را true میده
print(df_new.isnull())
#         ram   size  camera  product  Brand  Model  battery  price
# 0     False  False   False    False  False  False    False  False
# 1     False  False   False    False  False  False    False  False
# 2     False  False   False    False  False  False    False  False
# 3     False  False   False    False  False  False    False  False
# 4     False  False   False    False  False  False    False  False

# این برای یادگیری ماشین پرفایده است

# یا اینکه
# میگه ایا توی کل ستون داریم یا نه اگر یه دونه هم باشه ۱ میزنه
print(df_new.isnull().sum())
# ram        0
# size       0
# camera     0
# product    0
# Brand      0
# Model      0
# battery    0
# price      0
# dtype: int64

# مساله اینه که
# در CAMERA
# اگر استرینگ هم باشه یعنی
# '' یا ' ' یا '  '
# بازهم ۰ میده یعنی خالی نداریم

# پس از تبدیل

# حالا تبدیل میشه
print(df_new.isnull().sum())
# ram          0
# size         0
# camera     198
# product      0
# Brand        0
# Model        0
# battery      0
# price        0
# dtype: int64


# ////
# کار با   NaN,null ها در استرینگ ها

# تبدیل  null ها به خالی یا چیزی که میخوایم
# https://sparkbyexamples.com/pandas/pandas-replace-nan-with-blank-empty-string/#:~:text=Use%20df.,in%20the%20Pandas%20DataFrame%20column.
# اگر داشته باشیم در یک ستون مشخص به اسم camera
print(df_new['camera'])

# 1580     50
# 1581    NaN


# حالا تبدیل null ها با صفر
df_new['camera']=df_new['camera'].fillna(0)
print(df_new['camera'])
# 1580     50
# 1581      0


# تبدیل خالی ها به nall یا چیزی که میخوایم
# https://sparkbyexamples.com/pandas/pandas-replace-blank-values-with-nan/#:~:text=Pandas%20Replace%20Blank%20Values%20with,the%20condition%20evaluates%20to%20True.

# mask

# میاد تو کل این ستون خالی ها را با Nan جایگزین میکنه
df['camera']=df['camera'].mask(df['camera'] == '')
# مثلا وقتی که دیتا بیس ما با خالی یا با ' ' یا '  ' پرشده باشه
# ولی اگر با هر دو پر شده باشه
df['camera']=df['camera'].mask(df['camera'] == '')
df['camera']=df['camera'].mask(df['camera'] == ' ')
df['camera']=df['camera'].mask(df['camera'] == '  ')

# حالا تبدیل میشه
print(df_new.isnull().sum())
# ram          0
# size         0
# camera     198
# product      0
# Brand        0
# Model        0
# battery      0
# price        0
# dtype: int64

# //////
# ساخت یک دیتا فریم خالی تازه و سپس افزودن لیست ها به اون

# import pandas library as pd
import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame()

print(df)

# append columns to an empty DataFrame
df['Name'] = ['Ankit', 'Ankita', 'Yashvardhan']
# احتمالا بشه اینجا حلقه هم زد
df['Articles'] = [97, 600, 200]

df['Improved'] = [2200, 75, 100]

# df



# یا

# import pandas library as pd
import pandas as pd

# create an Empty DataFrame object With
# column names and indices
df = pd.DataFrame(columns=['Name', 'Articles', 'Improved'],
                  index=['a', 'b', 'c'])

print("Empty DataFrame With NaN values : \n\n", df)

# adding rows to an empty
# dataframe at existing index
df.loc['a'] = ['Ankita', 50, 100]
df.loc['b'] = ['Ankit', 60, 120]
df.loc['c'] = ['Harsh', 30, 60]

# df


# ////////////






