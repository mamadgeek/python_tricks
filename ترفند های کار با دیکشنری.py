import statistics
from statistics import mean

from traceback import print_list
import collections
from  collections import OrderedDict
# //////////
# dir:     همه توابع درونی دیکشنری 
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', 
# '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', 
# '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get',
# 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# //////////1
# # اول برای متغیر باید تعریف کنی دیکت
my_character=dict()
# # ۱ نوع تعریف دیکشنری اینه

my_character['name']='mamad'
# خروجی دیکشنری 
# نمایش دیکشنری
print(my_character)
# {'name': 'mamad'}

# //////
# یه نوع تعریف هم اینه
my_character={'name':'mamad'}
print(my_character)
# {'name': 'mamad'} 

# /////
# افزودن کلید و ولیو تازه به دیکشنری
# حالا میشه  کلید و ولیو دیگر هم اضافه کرد . هرجوری تعریف بشه

my_character['family']='namjoo'
print(my_character)  
# {'name': 'mamad', 'family': 'namjoo'}

# ///////

# پرینت کردن کلید ها . 
# دسترسی به کلید ها
my_dict={'a':3,'b':4,'d':'aban'}
print(my_dict.keys())
# dict_keys(['a', 'b', 'd'])
# دسترسی به ولیو ها
print(my_dict.values())
# dict_values([3, 4, 'aban'])


print("///////////")
# تعریف دیکشنری
# سینتکسش اینه در تعریف دیکشنری
Dictionary[key] = value

# یا اینه 
dictionary={key:value , key2:value2}

# ///////

# استفاده دیکشنری
# لیست میکنه کلید ها را
print(list(my_character.keys()))
# ['name', 'family']

# ///////////
# تعداد کلید ها را میگه
print(len(my_character.keys()))
# 2

# /////////////
# ایا یه چیزی جزو کلید های دیکشنری است؟
print(('family' in my_character))
# True

# ///
# دسترسی به  ولیو یک کلید
my_dict={'a':3,'b':4,'d':'aban'}
print(my_dict['a'])
# 3

print("///////////")
# راه دیگر تعریف دیکشنری
# درست کردن دیکشنری 
# سینتکس دیگر اینه که میاد اول ای را به
# عنوان دیکشنری تعیرف میکنی و بعد کلید و ولیو را میریزی
a={'salam': 'hi'}
# یا
a=dict()
a['salam']='hi'
print( (a))

# ///////////////////
# نمیشه یه ضرب اورد ریخت توش.  

a['salam']='hi'
# اول باید دیکشنری تعریف کرد
a=dict()
# و بعد کلید و ارزش ریخت توش
a['salam']='hi'
# ////////////////////////
# به روز رسانی دیکشنری   در مدل تعریف کردن سینتکس خالی
# اولی که ای تعریف میشه و بعد که بعدی را میاری خودش اضافه میکنه
a=dict()
a['salam']='hi'
print( (a))
# {'salam': 'hi'}
a['by']='nai'
print( (a))
# {'salam': 'hi', 'by': 'nai'}
# //////////
# ساخت دیکشنری با استفاده از اینپوت گرفتن از کاربر
# اول ولیو را میپرسه سپس کلید را
mydict={}
mydict[input (' give me the key: ')]= input('give me the value: ')
print(mydict)

# give me the value: 31
#  give me the key: mamad
# {'mamad': '31'}

# حالا چطور به تعداد مشخصی مثلا ۱۰ تا کلید و ولیو بپرسم/

# ////////////
# زدن حلقه برای اجرای حلقه
myprinter={'ali':3, 'hasan':2}
for kelid  in myprinter :
    print  (kelid , myprinter[kelid])
# ali 3
# hasan 2

# /////////
# حلقه زدن در دیکشنری
for kelid, arzesh in myprinter.items():
    print (kelid, arzesh)
# ali 3
# hasan 2


# ////////////
# تبدیل دیکشنری معمولی به دیکشنری ترتیبی 
# dict به OrderedDict
myprinter={'hasan':3, 'ali':2}
for kelid  in myprinter :
    print  (kelid , myprinter[kelid])
ordered_dict = OrderedDict (sorted(myprinter.items()))
print(ordered_dict)
# حالا تبدیلش میکنی به اردرد دیکت
# OrderedDict([('ali', 2), ('hasan', 3)])


# روش های دیگر تبدیل تاپل و ... هستند
# این لینک را ببین
# https://stackoverflow.com/questions/15711755/converting-dict-to-ordereddict

from collections import OrderedDict
# این میاد به یک بار کلید ها را لیست میکنه 

order_of_keys = ["key1", "key2", "key3", "key4", "key5"]
# پس ا اون هنوز دیکشنری ا دست نزده و میاد تاپل میکنه 
list_of_tuples = [(key, your_dict[key]) for key in order_of_keys]
# به دیکشنری تبدیل میکنه
your_dict = OrderedDict(list_of_tuples)
# ////////////////

# ایا اگر دو بار ازز دیکشنری استفاده کنیم هر بار جدا باید اردر دیکت کنیم ؟


# ///////

# زیپ کردن دو لیست برای ساخت دیکشنری
myplayerlist=['Hossein','Maziar','Akbar','Nima','Mehdi','Farhad','Mohammad','Khashayar','Milad','Mostafa','Amin','Saeid','Pouya','Poria','Reza','Ali','Behzad','Soheil','Behrooz','Shahrooz','Saman','Mohsen']
m_players=[player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16, player17, player18, player19, player20, player21, player22]
mydict={}
for member, my_player in zip(m_players,myplayerlist):
        mydict [member.name]=Footballer(my_player)
# 'player1': Hossein, 'player2': Maziar, 'player3': Akbar, 'player4': Nima, 'player5': Mehdi, 'player6': Farhad, 'player7': Mohammad, 'player8': Khashayar, 'player9': Milad, 'player10': Mostafa, 'player11': Amin, 'player12': Saeid, 'player13': Pouya, 'player14': Poria, 'player15': Reza, 'player16': Ali, 'player17': Behzad, 'player18': Soheil, 'player19': Behrooz, 'player20': Shahrooz, 'player21': Saman, 'player22': Mohsen}

# ////////////
# تعریف دیکشنری به روش دیگر هم میشه
# اول یه خالی تعریف میکنی
a={}
# بعد بهش اضافه میکنی در حلقه

my_key=['a','b','c' ]
my_val=['1','2','3']
print(my_key , my_val)
a={}
for i in my_key:
    for j in my_val:
        a[i]=j
print(a)
# اینجا خطا میده چون فقط متغیر سوم را میاره در هر ای میریزه و قبلی ها را پاک میکنه
# یعنی فقط اخری را میده
# {'a': '3', 'b': '3', 'c': '3'}

# اگر از 
# product
# و 
# OrderedDict
# هم استفاده کنی همونه

a={}
b= OrderedDict(product(my_key,my_val))
print(b)
# OrderedDict([('a', '3'), ('b', '3'), ('c', '3')])

# و
# pairwise
#   هم فقط در مورد یک لیست کار میکنه

# combinations
# این هم جفتی از تاپل ها را میده . خودشو به عنوان ولیو میده
my_key=['a','b','c' ]
my_val=['1','2','3']
# print(my_key , my_val)
a={}
for ke in combinations(my_key,2):
    a[ke]=ke
print(a)
# {('a', 'b'): ('a', 'b'), ('a', 'c'): ('a', 'c'), ('b', 'c'): ('b', 'c')}



# راه حل
# پس با زیپ بهتره
# یا با زیپ
# اما چون دیکشنری ترتیب را بهم میزنه خراب میکنه

# زیپ  zip
# جفت کردن ۲ لیست
# ایندکس همون متغیر بشه ولیو بعدی
# چون دیکشنری ترتیب را بهم میزنه بهتره از واژه نامه ترتیبی استفاده کنیم
from itertools import combinations , permutations , product ,  combinations_with_replacement , pairwise
from collections import OrderedDict
my_key=['a','b','c' ]
my_val=['1','2','3']
a= OrderedDict(zip(my_key,my_val))
print(a)
# OrderedDict([('a', '1'), ('b', '2'), ('c', '3')])
# ///////
# یا در حلقه 
my_key=['a','b','c' ]
my_val=['1','2','3']
# print(my_key , my_val)
a={}
for  k,v in zip(my_key,my_val):
    a= {k:v}
    print(a)
print(a)
# {'c': '3'}
# مشکلی که داره اینه که فقط اخری را میزنه و بقیه را انگار ذخیره نمیکنه

# پس یا این روش بهتره
# روش براکت 
# در مقابل روش دو نقطه
a={}
for k,v in zip(my_key,my_val):
    a[k]=v
print(a)

# ساخت دیکشنری از دو لیست
# یا
# برای این باید  یا از دیکشنری تو در تو استفاده کرد 
my_key=['a','b','c' ]
my_val=['1','2','3']
# print(my_key , my_val)
a={k:v for k,v in zip(my_key,my_val)}
print(a)
# {'a': '1', 'b': '2', 'c': '3'}


# /////////
# در تعریف دیکشنری به روش براکت گرد به روز کردن دیکشنری اینجوریه
# (رج جادی)

print("///////////")
# کلید ها را پرینت دادن
b=dict()
b[4]='34'
print(b.values())
print(b.keys())
#dict_values(['34'])
#dict_keys([4])

# /////////////

# کلید ها را در حلقه میده
my = {1: 7, 3: 10}
for price in my:
    print (price)
# 1
# 3

# ////////

# ولیو ها را در حلقه میده
my = {1: 7, 3: 10}
for price in my:
    # حالا چطور متغیر های درون  یک دیکشنری را مقایسه کنم؟
    print (my[price])
# 7
# 10

print("///////////")
# ترکیب شرط و حلقه در دیکشری
# اشاره به ولیو 
# تشخیص ولیو با  یک حلقه
# در حلقه انداختن  یک دیکشنری 
#  متغیر نخست حلقه را هم ارز کلید قرار میده
my_name={'name':'mamad'}
for char in my_name :
    # در چهارگوش باید کلید بزاری و چون حلقه کلید 
    # را متغیر نخست میده پس اونو درون چهارگوش میاریم
    # ما برای این جور سنجیدن ها معمولا  ولیو را میسنجیم که ایا اون هست یا خیر؟ 
    # ولیو سنجی در شرطی
    if my_name[char]=='mamad':
        print('mamad! toii?')
  
# حالا چطور باید کلید سنجی کنیم در شرط؟ و حلقه
# به وسیله ی in
# میشه این کار را کرد. یعنی میبیینیم که ایا اون کلید خاص هستش توی حلقه ای ؟
    if 'name' in my_name:
        print('kelid mamad hast')
# kelid mamad hast

# ولیو سنجی
# البته راه دیگر ولیو سنجی در شرط هم اینه
# یعنی از in میشه استفاده کرد
    if 'mamad' in my_name.values():
        print('kelid mamad hast')
# kelid mamad hast

# ///////
# تبدیل  لیست به دیکشنری

# عنصر های اول لیست تو در تو میشه کلید
# عنصر های دوم میشه ولیو
mylist=[[1,10],[7,3]]
my_dict={}
for k in mylist:
    my_dict[k[0]]=k[1]
print(my_dict)
# {1: 10, 7: 3} 
# /////////////////////////////////
# تبدیل لیست تو در تو به دیکشنری
# عنصر های  لیست اول میشه کلید 
# کل لیست دوم میشه ولیو

mylist=[[1,10],[7,3]]
my_dict={}
for k in mylist[0]:
    for j in mylist[1:]:
        my_dict[k]=j
print(my_dict)
# {1: [7, 3], 10: [7, 3]}   


# ///////////
# عنصر های اولی میشه کلید فقط عنصر اولی دوم میشه ولیو
mylist=[[1,10],[7,3]]
my_dict={}
for k in mylist[0]:
    for j in mylist[1:]:
        my_dict[k]=j[0]
print(my_dict)
# {1: 7, 10: 7}

# ///////
my_dict={}
for k in mylist[0]:
    print('k is ', k)
    for j in mylist[1]:
        print('j is',j)
        my_dict[k]=j
print(my_dict)
# k is  1
# j is 7
# j is 3
# k is  10
# j is 7
# j is 3
# این فقط عنصر اخری  را چاپ میکنه
# چگونه ذخیره کنه در دیکشنری؟

# {1: 3, 10: 3}
# ////////
# اما این کد چطور میشه؟
# با zip میشه
# {1: 7, 10: 3}
mylist=[[1,10],[7,3]]  
my=OrderedDict(zip(*(mylist)))
print(my)
# OrderedDict([(1, 7), (10, 3)])
# یا دیکشنری 
my_dict=dict(zip(*(mylist)))
print(my_dict)
# {1: 7, 10: 3}

# /////////
# ترکیب حلقه و شرط 
# شماردن استرینگ به وسیله دیکشنری
gomle='hi my name is mamad namjoo and i am here for learning python' #input('give me the sentence for checking your words: ')
# برای شماردن یا کاری به وسیله ی دیکشنری کردن نخست باید یه دیکشنری خالی تعریف کنیم
counter=dict()
for character in gomle:
    # در شرطی نباید نوشت در جمله هست باید نوشت در کانتر که عنوان دیکشنری هست باشه
    # if character in gomle:
    if character in counter:
        # در حلقه هم باید عنوان دیکشنری اورد
        # کاراکتر را کلید کرد. که در اون صورت به ولیو اشاره داره
        # gomle[character] غلطه
        # counter[character] باید اینو نوشت
        
        # این یه دونه اضافه میکنه به ولیو.. 
        # اگر مساوی یک میکردیم یعنی هروقت میرسیدد ۱ را میریخت توش
        counter[character]+=1
    else:
        counter[character]=1
print(counter)

# {'h': 3, 'i': 4, ' ': 12, 'm': 6, 'y': 2, 'n': 6, 'a': 7, 'e': 4, 's': 1, 'd': 2, 'j': 1, 'o':
# 4, 'r': 3, 'f': 1, 'l': 1, 'g': 1, 'p': 1, 't': 1}


# ////////
# حلقه - استرینگ - دیکشنری
# حالا اگر میخوایم یه سری کلید ها را پشت سر هم چاپ کنه یا کار دیگری کنه
for this_one in counter.keys():
    print(this_one)

# y
# n
# a
# e
# s
# همه کلید های استرینگ شده را لیست میکنه
for this_one in (counter.keys()):
    print (list(this_one))
# ['h']
# ['i']
# حتی میشد از اول گفت به لیست تبدیلش کن
for this_one in list(counter.keys()):
    print (list(this_one))
# ['h']
# ['i']

# ///////////
# هرچند با این هم بیرون میده کلید ها یا ولیو ها را ولی هنوز در فرمت دیکشنری هست
print(counter.keys())
# dict_keys(['h', 'i', ' ', 'm', 'y', 'n', 'a', 'e', 's', 'd', 'j', 'o', 'r', 'f', 'l', 'g', 'p', 't'])

# /////////
# ولیو و کلید را میده
# 34
# 4
b=dict()
b[4]='34'
print(*b.values())
print(*b.keys())

print("///////////")
# کلاس ولیو و کلید را میده 
# فرمت را بهمون میده
# <class 'int'>
# <class 'int'>
b=dict()
b[4]=34
print(type(*b.values()))
print(type(*b.keys()))

print("///////////")

# <class 'str'>
# <class 'int'>
b=dict()
b[4]='34'
print(type(*b.values()))
print(type(*b.keys()))


print("///////////")
# <class 'int'>
# <class 'int'>
b=dict()
b[4]='34'
print(type(int(*b.values())))
print(type(*b.keys()))

print("///////////")

# <class 'str'>
# <class 'str'>
b = dict()
b[4] = '34'
print(type(*b.values()))
print(type(str(*b.keys())))

print("///////////")
# بدون حلقه 
# همه ی عناصر values  را لیست میکنه
# [1, 14, 47]
d = {'key1': 1,'key2': 14,'key3': 47}
print(list(d.values()))
# 
rint("///////////")
# moh96ordo@gmail.com
# میشه موقع نوشتن دیکشنری اینطور هم نوشت که راحت تر است
me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}
print(me["email"])
print("///////////")

# دو ارزشی کردن بررسی ها 
# درست و غلط
# True
me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}
# میشه رست و غلط را به متغیر داد
isExist = "name" in me
print(isExist)


print("///////////")
# شرطی ادن یک دیکشنری 
# بررسی دیکشنری در شرط 
me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}
if "email" in me:
    print(me["email"])
else:
    print("there is no email key in me")

print("///////////")
# میخوام با اسپیلیت بیاد اعدادبعد اسپیس را جدا کنه
# باولی را کلید و دومی را ولیو کنه
aa=dict(input(' give me the any point: ').split())
print((aa))

# give me the any point: my is
# {'m': 'y', 'i': 's'}

# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# در طولانی تر از ۲ تا این خطا را میده
# ValueError: dictionary update sequence element #1 has length 1; 2 is required
# ولی برای دو تا حرفی کار میکنه . یکی را کلید میکنه یکی را ولیو
# میخوام واژه نخست بشه کلید و واژه دوم کلید
# یا چطور واژه های زوج بشن کلید واژه های فرد بشن ولیو؟ ؟

# ///////////
# تبدیل یه استرینگ به دیکشنری ای از شماره ها و تعداد حروف اون استرینگ
# Using split() + loop
#  اون واژه چندمین حرف در رشته است

# ولی  با افزودن این تیکه در اولش هر واژه را یه لیست میکنه

test_str = 'gfg_is_best_for_geeks'
print("The original string is : "
      + str(test_str))
 # The original string is : gfg_is_best_for_geeks 
 
 
delim = "_"
temp = test_str.split(delim)
print(temp)
# ['gfg', 'is', 'best', 'for', 'geeks']    تا اینجا به لیست تبدیل میکنی

# حالا تبدیل  لیست به دیکشنری . که بشماره هر واژه چند بار بکار رفته در اون لیست
res = dict()
# using loop to reform dictionary with splits
# انومریت یعنی میشماره اون لیست تمپ را
for idx, ele in enumerate(temp):
    res[idx] = ele
    
print("Dictionary after splits ordering : "
      + str(res))
# اینجا کلید را شمارنده قرار داده من میخوام ولیو را شمارنده قرار بده
# Dictionary after splits ordering : {0: 'gfg', 1: 'is', 2: 'best', 3: 'for', 4: 'geeks'}

# این شمارنده ولیو قرار میده
res = dict()
# using loop to reform dictionary with splits
# انومریت یعنی میشماره اون لیست تمپ را
# درون چهارگوش میشه کلید
for idx, ele in enumerate(temp):
    res[ele] = idx
print("Dictionary after splits ordering : "
      + str(res))

# Dictionary after splits ordering : {'gfg': 0, 'is': 1, 'best': 2, 'for': 3, 'geeks': 4}

# یا همونه: دیکشنری تو در تو

res = {idx: ele for idx, ele in
       enumerate(test_str.split(delim))}

# Dictionary after splits ordering : {0: 'gfg', 1: 'is', 2: 'best', 3: 'for', 4: 'geeks'}
# Dictionary after splits ordering : {'gfg': 0, 'is': 1, 'best': 2, 'for': 3, 'geeks': 4}

# /////////
# کاربرد in
# اگر لوکیشن ما در اون دیکشنری بود ادرسو بهش بده
    def seller(location) :
        Sales_representative={'tehran':'gomhori','shiraz':'golsar','rasht':'darvaze ghoran'}
        if  location in Sales_representative:
            print(Sales_representative[location])
# فقط باید بگی فروشنده اش کجاست            
print(seller ('tehran'))
# gomhori

# //////////
# بررسی اینکه ایا حرفی خاص در ولیو است یا خیر؟
# True
me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}
isNameExist = "mohammad" in me.values()
print(isNameExist)


print("///////////")
# {'name': 'mohammad', 'family': 'ordookhani', 'age': 24, 'email': 'moh96ordo@gmail.com'}
me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}
print(me)

# ////////
# متد خالی کردن دیکشنری
print(me.clear())
# None

print("///////////")


# نمایش کلید ها
d={'a':'apple','b':'ball'}
d.keys()  # displays all keys in list
# ['a','b']
# نمایش ولیو ها
d.values() # displays your values in list
# ['apple','ball']
# نمایش کلید و ولیو ها با هم
d.items() # displays your pair tuple of key and value  
# [('a','apple'),('b','ball')



# /////////
# تاپل دادن درون دیکشنری


me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}
newUser = {"name": "unknown", "family": "unknown"}
# {'name': 'unknown', 'family': 'unknown'}


newUser_2 = dict.fromkeys(["name","family"], "unknown")
#newUser_3 = {}.fromkeys(["name","family"], "unknown")
print(newUser)


print(newUser_2)
# {'name': 'unknown', 'family': 'unknown'}

# /////////////////////
# fromkeys
# ولیو ای که مد نظر ما است را به همه کلید ها میده
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
# {'key1': 0, 'key2': 0, 'key3': 0}
# ///////////////////////////////
print(dict.fromkeys([1,2,3,4],'hello'))
# {1: 'hello', 2: 'hello', 3: 'hello', 4: 'hello'}

print(dict.fromkeys([1,2,3,4],['hello','boro']))
# {1: ['hello', 'boro'], 2: ['hello', 'boro'], 3: ['hello', 'boro'], 4: ['hello', 'boro']}

# //////
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# حلقه زدن برای تولید دیکشنری

enter= int(input('give me whole votes: '))
# ایده این باشه که به همون تعداد ازمون بپرسه که کشور کدومه
# و بعد اون ورودی را یه ورودی تازه کنه و بشماره
# یه کلید واسش درست کنه و ولیوش هم شمارشش بشه
all_country={}
for key,value in range(enter):
    key: input('give me the name of country: ')
    print(key.keys())
# این سینتکس غلطه 
# چونمیگه 
# ypeError: cannot unpack non-iterable int object 

print("///////////")
# زدن حلقه در دیکشنری
#هرکدوم از کلید ها یا ولیو های داخل یه دیکشنری را لیست میکنه
# 8.401530612244898
# mandana
# 7.5
# hamid
# 6.066666666666666
# sina
# 11.285714285714286
# sara
# 9.75
# soheila
# 7.833333333333333
# ali
# 5.0
# sarvin
# 11.375
cor = {'mandana': 7.5, 
       'hamid': 6.066666666666666, 
       'sina': 11.285714285714286, 
       'sara': 9.75,
       'soheila': 7.833333333333333, 
       'ali': 5.0, 
       'sarvin': 11.375
       }
for k in cor:
    print(k)
    print(cor[k])


print("///////////")
# متد items
# کلید و ولیو ها را تاپل میده

my={'a':4,'b':3,'c':2}
print(my.items())
# dict_items([('a', 4), ('b', 3), ('c', 2)])
# ///

# زدن حلقه و اجرای ایتم
# ('mandana', [5.0, 7.0, 3.0, 15.0])
# ('hamid', [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0])
# ('sina', [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0])
# ('sara', [0.0, 5.0, 20.0, 14.0])
# ('soheila', [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0])
# ('ali', [1.0, 9.0])
# ('sarvin', [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0])

cor={'mandana': [5.0, 7.0, 3.0, 15.0], 'hamid': [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0], 'sina': [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0], 'sara': [0.0, 5.0, 20.0, 14.0], 'soheila': [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0], 'ali': [1.0, 9.0], 'sarvin': [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0]}
for esm in cor.items():
    print(esm)

print("///////////")
# درون دیکشنری فقط یکی از کلید ها را میتونیم بدیم و بهمون ولیو را بده

#{'name': 'mamad', 'sen': '29', 'ghad': 167}
c={'name':'mamad', 'sen':'29','ghad':167}
print(c)
print(c['sen'])
#29
print("////////")
# بصورت جدا کنار هم میتونه کلید و ولیو را چاپ کنه
# name mamad
# sen 29
# ghad 167
d={'name':'mamad', 'sen':'29','ghad':167}
for i in d:
    print (i, d[i])

print("////////")
# همون کار بالا با متد جدا
# بصورت جدا کنار هم میتونه کلید و ولیو را چاپ کنه

# name mamad
# sen 29
# ghad 167
cor={'name': 'mamad', 'sen': '29', 'ghad': 167}
for x in list(cor.keys()):
    print(x,cor[x])

print("//////////")
# ولیو ها را در حلقه میده
# mamad
# 29
# 167
cor={'name': 'mamad', 'sen': '29', 'ghad': 167}
for x in list(cor.keys()):
    print(cor[x])

print("//////////")
# همون با روش دیگر
# ولیو ها را در حلقه میده
# mamad
# 29
# 167
d={'name':'mamad', 'sen':'29','ghad':167}
for i in d:
    print (d[i])

print("//////////")
# ولیو ها را در یک راستا میده
# dict_values(['mamad', '29', 167])
c={'name':'mamad', 'sen':'29','ghad':167}
print(c.values())

print("//////////")
# کلید ها را در یک خط میده
# dict_keys(['name', 'sen', 'ghad'])
c={'name':'mamad', 'sen':'29','ghad':167}
print(c.keys())


print("//////////")
# کلید ها و ولیو ها را در یک خط ولی جدا از هم میده


c={'name':'mamad', 'sen':'29','ghad':167}
print(c.keys(),c.values() )
# dict_keys(['name', 'sen', 'ghad']) dict_values(['mamad', '29', 167])

print("////////")
# همه کلید ها را در یک دیکشتری میده
# name sen ghad
c={'name':'mamad', 'sen':'29','ghad':167}
print(*c.keys())

print("////////"
# همه ولیو ها و کلید ها را در یک خط میده
# name sen ghad mamad 29 167
c={'name':'mamad', 'sen':'29','ghad':167}
print(*c.keys(),*c.values() )


print("////////")
# متد get 
my_dict={'my':4, 'your':7 , 'their':6 , 'our': 3}
# print(my_dict)
# {'my': 4, 'your': 7, 'their': 6, 'our': 3}

# اگر کلید بدی 
# متد گت بر ]میگردونه اون ولیو که هیست را
my_dict={'my':4, 'your':7 , 'their':6 , 'our': 3}
print(my_dict.get('my'))
# 4

# بر میگردونه ولیو کلیدی را و اگر
# اون کلید را نداشت یه ولیو که خواستیم را بر میگردونیم
# سینتکسش اینه که میاد اون اسم دیکشنری . سپس گت کن .
# کلید  را بده که ولیو را اون بهت بده . حالا اگر 
# چیزی نداد ۵ را بهش بده
print(my_dict.get('oh',5))
# 5


# /////////
# متد گت  get  را میشه به عنوان 
# شرطی و else هم بکار برد


my_sentence= ' hello darling im here for education '
my_dict={}
for letter in my_sentence:
    
    # میگه مای دیکت لتر مساوی است با .. یعنی میگه  ولی اون کلید لتر مساوی است با
    # مای دیکت گت کن لتر را اگر نبود صفر برگردون
    # که اگر بود به علاوه یک میکنه عدد قبلی را 
    # ولی اگر هم نبود صفر داد به علاوه ۱ میکنه که میشه یک
    my_dict[letter] =my_dict.get(letter,0) +1
print(my_dict)
# {' ': 7, 'h': 2, 'e': 4, 'l': 3, 'o': 3, 'd': 2, 'a': 2, 'r': 3, 'i': 3, 'n': 2, 'g': 1, 'm': 1, 'f': 1, 'u': 1, 'c': 1, 't': 1}

# این دو کد یکی هستند

# این یعنی همون اگر و وگرنه
my_sentence= ' hello darling im here for education '
my_dict={}
for letter in my_sentence:
    if letter in my_dict:
        my_dict[letter]+=1
    else:
        my_dict[letter]=1
print(my_dict)
# {' ': 7, 'h': 2, 'e': 4, 'l': 3, 'o': 3, 'd': 2, 'a': 2, 'r': 3, 'i': 3, 'n': 2, 'g': 1, 'm': 1, 'f': 1, 'u': 1, 'c': 1, 't': 1}

# /////

# ساخت دیکشنری تازه
# ساخت دیکشنری تازه از دیکشنری قدیمی و اجرای یه متد روی دیکشنری 
my_dict ={0:' a',1:'b',2:'c'}
# kl = my_dict.items()
# چطور بریزیم توی یه دیکشنری دیگه مثل لیست ها قاطی کنمشون رندوم
# ((random.shuffle(list(kl))))
kelid=list(my_dict.keys())
# print(kelid) #[0, 1, 2]
random.shuffle(kelid)
# print(kelid)  #[0, 1, 2]
NEfW={}
# میگه به ازای هر کلید  که در اون لیسته
# ولیو اون کلید در دیکشنری اول را میره پیدا میکنه . بخاطر اسم مشترک
# کلید را میزاره همین کلید
# ولیو را از اون دیکشنری اول میگیره

# این روش است. کلید را همین لیسته میزاری ولیو را میگی ولیو اون قبلی که همونه  انگار زیپ کردی
for k  in kelid:
    NEfW[k]=my_dict[k]
print(NEfW)
# /////
my_sentence= ' hello darling im here for education '
my_dict={}
for letter in my_sentence:
    
    # اگر اینطور بنویسی  هیچی میاره
    # چون اینجا اشاره نکردی که اون کلید مساوی است با 
    my_dict.get(letter,4) +1
print(my_dict)
# {}
# پس باید مثل شکل دوتا بالا بیاری

print("////////")
# اجرای یک متد در یک دیکشنری
# میانگین  لیست ولیو های یک کلید را میده
# mandana
# 5.233333333333333

from statistics import mean
cor = {'mandana': [7.5,5.2,3] }
# print(mean(cor[k] for k in cor))
#8.401530612244898
for k in cor:
    print(k)
    print (mean(cor[k]))
# /////////////
# تبدیل کلید های دیکشنری به لیست 
# دسته بندی
# sort کردن کلید ها
my={10:3 , 4:7}
my2= sorted((my))
print(my2)
# [4, 10]

# /////////////
# دسته بندی بر اساس کلیدد ها 
# تبدیل دیکشنری به تاپل  های سورت شده درون لیست

my={10:3 , 4:7}
my2= sorted((my.items()))
print(my2)
# [(4, 7), (10, 3)] 


print("////////")
# میانگین هر کدام را میده
# mandana
# 5.233333333333333
# ali
# 15
from statistics import mean
cor = {'mandana': [7.5,5.2,3],'ali':[12,14,19] }
# print(mean(cor[k] for k in cor))
#8.401530612244898
for k in cor:
    print(k)
    print (mean(cor[k]))

print("////////")

# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# اجرای یک متد فقط روی یک عدد و نه لیست
# . یعنی باید تبدیل کرد و بعد اون کارا را کرد.
from statistics import mean
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
print(mean(cor[k] for k in cor))
# 8.401530612244898
print("////////")
# در اینجا فقط حلقه را در یکی می زدیم 
# یک کلید را میداد
# name
# sen
# ghad
d={'name':'mamad', 'sen':'29','ghad':167}
for k in d:
    print (k)

# حال  در خود حلقه می تونیم اشاره کنیم در هم کلید و هم ولیوا
# name mamad
# sen 29
# ghad 167
d={'name':'mamad', 'sen':'29','ghad':167}
for k, v in d.items():
    print (k, v)

print("//////////")

print("//////////")

d={'name':'mamad', 'sen':'29','ghad':167}
print(list(iter(d)))
# ['name', 'sen', 'ghad']
# میگیرده به ترتیب کلید ها را میده


# این متد next
# کلید بعدی را میده
print(next(iter(d)))
# میگرده به ترتیب میده
# name


# /////////
# ولی اینجا خودشو دوباره با خودش مقایسه میکنه
# ایا چطور میشه که با بعدی بررسی کنه ؟
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟


my={4:2,3:1,5:4}
if (next(iter(my))) >(next(iter(my))):
    print('oh',(next(iter(my))))
else:
    print('no',(next(iter(my))))
# no 4
# در اینجا چون ۴ بزرگتر از ۴ نیست اورده جزو الس
# چون هیچ عددی بزررگتر از خودش نیست /// کوچکتر از خوودش هم نیست


# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# در دیکشنری چطور اشاره به ایندکس میشه 
# در پایتون ۳ به بالا نمیشه  در حلقه انداخت


# روش بهتر تعین ایندکس
# تعین ایندکس در دیکشنری
# ساخت دیکشنری دو تایی
# این میاد  از ۱ میشماره ایندکس میده
# دادن ای دی به دیکشنری
people = [{'name':'jo'},{'name':'rob'},{'name':'lin'}]
for idx, person in enumerate(people, start=1):
    person['id'] = idx
print(people)
# [{'name': 'jo', 'id': 1}, {'name': 'rob', 'id': 2}, {'name': 'lin', 'id': 3}]


# یا تک خطی
people = [(person | {'id': idx}) for idx, person in enumerate(people, start=1)]

# یا این
people = [{**person, 'id': idx} for idx, person in enumerate(people, start=1)]



# ////////////
# اساخت ایندکس
people = [{'name':'jo'},{'name':'rob'},{'name':'lin'}]
for idx, person in enumerate(people, start=1):
    # person['id'] = idx
    print(idx)
# 1
# 2
# 3
# /////////////

people = [{'name':'jo'},{'name':'rob'},{'name':'lin'}]
for idx, person in enumerate(people, start=1):
    # person['id'] = idx
    print(person)
# {'name': 'jo'}
# {'name': 'rob'}
# {'name': 'lin'}
# انومریت میاد دو تا چیز میگیر اسم دیکشنری و شماره

# پس برای هر کسی که دیکشنری ای داره
# میاد یه دیکشنری درست میکنه 
# اسم  کلید را میزاره ای دی  برای همه 
# ولی اسم متغیرش میشه انومریت


# ////////

print("//////////")
# ??????????????????????????????????????
# ('name', 'mamad') ('sen', '29') ('ghad', 167)
d={'name':'mamad', 'sen':'29','ghad':167}
# این به گمونم لیستی از تاپل ها میده
print(d.items())
# dict_items([('name', 'mamad'), ('sen', '29'), ('ghad', 167)])
# این چندتا  تاپل میده
print(*d.items())
# ('name', 'mamad') ('sen', '29') ('ghad', 167)

print("//////////")
#dict_items([('name', 'mamad'), ('sen', '29'), ('ghad', 167)])
d={'name':'mamad', 'sen':'29','ghad':167}
print(d.items())

print("//////////")
# خروجی دادن  در هر خط بطور جدا

# ('name', 'mamad')
# ('sen', '29')
# ('ghad', 167)
d={'name':'mamad', 'sen':'29','ghad':167}
print(*d.items(), sep='\n')

print("//////////")
# mandana [5, 7, 3, 15]
# hamid [3, 19, 17, 4, 6, 8]
# sina [19, 10, 14, 6, 3]
# sara [0, 5, 20, 14]
# soheila [13, 2, 5, 1, 12, 14, 4]
# ali [1, 9]
# sarvin [0, 16, 16, 7, 2, 19, 8, 14]

from  collections  import OrderedDict
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
for k, v in string.items():
    print (k, v)

print("//////////")
# همه ولیو ها را درون حلقه بیرون میده
# 5
# 7
# 3
# 15
# 3
# 19
# 17
# 4
# 6
# 8
# 19
# 10
# 14
# 6
# 3
# 0
# 5
# 20
# 14
# 13
# 2
# 5
# 1
# 12
# 14
# 4
# 1
# 9
# 0
# 16
# 16
# 7
# 2
# 19
# 8
# 14
from  collections  import OrderedDict
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
for k, v in string.items():
    for x in v:
        print(x)

print("//////////")
# میشه همه اعضای یک متغیر که بصورت لیست است را عملیاتی را انجام داد
# و خروجی را  جدا بیرون داد
# mandana [10, 14, 6, 30]
# hamid [6, 38, 34, 8, 12, 16]
# sina [38, 20, 28, 12, 6]
# sara [0, 10, 40, 28]
# soheila [26, 4, 10, 2, 24, 28, 8]
# ali [2, 18]
# sarvin [0, 32, 32, 14, 4, 38, 16, 28]
from  collections  import OrderedDict
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
for k, v in string.items():
    # اینجا همه ولیو ها را ضربدر دو میکنه 
    # یعنی چون لیست است دوباره حلقه ای در حلقه از ولیو ها میاره
    # یعنی همه وی ها را در نظر میگیره ضربدر دو میکنه بعد میریزه توی لیست اپند میکنه
    a= [x*2 for x in v]
    print(k , a)

print("//////////")
# زدون حلقه درون ولیو های دیکشنری
# همه اعضای درون یک لیست را با هم جمع میزنه ولیو میکنه
# mandana 30
# hamid 57
# sina 52
# sara 39
# soheila 51
# ali 10
# sarvin 82
from  collections  import OrderedDict
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
for k, v in string.items():
    a= 0
    for x in v:
        a+=x
    print(k, a)

print("///////////")
# میشه ولیو ها را که از لیست هستند را باز کنی و درون حلقه هر کاری خواستیم بکینم
# به ترتیب میشه سه تا خروجی بده جمع -  تعدا - میانگین
# mandana 30 4 7.5
# hamid 57 6 9.5
# mamad 52 5 10.4
# aida 39 4 9.75
# milad 51 7 7.285714285714286
# javid 10 2 5.0
# sarvin 82 8 10.25
from  collections  import OrderedDict
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'mamad': [19,10,14,6,3], 'aida': [0,5,20,14], 'milad': [13,2,5,1,12,14,4], 'javid': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
for k, v in string.items():
    a=0
    tedad= 0
    for x in v:
        a+=x
        tedad+=1
    miangin = a/tedad
    print(k, a, tedad , miangin)

print("///////////")
# ساخت میانگین به وسیله متد ایتمس
# mandana,7.5
# hamid,9.5
# mamad,10.4
# aida,9.75
# milad,7.285714285714286
# javid,5.0
# sarvin,10.25
from  collections  import OrderedDict
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'mamad': [19,10,14,6,3], 'aida': [0,5,20,14], 'milad': [13,2,5,1,12,14,4], 'javid': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
for k, v in string.items():
    a=0
    tedad= 0
    
    for x in v:
        # داره میگه هر عدد درون وی یعنی لیست را به علاوه قبلی کن . قبل یای که اولش صفر بوده
        a+=x
        tedad+=1
    miangin = a/tedad
    # خروجی منظم ددادن.اول کلید ها را بده سپس ولیو ها را
    print (k+','+str(miangin))

print("///////////")

#کار با متد mean
# همه ولیو ها را میاانگین میگیره با متد کتابخانه ها
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'mamad': [19,10,14,6,3], 'aida': [0,5,20,14], 'milad': [13,2,5,1,12,14,4], 'javid': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor=(OrderedDict())
# میگه به ازای هر کلید و ولی در استرینگ
for k, v in string.items():
    # میانگین بگیر همه ی وی ها را با هم . یعد تو همون کنار کلید بریز
    v= statistics.mean(v)
    print (k,',',v)
# mandana , 7.5
# hamid , 9.5
# mamad , 10.4
# aida , 9.75
# milad , 7.285714285714286
# javid , 5
# sarvin , 10.25
print("///////////")
# تبدیل تاپل به دیکشنری 
# برش زدن بخشی از تاپل که تقسیم هر بخش هر تکه به کلی و ولیو

#{'a': 'li'}
# {'a': 'li', '1': '2'}
# {'a': 'li', '1': '4'}
# {'a': 'li', '1': '6'}
# {'a': 'li', '1': '8'}
# {'a': 'li', '1': '8'}
khandan=(('ali'),'12','14','16','18')
cor = (dict())
# میگه به ازای هر تکه در اون تاپل
for khat in khandan :
    value= (khat[1:])   # ولیو را از کاراکتر یک به بعد قرار بده
    print(value)     #li   کاراکتر های یک به بعد میشه لی 
    key=(khat[0])     #a    کلید میشه عنصر اولی 
    print(key)
    #print('key bashe',key ,'value mishe ',value)
    cor[key]=value         #{'a': 'li'}    حالا این تکه ها که ساختی را دیکشنری کن دیکشنری کور
    print(cor)
print(cor)

print("//////////")

# این تیکه هم همون کار را میکنه فقط روی دیکشنری برش میزنه نه روی تاپل
# تبدیل دیکشنری به یه دیکشنری دیگه
# برش زدن دیکشنری

# {'m': 'andana'}
# {'m': 'andana', 'h': 'amid'}
# {'m': 'andana', 'h': 'amid', 's': 'ina'}
# {'m': 'andana', 'h': 'amid', 's': 'ara'}
# {'m': 'andana', 'h': 'amid', 's': 'oheila'}
# {'m': 'andana', 'h': 'amid', 's': 'oheila', 'a': 'li'}
# {'m': 'andana', 'h': 'amid', 's': 'arvin', 'a': 'li'}
# {'m': 'andana', 'h': 'amid', 's': 'arvin', 'a': 'li'}

string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
cor = (dict())
for khat in string :
    value= (khat[1:])
    key=(khat[0])
    #print('key bashe',key ,'value mishe ',value)
    cor[key]=value
    print(cor)
print(cor)


print("//////////")

print("//////////")
# وارد کردن کار با سی اس وی

#{'mandana': ['5', '7', '3', '15'], 'hamid': ['3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], 'sina': ['19', '10', '19', '6', '8', '14', '3'], 'sara': ['0', '5', '20', '14'], 'soheila': ['13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], 'ali': ['1', '9'], 'sarvin': ['0', '16', '16', '13', '19', '2', '17', '8']}
import csv
from collections import OrderedDict
# نشانی را در یک متغیر قرار میدی
a='np.csv'

# خواندن فایل 
# میگی  با اون نشانی کارهایی که من میگم را انجام بده

with open (a) as fi:
    khandan= csv.reader(fi)
    cor = (dict())
    for khat in khandan :
        value=(khat[1:])
        key=(khat[0])
        cor[key]= value
        #print(cor)   'mandana': ['5', '7', '3', '15']

print(cor)

print('///////////')


print("///////")
#کار با دیکشنری و تغیر آیتم
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
car = {"brand": "Ford", "model": "Mustang", "year": 1964 }
x = car.items()
car["year"] = 2018
print(x)
# 2018

print('////////')
#کل یه دیکشنری را میریزه توی لیست و بعد به تاپل تبدیل میکنه
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print("//////////")

#کار map اجری یه تابع روی یه لیسته
def double(a):
    return a*2
z= (double(6))   #12 میداد
x=[1,2,3]
y=list(map(double, x))
print(y)

print("//////")
# کلید ها را میده
data = {'CNN': [5.89, 2.34], 'BBC': [6.78, 4.45]}
for x in data:
     print (x)   
#CNN
#BBC
print("//////////////")
# ولیو ها را میده
# [5.89, 2.34]
# [6.78, 4.45]
data = {'CNN': [5.89, 2.34], 'BBC': [6.78, 4.45]}
for x in data:
     print (data[x])
print('///////')
# ولیو و کلید را میده
#CNN [5.89, 2.34]
#BBC [6.78, 4.45]
data = {'CNN': [5.89, 2.34], 'BBC': [6.78, 4.45]}
for k, v in data.items():
     print (k, v)

print("//////////")
# یه تاپل را به دیکشنری تبدیل میکنه  بعد اون پس از مساوی ها را ولیو میکنه 
# حلقه زدن روی ولیو ها
numbers = dict(first=1, second=2, third=3)
squaredNumbers = {key: value ** 2 for key, value in numbers.items()}
print(squaredNumbers)
# {'first': 1, 'second': 4, 'third': 9}

print("//////////")
# هر بخش یه لیست را عملیاتی زدن و به دیکشنری تبدیل کردن
# تبدیل لیست به دیکشنری 
# خودشو به هم به عنوان کلید و هم به عنوان ولیو میگیره
# {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# دیکشنری یک خطی
simple1 = {num: num for num in [1, 2, 3, 4, 5]}
print(simple1)

# ////////
# تبدیل یک  لیستی از تاپل ها به دیکشنری در یک خط
# تبدیل نستد لیست به دیکشنری
# در یک خط . یک خطی. تک خطی

def converter_lt_2_d():
    list_of_tuples=[('say','goftan'),('go','raftan'),('sit','neshastan')]
    my_dict={ tuples[0]:tuples[1] for tuples in list_of_tuples}
    return my_dict
# این همونه ولی در سه خط 
    my_dict= {}
    for tuples in list_of_tuples:
        my_dict[tuples[0]]=tuples[1]

# {'say':'goftan','go':'raftan','sit':'neshastan'}
print("//////////")
# حلقه زدن در دیکشنری
# بررسی یک شرط در دیکشنری
# عملیات روی بخش هایی از ولیو 
# اگر عددی زوج باشه  در ارزش دیکشنری میگه زوج و اگر فرد باشه میگه فرد
simpleNumbers = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}
# ولیو را به عنوان یه تیکه کد گذاشته که از یه لیست بررسی میشه
print(simpleNumbers)
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

print("//////////")
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

# یه متد را فقط روی عناصر ارزش داخل یه لیست به عنوان اجرا میکنه
# {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
# زدن حلقه دریک یکشنری 
# دیکشنری یک خطی
# کار با متد برای ولیو ها
cor = {k: (mean(v)) for k, v in cor.items()}
print(cor)

print("//////////")
# اجرا در دیکشنری تو در تو
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

# میشه فرمان ها را پشت سر هم قرار داد
#یعنی اول میاد float میکنه و بعد برای 
# اینکه کار کنه روی یه لیست map میکنه و بعد به لیست تبدیل میکنه 
# و بعد اون لیست را میانگین 
# میگیره
# {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

cor = {k: (mean(list(map(float, v)))) for k, v in cor.items()}
print(cor)


print("//////////")
# مقایسه دیکشنری تو در تو و دیکشنری ساده

cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}


cor = {k: (mean(list(map(float, v)))) for k, v in cor.items()}
print(cor)

# کار با متد فرمت 
# میشه در خود دستور حلقه سورت شده را گرفت از اول
# یعنی عملیات در خود کار  نه در خروجی

for (key, value) in sorted(cor.items()):
    cor = ("{},{}".format(key, value))
    print(cor)

# {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
# ali,5.0
# hamid,6.066666666666666
# mandana,7.5
# sara,9.75
# sarvin,11.375
# sina,11.285714285714286
# soheila,7.833333333333333

print("/////////////")
# خروجی دادن با فرمت
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

# ali,5.0
# hamid,6.066666666666666
# mandana,7.5
# sara,9.75
# sarvin,11.375
# sina,11.285714285714286
# soheila,7.833333333333333
for (key, value) in sorted(cor.items()):
    print("{},{}".format(key, value))

print("//////////")
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

for (key, value) in sorted(cor.items()):
    cor = ("{},{}".format(key, value))
print(cor)

print("//////////")
# استرینگ
# <class 'str'>

cor = ("{},{}".format(key, value))
print(type(cor))

print("//////////")

# <class 'set'>
cor = {"{},{}".format(key, value)}
print(type(cor))

print("//////////")

# هم ولیو و هم کلید را به عنوان ولیو میاره
# {'ali': ('ali', 5.0), 'hamid': ('hamid', 6.066666666666666), 'mandana': ('mandana', 7.5), 'sara': ('sara', 9.75), 'sarvin': ('sarvin', 11.375), 'sina': ('sina', 11.285714285714286), 'soheila': ('soheila', 7.833333333333333)}
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

cor = {key: ((key, value)) for key, value in sorted(cor.items())}
print(cor)

print("//////////")

# استفاده هر تکه از کد پیشین
# اجرای یک تابع روی ارزش ها
# اجرای دو تابع روی ولیو ها
# این کد میاد در هر ایتم را فلوت میکنه به لیست تبدیل میکنه  و دیکشنری میده
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}

cor_dict = {k: (mean(list(map(float, v)))) for k, v in cor.items()}

# این کد میاد سورت میکنه کور دیکت را ولی فقط ولیو ها را میده به ترتیب 
cor={'mandana': [5.0, 7.0, 3.0, 15.0], 'hamid': [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0], 'sina': [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0], 'sara': [0.0, 5.0, 20.0, 14.0], 'soheila': [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0], 'ali': [1.0, 9.0], 'sarvin': [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0]}
corlist_value = [((value)) for key, value in sorted(cor.items())]
print(corlist_value)
# [5.0, 6.066666666666666, 7.5, 9.75, 11.375, 11.285714285714286, 7.833333333333333]


# ///////

# این کد دسته بندی میکنه  کلید و ولیو را لیستی از تاپل ها میده
corlist = [((key, value)) for key, value in sorted(cor.items())]
print(corlist)
# [('ali', 5.0), ('hamid', 6.066666666666666), ('mandana', 7.5), ('sara', 9.75), ('sarvin', 11.375), ('sina', 11.285714285714286), ('soheila', 7.833333333333333)]

# ////
# تبدیل دیکشنری سورت شده از دیکشنری قبلی 
myDict2={char[0]:char[1]  for char in khan }
        print(myDict2)
# {'mandana': '7.5', 'hamid': '6.066666666666666', 'sina': '11.285714285714286', 'sara': '9.75',
# 'soheila': '7.833333333333333', 'ali': '5', 'sarvin': '11.375'}        
        myDict3={key:myDict2[key] for key in sorted(myDict2)}
        print(myDict3)
# {'ali': '5', 'hamid': '6.066666666666666', 'mandana': '7.5', 'sara': '9.75', 'sarvin': '11.375', 'sina': '11.285714285714286', 'soheila': '7.833333333333333'}


# /////

print("////////")
# اجری یک متد روی ولیو هایی که شاملی از لیست ها هستند
# همه ی ولیو های استرینگ شده را عدد میکنه
# ولی بعد به همون صورت که بود پس میده
#data = {'CNN': ['5.89', '2.34'], 'BBC': ['6.78', '4.45']}
data = {'CNN': [5.89, 2.34], 'BBC': [6.78, 4.45]}
# این داره میگه  برای هر کدام از کلید و ولیو ها در ایتم که میکنی
# اگر ایتم نکنی نمیاره
# بیا کلید را کا قرار بده که می شنه سی ان ان و... و سپس 
# متد فلوت را روی وی ها اجرا کن اون را لیست تحویل بده 
data = {k : list(map(float,(v))) for k, v in data.items()}
print(data)


# این کد همونه ولی به روش دیکشنری تو ر تو نیست
# #or:
data = {'CNN': ['5.89', '2.34'], 'BBC': ['6.78', '4.45']}
data_float = {}
    # این میگه هر کی و ولیو را ایتم ای بیار یعنی دوتایی

for k,v in data.items():
# بعد  بریز توی یه دیکشنری
# کلیدش بشه کا 
# ولیو اش بشه 
# هر کوم از اعضایی که در وی هساند  . متد فلوت را روشون اجرا کن سپس لیست شده اش را بده
    data_float[k] = [float(elem) for elem in v]
print(data_float)


# اینم همونه ولی در حلقه و لیست تو در تو
#  دو تا دیکشنری جدا درون یک لیست 
#  حال فقط ولیو هاشو اینتیجر میکنه
# هر ولیو استرینگ را اینتیجر میکنه

#list = [ { 'a':1 , 'b':2 , 'c':3 }, { 'd':4 , 'e':5 , 'f':6 } ]
list = [ { 'a':'1' , 'b':'2' , 'c':'3' }, { 'd':'4' , 'e':'5' , 'f':'6' } ]
data= [dict([a, int(x)] for a, x in b.items()) for b in list]
print(data)


# زدن دو حلقه در یک لیست برای اتبدیل به یکشنری
# تبدیل لیستی به دیکشنری 
# تبدیل ولیو ها به اینتیجر
# or:
list = [ { 'a':'1' , 'b':'2' , 'c':'3' }, { 'd':'4' , 'e':'5' , 'f':'6' } ]
for sub in list:
    for key in sub:
        sub[key] = int(sub[key])
print(sub)
# ولی طبق معمول این فقط اخرین متغیر را میگیره
# {'d': 4, 'e': 5, 'f': 6}

print("/////////////////")

#تبدیل یک دیکشنری به لیست
# ولیو ها را به لیست تبدیل میکنه

#['a', 'b']
d = {1: "a", 2: "b"}
d= [*d.values()]
print(d)

print("////////")
#['a', 'b']


print("////////")
# تبدیل ولیو دیکشنری به لیست
# ولیو ها را لیست میکنه
#['a', 'b']
d = {1: "a", 2: "b"}
a= (list(d.values()))
print(a)

#or

# تبدیل دیکشنری به لیست
# تبدیل ولیو ها به لیست به حلقه زدن
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}
res = []
for key in test_dict.keys():
    res.append(test_dict[key])
print(res)
# [1, 2, 3]
print("///////////")
# تاپل کردن دیکشنری 
# جدا کردن ولیو ها از دیکشنری 

d = {'key1': ['PTRG0097', 'CPOG0893', 'MMUG0444', 'BTAG0783'], 'key2': ['CPOG0893', 'MMUG0444', 'PPYG0539', 'BTAG0083']}
l1, l2 = d.values() # or this: d['key1'], d['key2']
print(l1)
#['PTRG0097', 'CPOG0893', 'MMUG0444', 'BTAG0783']

l2
#['CPOG0893', 'MMUG0444', 'PPYG0539', 'BTAG0083']

print("///////////")
#اگر دیکشنری ای داشته  باشیم میتونیم هر کدوم از متغیر هاشو پرینت کنیم
cor={'mandana': [5.0, 7.0, 3.0, 15.0], 'hamid': [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0], 'sina': [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0], 'sara': [0.0, 5.0, 20.0, 14.0], 'soheila': [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0], 'ali': [1.0, 9.0], 'sarvin': [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0]}

for value in cor.values():
    print(value)

# [5.0, 7.0, 3.0, 15.0]
# [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0]
# [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0]
# [0.0, 5.0, 20.0, 14.0]
# [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0]
# [1.0, 9.0]
# [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0]

print("///////////")

#  ایندکس هر کدوم از کلید ها را میده در دیکشنری
for i in range(len(my)):
    print(i)
# 0
# 1
# 2   

# ////////////////
# پیدا کردن کلید و ولیو  از لن مشترک

for i in range(len(my.keys())):
    print(i)
    for j in range(len(my.values())):
        print(j)
        if i==j:
            print('i find', i , j)

# 0
# 0
# i find 0 0
# 1
# 2
# 1
# 0
# 1
# i find 1 1
# 2
# 2
# 0
# 1
# 2
# i find 2 2
# ///////
# خطای ۰ 
# وقتی که تلاش میکنی دسترسی داشته باشی وقتی اون اصلا وجود نداره 
# بعد میگه باش میتونی از گت استفاده کنی
The “KeyError: 0 exception” occurs in Python when the user tries to access a “0” key in the given dictionary where the key value is not present. To rectify this error, various methods are used, such as the get() method, try-except exception handling, set specific key value, using for loop, and using “defaultdict”.

# //////////



# ////////

# تبدیل لیست تو در تو به دیکشنری
# عنصر های لیست اول میشه کلید
# لیستی از دیکشنری میده

a = [['Column1', 'Column2', 'Column3', 'Column4', 'Column5'], ['Value1Column1', 'Value1Column2', 'Value1Column3', 'Value1Column4', 'Value1Column5'], ['Value2Column1', 'Value2Column2', 'Value2Column3', 'Value2Column4', 'Value2Column5']]
# میگه هر ای که در رنج طول آ در عنصر های صفر آ هستش . یعنی لیستی که نوشته کلامن

# اشاره به ایندکس ای در دیکشنری 
# همتراز کردن  کلید با همون ولیو در یک دیکشنری توسط ایندکس


# برای ایشاره به ایندکس باید در حلقه که میزنیم لن را بیاریم
# اون عنصر صفرم آی میشه کلید ر 
# و ولیو اش هم میشه لیست
# هر جی که در که در لیست آ از یک به پس هستش   
# همون ایندکس آیم جی اش را بده
print([{a[0][i]: [j[i] 9for j in a[1:]] for i in range(len(a[0]))}])
#[{'Column1': ['Value1Column1', 'Value2Column1'], 
# 'Column2': ['Value1Column2', 'Value2Column2'],
# 'Column3': ['Value1Column3', 'Value2Column3'], 
# 'Column4': ['Value1Column4', 'Value2Column4'], 
# 'Column5': ['Value1Column5', 'Value2Column5']}]


# با روش زیپ 
# or
# میگه هر  کاراکتر را لیست کن برش بزن 
# اون عنصر اولشو بکن کلید عنصر دوم به بعد راولیو کن
d = {s[0]: list(s[1:]) for s in zip(*a)}
print(d)
# {'Column1': ['Value1Column1', 'Value2Column1'], 'Column2': ['Value1Column2', 'Value2Column2'],
# 'Column3': ['Value1Column3', 'Value2Column3'], 'Column4': ['Value1Column4', 'Value2Column4'], 'Column5': ['Value1Column5', 'Value2Column5']}


# توضیحات جزیی

# توضیحات  مجزا
# تفاوت ریپ استار و زیپ

# حلقه ساده درون لیست لیست ها
for s in (a):
    print(s)
# ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
# ['Value1Column1', 'Value1Column2', 'Value1Column3', 'Value1Column4', 'Value1Column5']
# ['Value2Column1', 'Value2Column2', 'Value2Column3', 'Value2Column4', 'Value2Column5']

# تاپلی از لیست ها میده
for s in zip(a):
    print(s)
# (['Column1', 'Column2', 'Column3', 'Column4', 'Column5'],)
# (['Value1Column1', 'Value1Column2', 'Value1Column3', 'Value1Column4', 'Value1Column5'],)
# (['Value2Column1', 'Value2Column2', 'Value2Column3', 'Value2Column4', 'Value2Column5'],)


# حالا با زیپ استار میاد زیپ میکنه
# از هر لیست یک تکه برمیداره تاپل میکنه
for s in zip(*a):
    print(s)
# ('Column1', 'Value1Column1', 'Value2Column1')
# ('Column2', 'Value1Column2', 'Value2Column2')
# ('Column3', 'Value1Column3', 'Value2Column3')
# ('Column4', 'Value1Column4', 'Value2Column4')
# ('Column5', 'Value1Column5', 'Value2Column5')



# حالا این تیکه  اول 
# که در حقیقت اجرای پس از زیپ است
# چون دیکشنری یعنی 
# key:value
# پس 
# اینم همون ساختار را داره
# فقط پیچیده تره

# داره میگه ولیو میشه اسی که داشتیم 
# یعنی کل اس اینه 
# ('Column1', 'Value1Column1', 'Value2Column1')

# حالا اس ۱ به بعد یعنی 
# 'Value1Column1', 'Value2Column1')
# که لیست میشه 
# ['Value1Column1', 'Value2Column1']


# حالا میرسه به کلید که کلی هم یعنی این
# 'Column1
# دو نقطه 
# 'Column1': ['Value1Column1', 'Value2Column1']
d = {s[0]: list(s[1:])
     for s in zip(*a)}

# حالا کل همه اینها هم یه دیکشنری باشه به اسم دی

# /


# ////////////
# تبدیل دیکشنری تاپلی از لیست
# لیست تو در توی نخست کلید ها میشه و لیست های دیگر ولیو ها.جزو تاپل ها
# value هار را به عنوان تاپل میده
# {'Column1': ('Value1Column1', 'Value2Column1', 'ValueXColumn1'),
#  'Column2': ('Value1Column2', 'Value2Column2', 'ValueXColumn2'),
#  'Column3': ('Value1Column3', 'Value2Column3', 'ValueXColumn3'),
#  'Column4': ('Value1Column4', 'Value2Column4', 'ValueXColumn4'),
#  'Column5': ('Value1Column5', 'Value2Column5', 'ValueXColumn5')}
a = [['Column1', 'Column2', 'Column3', 'Column4', 'Column5'], ['Value1Column1', 'Value1Column2', 'Value1Column3', 'Value1Column4', 'Value1Column5'], ['Value2Column1', 'Value2Column2', 'Value2Column3', 'Value2Column4', 'Value2Column5']]
d = {s[0]: s[1:] for s in zip(*a)}

print("///////////")
# شیوه نوشتن دیکشنری
numbers_dict = {
    "yek": 1,
    "seh": 3,
    "do": 2,
    "panj": 5,
    "chahar": 4
}

list_of_keys = numbers_dict.keys()
print(list_of_keys)
# dict_keys(['yek', 'seh', 'do', 'panj', 'chahar'])

list_of_values = numbers_dict.values()
print(list_of_values)
# dict_values([1, 3, 2, 5, 4])

print("///////////")
# کلید ها را لیست میکنه
# ['yek', 'seh', 'do', 'panj', 'chahar']
numbers_dict = numbers_dict = { "yek": 1,"seh": 3, "do": 2, "panj": 5 "chahar": 4 }

list_of_keys = numbers_dict.keys()
list_of_values = numbers_dict.values()
print(list(numbers_dict))

print("///////////")
#لیست ها را به ترتیب کلید الفبا مرتب میکند
# دسته بندی
# سورت
numbers_dict = { "yek": 1,"seh": 3, "do": 2, "panj": 5 "chahar": 4 }

# وقتی چینین چیزی بداریم
list_of_keys = numbers_dict.keys()
list_of_values = numbers_dict.values()
print(list(numbers_dict))
# ['yek', 'seh', 'do', 'panj', 'chahar']

sorted_numbers_dict_keys = sorted(list(numbers_dict))
# ['chahar', 'do', 'panj', 'seh', 'yek']

print(sorted_numbers_dict_keys)

print("///////////")
#حالا اگر بخوایم یه لیست  از دیکشنری را وارونشو نشون بده از reverse استفاده میکنمی


numbers_dict = { "yek": 1,"seh": 3, "do": 2, "panj": 5 "chahar": 4 }

list_of_keys = numbers_dict.keys()
list_of_values = numbers_dict.values()
print(list(numbers_dict))
# ['yek', 'seh', 'do', 'panj', 'chahar']


sorted_numbers_dict_keys = sorted(list(numbers_dict))

print(sorted_numbers_dict_keys)
# ['chahar', 'do', 'panj', 'seh', 'yek']

# یعنی برعکس سورت را میده
reverse_sorted_numbers_dict_keys = sorted(list(numbers_dict), reverse=True)
print(reverse_sorted_numbers_dict_keys)
# ['yek', 'seh', 'panj', 'do', 'chahar']

# ////
# حذف یک کلید و متغیرش از دیکشنری
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ['Charlie']
print(Dict)
# {'Tim': 18, 'Tiffany': 22, 'Robert': 25}

# ////////
# سورت کردن طبق ولیو
# با متد گت
d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
for k in sorted(d, key=d.get, reverse=True):
    k, d[k]
# ('bb', 4)
# ('aa', 3)
# ('cc', 2)
# ('dd', 1)


# یا
from collections import OrderedDict
from operator import itemgetter    

d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
print(OrderedDict(sorted(d.items(), key = itemgetter(1), reverse = True)))

print("///////////")
#مرتب کردن یک لیست بر اساس value ها . و معکوس کردن آنها

numbers_dict = { "yek": 1,"seh": 3, "do": 2, "panj": 5 "chahar": 4 }
list_of_keys = numbers_dict.keys()
list_of_values = numbers_dict.values()
print(list_of_values)
# dict_values([1, 3, 2, 5, 4])

sorted_by_values = sorted(numbers_dict.values())
print(sorted_by_values)
# [1, 2, 3, 4, 5]
# برعکس کردن ولیو ها
sorted_by_values = sorted(numbers_dict.values(), reverse=True)
print(sorted_by_values)
# [5, 4, 3, 2, 1]

# /////////////
# سورت کردن با متد گت
# توضیح
sorted(dict1, key=dict1.get)

# کلا متد 
get('X') 
# ایکس را از دیکشنری خارج میکنه

# حالا
sorted([2, 3, 1])   # returns [1, 2, 3]
# برای یک کار میکنه

# حالا اگر طبق تابعی که ما بخوایم بهش بدیم رفتار کنه

def string_length(s):
    return len(s)

sorted(['abcd', 'efghi', 'jk'], key=string_length)  # returns ['jk', 'abcd', 'efghi']
# در اینجا چون
# طول اینها کوچکتر بود 
# string_length('jk') < string_length('abcd') < string_length('efghi')

# حالا بجای تابع میتونی نوع دیگری از 
callable
# را بدی 
# مثلا دیکشنری را
dict1 = {'a':3, 'b':1, 'c':2}
sorted(dict1, key=dict1.get) # returns ['b', 'c', 'a']
چون که طبق ولیو 
# dict1.get('b') < dict1.get('c') < dict1.get('a')

# طبق مثال
d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
for k in sorted(d, key=d.get):
    k, d[k]
    # ('dd', 1)
    # ('cc', 2)
    # ('aa', 3)
    # ('bb', 4)
    
    # حالا اگر برعکس را بدیم این میشه
    # سورت کردن طبق ولیو
# با متد گت
d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
for k in sorted(d, key=d.get, reverse=True):
    k, d[k]
# ('bb', 4)
# ('aa', 3)
# ('cc', 2)
# ('dd', 1)

# گت در حلق میخوره

# /////
# بجای
sorted(dict1, key=lambda x: dict1[x] if x in dict1 else None)
# بزار
sorted(dict1, key=dict1.get)
# که پایتونیک تره
//////

print("///////////")
# منطبق کردن کلید و ولیو پس از مجزا کردنشون
# با متد items میاد ترتیب بندی میکنه یه سری
# chahar :: 4
# do :: 2
# panj :: 5
# seh :: 3
# yek :: 1

numbers_dict = { "yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4 }
for item in sorted(numbers_dict.items()):
    print("{} :: {}".format(item[0], item[1]))

print("///////////")
#
# chahar :: 4
# do :: 2
# panj :: 5
# seh :: 3
# yek :: 1
for (key, value) in sorted(numbers_dict.items()):
    print("{} :: {}".format(key, value))

print("///////////")

# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# تجزیه کن
#مرتب بسازی دیکشنری  با لامبدا از
# تبدیل دیکشنری به تاپل ها

numbers_dict = { "yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4 }
anonymus_func = lambda x: len(x[0])

# برای سورت کردن هم کلید را اون تابع که عنصر صفر بوده تعریف میکنه 
# کلید ها را  عنصر های صفر تعریف میکنه در تابع انانیموس
# سورت میکنه . سینتکس سورت اینه 
list_of_tuples = sorted(numbers_dict.items(), key=anonymus_func)
# بعد لیستی از تاپل ها میده
print(list_of_tuples)
# [('do', 2), ('yek', 1), ('seh', 3), ('panj', 5), ('chahar', 4)]


# حالا توضیحات در باره جزییات بیشتر

numbers_dict = { "yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4 }
anonymus_func = lambda x: len(x[0])
print((anonymus_func))

# <function <lambda> at 0x0000024020A73E20>
# خوب تا حالا فقط تعریف کردی الان باید کاربردشو بیاری 

# این تیکه کد بر اساس کلید ها دسته  بندی میکنه 
# ایتم هم گفتیم که کلید و ولیو را میده
list_of_tuples = sorted(numbers_dict.items())
# بعد لیستی از تاپل ها میده
print(list_of_tuples)
# [('chahar', 4), ('do', 2), ('panj', 5), ('seh', 3), ('yek', 1)]

# حالا نیازه که کلید را کنیم ولیو ها
# برای این از لامبدا استفاده میکنم
list_of_tuples = sorted(numbers_dict.items(),key= lambda x:x[1])
print(list_of_tuples)
# اما این بر اساس حروف الفبای عنصر دوم میده 
# [('yek', 1), ('do', 2), ('seh', 3), ('chahar', 4), ('panj', 5)]
# اگر بر اساس تعداد حروف عنصر دوم بخوایم دسته بندی کنیم این میشه

# list_of_tuples = sorted(numbers_dict.items(),key= lambda x:len(x[1]))
print(list_of_tuples)
# این خطا را میده چون اینتیجر طول نداره
# TypeError: object of type 'int' has no len()

# حالا اگر  بر اساس حروف بود که یعنی عنصر اول 
list_of_tuples = sorted(numbers_dict.items(),key= lambda x:len(x[0]))
print(list_of_tuples)
# [('do', 2), ('yek', 1), ('seh', 3), ('panj', 5), ('chahar', 4)]

# که البته این همونه فقط در یه متغیر جدا ریخته از قبل که بعدا کلید را بده بهش
anonymus_func = lambda x: len(x[0])
list_of_tuples = sorted(numbers_dict.items(), key=anonymus_func)
# [('do', 2), ('yek', 1), ('seh', 3), ('panj', 5), ('chahar', 4)]
# همون خروجی

# ////////////////

# مقایسه گت و لامبدا

numbers_dict = { "yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4 }

# کلید ها را طبق سورت ولیو میده
list_of_tuples0 = sorted(numbers_dict, key=numbers_dict.get)
print(list_of_tuples0)
# ['yek', 'do', 'seh', 'chahar', 'panj']

# کلید ها را طبق سورت کلید میده
anonymus_func = lambda x: x[0]
list_of_tuples5 = sorted(numbers_dict, key=anonymus_func)
print(list_of_tuples5)
# ['chahar', 'do', 'panj', 'seh', 'yek']

# ؟؟؟؟؟؟؟؟؟
# کلید ها را میده 
# طبق  کلید قرار دادن ولیو
# اما 
anonymus_func = lambda x: x[1]
list_of_tuples3 = sorted(numbers_dict, key=anonymus_func)
print(list_of_tuples3)
# ['panj', 'yek', 'seh', 'chahar', 'do']

list_of_tuples2 = (sorted(numbers_dict.items(), key= lambda x:(x[1],x[0])))
print(list_of_tuples2)
# [('yek', 1), ('do', 2), ('seh', 3), ('chahar', 4), ('panj', 5)]


# ولی این خطا میده 
# یعنی با متد گت نمیتونی ایتم را بیاری
list_of_tuples4 = (sorted(numbers_dict.items(), key= numbers_dict.get))
# print(list_of_tuples4)
# TypeError: '<' not supported between instances of 'NoneType' and 'NoneType'
    
# /////////


print("///////////")
#مرتب سازی با لامبدا
# سورت کردن بر اساس ولیو

    # اعداد values ها را از (کوچک به بزرگ ) مرتیب سازی میکنه) به لیست تبدیل میکنه
# [('yek', 1), ('do', 2), ('seh', 3), ('chahar', 4), ('panj', 5)]
numbers_dict = { "yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4 }
anonymus_func = lambda x: x[1]
list_of_tuples = sorted(numbers_dict.items(), key=anonymus_func)
print(list_of_tuples)

اینم همونو میده 
numbers_dict = { "yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4 }
# anonymus_func = lambda x: x[1]
list_of_tuples = sorted(numbers_dict, key=numbers_dict.get)
print(list_of_tuples)
# ['yek', 'do', 'seh', 'chahar', 'panj']
print("///////////")
# اعداد درون values ها را به ترتیب از کوچک به بزرگ لیست میکنه و به
# دیکشنری تبدیل میکنه تحویل میده
#     {'yek': 1, 'do': 2, 'seh': 3, 'chahar': 4, 'panj': 5}
    numbers_dict = {"yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4}
    anonymus_func = lambda x: x[1]
    list_of_tuples = dict(sorted(numbers_dict.items(), key=anonymus_func))
    print(list_of_tuples)

print("///////////")

# دیکشنری را طبق برعکس  ترتیب ولیو ها چاپ میکنه 
# اعدادvalues  را به ترتیب برعکس (از بزرگ به کوچک )چاپ میکنه
    # {'panj': 5, 'chahar': 4, 'seh': 3, 'do': 2, 'yek': 1}
    numbers_dict = {"yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4}
    anonymus_func = lambda x: x[1]
    list_of_tuples = dict(reversed(sorted(numbers_dict.items(), key=anonymus_func)))
    print(list_of_tuples)


print("///////////")
# کلید ها را به ترتیب از کوچک به بزرگ میچینه
# و به دیکشنری (یا میشه به لیست ) تحویل میده
    numbers_dict = {"yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4}
    anonymus_func = lambda x: x[0]
    list_of_tuples = dict(sorted(numbers_dict.items(), key=anonymus_func))
    print(list_of_tuples)
# {'chahar': 4, 'do': 2, 'panj': 5, 'seh': 3, 'yek': 1}

print("///////////")
## کلید ها را به ترتیب از بزرگ به کوچک میچینه
# و به دیکشنری (یا میشه به لیست ) تحویل میده
    # در برنامه نویسی بزرگ حروف بعدی هستند.
    # {'yek': 1, 'seh': 3, 'panj': 5, 'do': 2, 'chahar': 4}

    numbers_dict = {"yek": 1, "seh": 3, "do": 2, "panj": 5, "chahar": 4}
    anonymus_func = lambda x: x[0]
    list_of_tuples = dict(reversed(sorted(numbers_dict.items(), key=anonymus_func)))
    print(list_of_tuples)

print("///////////")
# مقایسه یه دیکشنری با یه تاپل
# فیلتر کردن دیکشنری 
# فقط کلید هایی که بهش مقید کردیم را بهمون میده
#گزینشی اون کلید هایی را که بهش دادیم را بهمون کلید و متغیر را در یک دیکشنری میزاره

d = {1: 2, 3: 4, 5: 6, 7: 8}
l = (1, 5)
# میگه هر کا که در ال هست یعنی یک و پنج
# اگر اون کا در دی بود که تبعا منظورش در کلید دی بود
# اون موقع اون کا را کلید کن و اون  کا را از دیکشنری را ولیو ش هم از اون دی بده
print({k: d[k] for k in l if k in d})
# {1: 2, 5: 6}

print("///////////")
# گزینشی اون متغیر ها را پرینت میکنه
# این فقط ولیو های مشترک را میده
    for k in l:
        if k in d:
            print(d[k])
print("///////////")
# برش میزنه ولیو داخل لیست های یک دیکشنری را . تا 
# اون مورد که خودش تعین میکنه . مثلا 
# در پایین تا چهار تا را برش زده

    test_dict = {"Gfg": [1, 6, 3, 5, 7],
                 "Best": [5, 4, 2, 8, 9],
                 "is": [4, 6, 8, 4, 2]}
    print("The original dictionary is : " + str(test_dict))
    # {'Gfg': [1, 6, 3, 5, 7], 'Best': [5, 4, 2, 8, 9], 'is': [4, 6, 8, 4, 2]}

    K = 4
    res = dict()
    # میگه هر سابی که در تست دیکت است
    for sub in test_dict:
    # کلید را بار ساب که همون کلید تست میشه
    # و ولیو هم میشه برش زده اون دیکشنری اولی 
        res[sub] = test_dict[sub][:K]
    print("The dictionary after conversion " + str(res))
    
# {'Gfg': [1, 6, 3, 5], 'Best': [5, 4, 2, 8], 'is': [4, 6, 8, 4]}
    print("///////////")
# دادن یکی از ولیو هایی که لیست است به دیکشنری
# انتخاب یکی از ولیو ها
# برش و برداشتن یه تیکه از دیکشنری قبلی به دیکشنری تازه

test_dict = {"Gfg": [1, 6, 3, 5, 7],
                 "Best": [5, 4, 2, 8, 9],
                 "is": [4, 6, 8, 4, 2]}
print("The original dictionary is : " + str(test_dict))
K = 4
res = dict()
for sub in test_dict:
    # دی اینجا ولیو را عنصر سوم یعنی ایندکس ۲ میده
    res[sub] = test_dict[sub][2]

print(res)
# {'Gfg': 3, 'Best': 2, 'is': 8}

print("///////////")
#همون کار بالا
# {'Gfg': [1, 6, 3, 5, 7], 'Best': [5, 4, 2, 8, 9], 'is': [4, 6, 8, 4, 2]}
# {'Gfg': [1, 6, 3, 5], 'Best': [5, 4, 2, 8], 'is': [4, 6, 8, 4]}
test_dict = {"Gfg": [1, 6, 3, 5, 7],
            "Best": [5, 4, 2, 8, 9],
            "is": [4, 6, 8, 4, 2]}
print("The original dictionary is : " + str(test_dict))
K = 4
res = {key: val[:K] for key, val in test_dict.items()}
print("The dictionary after conversion " + str(res))

print("///////////")
# دیکشنری comperhention
#اعداد زوج را از درون لیست ها حذف میکنه
 # {'gfg': [1, 3, 4, 10], 'is': [1, 2, 8], 'best': [4, 3, 7]}
 # {'gfg': [1, 3], 'is': [1], 'best': [3, 7]}
    test_dict = {'gfg': [1, 3, 4, 10], 'is': [1, 2, 8], 'best': [4, 3, 7]}
    print("The original dictionary is : " + str(test_dict))
    res = {key: [idx for idx in val if idx % 2]
           for key, val in test_dict.items()}
    print("The filtered values are : " + str(res))

print("///////////")
#اعداد گزینش شده را فقط میده و میریزه تن یه دیکشنری دیگه
    # {0: 1, 1: 2, 2: 3, 100: 7, 101: 8, 102: 9}
# فیلتر کردن یه دیکشنری با یه تاپل دیگه
    d = {0: 1, 1: 2, 2: 3, 10: 4, 11: 5, 12: 6, 100: 7, 101: 8, 102: 9, 200: 10, 201: 11, 202: 12}
    keys = (0, 1, 2, 100, 101, 102)
    d1 = {k: d[k] for k in keys}
    print(d1)
print("///////////")
#همه values ها را میریزه توی یه لیست
# داخل یه لیست واحد

# {'Gfg': [4, 5], 'is': [6, 8], 'best': [10]}
    test_dict = {"Gfg": [4, 5], "is": [6, 8], "best": [10]}
    print("The original dictionary is : " + str(test_dict))
    res = sum(test_dict.values(), [])
    print("The Concatenated list values are : " + str(res))
# [4, 5, 6, 8, 10]

print("///////////")
# همون بالاییه.همه ولیوهارا داخل یه لیست میریزه
# متد چین
# {'Gfg': [4, 5], 'is': [6, 8], 'best': [10]}
#  [4, 5, 6, 8, 10]
    from itertools import chain
    test_dict = {"Gfg": [4, 5], "is": [6, 8], "best": [10]}
    print("The original dictionary is : " + str(test_dict))
    res = list(chain(*test_dict.values()))
    print("The Concatenated list values are : " + str(res))


print("///////////")
# نستد لیست درست کردن از ولیو هایی که بطور مجزا لیست هستند
#همهرا value ها را جدا جدا داخل یه لیست میریزه
# {'Gfg': [4, 5], 'is': [6, 8], 'best': [10]}
#  [[4, 5], [6, 8], [10]]
#همه value ها را داخل یه لیست میریزه
    from itertools import chain
    test_dict = {"Gfg": [4, 5], "is": [6, 8], "best": [10]}
    print("The original dictionary is : " + str(test_dict))
    res = list(chain(test_dict.values()))
    print("The Concatenated list values are : " + str(res))

print("///////////")
# زنجیر کردن کلید ها و ریهتن در یک لیست
 #  {'Gfg': [4, 5], 'is': [6, 8], 'best': [10]}
 # ['Gfg', 'is', 'best']
    from itertools import chain
    test_dict = {"Gfg": [4, 5], "is": [6, 8], "best": [10]}
    print("The original dictionary is : " + str(test_dict))
    res = list(chain(test_dict.keys()))
    print("The Concatenated list values are : " + str(res))

print("///////////")



print("///////////")
# اشتراک گیری 
# کلید های مشترک را ولیو هاشو لیست میکنه
# دیکشنری تو در تو از لیست تودرتو ی تاپل ها
# لیستی از تاپل ها را تبدیل به دیکشنری میکنه . اونا که
# کلید مشترک دارن را هم میریزه تو یه لیست واحد
    from collections import defaultdict
    test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]
    print("The original list is : " + str(test_list))
    #The original list is : [(1, ‘gfg’), (1, ‘is’), (2, ‘best’), (3, ‘for’), (4, ‘CS’)]

    res = defaultdict(list)
    for i, j in test_list:
        res[i].append(j)
    print("The merged dictionary is : " + str(dict(res)))
    # The merged dictionary is : {1: [‘gfg’, ‘is’], 2: [‘best’], 3: [‘for’], 4: [‘CS’]}

print("///////////")
    # defaultdict(<class 'list'>, {})
    res = defaultdict(list)
    print((res))

# ///////////

# اگر مقداری نداشت مقدار پیشفرض را پس میده

from collections import defaultdict
dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

dd["dogs"]
['Rufus', 'Kathrin', 'Mr Sniffles']
# /////////////
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟/
from collections import defaultdict
test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]
print("The original list is : " + str(test_list))
# The original list is : [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]
# برای دیفالت دیکت ما لیست میدیم که جلو اپند بشه بهش
res = defaultdict(list)
print((res))
# defaultdict(<class 'list'>, {})
for i, j in test_list:
    res[i].append(j)  # این الان کلید است یا اشاره به عنصر ای ام لیست است؟
    
print("The " + str(dict(res)))
# The {1: ['gfg', 'is'], 2: ['best'], 3: ['for'], 4: ['CS']}

# /////////////


# اینم حلقه تکه تکشه
    # The
    # {1: ['gfg']}
    # The
    # {1: ['gfg', 'is']}
    # The
    # {1: ['gfg', 'is'], 2: ['best']}
    # The
    # {1: ['gfg', 'is'], 2: ['best'], 3: ['for']}
    # The
    # {1: ['gfg', 'is'], 2: ['best'], 3: ['for'], 4: ['CS']}

print("///////////")


# اینت در دیفالت دیکت یه دونه اضافه میکنه
# این کد میاد میبینه از هر کدوم از اعداد درونش چند
# بار بکار رفته که بشماره اون را به عنوان دیکشنری
# Defining the dict
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to 
    # enter the key first

    print('before','d[i] is ',d[i] ,'and i is' ,i)
    
    d[i] += 1
    
    print('after ','d[i] is ',d[i] ,'and i is',i)
    # print(d)
# before d[i] is  0 and i is 1   اولین ایندکسش صفر است و محتواش ۱ است
# after  d[i] is  1 and i is 1     پس از ریختن یک ولیو یه دونه به صفر افزوده میشه و میشه ۱
# defaultdict(<class 'int'>, {1: 1})    پس تا حالا دیکشنریمون میشه
# before d[i] is  0 and i is 2             ایندکس هنوز صفر است و  عدد بعدی در لیست ۲ است
# دی ای هنوز صفر است    اما چرا؟؟؟؟؟؟؟؟؟
# چون اول ۱ ا در نظر میگیره
# after  d[i] is  1 and i is 2      طبق دیفالت دیکت یه دونه اضافه میکنه  .چون ایندکس یک است و عدده ۲ است
# حالا طبق دیفالت ایکس یه دونه اضافه میکنه   
# defaultdict(<class 'int'>, {1: 1, 2: 1})
# before d[i] is  0 and i is 3       ایندکس ما هنوز صفر است  . ای که بررسی میکنه ۳ است.
# after  d[i] is  1 and i is 3     پس از بررسی ۳ را هم طبق دیکت ۱ میده
# defaultdict(<class 'int'>, {1: 1, 2: 1, 3: 1})    پس دیکشنری میشه
# before d[i] is  0 and i is 4    عدد بعدی ۴ است ایندکس هم ایندکس صفر یعنی عدد ۱ است
# after  d[i] is  1 and i is 4       طبق دیفالت دیکت یه دونه هم به ۴ افزوده میشه
# defaultdict(<class 'int'>, {1: 1, 2: 1, 3: 1, 4: 1})
# before d[i] is  1 and i is 2        عدد بعدی چون ۲ است ایندکسش میشه ۱
# after  d[i] is  2 and i is 2     پس از دادن عدد میشه ۲
# defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 1, 4: 1})
# before d[i] is  1 and i is 4
# after  d[i] is  2 and i is 4
# defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 1, 4: 2})
# before d[i] is  1 and i is 1
# after  d[i] is  2 and i is 1
# defaultdict(<class 'int'>, {1: 2, 2: 2, 3: 1, 4: 2})
# before d[i] is  2 and i is 2
# after  d[i] is  3 and i is 2
# defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
# defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
print(d)
# defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})



# /////////////

# تجزیه کن؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# مقایسه دو لیست برای تعین تکرار در دیکشنری
# میبینه همتای اون ۵ ها کدوم است  اونا را به عنوان ولیو میریزه
#دوتا لیست را یر به یر میاره تراز میکنه 
# و اونا که حرف مشترک دارن را میزاره تو یه کلید
# یعنی دو ولیو و یه کلیدد
    test_list1 = [5, 6, 6, 4, 5, 6]
    test_list2 = [8, 3, 2, 9, 10, 4]
    res = {key: [] for key in test_list1}
    for key, val in zip(test_list1, test_list2):
        # متد اپند  در دیکشنری
        print(res)
        res[key].append(val)
 # {5: [], 6: [], 4: []}   اول همشو خالی میاره طبق بالا
# {5: [8], 6: [], 4: []}     بعد چون اپند کرده اون عددد را میریزه توی یه لیست
# {5: [8], 6: [3], 4: []}
# {5: [8], 6: [3, 2], 4: []}
# {5: [8], 6: [3, 2], 4: [9]}
# {5: [8, 10], 6: [3, 2], 4: [9]}
# {5: [8, 10], 6: [3, 2, 4], 4: [9]}
print(res)
# {5: [], 6: [], 4: []}
    print(": " + str(res))
    # : {5: [8, 10], 6: [3, 2, 4], 4: [9]}

print("///////////")

# افزودن یه تیکه به دیکشنری 
# میشه اون یه تیکه از لیست باشه
# بدون به علاوه هم در اینجا میشد
# حتی بدون ایج در دیکشنری اول هم میشد
Details = {"Destination": "China", 
           "Nstionality": "Italian", "Age": []}
Details["Age"] += [20, "Twenty"]
print(Details)
# {'Destination': 'China', 'Nstionality': 'Italian', 'Age': [20, 'Twenty']}

# ///////////
# افزودن یک عنصر جدید یه لیست کد با اپند 
Details = {}
Details["Age"] = [20]
print(Details)
# {'Age': [20]}

if "Age" in Details:
    Details["Age"].append("Twenty")
    print(Details)
# {'Age': [20, 'Twenty']}



# ///////////
# افزودن یه تیکه به یه دیکشنری با دیفالت دیکت
from collections import defaultdict
Details = defaultdict(list)
Details["Country"].append("India")
print(Details)
# defaultdict(<class 'list'>, {'Country': ['India']})
# /////////
# آپدیت کردن دیکشنری
# بروز کردن دیکشنری
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x)
# {'apple', 'cherry', 'banana', 'microsoft', 'google'}

# /////
# اپدیت کردن یه دیکشنری
# اگر چیزی هم داشت بازهم فرقی نمیکرد پاکش میکنه 
Details = {}
Details["Age"] = [2,4]
print(Details)
# {'Age': [2, 4]}

Details.update({"Age": [18, 20, 25, 29, 30]})
print(Details)
# {'Age': [18, 20, 25, 29, 30]}

# ////
# حالا اگر اینو داشتیم 

Details = {}
Details["Age"] = [2,4]
print(Details)
# {'Age': [2, 4]}

Details.update({"pai": [18, 20, 25, 29, 30]})
print(Details)
# {'Age': [2, 4], 'pai': [18, 20, 25, 29, 30]}

# بهش اضافه میکرد و قبلی را هم نگا ه میداشت
# پس اگر کلید همنام بود متغیر های قبلی را حذف و تازه را جایگزین میکنه و
# اگر نبود ایجاد میکنه یعنی اضافه میکنه
# مثل متد اپد میمونه در لیست از این لحاظ


# ///////
# یه دیکشنری را برش میزنه
# به اندازه ای که خودمون تعنی کنیم 
 # 
import itertools
test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
 # {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
print("The original dictionary : " + str(test_dict))
N = 3
out = dict(itertools.islice(test_dict.items(), N))
print("Dictionary limited by K is : " + str(out))
# {'Geeks': 1, 'For': 2, 'is': 3}
print("///////////")

# چگونه یک دیکشنری را به تعداد دلخواه برش بزنیم
N=3
out = dict(itertools.islice(cor.items(), N))
print(str(out))


# به نصف برش بزنه

from itertools import islice
mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            
my=dict(islice(mydictha.items(),len(mydictha)//2))
print(my)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}

print("///////////")
# یک دیکشنری را برش میزند . بدون استفاده از متد . بلکه با لیست
# {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
# {'Geeks': 1, 'For': 2, 'is': 3}
test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
print("The original dictionary : " + str(test_dict))
N = 3
out = dict(list(test_dict.items())[0: N])
print("Dictionary limited by K is : " + str(out))

print("///////////")
# برش دادن بر دیکشنری که از N تای آخری را میده
# {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}

test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
print("The original dictionary : " + str(test_dict))
N = 3
out = dict(list(test_dict.items())[N:])
print("Dictionary limited by K is : " + str(out))
# {'best': 4, 'for': 5, 'CS': 6}


print("///////////")
# برش میزنه . N تای اول را برعکس میکنه میده
#     {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
print(" " + str(test_dict))
out = dict(list(test_dict.items())[3::-1])
print(" " + str(out))
#     {'best': 4, 'is': 3, 'For': 2, 'Geeks': 1}

print("///////////")
#دیکشنری را برعکس میکنه میده تا تعداد دلخواه
# {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
# {'CS': 6, 'for': 5, 'best': 4, 'is': 3, 'For': 2, 'Geeks': 1}
    test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
    print(" " + str(test_dict))
    N = 3
    out = dict(list(test_dict.items())[::-1])
    print(" " + str(out))


print("///////////")
# برش میزنه دیکشنری را از یه تعداد به قبل بر عکس میکنه
#     {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
#     {'best': 4, 'is': 3, 'For': 2, 'Geeks': 1}
    test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
    print(" " + str(test_dict))
    N = 3
    out = dict(list(test_dict.items())[N::-1])
    print(" " + str(out))

print("///////////")
# فقط سه تای آخر را میشماره میاره
    # {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
    # {'best': 4, 'for': 5, 'CS': 6}
    test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
    print(" " + str(test_dict))
    N = 3
    out = dict(list(test_dict.items())[-3:])
    print(" " + str(out))

print("///////////")
#4 تا میره عقب
    # {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6, 'kk': 6, 'GG': 6, 'PP': 6}
    # {'PP': 6, 'GG': 6, 'kk': 6, 'CS': 6}
    test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6, 'kk': 6, 'GG': 6, 'PP': 6, }
    print(" " + str(test_dict))
    out = dict(list(test_dict.items())[:-5:-1])
    print(" " + str(out))

print("///////////")
#موقع مثبت 5 تا میره از عقب به اول
    # {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6, 'kk': 6, 'GG': 6, 'PP': 6}
    # {'for': 5, 'best': 4, 'is': 3, 'For': 2, 'Geeks': 1}
    test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6, 'kk': 6, 'GG': 6, 'PP': 6, }
    print(" " + str(test_dict))
    out = dict(list(test_dict.items())[-5::-1])
    print(" " + str(out))


print("///////////")
# سورت میکنه به ترتیب کلید های دیکشنری
    # ولی نمیریزه تو یه تاپل واحد یا دیکشنری واحد بلکه برای پرینت میده
    # a: 1
    # b: 2
    # c: 3
    # d: 4
    my_dict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
    sorted_dict = my_dict.keys()
    sorted_dict = sorted(sorted_dict)
    print((sorted_dict))
    print("Sorted dictionary using sorted() and keys() is : ")
    for key in sorted_dict:
        print(key, ':', my_dict[key])

print("///////////")
# میاد به ترتیبی میریزه تو یه تاپل
#  [(1, 'two'), (2, 'three'), (3, 'four'), (4, 'five')]
    # 1 two
    # 2 three
    # 3 four
    # 4 five
    my_dict = {2: 'three', 1: 'two', 4: 'five', 3: 'four'}
    sorted_dict = sorted(my_dict.items())
    print("Sorted dictionary using sorted() and items() is :",sorted_dict)
    for k, v in sorted_dict:
        print(k, v)

print("///////////")

#بنابر کوچکترین به بزرگترین ولیو سورت میکنه . در values ha
    # lambda is: {'e': 12, 'a': 23, 'g': 67, 45: 90}

    my_dict = {'a': 23, 'g': 67, 'e': 12, 45: 90}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    print("Sorted dictionary using lambda is : ", sorted_dict)


print("///////////")
# همه عضو ها را جمع میزند
Sum: 600
    def returnSum(myDict):
        sum = 0
        for i in myDict:
            sum = sum + myDict[i]   # میگه هرکوم از ولیو ها را جمع بزن بریز توی سام با سام قبلی جمع کن
        return sum
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum :", returnSum(dict))
# Sum : 600

print("///////////")
# همه را میریزه تو یه دیکشنری جدید جمع میکنه
# {'hame': 600}
dicte = {'a': 100, 'b': 200, 'c': 300}
sum = 0
for i in dicte:
    sum = sum + dicte[i]
gam=dict()
gam['hame']= sum
print( (gam))

print("///////////")
# جمع زدن ولیو ها

# Sum: 600
    def returnSum(myDict):
        sum = 0
     sum = 0
     for i in dict.values():
           sum = sum + i
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum :", returnSum(dict))


print("///////////")
#کلید ها را از بزرگ به کوچک لیست میکنه. فقط کلید ها را

# The original dictionary is : {1: 'Gfg', 5: 'is', 4: 'the', 2: 'best'}
# The reversed order of dictionary keys : [5, 4, 2, 1]
test_dict = {1: "Gfg", 5: "is", 4: "the", 2: "best"}
print("The original dictionary is : " + str(test_dict))
res = []
for ele in reversed(sorted(test_dict.keys())):
    res.append(ele)
print("The reversed order of dictionary keys : " + str(res))


print("///////////")
# کلید ها را از بزرگ به کوچک لیست میکنه. و چون حروف بعدتر بزرگترند پس میاره.
# The original dictionary is : {'A': 'Gfg', 'B': 'is', 'C': 'the', 'D': 'best'}
# The reversed order of dictionary keys : ['D', 'C', 'B', 'A']
test_dict = {"A": "Gfg", "B": "is", "C": "the", "D": "best"}
print("The original dictionary is : " + str(test_dict))
res = []
for ele in reversed(sorted(test_dict.keys())):
    res.append(ele)
print("The reversed order of dictionary keys : " + str(res))

print("///////////")
# کلید ها را به ترتیب از بزرگ به کوچک میده
# The original : {1: 'Gfg', 5: 'is', 4: 'the', 2: 'best'}
# The reversed order: [5, 4, 2, 1]
#
test_dict = {1: "Gfg", 5: "is", 4: "the", 2: "best"}
print("The original dictionary is : " + str(test_dict))
res = list(reversed(sorted(test_dict.keys())))
print("The reversed order of dictionary keys : " + str(res))

print("///////////")
# لامبدا روی دیکشنری
# [1, 2]
#ولیو ها را داخل یه لیست میریزه لیست واحد که از دیکشنری گرفته
d = {'a': 1, 'b': 2}
values = list (map(lambda key: d[key], d.keys()))
print(values)

print("///////////")
# جمع بستن ولیو های دیکشنری
# 62
d = {'key1': 1,'key2': 14,'key3': 47}
print(sum(d.values()))
# /////
# ححلقه زدن تی بر دو دیکشنری  در یک حلقه
A={'player3': hagi, 'player1': ali}
B={'player2': mashti, 'player4': kablaii}

from collections import OrderedDict
for charA, charB in A , B:
    print(charA ,charB)
# player1 player3
# player4 player2  


# انم ولیو ها را میده
for charA, charB in A.values() , B.values():
    print(charA , charB)
    
# cvfv fgy
# fvg vgb

# print("///////////")
# حلقه یک خطی  در دیکشنری
# جمع بستن ولی ها 
# 62
d = {'key1': 1,'key2': 14,'key3': 47}
sum1 = sum(d[item] for item in d)
print(sum1)


print("///////////")
# جمع میکنه کنار اسم پرینت میزنه
# همه اعضای رون یک لیست را که ولیو است را با هم جمع میزنه
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
for k, v in string.items():
    print(k, sum(v))
# mandana 30
# hamid 57
# sina 52
# sara 39
# soheila 51
# ali 10
# sarvin 82
print("///////////")
# همه را جمع میزنه میریزه تو متغیرخودش
# دیکشنری یک خطی
# از لیست بودن خارج میکنه
# {'mandana': 30, 'hamid': 57, 'sina': 52, 'sara': 39, 'soheila': 51, 'ali': 10, 'sarvin': 82}
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
new= {k:(sum(v)) for k, v in string.items()}
print(new)

/////
# همون کد ولی خود  ولیو را لیست میکنه
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
new= {k:[(sum(v))] for k, v in string.items()}
print(new)
# {'mandana': [30], 'hamid': [57], 'sina': [52], 'sara': [39], 'soheila': [51], 'ali': [10], 'sarvin': [82]}



# /////////
# اما اگر اسکوار براکت را پشت بزاری میگه کلید را تعریف نکردی
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
new= {k:[(sum(v)) for k, v in string.items]}
print(new)
# {'mandana': [30], 'hamid': [57], 'sina': [52], 'sara': [39], 'soheila': [51], 'ali': [10], 'sarvin': [82]}
# NameError: name 'k' is not defined

print("///////////")
# جمع زدن متغیر ها

d = {'data': 100, 'data2': 200, 'data3': 500}
total = 0
for i in d.values():
    total += i
print(total)
# 800

print("///////////")
# جمع زدن ولیو ها با هم
d = {'key1': 1,'key2': 14,'key3': 47}
sum(list(d.values()))
# 62
print("///////////")
# میانگین همه ولیو ها با هم
from statistics import mean
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
print(mean(cor[k] for k in cor))
#8.401530612244898

print("///////////") 
# میانگین ولیو های یک دیکشنری با نام پای و پانداس
#8.401530612244898

from numpy import array
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
print(array([cor[k] for k in cor]).mean())
8.4015306122449


cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
import pandas
from pandas import Series
print(Series([cor[k] for k in cor]).mean())


print("///////////")
# جمع میبنده  همه ولیو ها را
# کلا متغیر را اینجوری حساب میکنه
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
print(sum(cor[k] for k in cor))

print("///////////")
print("///////////")
print("///////////")
print("///////////")
# جمع اخری را میده در یک دیکشنری دیگه میریزه
# {'k': 82}
string={'mandana': [5, 7, 3, 15], 'hamid': [3, 19,17,4,6,8], 'sina': [19,10,14,6,3], 'sara': [0,5,20,14], 'soheila': [13,2,5,1,12,14,4], 'ali': [1,9], 'sarvin': [0,16,16,7,2,19,8,14]}
new= {"k":(sum(v)) for k, v in string.items()}
print(new)


print("///////////")
# انجام عملیات  ریختن در یک دیکشنری جدید
#میانگین گرفتن و ریختن در یک دیکشنری جدید
#8.401530612244898

from statistics import mean
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
# همه ولیو ها را میانگین بگیر بعد کلید را کا قرار بده
cor_5= {'k' :mean(cor[v] for v in cor)}
print(cor_5)
# {'k': 8.401530612244898}
print("///////////")


print("///////////")


print("///////////")
# چگونه جای کلید ها و ولیو ها را عوض کنیم در دیکشنری ها ؟
# چگونه اعضای درون یک دیکشنری را ولیو ها را با هم جمع
# بزنیم( یعنی اعضا را ی هر کلید را جمع بزنیم درون یه لیست بریزیم) 
# و بعد اعضای همه ولیو را با هم جمع بزنیم و
# بریزیم تو یه ولیو و دیکشنری دیگه


# ////
print("//////////")

# سورت میکنه و بعد  از دیکشنری خارج میکنه تحویل میده
my_dict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
sorted_dict = my_dict.keys()
sorted_dict = sorted(sorted_dict)
print("Sorted dictionary using sorted() and keys() is : ")
for key in sorted_dict:
    print(key, ':', my_dict[key])
# a : 1
# b : 2
# c : 3
# d : 4
# ///////


print("//////////")
# بنابر  values ها دیکشنری را از بزرگ به کوچک میچینه
#The original dictionary is : {'Gfg': 1, 'is': 3, 'Best': 2, 'for': 3, 'Geeks': 2}
# Sorted dictionary : {'for': 3, 'is': 3, 'Best': 2, 'Geeks': 2, 'Gfg': 1}
test_dict = {"Gfg": 1, "is": 3, "Best": 2, "for": 3, "Geeks": 2}
print("The original dictionary is : " + str(test_dict))
res = {val[0]: val[1] for val in sorted(test_dict.items(), key=lambda x: (-x[1], x[0]))}
print("Sorted dictionary : " + str(res))

# //////
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟/
# نفهیمدم

d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
     'B': 34,
     'C': 12,
     'D': [7, 8, 9, 6, 4]}

print(sum([len(d[x]) for x in d if isinstance(d[x], list)]))
#14
# داره میگه هر کدوم از کلید هایی که در دی است
# اگر اون اون متغیر ولیو نوعش لیست بود


# توضیح جزیی
d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
     'B': 34,
     'C': 12,
     'D': [7, 8, 9, 6, 4]}
# ایزاینستنس تعین میکنه ایا این  ابجکت اون فرمت هست یا نه 
print(sum([len(d[x]) for x in d if isinstance(d[x], list)]))

for x in d:
    # print(x) 
# A
# B
# C
# D
    if isinstance(d[x],list):
        print(x)              # A  # D
        print(x,len(d[x]))    # A 9     D 5

# حالا میگه طول هر ایکس را بده که  اون ویژگی را داشت
# لن تعدادشو بده
# بعد چون دو تا اشتیم ای و بی 
# لن اون دو تا 9 , 5 با هم میشد ۱۴




# /////////////

# زدن حلقه 

enter= int(input('give me whole votes: '))
all_country=()
for key in range(enter):
    key =input('give me the name of country: ')
    all_country[key]='one'
    print(all_country)
# TypeError: 'tuple' object does not support item assignment


# //////////////
# جایگشت زدن روی دیکشنری
# یه بار عنصر اول را با دومی میاره یه بار عنصر دوم را با اولی
# خروجی تاپل میده
my = {1: 7, 3: 10}
import itertools
for k in itertools.permutations(my,2):
    print(k)
# (1, 3)
# (3, 1)

for k,v in itertools.permutations(my,2):
    print(k)
# 1
# 3
# ////////

# تبدیل کلید دیکشنری به تاپل ها به صورت دوبه دو
# ترکیب
# ترکیب در دیکشنری
# کلید ها را دو به دو مقایسه میکنه ترکیبشونو میاره
my = {1: 7, 3: 10}
print(list(itertools.combinations(my,2)))
# [(1, 3)]

# ////////////
# اوردن ولیو ها  در ترکیب
my = {1: 7, 3: 10}
from itertools import permutations , combinations , combinations_with_replacement
for k in combinations(my.values(),2):
    print(k)
# (7, 10)

# /////////
# اشاره به ایندکسی خاص در یک دیکشنری
# باید اردرد دیکت را اورد  و سپس اشاره به ایندکش کرد
from collections import OrderedDict
x = OrderedDict((("a", "1"), ("c", '3'), ("b", "2")))
x["d"] = 4
# x.keys().index("d")
# 3
print(list(x.keys()).index("c"))
# 1

# ولی نمیدونم چطور میشه در حلقه انداخت
# و در حلقه پرسید
# ///////////
# /////////
# بهم نریختن ترتیب هایی که در دیکشنری هست
# تبدیل دیکشنری به اردر دیکشنری
my = {1: 7, 3: 10}
x= OrderedDict(my)
print(x)
# OrderedDict([(1, 7), (3, 10)])

# ///////////////
# ساخت یک ددیکشنری خالی از اول از اردردیکشنری
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
# //////////
# مقایسه یک دیکشنری و یک لیست 
# و اگر عنصری از لیست توی دیکشنری بود ترجمه کنه وگرنه خودشو برگردونه ترجمه کنه
def requaired_sentence():
    # my_vanameh=converter_lt_2_d()
    my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
    my_vazhenameh=collections.OrderedDict(((my_vazhenameh.items())))
    print(my_vazhenameh) 
    # sentence=input('give me the sentence for translating: ').split()
    sentence=['you','say','to','i','guy','hello']
# ساخت لیست یک خطی و بررسی شرطی که اگر نبود خودشو بزاره و اگر بود جایگزین اون ولیو اون کلید را بزاره
    replaced_list=[ x if x not in my_vazhenameh  else my_vazhenameh[x]  for x in sentence]
    return (replaced_list)
# ['tu', 'say', 'to', 'man', 'guy', 'dorod']

# //////////////////////
# اینم همونه با لامبدا
replace = lambda my_dict, my_list: [x if x not in my_dict else my_dict[x] for x in my_list]

# ////////////////
# خودش تبدیل میکنه لیست تاپل ها را به دیکشنری
data = [('sravan', 23), ('ojaswi', 15),
        ('rohith', 8), ('gnanesh', 4), ('bobby', 20)]
 
# using dict method
dict(data)

# /////////////////////////////////////
# تبدیل یک لیست به دیکشنری 
# اجرای یک تابع روی تک تک اعضای یک لیست و تبدیل اعضا به ولیو

# با اجرایی که اول خود  عدد لیست قبلی را کلید کنه و ولیو را یه تابع باشه
# که از اعضای لیست بدست اومده 

# ۱- 
# این میاد به اندازه تعداد هر کدوم همه را لیست میکنه 
my_list=[4,1,2,19,100]
my_dict={ char :list(map(sqrt,my_list)) for char in (my_list) } 
# {4: [2.0, 1.0, 1.4142135623730951, 4.358898943540674, 10.0], 1: [2.0, 1.0, 1.4142135623730951,
# 4.358898943540674, 10.0], 2: [2.0, 1.0, 1.4142135623730951, 4.358898943540674, 10.0], 19: [2.0, 1.0, 1.4142135623730951, 4.358898943540674, 10.0], 100: [2.0, 1.0, 1.4142135623730951, 4.358898943540674, 10.0]}

# این تقریبا چیزی است که میخوام 
my_dict={ char :list(map(sqrt,[char])) for char in (my_list) }   
# {4: [2.0], 1: [1.0], 2: [1.4142135623730951], 19: [4.358898943540674], 100: [10.0]}

# اما اگر نخوام که درون لیست باشه چی؟


# ////////
# بد
# حالا اگر بخوایم به استرینگ تبدیل کنیم
my_dict={char:(list (str(map(sqrt,{char})))) for char in (my_list) }  
# {4: ['<', 'm', 'a', 'p', ' ', 'o', 'b', 'j', 'e', 'c', 't', ' ', 'a', 't', ' ', '0', 'x', '0', '0', '0', '0', '0', '1', '8', 'D', '4', '6', 'A', '3', 'F', 'E', '8', '0', '>'],
#  1: ['<', 'm','a', 'p', ' ', 'o', 'b', 'j', 'e', 'c', 't', ' ', 'a', 't', ' ', '0', 'x', '0', '0', '0', '0', '0', '1', '8', 'D', '4', '6', 'A', '3', 'F', 'E', '8', '0', '>'], 
#  2: ['<', 'm', 'a', 'p', ' ', 'o', 'b', 'j', 'e', 'c', 't', ' ', 'a', 't', ' ', '0', 'x', '0', '0', '0', '0', '0', '1', '8', 'D', '4', '6', 'A', '3', 'F', 'E', '8', '0', '>'], 
#  19: ['<', 'm', 'a', 'p', ' ', 'o', 'b', 'j', 'e', 'c', 't', ' ', 'a', 't', ' ', '0', 'x', '0', '0', '0', '0', '0', '1', '8', 'D', '4', '6', 'A', '3', 'F', 'E', '8', '0', '>'], 
#  100: ['<', 'm', 'a', 'p', ' ', 'o', 'b', 'j', 'e', 'c', 't', ' ', 'a', 't', ' ', '0', 'x', '0', '0', '0', '0', '0', '1', '8', 'D', '4', '6', 'A', '3', 'F', 'E', '8', '0', '>']}
# که خراب شده 

# ////////////


# //////////
هرجا مساوی دید
# دو حلقه در دیکشنری تک خطی
string = "a=0 b=1 c=3"
list = string.split()
dic = {}

 dict( (n,int(v)) for n,v in (a.split('=') for a in string.split() ) )
# {'a': 0, 'c': 3, 'b': 1}


# ////////////////

# Declaring a dictionary
d = {} 
  
# This is the list which we are 
# trying to use as a key to
# the dictionary
a =[1, 2, 3, 4, 5]
  
# converting the list a to a string
p = str(a)
d[p]= 1
  
# converting the list a to a tuple
q = tuple(a) 
d[q]= 1
  
for key, value in d.items():
    print(key, ':', value)
# [1, 2, 3, 4, 5] : 1
# (1, 2, 3, 4, 5) : 1

# ////////////////////////////////////////////////////////


# //////////////////
# فقط اخری را میاره
a = [['Robert'], ['Tommy'], ['Joe'], ['Will']]
dct = {}
for i in range(len(a)):
    dct['Name'] = a[i]
price(dct)

# {'Name': ['Will']}
# ////////////////////////////////////////////////
a = [['Robert'], ['Tommy'], ['Joe'], ['Will']]
dct = {}
for i in range(len(a)):
    dct['Name'] = a
print(dct)
# {'Name': [['Robert'], ['Tommy'], ['Joe'], ['Will']]}



# ///////////

# تبدیل دیکشنری به استرینگ
# تبدیل ولیو به استرینگ 
# تبدیل لیست به استرینگ
my_dict={4: [2.0], 1: [1.0], 2: [1.4142135623730951], 19: [4.358898943540674], 100: [10.0]}
# حالا اگر میخوایم که فقط ولیو ها را بیاره

# //////////
# این فقط ولیو ها را میاره
    for char in my_dict.values():
        print(char)
# [2.0]
# [1.0]
# [1.4142135623730951]
# [4.358898943540674]
# [10.0]


# ///////////////////
# اگر بخوایم که از لیست خارج کنه و ۴ رقم اعشار بده
# ایا این میشه
# نه
# این خود براکت لیست را هم استرینگ میده
for char in my_dict.values():
        l3.append((''.join(str(char))))
    print(l3)
# ['[2.0]', '[1.0]', '[1.4142135623730951]', '[4.358898943540674]', '[10.0]']

# اینم نمیشه
# جالبه متد جوین میشه درونش با or
# بکار بره
for char in my_dict.values():
        l3.append(('['or ']'.join(str(char))))
    print(l3)
# ['[', '[', '[', '[', '[']


    for char in my_dict.values():
        l3.append(('['and ']'.join(str(char))))
    print(l3)
# ['[]2].]0]]', '[]1].]0]]', '[]1].]4]1]4]2]1]3]5]6]2]3]7]3]0]9]5]1]]', '[]4].]3]5]8]8]9]8]9]4]3]5]4]0]6]7]4]]', '[]1]0].]0]]']

# ////////
# راه حل اینه که  دو حلقه بزنی 
# که از حلقه خارج کنه
    for char in my_dict.values():
        for i in char:
            print(i)
            
            
# این از حلقه خارج میکنه . اعشار را هم ۴ تا میده در پرینت
    for char in my_dict.values():
        for i in char:
            # a= ( (i))
            (print('%.4f'%i))
# 2.0000
# 1.0000
# 1.4142
# 4.3589
# 10.0000

# /////////////////////////////////////////////
# باز کردن دیکشنری 
# تبدیل ولیو لیست شده درون دیکشنری 
# اشاره به ولیو و کلید ها وقتی که ولیو لیست باشه 
    # my_dict={char:(list((map(sqrt,{char})))) for char in (my_list) } 
    my_dict={4: [2.0], 1: [1.0], 2: [1.4142135623730951], 19: [4.358898943540674], 100: [10.0]} 
    l3=[]
    for kel in my_dict:
        for val in my_dict[kel]:
            print(kel , val)
# 4 2.0
# 1 1.0
# 2 1.4142135623730951
# 19 4.358898943540674
# 100 10.0

# /////////////////////////////
# تبدیل لیست به دیکشنری . دیکشنری ببه دیکشنری 
# تبدیل یک دیکشنری به دیکشنری  تازه
# وقتی که یه عملیات روی ولیو  اجرا میکنی و سپس تیکه تیکه تبدیل میکنی

# همتراز کردن ایندکس یک ولیو با  کلید خودش بدون اشاره به ایندکس

# اپند کردن به دیکشنری تازه


    # my_dict={char:(list((map(sqrt,{char})))) for char in (my_list) }  
    my_dict={4: [2.0], 1: [1.0], 2: [1.4142135623730951], 19: [4.358898943540674], 100: [10.0]} 
    
    my2={}
    # میگی به ازای هر کلید در دیکشنری. چون همیشه وقتی اشاره نشه منظور کلید است
    for kel in my_dict:
        # به ازای هر کلید هر ولیو که داره را 
        # تیکه دوم حلقه برابر با همون ولیو است
        # توجه شود اگر شکلشو نمیزدیم این شکلی میرفت دوباره سایر کلید ها را با هم مقایسه میکرد . سینتکس مقید کرد به ولیو
        for val in my_dict[kel]:
            #   در اینجا اپند می کنیم .append() 
            # اپند در دیکشنری تازه
            my2[kel]=val
            # حالا اون کلید را کلید تازه کن و ولیو را باز شده کن ولیو کن . یعنی از لیست خارج کن و ولیو دیکشنری تازه کن
            
    print(my2)
    
    
# //////////////////////////
    my_dict={4: [2.0], 1: [1.0], 2: [1.4142135623730951], 19: [4.358898943540674], 100: [10.0]} 

    my2={}
    # میگی به ازای هر کلید در دیکشنری. چون همیشه وقتی اشاره نشه منظور کلید است
    for kel in my_dict:
        # به ازای هر کلید هر ولیو که داره را 
        # تیکه دوم حلقه برابر با همون ولیو است
        for val in my_dict[kel]:
            # در اینجا اپند می کنیم .append() 
            # اپند در دیکشنری تازه
            my2 [kel]=('%.2f'%val)
            # حالا اون کلید را کلید تازه کن و ولیو را باز شده کن ولیو کن . یعنی از لیست خارج کن و ولیو دیکشنری تازه کن
            # حالا بجای ولیو ساده میشد با درصد گذاری دسیمالشو دستکاری کنیم بدیم .حتی یه تابع هم یه ضرب پیاده کنیم روش
    # print(my2)
# {4: '2.00', 1: '1.00', 2: '1.41', 19: '4.36', 100: '10.00'}

# ///////////////////////


marks=[{'name':'Seema', 'age':22, 'marks':45}, {'name':'Anil', 'age':21, 'marks':56}, {'name':'Mike', 'age':20, 'marks':60}]
csvfile=open(marks.csv','w', newline='')
fields=list(marks[0].keys())
 
# name,age,marks

# //////////////
# ساخت دیکشنری تودروتو
Dict = { }
print("Initial nested dictionary:-")
print(Dict)
# Initial nested dictionary:-
# {}

Dict['Dict1'] = {}
# Adding elements one at a time
Dict['Dict1']['name'] = 'Bob'
Dict['Dict1']['age'] = 21
print("\nAfter adding dictionary Dict1")
print(Dict)
#  {'Dict1': {'name': 'Bob', 'age': 21}}

# Adding whole dictionary
Dict['Dict2'] = {'name': 'Cara', 'age': 25}
print("\nAfter adding dictionary Dict1")
print(Dict)

After adding dictionary Dict1
# {'Dict1': {'age': 21, 'name': 'Bob'}, 'Dict2': {'age': 25, 'name': 'Cara'}}


# //////////

# ساخت دیکشنری تو در تو از لیست تو در تو
import collections

L = [[0,[1,1.0]],
     [0,[2,0.5]],
     [1,[3,3.0]],
     [2,[1,0.33]],
     [2,[4,1.5]]]

d = collections.defaultdict(dict)
for k, (sub_k, v) in L:
    print('d[k]',d[k])
    print('k',k)
    print('sub_k',sub_k)
    print('v',v)
    print('[sub_k]',[sub_k])
    # این خط را در دیکشنری تودر تو پایین توضیح دادم
    d[k][sub_k] = v
# میاد اول دیکشنری را میاره که ساخته
# d[k] {}
# بعد این پایینی  عنصر  اول  لیست اول را کلید  میکنه یعنی کلید دیکشنری اول دیکشنری کلی 
# k 0
# بعد اشاره به  عنصر اول لیست  دومی درون لیست اولی  میکنه
# sub_k 1 
# این اشاره به عنصر دوم لیست میده
# v 1.0 
# اینجا اون عنصر اول لیست را هم به کلید تبدیل میکنه. کلیدی که خودش دیکشنری تو در تو است
# [sub_k] [1]
# d[k] {1: 1.0}
# k 0
# sub_k 2
# v 0.5
# [sub_k] [2]
# d[k] {}
# k 1
# sub_k 3
# v 3.0
# [sub_k] [3]
# d[k] {}
# k 2
# sub_k 1
# v 0.33
# [sub_k] [1]
# d[k] {1: 0.33}
# k 2
# sub_k 4
# v 1.5
# [sub_k] [4]
# print(dict(d))
# {0: {1: 1.0, 2: 0.5}, 1: {3: 3.0}, 2: {1: 0.33, 4: 1.5}}

# //////


# دسترسی به ایندکس  مد نظر خودمان در دیکشنری
# index
mydict={'z':3,'k':4,'n':'aban'}
# اگر همینجوری پرینت کنی خطا میده
# print((mydict.keys()[1]))
# TypeError: 'dict_keys' object is not subscriptable

# برای این باید بریزی توی یه اردر دیکت
from collections import OrderedDict
data = OrderedDict(mydict) # data = OrderedDict([('Key1', 'Value1'), ('Key2', 'Value2')])
print(list(data.keys())[0])
# z

# یا روش دیگر 
# این دفعه دسترسی به ایتمز ها
mydict={'z':3,'k':4,'n':'aban'}
print(list(mydict.items())[1])   
# ('k', 4)



# روش دیگر کاربرد نکست است
# ولی فقط اولی را میده
# چون در نکست اول از اولی اغاز میکنه دیگه
mydict={'z':3,'k':4,'n':'aban'}
first_key = next(iter(mydict.keys()))
print(first_key)
# z

print("///////////")

# کار با دیکشنری تودرتو
# https://www.geeksforgeeks.org/python-nested-dictionary/
# ////////////////
# دیکشنری تودرتو و دسترسی به اون
# پله پله ای
data= {bpi:{usd:{rate:36.852.61111}}}
# البته برای سهولت خوندن معمولا اینجوری مینویسن
{bpi:{usd:{rate:36.852.61111
        }
    }
}

# حالا برای دسترسی به اون  ریت
data[bpi][usd][rate]
# اگر پرینت کنیم
print(data[bpi][usd][rate])
# این خروجی را میده
36.852.61111

# ایا اگر یه کلید را نمیدونستیم که توی چند تا دلشه چجوری پیدا کنیم؟
# با find یا با where ?
# بیاد بگرده که کلید کدومه که اگر نبود بره ریز تر و اگر نبود بازهم میریه ریزتر همینطور تا اینکه پیدا کنه

# ///////
# دسترسی به دیکشنری تودرتو
# یکی درون یک بزرگتر
# کلید بیرون باشه

students = {
    123: {'name' : 'Alice', 'age': '23'},
    321: {'name' : 'Bob', 'age': '34'}
}
for key, value in students.items():
    print(f"{key}: {value['name']}")
# 123: Alice
# 321: Bob
# ///////////
توجه کلید نمیتونه متغیری باشه که از قبل تعریف نشه
باید استرینگ باشه
یا حتی میشه عدد باشه
ولی متغیر نمیتونه


SITUATIONS = {
                 situation_1: {{player_1: [1, 2, 3, 4]}, {player_2: [1, 2, 3, 4]}},
                 situation_2: {{player_1: [1, 2, 3, 4]}, {player_2: [1, 2, 3, 4]}},
                 situation_3: {{player_1: [1, 2, 3, 4]}, {player_2: [1, 2, 3, 4]}},
                 situation_4: {{player_1: [1, 2, 3, 4]}, {player_2: [1, 2, 3, 4]}},
# NameError: name 'situation_1' is not defined

# درست اینه
SITUATIONS = {
                 'situation_1': {{'player_1': [1, 2, 3, 4]}, {'player_2': [1, 2, 3, 4]}},
                 'situation_2': {{'player_1': [1, 2, 3, 4]}, {'player_2': [1, 2, 3, 4]}},
                 'situation_3': {{'player_1': [1, 2, 3, 4]}, {'player_2': [1, 2, 3, 4]}},
                 'situation_4': {{'player_1': [1, 2, 3, 4]}, {'player_2': [1, 2, 3, 4]}}}
# NameError: name 'situation_1' is not defined


# هرچند اینم این خطا را میده

unhashable type: 'dict'

# راه
'situation_1': {'player_1': [1, 2, 3, 4], 'player_2': [1, 2, 3, 4]}



                                //////////////
# دسترسی به دیکشنری تودروتو
# فقط کلید ها را بده
d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}
for i in d:
    print i
    for j in d[i]:
        print j
# dict1 
# foo
# bar

# dict2
# baz 
# quux


# ////
# دسترسی به دیکشنری های درون دیکشنری
# که این خطا را نده
# TypeError: unhashable type: 'dict'
# پاسخ: این دیکشنری نیست 
d= {
    {'a':3,'b':4,'d':'aban'},
    {'c':4,'g':6,'j':'f'}
}
# ساخت دیکشنری کلید و دو نقطه ولیو است
d={k:v}
# و این دو نقطه نداره
# {'a':3,'b':4,'d':'aban'}
# {'c':4,'g':6,'j':'f'}



# این را میتونی لیست کنی بعد دسترسی پیدا کنی
d= [
    {'a':3,'b':4,'d':'aban'},
    {'c':4,'g':6,'j':'f'}
]


#    یک دیکشنری میشه به عنوان ولیو باشه. ولی به عنوان کلید نمیشه
# TypeError: unhashable type: 'dict'
# اینم نمیشه
# راه حل اینه یا میتونی دیکشنری اول را کلید کنی و دیکشنری دوم را ولیو
d= {
    {'a':3,'b':4,'d':'aban'}:
    {'c':4,'g':6,'j':'f'}
}


# بلکه اینم نمیشه
d= {{'a':3,'b':4,'d':'aban'}:4}

# بلکه   یک دیکشنری میشه به عنوان ولیو باشه. ولی به عنوان کلید نمیشه
d= {4 :{'a':3,'b':4,'d':'aban'}}



# /////
# بعد اینو میخوام
# بگم عنصر اول هر دیکشنری را بده
# دسترسی به  دیکشنرهایی از لیست
# دیکشنری تودرتو

my_dict= [
    
        {'a':3,'b':4,'d':'aban'},{'c':4,'g':6,'j':'f'}

]
    
# مساله چگونه به این عضو دسترس داشته باشم
# a=3
# c=4

# یا حتی 
# 3
# 4

# دسترسی


# گام به گام
my_dict= [
        {'a':3,'b':4,'d':'aban'},{'c':4,'g':6,'j':'f'}
]

print(my_dict)
# [{'a': 3, 'b': 4, 'd': 'aban'}, {'c': 4, 'g': 6, 'j': 'f'}]

print(my_dict[0])
# {'a': 3, 'b': 4, 'd': 'aban'}

for char in my_dict:
    print(char)
# {'a': 3, 'b': 4, 'd': 'aban'}
# {'c': 4, 'g': 6, 'j': 'f'}

for char in my_dict:
    for k,v in char.items():
        print(k, v)
# a 3
# b 4
# d aban
# c 4
# g 6
# j f

# حالا اگر کلیدی  همون چیزی بود که ما میخواستیم 
for char in my_dict:
    for k,v in char.items():
        if k == 'a':
            print(k,v)
# a 3
# a 4

# یه شیوه دیگه اینه
print(my_dict[0]['a'])  
# 3 
print(my_dict[1]['a'])   
# 4  


# حالا 
# دسترسی به ایندکس کلید مدنظر دیکشنری های درون یک لیست
# مثلا ما فقط میخوایم کلید ایندکس یک را بده یعنی کلید دوم را از هر دیکشنری
my_dict= [
        {'a':3,'b':4,'d':'aban'},{'a':4,'g':6,'j':'f'}
]

for char in my_dict:
    new=OrderedDict(char)
    for k in (list(new.keys())[1]):
       print (k)
# b
# g

# اما برای ولیو اینو نمیده

# بجاش میشه ایتمز را بزنی هر دو را میده
my_dict= [
        {'a':3,'b':4,'d':'aban'},{'a':4,'g':6,'j':'f'}
]

for char in my_dict:
    new=OrderedDict(char)
    for k in (list(new.items())[1]):
       print (k)
# b
# 4
# g
# 6
  
# ولی مساله اینه که یک کلید داره

# این کد هم فقط ولیو ها را همشونو میده
for char in my_dict:
    new=OrderedDict(char)
    for k in ((new.items())):
       print (list(k)[1])
# 3
# 4
# aban
# 4
# 6
# f

# دسترسی به کلید های  همه دیکشنری های یک لیست
for char in my_dict:
    new=OrderedDict(char)
    for k ,v in ((new.items())):
       print ((k))
# a
# b
# d
# a
# g
# j

# دسترسی به کلید و ولیو های نخست هر دیکشنری 
for char in my_dict:
    print(char)
    # {'a': 3, 'b': 4, 'd': 'aban'}
    # {'a': 4, 'g': 6, 'j': 'f'}
    k, v = next(iter(char.items()))
    print(k,v) 
# a 3
# a 4

# این کد فقط ولیو را میده
for char in my_dict:
    print(char)
    k, v = next(iter(char.items()))
    print(v)
# 3
# 4

# اینم همونو میده
# دسترسی به ولیو های نخست یک کلید
for char in my_dict:
    print(char)
    v = next(iter(char.values()))
    print(v)
# 3
# 4


# اما اگر بخوایم به دومین کاراکتر ها دسترسی داشته باشیم چی؟
# ؟؟؟؟؟؟؟؟؟؟؟

# چگونه از نکست بعدی استاده کنیم؟

# راه ۱
# این کد دوباره همون را میزنه
for char in my_dict:
    print(char)
    v = next(iter(char.values()))
    g=next(iter(char.values()))
    print(v)
    print(g)
# 3
# 4

# راه ۲
# اردرد دیکت
# گام ۱
for char in my_dict:
    print(char)
    # {'a': 3, 'b': 4, 'd': 'aban'}
    # {'a': 4, 'g': 6, 'j': 'f'}
    new=OrderedDict(char)
    print(new)
# OrderedDict([('a', 3), ('b', 4), ('d', 'aban')])
# OrderedDict([('a', 4), ('g', 6), ('j', 'f')])

# تغیر نوع یک دیکشنری به نوع دیگر دیکشنری در حلقه. کافیه درون اون حلقه بیاری نه بیرون از اون

# گام ۲
for char in my_dict:
    print(char)
    new=OrderedDict(char)
    print(new)
    print(list(new.items())[1])
# ('b', 4)
# ('g', 6)

# حالا اگر فقط دسترسی داشته باشیم به ولیو های کلید دوم
for char in my_dict:
    print(char)
    new=OrderedDict(char)
    print(new)
    print(list(new.values())[1])
# 4
# 6

# توجه شود که اگر بجای 
char
# خود دیکشتری را بزاریم فقط کلیدهارا میده
for char in MYlist:
    print(char)
# {'player3': ffsdv ,43 , fv, 'player2': ffsdv ,43 , fv}
# {'player4': ffsdv ,43 , fv, 'player1': ffsdv ,43 , fv}
# چه مشکلی هست که اردر دیکت اومده ترتیب را فقط کلاس ها را لحاظ کرده و نه ولیو ها 
# و جالبه که حتی وقتی میزنیم ولیو اسم کلید را میده
    new=OrderedDict(MYlist)
    print(new)
# OrderedDict([('player3', 'player2'), ('player4', 'player1')])
# OrderedDict([('player3', 'player2'), ('player4', 'player1')])    
    print(list(new.items())[0])
# [('player3', 'player2'), ('player4', 'player1')]
# [('player3', 'player2'), ('player4', 'player1')]

    
# ////////////
# اجرای یک حلقه دوتایی روی  دو دیکشنری

a=my2[0]
b=my2[1]
# print(my2_1) #{'player3': hagi, 'player1': ali}
# print(my2_2) #{'player2': mashti, 'player4': kablaii}
A=OrderedDict(a)
B=OrderedDict(b)
# TypeError: 'odict_items' object is not subscriptable

for charA, charB in list(A.items()[0]) , list(B.items()[0]):
    print(charA , charB)

# .....
# ولی این کار میکنه
for charA, charB in A.items() , B.items():
    print(f'Team A IS : {list(charA)[1]} ,\n Team B IS : {list(charB)[1]}')
# {'player1': DF, 'player2': DVER, 'player3': QEERF, 'player4': JY}
# Team A IS : JY ,
#  Team B IS : DF
# Team A IS : DVER ,
#  Team B IS : QEERF

# که این تمیزتره
for charA, charB in A.items() , B.items():
    print({list(charA)[1]} , {list(charB)[1]}')
# {'player1': DF, 'player2': DVER, 'player3': QEERF, 'player4': JY}
# Team A IS : JY ,
#  Team B IS : DF
# Team A IS : DVER ,
#  Team B IS : QEERF

# //////
# دادن ولیو  بعدی  در دیکشنری
mydict={'a':3,'b':4,'d':'aban'}
my=(iter(mydict.values()))
print(next(my))
# 3
print(next(my))
# 4
print(next(my))
# aban
# ////////
# یه دیکشری تو در تو میخوام
# که این را بگیره
Week,Ali Khamenei: (Iran),Reza Pahlavi: (Iran)
# عدد اول خامنه ای و عدد دوم پهلوی

2022-01-16,9,1
2022-01-23,14,1
2022-01-30,15,1
2022-02-06,13,1
# بعد اینو بده
{2022-01-16,9,1}=[{Ali Khamenei: 9} ,{Reza Pahlavi: 1} ]
# که بعد بیام مقایسه کنم
# ولیو های اون ولیو ها را
{Ali Khamenei: 9} با  {Reza Pahlavi: 1}
# که مثلا رضا پهلوی رای هاش در این تاریخ بیشتر از خامنه ای بود 

# برای قسمت اول
    my_vrodi=csv.reader(vorodi)
    my_members=list(my_vrodi)
    my_dict={}
# ساخت  عنصر اول های دو دیکشنری, 
# از دسترسی به عنصر های اول لیست
# ساخت  لیستی از ولیو ها
    for char in (my_members[5:]):
        my_dict[char[0]]= [char[1],char[2]]
    print(my_dict)
    # این بهمون اینو میده
# {'2022-01-16': ['9', '1'],
# '2022-01-23': ['14', '1'], 
# '2022-01-30': ['15', '1'], 
# '2022-02-06':['13', '1'],
# '2022-02-13': ['11', '1'], }
# این ناقص است ولی اون چیزی نیست که دقیقا میخوام



# کل لیست اولیه  تو در تو ما اینه :
# [['Category: All categories'], ['# ع©ط¯غŒ ع©ظ‡ ط¨غŒط§ط¯  طھط§ط±غŒط® ط±ط§ ط¨ظ‡ ط´ظ…ط³غŒ طھط¨ط¯غŒظ„ ع©ظ†ظ‡ ظˆ ط³ظ¾ط³ ظ…ظ‚ط§غŒط³ظ‡ ع©ظ†ظ‡ '], ['#ط\xadطھغŒ ط¨ط¹ط¯ط´ ظ…طھ ظ¾ظ„ط§طھ ظ„غŒط¨ ع©ظ†ظ‡'], ['#ط¯غŒع©ط´ظ†ط±غŒ ع©ظ†ظ‡'], ['Week', 'Ali Khamenei: (Iran)', 'Reza Pahlavi: (Iran)'], ['2022-01-16', '9', '1'], ['2022-01-23', '14', '1'], ['2022-01-30', '15', '1'], ['2022-02-06', '13', '1'], ['2022-02-13', '11', '1'], ['2022-02-20', '10', '1'], ['2022-02-27', '10', '1'], ['2022-03-06', '9', '1'], ['2022-03-13', '9', '1'], ['2022-03-20', '15', '2'], ['2022-03-27', '13', '1'], ['2022-04-03', '14', '1'], ['2022-04-10', '13', '<1'], ['2022-04-17', '18', '<1'], ['2022-04-24', '16', '<1'], ['2022-05-01', '18', '1'], ['2022-05-08', '14', '1'], ['2022-05-15', '13', '1'], ['2022-05-22', '13', '1'], ['2022-05-29', '18', '6'], ['2022-06-05', '16', '5'], ['2022-06-12', '10', '2'], ['2022-06-19', '10', '2'], ['2022-06-26', '10', '1'], ['2022-07-03', '9', '1'], ['2022-07-10', '11', '1'], ['2022-07-17', '11', '1'], ['2022-07-24', '10', '1'], ['2022-07-31', '13', '1'], ['2022-08-07', '14', '1'], ['2022-08-14', '9', '2'], ['2022-08-21', '11', '1'],
# ['2022-08-28', '15', '1'], ['2022-09-04', '18', '1'], ['2022-09-11', '100', '1'], ['2022-09-18', '93', '4'], ['2022-09-25', '61', '4'], ['2022-10-02', '85', '4'], ['2022-10-09', '38', '4'],
# ['2022-10-16', '33', '6'], ['2022-10-23', '29', '4'], ['2022-10-30', '27', '3'], ['2022-11-06', '19', '3'], ['2022-11-13', '25', '3'], ['2022-11-20', '22', '2'], ['2022-11-27', '19', '2'], ['2022-12-04', '30', '2'], ['2022-12-11', '19', '2'], ['2022-12-18', '17', '2'], ['2022-12-25',
# '17', '2'], ['2023-01-01', '21', '2'], ['2023-01-08', '21', '2']]

# این کد جواب نمید
with open ('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\multiTimeline (2).csv','r')as vorodi:
    my_vrodi=csv.reader(vorodi)
    my_members=list(my_vrodi)
    my_dict={}
    khamenei={}
    pahlavi={}
    for char in (my_members[5:]):
        my_dict[char[0]]=  k
        hamenei[my_members[4][1]]= char[1] ,pahlavi[my_members[4][2]]=char[2]
    print(my_dict)
        
# ValueError: not enough values to unpack (expected 2, got 1)
# یا اگر تاپل کنی ولیو را
        my_dict[char[0]]=  (khamenei[my_members[4][1]]= char[1] ,pahlavi[my_members[4][2]]=char[2])

#  cannot assign to subscript here. Maybe you meant '==' instead of '='?
# //////////
# اگر تکی بیاری میشه
    for char in (my_members[5:]):
        khamenei[my_members[4][1]]= char[1]
        pahlavi[my_members[4][2]]=char[2]
        my_dict[char[0]]= khamenei[my_members[4][1]]= char[1] 
    print(my_dict)   
    # {'2022-01-16': '9', '2022-01-23': '14', '2022-01-30': '15', '2022-02-06': '13', '2022-02-13': '11', '2022-02-20': '10', '2022-02-27': '10', '2022-03-06': '9', '2022-03-13': '9', '2022-03-20': '15', '2022-03-27': '13', '2022-04-03': '14', '2022-04-10': '13', '2022-04-17': '18', '2022-04-24': '16', '2022-05-01': '18', '2022-05-08': '14', '2022-05-15': '13', '2022-05-22': '13', '2022-05-29': '18', '2022-06-05': '16', '2022-06-12': '10', '2022-06-19': '10', '2022-06-26': '10', '2022-07-03': '9', '2022-07-10': '11', '2022-07-17': '11', '2022-07-24': '10', '2022-07-31': '13', '2022-08-07': '14', '2022-08-14': '9', '2022-08-21': '11', '2022-08-28': '15', '2022-09-04': '18', '2022-09-11': '100', '2022-09-18': '93', '2022-09-25': '61', '2022-10-02': '85', '2022-10-09': '38', '2022-10-16': '33', '2022-10-23': '29', '2022-10-30': '27', '2022-11-06': '19', '2022-11-13': '25', '2022-11-20': '22', '2022-11-27': '19', '2022-12-04': '30', '2022-12-11': '19', '2022-12-18': '17', '2022-12-25': '17', '2023-01-01': '21', '2023-01-08': '21'}                    
# ولی مساله اینه که
# هم فقط ولیو را میاره نه نستد دیکشنری
# مثل این میمونه
my_dict[char[0]]= char[1]

# هم 
# هر دو با هم نمیشه یعنی دو تا دیکشنری نمیاره




# ///////
# در دو ضرب درست کنیم
# دو شات
# اما
# این هم فقط دیکشنری اخر را میاره 

    for char in (my_members[5:]):
        khamenei[my_members[4][1]]= char[1]
        pahlavi[my_members[4][2]]=char[2]
        # my_dict[char[0]]= 
     
    print(khamenei) 
    print(pahlavi)                        
# {'Ali Khamenei: (Iran)': '21'}
# {'Reza Pahlavi: (Iran)': '2'}    

# ValueError: not enough values to unpack (expected 2, got 1)


# ///////////
# ساخت دیکشنری تودرتو
Dict = { 'Dict1': { },
         'Dict2': { }}

# /////////////
# روش ساخت دیکشنری از لیست تودرتو
# وقتی لیستی بداری که ۲ تا تودرتویی  داشته باشه
# تبدیل لیست به دیکشنری
import collections
L = [[0,[1,1.0]],
     [0,[2,0.5]],
     [1,[3,3.0]],
     [2,[1,0.33]],
     [2,[4,1.5]]]

d = collections.defaultdict(dict)
for k , (sub_k ,v) in L:
    print('d[k]',d[k])
    print('k',k)
    print('sub_k',sub_k)
    print('v',v)
    print('[sub_k]',[sub_k])
    
    
    # اما این خط چه معنی ای داره؟
    # ساخت دیکشنری تودروتو جستجو کن
    # در بالا
    d[k][sub_k] = v  
# میاد اول دیکشنری را میاره که ساخته
# d[k] {}
# بعد این پایینی  عنصر  اول  لیست اول را کلید  میکنه یعنی کلید دیکشنری اول دیکشنری کلی 
# k 0
# بعد اشاره به  عنصر اول لیست  دومی درون لیست اولی  میکنه
# sub_k 1 
# این اشاره به عنصر دوم لیست میده
# v 1.0 
# اینجا اون عنصر اول لیست را هم به کلید تبدیل میکنه. کلیدی که خودش دیکشنری تو در تو است
# [sub_k] [1]
# d[k] {1: 1.0}
# k 0
# sub_k 2
# v 0.5
# [sub_k] [2]
# d[k] {}
# k 1
# sub_k 3
# v 3.0
# [sub_k] [3]
# d[k] {}
# k 2
# sub_k 1
# v 0.33
# [sub_k] [1]
# d[k] {1: 0.33}
# k 2
# sub_k 4
# v 1.5
# [sub_k] [4]
# print(dict(d))
# {0: {1: 1.0, 2: 0.5}, 1: {3: 3.0}, 2: {1: 0.33, 4: 1.5}}


# حالا اگر دیکشنری معمولی میزدیم این را میداد
# KeyError: 0
L = [[0,[1,1.0]],
     [0,[2,0.5]],
     [1,[3,3.0]],
     [2,[1,0.33]],
     [2,[4,1.5]]]

# d = collections.defaultdict(dict)
d={}
for k , (sub_k ,v) in L:
    print('d[k]',d[k])
    print('k',k)
    print('sub_k',sub_k)
    print('v',v)
    print('[sub_k]',[sub_k])
    d[k][sub_k] = v

# KeyError: 0


# اما دیفالت دیکت که کارش این بود متغیری نداشت پیشفرض را میداد
# اینجا چی کار کرد؟
# پاسخ: 
# هرچی بدی اونجا همون تبدیل میکنه 
# الان دیکشنری تبدیل میکنه

# ////////////////
# تبدیل یک لیست  تودرتو به دیکشنری
groups = [['Group1', 'A', 'B'], ['Group2', 'C', 'D']]
d = {k:row[0] for row in groups for k in row[1:]}
# {'D': 'Group2', 'B': 'Group1', 'C': 'Group2', 'A': 'Group1'}
# //////////
# تبدیل لیست تودرتو به دیکشنری تودرتو
[[a, b, c], [1, 'a', 'x'], [2, 'b', 'y']]

print({
    k: v for k, v in enumerate(dict(zip(val[0], v)) for v in val[1:])
})
# {0: {a:1, b:'a', c:'x'},
#  1: {a:2, b:'b', c:'y'}}

# ////////////

# تبدیل لیست برش خورده به دیکشنری
    for char in (my_members[5:]):
        dict[char[0]]= char[1] ,char[2]
# {'2022-01-16': ('9', '1')}



# /////////////////
# این هر دو را در یک سطر میده
situation_dict_extract={}
for situation ,value in situation_dict.items():
    situation_dict_extract[situation]=[value.values()]
# situation_dict_extract
pd.DataFrame(situation_dict_extract)


# این هر دو را در دو سطر میده
situation_dict_extract={}
for situation ,value in situation_dict.items():
    situation_dict_extract[situation]=value.values()
# situation_dict_extract
pd.DataFrame(situation_dict_extract)
# ////////
# این غلطه . نمیشه چیزی تعریف کنی که خالی باشه و بعدا همه چیز بهش اضافه کنی
# جلوتر داریم


    dict={}
    dict[]={}
    for char in (my_members[5:]):
        dict[char[0]]= char[1] ,char[2]
    
    print(dict)

# //////////////
# تبدیل لیست تودرتو به دیکشنری 
# عنصرهایی از یک لیست کلید بشن 
# و مابقی ولیو
# و هر کدام از لیست های بعدی عنصر اولی کلید بشه . عنصر دومی ولیو

# یعنی کلا ۱ دیکشنری مادربزرگ داریم 
# دو دیکشنری مادر  . به اسم خامنه ای و پهلوی
# هر کدوم از اینا یه عالمه دیکشنری فرزند دارن
# تاریخشون مشترکه یعنی کلید های واحد دارن اون فرزندان

my_members=[['Category: All categories'], ['# ع©ط¯غŒ ع©ظ‡ ط¨غŒط§ط¯  طھط§ط±غŒط® ط±ط§ ط¨ظ‡ ط´ظ…ط³غŒ طھط¨ط¯غŒظ„ ع©ظ†ظ‡ ظˆ ط³ظ¾ط³ ظ…ظ‚ط§غŒط³ظ‡ ع©ظ†ظ‡ '], ['#ط\xadطھغŒ ط¨ط¹ط¯ط´ ظ…طھ ظ¾ظ„ط§طھ ظ„غŒط¨ ع©ظ†ظ‡'], ['#ط¯غŒع©ط´ظ†ط±غŒ ع©ظ†ظ‡'], 
            ['Week', 'Ali Khamenei: (Iran)', 'Reza Pahlavi: (Iran)'],
            ['2022-01-16', '9', '1'], ['2022-01-23', '14', '1'], ['2022-01-30', '15', '1'], ['2022-02-06', '13', '1'], ['2022-02-13', '11', '1'], ['2022-02-20', '10', '1'], ['2022-02-27', '10', '1'], ['2022-03-06', '9', '1'], ['2022-03-13', '9', '1'], ['2022-03-20', '15', '2'], ['2022-03-27', '13', '1'], ['2022-04-03', '14', '1'], ['2022-04-10', '13', '<1'], ['2022-04-17', '18', '<1'], ['2022-04-24', '16', '<1'], ['2022-05-01', '18', '1'], ['2022-05-08', '14', '1'], ['2022-05-15', '13', '1'], ['2022-05-22', '13', '1'], ['2022-05-29', '18', '6'], ['2022-06-05', '16', '5'], ['2022-06-12', '10', '2'], ['2022-06-19', '10', '2'], ['2022-06-26', '10', '1'], ['2022-07-03', '9', '1'], ['2022-07-10', '11', '1'], ['2022-07-17', '11', '1'], ['2022-07-24', '10', '1'], ['2022-07-31', '13', '1'], ['2022-08-07', '14', '1'], ['2022-08-14', '9', '2'], ['2022-08-21', '11', '1'],
            ['2022-08-28', '15', '1'], ['2022-09-04', '18', '1'], ['2022-09-11', '100', '1'], ['2022-09-18', '93', '4'], ['2022-09-25', '61', '4'], ['2022-10-02', '85', '4'], ['2022-10-09', '38', '4'],
            ['2022-10-16', '33', '6'], ['2022-10-23', '29', '4'], ['2022-10-30', '27', '3'], ['2022-11-06', '19', '3'], ['2022-11-13', '25', '3'], ['2022-11-20', '22', '2'], ['2022-11-27', '19', '2'], ['2022-12-04', '30', '2'], ['2022-12-11', '19', '2'], ['2022-12-18', '17', '2'], ['2022-12-25',
            '17', '2'], ['2023-01-01', '21', '2'], ['2023-01-08', '21', '2']]
    my_vrodi=csv.reader(vorodi)
    my_members=list(my_vrodi)
    # print(my_members)
# لیست پنجم کلید ها بشه که البته باید باز بشه چون کاراکتر صفرمش بدرد نمیخوره
# کاراکتر  اول و دومش بدرد میخوره
    khamenei= (my_members[4][1])
    pahlavi=(my_members[4][2])
    # نقد و پرسش . نمیشد که ما اگر ۲۰ تا اسم داشتیم دونه دونه همه را مینوشتیم... 
    # نه . بهتر بود میومدیم واسه همینم حلقه تشکیل میدادیم و میریختیم توش
    # print(pahlavi, khamenei)
    # dict=defaultdict(dict)
    dict={}
    # برای ساخت دیکشنری تو در تو  یک دیکشنری خالی میسازی مادربزرگ
    # به تعداد مادر ها ولیو را خالی میدی
    dict[khamenei]={}
    dict[pahlavi]={}
    for char in (my_members[5:]):
        # حتما سینتکس اینه
        # 
        # کلید اول  کلید دیکشنری مادر است کلید دوم کلید دیکشنری فرزند یعنی همون تاریخ  در این دیکشنری است
        dict[khamenei][char[0]]= char[1]
        dict[pahlavi][char[0]]=char[2]
        # این دسترسی به لیست تودرتو بود
        # دسترسی به لیست تو در تو
        # برای ساخت دیکشنری تودرتو
        
    print(dict)
    # توجه شود که دو نقطه اول مال جلوش ایران نوشته خود استرینگ بوده
# { 'Ali Khamenei: (Iran)': {'2022-01-16': '9', '2022-01-23': '14', '2022-01-30': '15', '2022-02-06': '13', '2022-02-13': '11', '2022-02-20': '10', '2022-02-27': '10', '2022-03-06': '9', '2022-03-13': '9', '2022-03-20': '15', '2022-03-27': '13', '2022-04-03': '14', '2022-04-10': '13', '2022-04-17': '18', '2022-04-24': '16', '2022-05-01': '18', '2022-05-08': '14', '2022-05-15': '13', '2022-05-22': '13', '2022-05-29': '18', '2022-06-05': '16', '2022-06-12': '10', '2022-06-19': '10', '2022-06-26': '10', '2022-07-03': '9', '2022-07-10': '11', '2022-07-17': '11', '2022-07-24': '10', '2022-07-31': '13', '2022-08-07': '14', '2022-08-14': '9', '2022-08-21': '11', '2022-08-28': '15', '2022-09-04': '18', '2022-09-11': '100', '2022-09-18': '93', '2022-09-25': '61', '2022-10-02': '85', '2022-10-09': '38', '2022-10-16': '33', '2022-10-23': '29', '2022-10-30': '27', '2022-11-06': '19', '2022-11-13': '25', '2022-11-20': '22', '2022-11-27': '19', '2022-12-04': '30', '2022-12-11': '19', '2022-12-18': '17', '2022-12-25': '17', '2023-01-01': '21', '2023-01-08': '21'},
#   'Reza Pahlavi: (Iran)': {'2022-01-16': '1', '2022-01-23': '1', '2022-01-30': '1','2022-02-06': '1', '2022-02-13': '1', '2022-02-20': '1', '2022-02-27': '1', '2022-03-06': '1', '2022-03-13': '1', '2022-03-20': '2', '2022-03-27': '1', '2022-04-03': '1', '2022-04-10': '<1', '2022-04-17': '<1', '2022-04-24': '<1', '2022-05-01': '1', '2022-05-08': '1', '2022-05-15': '1', '2022-05-22': '1', '2022-05-29': '6', '2022-06-05': '5', '2022-06-12': '2', '2022-06-19': '2', '2022-06-26': '1', '2022-07-03': '1', '2022-07-10': '1', '2022-07-17': '1', '2022-07-24': '1', '2022-07-31': '1', '2022-08-07': '1', '2022-08-14': '2', '2022-08-21': '1', '2022-08-28': '1', '2022-09-04': '1', '2022-09-11': '1', '2022-09-18': '4', '2022-09-25': '4', '2022-10-02': '4', '2022-10-09': '4', '2022-10-16': '6', '2022-10-23': '4', '2022-10-30': '3', '2022-11-06': '3', '2022-11-13': '3', '2022-11-20': '2', '2022-11-27': '2', '2022-12-04': '2', '2022-12-11': '2', '2022-12-18': '2', '2022-12-25': '2', '2023-01-01': '2', '2023-01-08': '2'}}

# بررسی با

# در دیکشنری تودرتو
    print('2022-01-16' in dict)
    # False
    print('2022-01-16' in dict[khamenei])
    # True
# یعنی برای بررسی متغیر را فقط به یه نسل بالاتر میتونی بررسی کنی نه در مادربزرگ هاو...
# که نسل دورتر هستند . یعنی شباهت خانوادگی ویتگنشتاینی داره
# /////////////
# اما اگر چیزی که میخواستم این بود
# ساخت دیکشنری تو درتو 
# { {'2022-01-16': ('Ali Khamenei: (Iran)' : '9'),('Reza Pahlavi: (Iran)':'1') },{'2022-01-17': 'Ali Khamenei: (Iran)' : '5','Reza Pahlavi: (Iran)':'2' }   }


# ////////
# مقایسه دو دیکشنری
from deepdiff import DeepDiff
 
a = {'Name': 'asif', 'Age': 5}
b = {'Name': 'lalita', 'Age': 78}
 
diff = DeepDiff(a, b)
 
print(diff)
# {‘values_changed’: {“root[‘Name’]”: {‘new_value’: ‘lalita’, ‘old_value’: ‘asif’}, “root[‘Age’]”: {‘new_value’: 78, ‘old_value’: 5}}}

# /////
# مقایسه دو دیکشنری
d = {"a": 3, "b": 2}
d1 = {"a": 2, "b": 3}
res = all((d1.get(k) == v for k, v in d.items()))
print(res)

# //
# مقایسه دو دیکشنری
dict1 = {'Name': 'asif', 'Age': 5}
dict2 = {'Name': 'lalita', 'Age': 78}
 
if dict1 == dict2:
    print "dict1 is equal to dict2"
else:
    print "dict1 is not equal to dict2"

# /////////////////
# مقایسه دو دیکشنری
# مقایسه دو دیکشنری با هم وقتی که کلید های برابری دارند کلید هاشو نشون میده
a = {   'x' : 1,   'y' : 2,   'z' : 3 }
b = {   'w' : 10,   'x' : 11,   'y' : 2 }
# Find keys in common of two dictionaries in Python
# Here, we write a code that finds the keys that are common in two dictionary as:

a = {   'x' : 1,   'y' : 2,   'z' : 3 }
b = {   'w' : 10,   'x' : 11,   'y' : 2 } 
common_keys = a.keys() & b.keys() # intersection operation on keys
print("The common keys are :",common_keys)


# ///////////
# برای مقایسه ولیو یک دیکشنری تو در تو که کلید مشترکی دارند
# وقتی دیکشنری ها این باشه
{{'2022-01-16': 1, '2022-01-23': 1, '2022-01-30': 1, '2022-02-06': 1, '2022-02-13': 1, '2022-02-20': 1, '2022-02-27': 1, '2022-03-06': 1, '2022-03-13': 1, '2022-03-20': 2, '2022-03-27': 1, '2022-04-03': 1, '2022-04-10': 1, '2022-04-17': 1, '2022-04-24': 1, '2022-05-01': 1, '2022-05-08': 1, '2022-05-15': 1, '2022-05-22': 1, '2022-05-29': 6, '2022-06-05': 5, '2022-06-12': 2, '2022-06-19': 2, '2022-06-26': 1, '2022-07-03': 1, '2022-07-10': 1, '2022-07-17': 1, '2022-07-24': 1, '2022-07-31': 1, '2022-08-07': 1, '2022-08-14': 2, '2022-08-21': 1, '2022-08-28': 1, '2022-09-04': 1, '2022-09-11': 1, '2022-09-18': 4, '2022-09-25': 4, '2022-10-02': 4, '2022-10-09': 4, '2022-10-16': 6, '2022-10-23': 4, '2022-10-30': 3, '2022-11-06': 3, '2022-11-13': 3, '2022-11-20': 2, '2022-11-27': 2, '2022-12-04': 2, '2022-12-11': 2, '2022-12-18': 2, '2022-12-25': 2, '2023-01-01': 2, '2023-01-08': 2}
{'2022-01-16': 9, '2022-01-23': 14, '2022-01-30': 15, '2022-02-06': 13, '2022-02-13': 11, '2022-02-20': 10, '2022-02-27': 10, '2022-03-06': 9, '2022-03-13': 9, '2022-03-20': 15, '2022-03-27': 13, '2022-04-03': 14, '2022-04-10': 13, '2022-04-17': 18, '2022-04-24': 16, '2022-05-01': 18, '2022-05-08': 14, '2022-05-15': 13, '2022-05-22': 13, '2022-05-29': 18, '2022-06-05': 16, '2022-06-12': 10, '2022-06-19': 10, '2022-06-26': 10, '2022-07-03': 9, '2022-07-10': 11, '2022-07-17': 11, '2022-07-24': 10, '2022-07-31': 13, '2022-08-07': 14, '2022-08-14': 9, '2022-08-21': 11, '2022-08-28': 15, '2022-09-04': 18, '2022-09-11': 100, '2022-09-18': 93, '2022-09-25': 61, '2022-10-02': 85, '2022-10-09': 38, '2022-10-16': 33, '2022-10-23': 29, '2022-10-30': 27, '2022-11-06': 19, '2022-11-13': 25, '2022-11-20': 22, '2022-11-27': 19, '2022-12-04': 30, '2022-12-11': 19, '2022-12-18': 17, '2022-12-25': 17, '2023-01-01': 21, '2023-01-08': 21}}
    number=len( (dict))
    for x in range (number):
        if  dict[khamenei].keys() & dict[pahlavi].keys():
            if dict[khamenei].values() > dict[pahlavi].values():
                print('yes')
# این خطا را میده
# TypeError: '>' not supported between instances of 'dict_values' and 'dict_values'

# حالا اگر زیپ کنیم  لیست یا تاپلی از اون ولیو هایی که کلید مشترکی دارند میده
    number=len( (dict))
    for x in range (number):
        if  dict[khamenei].keys() & dict[pahlavi].keys():
            print(list(zip(dict[khamenei].values(),dict[pahlavi].values())))
        
# [(9, 1), (14, 1), (15, 1), (13, 1), (11, 1), (10, 1), (10, 1), (9, 1), (9, 1), (15, 2), (13, 1), (14, 1), (13, 1), (18, 1), (16, 1), (18, 1), (14, 1), (13, 1), (13, 1), (18, 6), (16, 5), (10, 2), (10, 2), (10, 1), (9, 1), (11, 1), (11, 1), (10, 1), (13, 1), (14, 1), (9, 2), (11, 1), (15, 1), (18, 1), (100, 1), (93, 4), (61, 4), (85, 4), (38, 4), (33, 6), (29, 4), (27, 3), (19,
# 3), (25, 3), (22, 2), (19, 2), (30, 2), (19, 2), (17, 2), (17, 2), (21, 2), (21, 2)]


# اما من میخوام مقایسه کنم و بگم که اگر در اون کلید یکی بودند 
# هم کلید را بده 
# هم بیشتر بودن مثلا پهلوی را
# نیاز به مقایسه داریم
# بعد بررسی کنه حتی تعداد را بده یا مقدار بیشتر بودن پهلوی را بگه 
# یا صرفا بگه پهلوی در این تاریخ

# این هم اینو میده:
# تاپلی که خودش تاپل  است که فقط عنصر اولشون مشترک است
    number=len( (dict))
    for x in range (number):
        # print  (dict[khamenei].items() , dict[pahlavi].items())
            print(list(zip(dict[khamenei].items(),dict[pahlavi].items())))
# [(('2022-01-16', 9), ('2022-01-16', 1)), (('2022-01-23', 14), ('2022-01-23', 1)), (('2022-01-30', 15), ('2022-01-30', 1)), (('2022-02-06', 13), ('2022-02-06', 1)), (('2022-02-13', 11), ('2022-02-13', 1)), (('2022-02-20', 10), ('2022-02-20', 1)), (('2022-02-27', 10), ('2022-02-27', 1)), (('2022-03-06', 9), ('2022-03-06', 1)), (('2022-03-13', 9), ('2022-03-13', 1)), (('2022-03-20', 15), ('2022-03-20', 2)), (('2022-03-27', 13), ('2022-03-27', 1)), (('2022-04-03', 14), ('2022-04-03', 1)), (('2022-04-10', 13), ('2022-04-10', 1)), (('2022-04-17', 18), ('2022-04-17', 1)), (('2022-04-24', 16), ('2022-04-24', 1)), (('2022-05-01', 18), ('2022-05-01', 1)), (('2022-05-08', 14), ('2022-05-08', 1)), (('2022-05-15', 13), ('2022-05-15', 1)), (('2022-05-22', 13), ('2022-05-22', 1)), (('2022-05-29', 18), ('2022-05-29', 6)), (('2022-06-05', 16), ('2022-06-05', 5)), (('2022-06-12', 10), ('2022-06-12', 2)), (('2022-06-19', 10), ('2022-06-19', 2)), (('2022-06-26', 10), ('2022-06-26', 1)), (('2022-07-03', 9), ('2022-07-03', 1)), (('2022-07-10', 11), ('2022-07-10', 1)), (('2022-07-17', 11), ('2022-07-17', 1)), (('2022-07-24', 10), ('2022-07-24',
# 1)), (('2022-07-31', 13), ('2022-07-31', 1)), (('2022-08-07', 14), ('2022-08-07', 1)), (('2022-08-14', 9), ('2022-08-14', 2)), (('2022-08-21', 11), ('2022-08-21', 1)), (('2022-08-28', 15), ('2022-08-28', 1)), (('2022-09-04', 18), ('2022-09-04', 1)), (('2022-09-11', 100), ('2022-09-11', 1)), (('2022-09-18', 93), ('2022-09-18', 4)), (('2022-09-25', 61), ('2022-09-25', 4)), (('2022-10-02', 85), ('2022-10-02', 4)), (('2022-10-09', 38), ('2022-10-09', 4)), (('2022-10-16', 33), ('2022-10-16', 6)), (('2022-10-23', 29), ('2022-10-23', 4)), (('2022-10-30', 27), ('2022-10-30', 3)), (('2022-11-06', 19), ('2022-11-06', 3)), (('2022-11-13', 25), ('2022-11-13', 3)), (('2022-11-20', 22), ('2022-11-20', 2)), (('2022-11-27', 19), ('2022-11-27', 2)), (('2022-12-04', 30), ('2022-12-04', 2)), (('2022-12-11', 19), ('2022-12-11', 2)), (('2022-12-18', 17), ('2022-12-18', 2)), (('2022-12-25', 17), ('2022-12-25', 2)), (('2023-01-01', 21), ('2023-01-01', 2)), (('2023-01-08', 21), ('2023-01-08', 2))]
# [(('2022-01-16', 9), ('2022-01-16', 1)), (('2022-01-23', 14), ('2022-01-23', 1)), (('2022-01-30', 15), ('2022-01-30', 1)), (('2022-02-06', 13), ('2022-02-06', 1)), (('2022-02-13', 11), ('2022-02-13', 1)), (('2022-02-20', 10), ('2022-02-20', 1)), (('2022-02-27', 10), ('2022-02-27', 1)), (('2022-03-06', 9), ('2022-03-06', 1)), (('2022-03-13', 9), ('2022-03-13', 1)), (('2022-03-20', 15), ('2022-03-20', 2)), (('2022-03-27', 13), ('2022-03-27', 1)), (('2022-04-03', 14), ('2022-04-03', 1)), (('2022-04-10', 13), ('2022-04-10', 1)), (('2022-04-17', 18), ('2022-04-17', 1)), (('2022-04-24', 16), ('2022-04-24', 1)), (('2022-05-01', 18), ('2022-05-01', 1)), (('2022-05-08', 14), ('2022-05-08', 1)), (('2022-05-15', 13), ('2022-05-15', 1)), (('2022-05-22', 13), ('2022-05-22', 1)), (('2022-05-29', 18), ('2022-05-29', 6)), (('2022-06-05', 16), ('2022-06-05', 5)), (('2022-06-12', 10), ('2022-06-12', 2)), (('2022-06-19', 10), ('2022-06-19', 2)), (('2022-06-26', 10), ('2022-06-26', 1)), (('2022-07-03', 9), ('2022-07-03', 1)), (('2022-07-10', 11), ('2022-07-10', 1)), (('2022-07-17', 11), ('2022-07-17', 1)), (('2022-07-24', 10), ('2022-07-24',
# 1)), (('2022-07-31', 13), ('2022-07-31', 1)), (('2022-08-07', 14), ('2022-08-07', 1)), (('2022-08-14', 9), ('2022-08-14', 2)), (('2022-08-21', 11), ('2022-08-21', 1)), (('2022-08-28', 15), ('2022-08-28', 1)), (('2022-09-04', 18), ('2022-09-04', 1)), (('2022-09-11', 100), ('2022-09-11', 1)), (('2022-09-18', 93), ('2022-09-18', 4)), (('2022-09-25', 61), ('2022-09-25', 4)), (('2022-10-02', 85), ('2022-10-02', 4)), (('2022-10-09', 38), ('2022-10-09', 4)), (('2022-10-16', 33), ('2022-10-16', 6)), (('2022-10-23', 29), ('2022-10-23', 4)), (('2022-10-30', 27), ('2022-10-30', 3)), (('2022-11-06', 19), ('2022-11-06', 3)), (('2022-11-13', 25), ('2022-11-13', 3)), (('2022-11-20', 22), ('2022-11-20', 2)), (('2022-11-27', 19), ('2022-11-27', 2)), (('2022-12-04', 30), ('2022-12-04', 2)), (('2022-12-11', 19), ('2022-12-11', 2)), (('2022-12-18', 17), ('2022-12-18', 2)), (('2022-12-25', 17), ('2022-12-25', 2)), (('2023-01-01', 21), ('2023-01-01', 2)), (('2023-01-08', 21), ('2023-01-08', 2))]

# خوب راهکار این میتونه باشه که بریزیم توی یه متغیر تازه 
# بعد طوری مقایسه کنیم که با یه تاپل تودرتو روبرو هستیم
# و سپس خروجی مدنظر را بده
# اما راه حل حرفه ای تر نداریم؟

# //////

# TypeError: first argument must be callable
>>> from collections import defaultdict
>>> dct = defaultdict(float('-inf'))

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dct = defaultdict(float('-inf'))
TypeError: first argument must be callable
Providing e.g. a lambda expression instead solves the problem:

>>> dct = defaultdict(lambda: float('-inf'))



# /////
#  تبدیل یک لیستی از تاپل های تودرتو به دیکشنری
# عنصر اول تاپل اول میشه کلید عنصر های دوم میشه ولیو ها

my= [(('2022-01-16', 9), ('2022-01-16', 1)), (('2022-01-23', 14), ('2022-01-23', 1)), (('2022-01-30', 15), ('2022-01-30', 1)), (('2022-02-06', 13), ('2022-02-06', 1)), (('2022-02-13', 11), ('2022-02-13', 1)), (('2022-02-20', 10), ('2022-02-20', 1)), (('2022-02-27', 10), ('2022-02-27', 1)), (('2022-03-06', 9), ('2022-03-06', 1)), (('2022-03-13', 9), ('2022-03-13', 1)), (('2022-03-20', 15), ('2022-03-20', 2)), (('2022-03-27', 13), ('2022-03-27', 1)), (('2022-04-03', 14), ('2022-04-03', 1)), (('2022-04-10', 13), ('2022-04-10', 1)), (('2022-04-17', 18), ('2022-04-17', 1)), (('2022-04-24', 16), ('2022-04-24', 1)), (('2022-05-01', 18), ('2022-05-01', 1)), (('2022-05-08', 14), ('2022-05-08', 1)), (('2022-05-15', 13), ('2022-05-15', 1)), (('2022-05-22', 13), ('2022-05-22', 1)), (('2022-05-29', 18), ('2022-05-29', 6)), (('2022-06-05', 16), ('2022-06-05', 5)), (('2022-06-12', 10), ('2022-06-12', 2)), (('2022-06-19', 10), ('2022-06-19', 2)), (('2022-06-26', 10), ('2022-06-26', 1)), (('2022-07-03', 9), ('2022-07-03', 1)), (('2022-07-10', 11), ('2022-07-10', 1)), (('2022-07-17', 11), ('2022-07-17', 1)), (('2022-07-24', 10), ('2022-07-24',
1)), (('2022-07-31', 13), ('2022-07-31', 1)), (('2022-08-07', 14), ('2022-08-07', 1)), (('2022-08-14', 9), ('2022-08-14', 2)), (('2022-08-21', 11), ('2022-08-21', 1)), (('2022-08-28', 15), ('2022-08-28', 1)), (('2022-09-04', 18), ('2022-09-04', 1)), (('2022-09-11', 100), ('2022-09-11', 1)), (('2022-09-18', 93), ('2022-09-18', 4)), (('2022-09-25', 61), ('2022-09-25', 4)), (('2022-10-02', 85), ('2022-10-02', 4)), (('2022-10-09', 38), ('2022-10-09', 4)), (('2022-10-16', 33), ('2022-10-16', 6)), (('2022-10-23', 29), ('2022-10-23', 4)), (('2022-10-30', 27), ('2022-10-30', 3)), (('2022-11-06', 19), ('2022-11-06', 3)), (('2022-11-13', 25), ('2022-11-13', 3)), (('2022-11-20', 22), ('2022-11-20', 2)), (('2022-11-27', 19), ('2022-11-27', 2)), (('2022-12-04', 30), ('2022-12-04', 2)), (('2022-12-11', 19), ('2022-12-11', 2)), (('2022-12-18', 17), ('2022-12-18', 2)), (('2022-12-25', 17), ('2022-12-25', 2)), (('2023-01-01', 21), ('2023-01-01', 2)), (('2023-01-08', 21), ('2023-01-08', 2))]
    # dictio=collections.defaultdict(list)
    my_dict={}
    for (madar,dokhtar),(pedar,pesar) in my:
        my_dict[madar]=dokhtar,pesar
        # print(pedar,pesar)
    print(my_dict)
# {'2022-01-16': (9, 1), '2022-01-23': (14, 1), '2022-01-30': (15, 1), '2022-02-06': (13, 1), '2022-02-13': (11, 1), '2022-02-20': (10, 1), '2022-02-27': (10, 1), '2022-03-06': (9, 1), '2022-03-13': (9, 1), '2022-03-20': (15, 2), '2022-03-27': (13, 1), '2022-04-03': (14, 1), '2022-04-10': (13, 1), '2022-04-17': (18, 1), '2022-04-24': (16, 1), '2022-05-01': (18, 1), '2022-05-08':
# (14, 1), '2022-05-15': (13, 1), '2022-05-22': (13, 1), '2022-05-29': (18, 6), '2022-06-05': (16, 5), '2022-06-12': (10, 2), '2022-06-19': (10, 2), '2022-06-26': (10, 1), '2022-07-03': (9, 1), '2022-07-10': (11, 1), '2022-07-17': (11, 1), '2022-07-24': (10, 1), '2022-07-31': (13, 1), '2022-08-07': (14, 1), '2022-08-14': (9, 2), '2022-08-21': (11, 1), '2022-08-28': (15, 1), '2022-09-04': (18, 1), '2022-09-11': (100, 1), '2022-09-18': (93, 4), '2022-09-25': (61, 4), '2022-10-02': (85, 4), '2022-10-09': (38, 4), '2022-10-16': (33, 6), '2022-10-23': (29, 4), '2022-10-30': (27, 3), '2022-11-06': (19, 3), '2022-11-13': (25, 3), '2022-11-20': (22, 2), '2022-11-27': (19, 2), '2022-12-04': (30, 2), '2022-12-11': (19, 2), '2022-12-18': (17, 2), '2022-12-25': (17, 2), '2023-01-01': (21, 2), '2023-01-08': (21, 2)}
        

# /////
# تبدیل یه لیست تودرتو به دیکشنری که عنصر اول هر لیست بشه کلید و بقیه لیست بشن
# [['mandana', '5', '7', '3', '15'], ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], ['sina', '19', '10', '19', '6', '8', '14', '3'], ['sara', '0', '5', '20', '14'], ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], ['ali', '1', '9'], ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8'], [], [], [], [], [], [], [], [], []]
        roder=list(my_Reader)
        my={}
        for charr in roder:
            # print(charr)
            while '' in charr:
                charr.remove('')
            for harf in charr:
            #     print(charr[1:])
                my[charr[0]]=charr[1:]
# {'mandana': ['5', '7', '3', '15'], 'hamid': ['3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], 'sina': ['19', '10', '19', '6', '8', '14', '3'], 'sara': ['0', '5', '20', '14'], 'soheila': ['13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], 'ali': ['1', '9'], 'sarvin': ['0', '16', '16', '13', '19', '2', '17', '8']}        

# //////////////
# تبدیل ولیو هایی که استرینگ هستند به اینتیجر
# اوردن زدن ولیو ها به تک خطی 
# تک خطی کردن ولیو ها
# اشاره به ایندکس های یک لیست و تبیل ایندکس ها به دیکشنری

        my={}
        for charr in roder:
            # print(charr)
            while '' in charr:
                charr.remove('')
            for harf in charr:
                # میشه  همه ولیو ها را تغیر داد 
                my[charr[0]]= (list (int(x) for x in charr[1:]))
                # تبدیل ایندکس به کلید دیکشنری
# ////////////
# شماردن اینکه یه متغیر چند بار در یه لیست بکار رفته 
from collections import Counter
my_powers=[2,2,2,2,2,3]
print(Counter(my_powers))
# Counter({2: 5, 3: 1})

# ////////////
# تبدیل اشتراک ها به کلید و بقیه ولیو
# زوج بندی
# defaultdict
lst = [(1,'a'), (2,'b'), (2,'c'), (3,'d')]
from collections import defaultdict, OrderedDict
d = defaultdict(list)
#  خودش میاد مشترک ها را پیدا میکنه
# کلید مشترک که دید متغیر هاشو جلوش لیست میکنه
# در اپند
for k,v in lst:
    d[k].append(v)
print(d)
# defaultdict(<class 'list'>, {1: ['a'], 2: ['b', 'c'], 3: ['d']})

# ///////////
# همون کد در تک خطی 
# با گروپبای
# به کتابخانه ایترتولز مراجعه شود
from itertools import groupby

lst = [(1, 'a'), (2, 'b'), (2, 'c'), (3, 'd')]
# چون گروب بای کلید میگیره کلید را لامبدا میکنه که  عنصر صفرم لامبدا
# و لیست هم بهش میده
res = {k: [b for a, b in g] for k, g in groupby(lst, key=lambda x: x[0])}
print(res)
# {1: ['a'], 2: ['b', 'c'], 3: ['d']}

# //////////
# ؟؟؟؟؟
# این کار ببالا را میکنه ولی معنای کدشو تیکه تیکه نفهمیدم چی گفته
dic = next(g  for g in [{}] if not any(g.setdefault(k,[]).append(v) for k,v in lst))

# Or this:

dic = {}; dic.update((k,dic.get(k,[])+[v]) for k,v in lst)

# ///////////
# ولیو کلید ها را میده
# ست دیفالت
# اگر کلید در دیکشنری بود اونو برمیگردونه وگرنه اون چیزی که بهش دادیم را برمیگردونه
d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
# space key added using setdefault() method
d.setdefault(' ', 32)
print(d)
# {'a': 97, 'b': 98, 'c': 99, 'd': 100, ' ': 32}


# //
# این بود همونو میده
Dictionary1 = { 'A': 'Geeks', 'B': 'For'}
print("Dictionary before using setdefault():", Dictionary1)
  
# using setdefault() when key is non-existing
ret_value = Dictionary1.setdefault('A', "Geeks")
print("Return value of setdefault():", ret_value)
  
print("Dictionary after using setdefault():", Dictionary1)
# Dictionary after using setdefault(): {'A': 'Geeks', 'B': 'For'}


# حالا اگر نبود/////////////////////
Dictionary1 = { 'A': 'Geeks', 'B': 'For'}
print("Dictionary before using setdefault():", Dictionary1)
  
# using setdefault() when key is non-existing
ret_value = Dictionary1.setdefault('C', "Geeks")
print("Return value of setdefault():", ret_value)
  
print("Dictionary after using setdefault():", Dictionary1)
# Dictionary after using setdefault(): {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# /////
# ست دیفالت
# ساخت دیکشنری از لیست اینستنس های کلاس
# وقتی که یک اتربیوت کلید باشه
# ساخت کلاس

class Dummy:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
# ساخت ک اینستنس هایی از کلاس
# وقتی که بعض هاشون اسم یکسان دارند

# اما این به معنی اینه که اسم اون اینستنس  اینه
# ساخت اینستنس های جدا با استفاده از یک کلاس
classes = [Dummy('a'), Dummy('b'), Dummy('b'), Dummy('c'), Dummy('d')]

# اکنون یک  دیکشنری میسازیم که اینستنس های کلاس ر ا بسازه
classes_dict = {}


# ما بر  این لیست تکرار میزنیم
# برای هر المان در لیست 
# ما به دیکشنری اضافه میکنیم با استفاده از ست دیفالت
# به این معنی که اگر کلید از قبل در دیکشنری بود ما اون المان را به لیست کلید اضافه میکنیم وگرنه  به  ما به کلید چیزی اضافه میکنیم. انگار که به یک لیست خالی اضافه میکنیم
for each_class in classes:
    classes_dict.setdefault(each_class.name, []).append(each_class)
# این تیکه میگه برای هر کاراکتر که در کلاس ها هستند اتربیوت نیمی که دادیم 
# و چون ست دیفالت میگه اگر بود  اپند کن بهش و اگر نبود یه لیست خالی بساز ازش بعد اپند کن

print(classes_dict)
# نتیجه نهایی
# {'a': [a], 'b': [b, b], 'c': [c], 'd': [d]}



# ///


# دیکشنری تک خطی
# دیکشنری کامپرهنشن
# ساخت دیکشنری از این لیست
# اجرای متد بر بخشی از لیست

# [['mandana', 5, 7, 3, 15], ['hamid', 3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1], ['sina', 19, 10, 19, 6, 8, 14, 3], ['sara', 0, 5, 20, 14], ['soheila', 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7], ['ali', 1, 9], ['sarvin', 0, 16, 16, 13, 19, 2, 17, 8], [], [], [], [], [], [], [], [], []]
        Origin={k : mean(char[1:]) for char in my for k in char[0:1]}
        # اینو میده
# {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            

# ساختار دیکنشری تک خطی
# دیکشنری تک خطی دو حلقه

# ساختار اینه 
dictname={k:v  1 for  2 for}
# که یک نوع کلید یا ولیو از حلقه دومی میاد معمولا
dictname={k(y as key):v (methods on  x)   1 for x in origin_list  2 for y in x}
# یه نوع دیگه اینه
dictname={k (methods on  x) :v (y as value)   1 for x in list  2 for y in x}

# ////////
# این نمیاد درون دیکشنری چیزی بریزه چون دیکشنری از کاراکتر 
# charr
# میاد میگیره 
# و چون در یک راستا هستش چیزی نمیریزه درونش
# بلکه یه دندانه بره جلو

    roder=calculate_averages()
    my={}
    for charr in roder:
        while '' in charr:
            charr.remove('')
    for harf in charr:
        my[charr[0]]=mean(list(int(x) for x in charr[1:]))
        # print(my)
    return (my)
print(dictionary_av())
#  {}


# بجاش باید این کار را کرد
    for charr in roder:
        while '' in charr:
            charr.remove('')
        for harf in charr:
            my[charr[0]]=mean(list(int(x) for x in charr[1:]))
        # print(my)
    return (my)
print(dictionary_av())
# این روش اپند کردن در دیکشنری  بطور اتوماتیک هم است
# //////


    #   عنصر دومی که اون کارها را کرد روش را به تعداد دو تا میده  
my4= [ (sorted(my3.items() , key= lambda x: x[1],reverse=True))[2] for i in range(2) ]
        print(my4)
# [('sara', 9.75), ('sara', 9.75)]

#  دو بار هر کدوم از عناصر را میده  ولی پس از لیست کردن یه دوره
my4= [ (sorted(my3.items() , key= lambda x: x[1],reverse=True)) for i in range(2) ]
# [[('sarvin', 11.375), ('sina', 11.285714285714286), ('sara', 9.75), ('soheila', 7.833333333333333), ('mandana', 7.5), ('hamid', 6.066666666666666), ('ali', 5.0)], [('sarvin', 11.375), ('sina', 11.285714285714286), ('sara', 9.75), ('soheila', 7.833333333333333), ('mandana', 7.5), ('hamid', 6.066666666666666), ('ali', 5.0)]]


# هرکدوم را دو بار پشت سر هم میاره
my4= [char  for char in (sorted(my3.items() , key= lambda x: x[1],reverse=True)) for i in range(2) ]
# [('sarvin', 11.375), ('sarvin', 11.375), ('sina', 11.285714285714286), ('sina', 11.285714285714286), ('sara', 9.75), ('sara', 9.75), ('soheila', 7.833333333333333), ('soheila', 7.833333333333333), ('mandana', 7.5), ('mandana', 7.5), ('hamid', 6.066666666666666), ('hamid', 6.066666666666666), ('ali', 5.0), ('ali', 5.0)]

# دوتای اول کل دیکشنری را را میده
from itertools import islice
my4= list (islice (sorted(my3.items(), key= lambda x: x[1],reverse=True),3))
        print(my4)
# کل داستان  نوشتن سورت کردن براساس ولیو های بالاتر است که داخل پرانتز مینویسیم
# ولی مرحله بعد از اسلایس برشش میزنه فقط
# [('sarvin', 11.375), ('sina', 11.285714285714286), ('sara', 9.75)]

# همونه ولی با روش ساده برش زدن
# برش
my4= list ((sorted(mydict.items(), key= lambda x: x[1],reverse=True)[0:3]))
        print(my4)
# [('sarvin', 11.375), ('sina', 11.285714285714286), ('sara', 9.75)]


# سه تای اول  ولیو های دیکشنری را برش میزنه
print(list(mydict[k] for k in  sorted(mydict,key= mydict.get)[0:3]))
# [5.0, 6.066666666666666, 7.5]


# //////////
# منتخب کردن یک دیکشنری کلی بر اساس اینی که میده
# فیلتر کردن دیکشنری
d={0:1, 1:2, 2:3, 10:4, 11:5, 12:6, 100:7, 101:8, 102:9, 200:10, 201:11, 202:12}


0, 1, 2, 100, 101, 102.

# خروجی را این بده
d1={0:1, 1:2, 2:3, 100:7, 101:8, 102:9}

# راه ۱
d = {0:1, 1:2, 2:3, 10:4, 11:5, 12:6, 100:7, 101:8, 102:9, 200:10, 201:11, 202:12}
keys = (0, 1, 2, 100, 101, 102)
d1 = {k: d[k] for k in keys}

# راه ۲
import itertools as it

d = {0:1, 1:2, 2:3, 10:4, 11:5, 12:6, 100:7, 101:8, 102:9, 200:10, 201:11, 202:12}
d1 = {k: d[k] for k in it.ifilter(lambda x: 1 < x <= 11, d.keys())}
# /////////

# انتخاب یه دیکشنری از یه چیزی 
# فیلتر کردن  دیکشنری
# اینو داریم 
da = {'Apple': 1, 'Banana': 9, 'Carrot': 6, 'Baboon': 3, 'Duck': 8, 'Baby': 2}
# اینو میخوایم
# {'Banana': 9, 'Baby': 2, 'Baboon': 3}

def slicedict(d, s):
    return {k:v for k,v in d.items() if k.startswith(s)}
# این تابع میگه دو تا چیز بگیر 
# اگر اون شرط را داشت اون دومی 
# فقط کلید و ولیو را برگردون

print(slicedict(da,'Ba'))
# {'Banana': 9, 'Baboon': 3, 'Baby': 2}


# راه ۲
dict(filter(lambda item: item[0].startswith(string),sourcedict.iteritems()))


# /////////////
iteritems

# /////
# معنی این کد چیه؟
# دیکشنری تودرتو
# دیکنشری تک خطی
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# callable
# https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields
dict((key, value) for key, value in f.__dict__.iteritems() 
    if not callable(value) and not key.startswith('__'))


# /////

# ساخت یک دیکشنری از دو لیست
# رجوع شود به لیست ها . همین کلید را جستجو کن
# تبدیل رندوم دو لیست به یک دیکشنری 
# بطوریکه عضو یکی بشه کلید و عضویا عضو های دیگر بشه ولیو
# https://stackoverflow.com/questions/40298116/python-how-to-merge-two-lists-into-a-dictionary-in-a-total-random-order

# //////////
# وقتی یه دیکشنری را به لیست تبدیل کنیم فقط کلید هاشو میده
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}

myfirst=list(dict(zip(keys[:myhalf] , values[:myhalf])))
print(myfirst)
# ['hamid', 'sina', 'sara']
# ////


# تقسیم  دیکشنری به دو لیست  در ولیو و کلید ها 
# در دو لیست جدا
mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            
keys, values = zip(*mydictha.items())
print(list(keys))
print(list(values))
# ['hamid', 'sina', 'sara', 'soheila', 'ali', 'sarvin']
# [6.066666666666666, 11.285714285714286, 9.75, 7.833333333333333, 5, 11.375]

# فایده استار
# فایده ستاره
# اگر ستاره را پشت نزاریم یان خطا را میده
# ValueError: too many values to unpack (expected 2)
# ////////
# تقسیم کردن یک دیکشنری 
# برش زدن یک دیکشنری به دو قسمت مساوی
mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            
# اینجا میاد کلید و ولیو را جدا میکنه از هم
# جدا کردن دیکشنری از کلید و ولیو
keys, values = zip(*mydictha.items())
print(list(keys)) #['hamid', 'sina', 'sara', 'soheila', 'ali', 'sarvin']
print(list(values)) #[6.066666666666666, 11.285714285714286, 9.75, 7.833333333333333, 5, 11.375]

myhalf=len(mydictha)//2
print(myhalf)
# 3

# برش زدن کلید ها به نصف 
print( (keys[:myhalf]))
# ('hamid', 'sina', 'sara')

print(keys[myhalf:])
# ('soheila', 'ali', 'sarvin')
# برای ولیو ها هم به همین ترتیب

# حالا این تیکه میچسبونه اونها را به هم
# یه تاپل به ترتیب میده
myfirst=keys[:myhalf] , values[:myhalf]
print(myfirst)
# (('hamid', 'sina', 'sara'), (6.066666666666666, 11.285714285714286, 9.75))

# حالا زیپ کنیمشون
# لیستی از تاپل ها میده
myfirst=list(zip(keys[:myhalf] , values[:myhalf]))
print(myfirst)
# [('hamid', 6.066666666666666), ('sina', 11.285714285714286), ('sara', 9.75)]
myfirst=dict(zip(keys[:myhalf] , values[:myhalf]))
print(myfirst)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}


# پس بطور خلاصه
mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            

keys, values = zip(*mydictha.items())
myhalf=len(mydictha)//2

myfirst=(dict(zip(keys[:myhalf],values[:myhalf])))
print(myfirst)
mysecond=dict(zip(keys[myhalf:],values[:myhalf]))
print(mysecond)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}
# {'soheila': 6.066666666666666, 'ali': 11.285714285714286, 'sarvin': 9.75}


# راه دوم
# https://www.geeksforgeeks.org/python-split-given-dictionary-in-half/

# /////////
# ساخت یک دیکشنری بصورت رندوم
# دیکشنری رندوم
# ولیو دیکشنری رندوم بشه
def random_dict():
    my_dict={}
    for i in range(10):
        # نوشتن یک  کلید  استرینگی در لید دیکشنری
        my_dict['key'+str(i)]=randrange(10)
    return my_dict
print(random_dict())
# {'key0': 3, 'key1': 1, 'key2': 9, 'key3': 6, 'key4': 7, 'key5': 4, 'key6': 1, 'key7': 3, 'key8': 2, 'key9': 6}


# ///////
# گرفتن رندوم از یک دیکشنری
my_dict ={0:' a',1:'b',2:'c'}
k , v=random.choice(list(my_dict.items()))
print(k,v)
# 2 c

# توجه شود که اگر در لیست نزاری اینو میده خطای غیر قابل اشتراک گذاری
k , v=random.choice((my_dict.items()))

# 'dict_items' object is not subscriptable


# /////
# دادن رندوم ولیو ها
print(random.choice(list(my_dict.values())))

# b


# //////
from random import sample ,randint,randrange,shuffle
import random
my_dict ={0:' a',1:'b',2:'c'}
import random
kl = my_dict.keys()
random.shuffle(list(kl))
for key in kl:
    print (key, my_dict[key])

# 0  a
# 1 b
# 2 c
# و جالبه که با وجود اینکه ریخیتم توی کلید بازهم بهمون میده
# /////
# پاپ ایتم
# اخرین جفت کلید و ولیو  را میده بهمون
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
print(cor.popitem())
# ('sarvin', 11.375)


# حالا اگر روی دیکشنری پاپ کنیم
# بطور جدا کنه بهمون بده
# حالا اگر روی دیکشنری اصلی پیاده کنیم
key,val=(cor.popitem())
print(key , val)
# sarvin 11.375
# ///////



# چطور بریزیم توی یه دیکشنری دیگه مثل لیست ها قاطی کنمشون رندوم
# شافل کردن دیکشنری
from random import sample ,randint,randrange,shuffle
my_dict ={0:' a',1:'b',2:'c'}
# kl = my_dict.items()
# چطور بریزیم توی یه دیکشنری دیگه مثل لیست ها قاطی کنمشون رندوم
# ((random.shuffle(list(kl))))
kelid=list(my_dict.keys())
# print(kelid) #[0, 1, 2]
random.shuffle(kelid)
# print(kelid)  #[0, 1, 2]
NEfW={}
# میگه به ازای هر کلید  که در اون لیسته
# ولیو اون کلید در دیکشنری اول را میره پیدا میکنه . بخاطر اسم مشترک
# کلید را میزاره همین کلید
# ولیو را از اون دیکشنری اول میگیره
for k  in kelid:
    NEfW[k]=my_dict[k]
print(NEfW)

# با این شیوه  انگار هر  متد لیست ها را میشه روی دیکشنری پیاده کرد
# {2: 'c', 0: ' a', 1: 'b'}
# توجه شود که شافل کردن اگر بکار میبری خود اردر دیکت را بکار نبری که خنثی میکنه

# شیوه دوم
# رندوم کردن دیکشنری
def shuffle_dict(my_dict):
    # my_dict ={0:' a',1:'b',2:'c'}
    kelid=list(my_dict.items())
    shuffle(kelid)
    newdict=dict(kelid)
    return (newdict)
print(shuffle_dict(my_dict ={0:' a',1:'b',2:'c'}))
# {2: 'c', 0: ' a', 1: 'b'}
# /////////
# ساخت یک دیکشنری از دو دیکشنری
# وقتی که کلید ها از یک دیکشنری و ولیو ها از یک دیکشنری دیگر باشد
# با ترتیب رندوم کلید ها

# وقتی که کلید ها یکسان باشند
my_dict ={0:' a',1:'b',2:'c'}
fake_dict ={0:' m',1:'K',2:'J'}

kelid=list(my_dict.keys())
NEfW={}
for k  in kelid:
    NEfW[k]=fake_dict[k]
print(NEfW)
# این انگار همون دیکشنری اول است که !!!!!!!!!
# {2: 'J', 0: ' m', 1: 'K'}

# ///////
# اینم فقط سومی را میاره انگار  قبلیها را حذف میکنه
# اما چطور رندوم اونا را بریزه توش؟؟؟؟؟؟؟
my_dict ={0:' a',1:'b',2:'c'}
fake_dict ={0:' m',1:'K',2:'J'}

kelid=list(my_dict.keys())
NEfW={}
for k  in my_dict:
    for j in fake_dict:
        NEfW[k]=fake_dict[j]
print(NEfW)
# {0: 'J', 1: 'J', 2: 'J'}

# ///////////
# ساخت یک دیکشنری از دو دیکشنری
# کلید های یکی کلید دیشکنری تازه میشن
# کلید های یکی ولیو میشن
my_dict ={0:' a',1:'b',2:'c'}
fake_dict ={3:' m',4:'K',5:'J'}

kelid=list(my_dict.keys())
NEfW=dict(zip(my_dict,fake_dict))

print(NEfW)
# {0: 3, 1: 4, 2: 5}
# ////////

# کلید های یکی کلید دیکشنری میشن
# ولیو ها ی دیکشنری دیگر ولیو دیکشنری تازه میشن
my_dict ={0:' a',1:'b',2:'c'}
fake_dict ={3:' M',4:'K',5:'J'}

kelid=list(my_dict.keys())
NEfW=dict(zip(my_dict,fake_dict.values()))

print(NEfW)
# {0: 'M', 1: 'K', 2: 'J'}

# /////////////

# ساخت دیکشنری رندوم ای از دو لیست
from random import shuffle,choice
m_players=['Human1', 'Human2', 'Human3',]
myplayerlist=['Hossein','Maziar','Akbar'] 
# shuffle(myplayerlist)
# shuffle(m_players)    یا اینجا میتونی تعریف کنی یا داخل تابع اصلی 
def two_list_dict(key_list,value_list):
    mydict={}
    shuffle(key_list)
    shuffle(value_list)    # یا اینجا میتونی تعریف کنی
    for key, value in zip(key_list,value_list):
            mydict [key]=(value)
    return mydict
mydict=(two_list_dict(m_players,myplayerlist))
print(mydict)  
# یه بار اینو میده
# {'Human3': 'Akbar', 'Human2': 'Hossein', 'Human1': 'Maziar'}
# {'Human2': 'Akbar', 'Human3': 'Maziar', 'Human1': 'Hossein'}


# ///////
# دیکشنری ۴ متغیره
# دیکشنری چند متغیره
# حالا تبدیل  چهار لیست وقتی که سه تاش ولیو بشه و یکیش کلید
# دادن  تاپلی از ولیو ها
def two_list_dict(key_list,value_list):
    mydict={}
    shuffle(key_list)
    shuffle(value_list)    # یا اینجا میتونی تعریف کنی
    for key, value ,j, k in zip((key_list),(value_list),(price),(post)):
            mydict [key]=(value,j,k)
    return mydict
mydict=(two_list_dict(m_players,myplayerlist))
print(mydict)

# یا حتی این
# دادن تاپلی از کلید ها
            mydict [key,k]=(value,j)
            
# یا حتی چیزی هم در کلید باشه  و هم  در ولیو
            mydict [key,k]=(value,j,k)
          
          
# ???????????
# سوال ایا میشه این هارو با استار نوشت  
# *
 
# /////////



# //////////////////////////////////////

# اگر در کلاس  دیکشنری ای داشته باشیم  
# که ویژگی ای از قبل واسش تعریف کرده باشیم
# این میگیره
# ولی اگر  ک در کلاسس نباشه نمیشه و میگه باید ولیو را بدی
from random import shuffle
# کلاس انسان را ساختیم که  فقط  اسم ها را داشته باشه
class Human:
    def __init__(self,name):
        self.name=name
    # اینم برای بازنمایی اوردیم
    def __repr__(self):
        return f'{self.name}'    

# کلاس فوتبالر از انسان ارث بری میکنه  ولی به غیر از اسم سن و پست هم داره
class Footballer(Human):
    job='Football Player'
    def __init__(self,name,post,price):
        super().__init__(name)
        self.post=post
        self.price=price
    # اینم برای بازنمایی اوردم 
    # ایا اگر این متد در مادر باشه و پارامتر های تازه داشته باشه از ن بنویسیم؟
    def __repr__(self):
        return f'{self.name} {self.post} {self.price}'


def player_objects():
    m_players=[]
    for char in range(1,2):
        name='Human'
        m_players.append((Human('%s%i'%(name,char))))
    return m_players
m_players= (player_objects())
# print(m_players) # [Human1, Human2, Human3, etc.....]

# این هم اعضای کل هستند که طبق صورت مساله سوال بود
myplayerlist=['Hossein','Maziar','Akbar','Nima','Mehdi','Farhad','Mohammad','Khashayar','Milad','Mostafa','Amin','Saeid','Pouya','Poria','Reza','Ali','Behzad','Soheil','Behrooz','Shahrooz','Saman','Mohsen']


# اینجا چطور پارامتر های دیگه را تبدیل کنم؟
def two_list_dict(key_list,value_list):
    mydict={}
    for key, value in zip(key_list,value_list):
# حتما باید اسمشو داشته باشی
# وگرنه اینو میزنه
# NameError: name 'value' is not defined. Did you mean: 'False'?
            mydict [key.name]=Footballer(value,post=input('give me post: '),price=input('give me the price: '))
    return mydict
mydict=(two_list_dict(m_players,myplayerlist))
print(mydict)  #{'Human1': Hossein, 'Human2': Maziar, etc.....}
# give me post: fd
# give me the price: df
# {'Human1': Hossein fd df}
        # یعنی کل اون کاراکتر را ولیو میکنه 
# اصلا مهم نیست  ولیو در اون دیکشنری نوشته باشه ولیو

# به غیر از ولیو اگر مقدار را بدیم  میشه و کل بخش دوم را تاپل میکنه


# به تمرین دوم رجوع شود

# //////

# ساخت یه دیکشنری تازه به وسیله یکی از ولیو های دیکشنری پیشین
# چند ولیو
# چندویلو
# بروزرسانی دیکشنری
# کم کردن تعداد ولیو ها
# فیلتر کردن تعداد ولیوها
# اگر فقط بخوایم دسترسی بداریم به یکی  از ولیو ها
my= { 'a' : ( 1, 2, 3),' b': ( 4, 5, 6)}
for k in my:
    print(my[k][0])
# 1
# 4


# حالا اگر بخوایم اونو دیکشنری کنیم
# ساخت دیکشنری تازه از دیکشنری پیشین
for k in my:
    my[k]=(my[k][0])
print(my)
# {'a': 1, ' b': 4}
# اینم تک خطی
# 
# کامپرهنشن
dict2 = {k: my[k][2] for k in my}


# /////
# ساخت یک دیکشنری با فیلتر کردن اونایی که میخوایم
# و ارزش هر کدوم را بگه
words=['ABCD', 'abcd', 'AB55', '55CD', 'A55D', '5555']

lists = {}
for s in words:
    s_list = []
    for c in s:
        s_list.append(c.isdigit())
    lists[s] = s_list
print(lists)

# ///////////
# حذف اونایی که استرینگ دارند و خالص کردن رشته
if 'GB' in (char[1][0]):
    print(char[1][0])
    char[1][0] = ''.join([i for i in char[1][0] if i.isdigit()])

# ///////////
