import itertools
from itertools import combinations ,permutations, pairwise ,cycle
from random import random , randint,randrange, shuffle, sample,choice

from more_itertools import collapse,interleave




# ///
from itertools import combinations, permutations
# برای جایگشت باید تاپلی از لیست باشه


# سینتکس اینه داخل تاپل لیست بده
my_list=permutations([1,2,3])
for i in (my_list):
    print(i)
# (1, 2, 3) حالت معیار
# (1, 3, 2)   # حالت دو جاشون عوض شده یعنی دو رفه جای سه و سه رفته جای دو
# (2, 1, 3)   # یک اومده جای دو سه سرجاشه
# (2, 3, 1) # حالت دو اومده جای یک حالت سه رفته جای دو و حالت یک رفته جای سه
# (3, 1, 2)   # حالت سه رفته جای یک و حالت یک رفته جای دو و حالت دو رفته جای سه
# (3, 2, 1)  # حالت سه و یک رفته جای هم و دو ثابه


# پرسش 
# ایا  در جایگشت میشه بگه نسبت به حالت اولی چیش عوض شده؟
# مثلا بگه حالت اول که معیار بود الان  در حالت دوم کاراکتر دوم و سوم عوض شدن
# در حالت آخر کاراکتر اول و سوم جابجا شدن
# و.....

# این در نظریه بازی که معمای زندانی بازی معروفه است بدرد میخوره

# ////////////////////
# ۲ تا دو تا مقایسه میکنه جایگشت میکنه
from itertools import combinations, permutations
my_list=permutations([1,2,3],2)
for i in (my_list):
    print(i)
    
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)
# ////////////////
# ترکیب ها
# در ترکیب مقایسه تکراری نیست
# یعنی یک بار که اورد یک و دو دفعه بعد دیگه دو و یک را مقایسه نمیکنه
from itertools import combinations, permutations
my_list=combinations([1,2,3],2)
for i in (my_list):
    print(i)

# (1, 2)
# (1, 3)
# (2, 3)

# ///////////
# سه تا سه تا . اگر کل عضو سه تا باشه یه بار ترکیب میکنه
from itertools import combinations, permutations
my_list=combinations([1,2,3],3)
for i in (my_list):
    print(i)
# (1, 2, 3)

# ////////
# اگر میخوای خودشم بیاره در ترکیب 
# باید 
# را بیاری
# حتما هم باید تعریف کنی چند تا چندتا و پیشفرض نداره

# یا اعضای اولی باید لیست باشه یا تاپل
from itertools import combinations, permutations ,combinations_with_replacement
my_list=combinations_with_replacement([1,2,3],3)
for i in (my_list):
    print(i)
    
# (1, 1, 1)
# (1, 1, 2)
# (1, 1, 3)
# (1, 2, 2)
# (1, 2, 3)
# (1, 3, 3)
# (2, 2, 2)
# (2, 2, 3)
# (2, 3, 3)
# (3, 3, 3)
# ////////////////////
# ترکیب با تکرار خودش
from itertools import combinations, permutations ,combinations_with_replacement
my_list=combinations_with_replacement([1,2,3],2)
for i in (my_list):
    print(i)
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 2)
# (2, 3)
# (3, 3)
# //////////////////
# در حلقه انداختن یک استرینگ . هر دکدوم از کاراکتر هاش را جدا میکنه
# جایگشت کردن استرینگ
from itertools import combinations, permutations ,combinations_with_replacement
my_list=('123')
for i in permutations(my_list):
    print(i)
# ('1', '2', '3')
# ('1', '3', '2')
# ('2', '1', '3')
# ('2', '3', '1')
# ('3', '1', '2')
# ('3', '2', '1')
# ////////////////
# ترکیب استرینگ
from itertools import combinations, permutations ,combinations_with_replacement
my_list=('123')
for i in combinations(my_list,2):
    print(i)
# ('1', '2')
# ('1', '3')
# ('2', '3')

# ////////
# حلقه انداختن  ترکیب 
from itertools import combinations, permutations ,combinations_with_replacement
# اگر خواستی ترکیب کنی باید  در خود حلقه بیاری نه در لیت متغیر اول
my_list=(1,2,3)
for i in combinations(my_list,2):
    print(i)
# (1, 2)
# (1, 3)
# (2, 3)


# /////////////
# تبدیل کلید دیکشنری به تاپل ها به صورت دوبه دو
# ترکیب
# ترکیب در دیکشنری
# کلید ها را دو به دو مقایسه میکنه ترکیبشونو میاره
my = {1: 7, 3: 10}
print(list(itertools.combinations(my,2)))
# [(1, 3)]

# ///////////////
# اوردن ولیو ها  در ترکیب
my = {1: 7, 3: 10}
from itertools import permutations , combinations , combinations_with_replacement
for k in combinations(my.values(),2):
    print(k)
# (7, 10)
# ///////////////////
# بدون نیاز به حلقه جایگشت زدن
# بدون حلقه
# رنج بدون حلقه
# این از عدد ۱ تا ۴ را میاره و چون خود ۴ حساب نمیشه در رنج تا ۳ میاره
my=list(permutations(range (1,4)))
print(my)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# ////////////

# دو تا تاپل را دو به دو  هر کدوم از متغیر هاشو میاره
# یا تاپل ای از تاپل ها میاره
from itertools import combinations, permutations ,combinations_with_replacement ,product
my_list=(1,2,3)
my_list2=(4,5,6)
my=list(product(my_list,my_list2))
print(my)
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

# /////////////
# جفت کردن دو به دو
# pairwise
from itertools import combinations , permutations , product ,  combinations_with_replacement , pairwise
from collections import OrderedDict
my_key=['a','b','c' ]
a= list(pairwise(my_key))
print(a)
# [('a', 'b'), ('b', 'c')]
# /////////
# زیپ  zip
# جفت کردن ۲ لیست
# ایندکس همون متغیر بشه ولیو بعدی
from itertools import combinations , permutations , product ,  combinations_with_replacement , pairwise
from collections import OrderedDict
my_key=['a','b','c' ]
my_val=['1','2','3']
b={}
a= OrderedDict(zip(my_key,my_val))
print(a)
# OrderedDict([('a', '1'), ('b', '2'), ('c', '3')])

# ////////

from more_itertools import flatten, chunked , spy , difference , distinct_combinations , distinct_permutations , divide
# کار با کتابخانه مور ایترتولز
# more itertools
# flatten
# همه دسته بندی های درون لیست را باز میکنه و میریزه تو یه لیست یا تاپل
my_list=[(1,2),(3,4)]
print(list(flatten(my_list)))
# [1, 2, 3, 4]

# //////////////////

# chunked
# لیست را دسته بندی میکنه  تکه تکه میکنه درون لیست میریزه یا تاپل میریزه
my_list=[1,2 , 3,4]
print(tuple(chunked(my_list,2)))
# [[1, 2], [3, 4]]
# ([1, 2], [3, 4])

# //////////
# ترکیب  
# pairwise
# و 
# combinations

# با هم در دو حلقه برای ساخت دیکشنری
from itertools import combinations , permutations , product ,  combinations_with_replacement , pairwise
from collections import OrderedDict
my_key=['a','b','c' ]
my_val=['1','2','3']
# print(my_key , my_val)
a={}
for ke in pairwise(my_key):
    for va in combinations(my_val,2):
        a[ke]=va
print(a)
# {('a', 'b'): ('2', '3'), ('b', 'c'): ('2', '3')}


# /////////////
# برای حلقه زدن ایتر تولز
# مقایسه ترکیب و جایگشت
# در جایگشت ترتیب مهم است
zia='۱۲۳۴'
zia2=(list(permutations(zia)))
count=0
for tup in zia2:
    count+=1
    print('number : ', count ,', and the permutation is', tup)

# number :  1 , and the permutation is ('۱', '۲', '۳', '۴')
# number :  2 , and the permutation is ('۱', '۲', '۴', '۳')
# number :  3 , and the permutation is ('۱', '۳', '۲', '۴')
# number :  4 , and the permutation is ('۱', '۳', '۴', '۲')
# number :  5 , and the permutation is ('۱', '۴', '۲', '۳')
# number :  6 , and the permutation is ('۱', '۴', '۳', '۲')
# number :  7 , and the permutation is ('۲', '۱', '۳', '۴')
# number :  8 , and the permutation is ('۲', '۱', '۴', '۳')
# number :  9 , and the permutation is ('۲', '۳', '۱', '۴')
# number :  10 , and the permutation is ('۲', '۳', '۴', '۱')
# number :  11 , and the permutation is ('۲', '۴', '۱', '۳')
# number :  12 , and the permutation is ('۲', '۴', '۳', '۱')
# number :  13 , and the permutation is ('۳', '۱', '۲', '۴')
# number :  14 , and the permutation is ('۳', '۱', '۴', '۲')
# number :  15 , and the permutation is ('۳', '۲', '۱', '۴')
# number :  16 , and the permutation is ('۳', '۲', '۴', '۱')
# number :  17 , and the permutation is ('۳', '۴', '۱', '۲')
# number :  18 , and the permutation is ('۳', '۴', '۲', '۱')
# number :  19 , and the permutation is ('۴', '۱', '۲', '۳')
# number :  20 , and the permutation is ('۴', '۱', '۳', '۲')
# number :  21 , and the permutation is ('۴', '۲', '۱', '۳')
# number :  22 , and the permutation is ('۴', '۲', '۳', '۱')
# number :  23 , and the permutation is ('۴', '۳', '۱', '۲')
# number :  24 , and the permutation is ('۴', '۳', '۲', '۱')

# ترکیب ۴ تایی
# ترکیب ۴ تایی از ۴ حرفو این میشه
# همون ترکیب دو به دو این میشه
# در ترکیب ترتیب مهم نیست
zia3=(list(combinations(zia,4)))
print(zia3)
# [('۱', '۲', '۳', '۴')]
count=0
for tup in zia3:
    count+=1
    print('number : ', count ,', and the combination is', tup)
# number :  1 , and the combination is ('۱', '۲', '۳', '۴')

# ///////
# همون ترکیب دو به دو این میشه
zia3=(list(combinations(zia,2)))
print(zia3)
# [('۱', '۲'), ('۱', '۳'), ('۱', '۴'), ('۲', '۳'), ('۲', '۴'), ('۳', '۴')]
count=0
for tup in zia3:
    count+=1
    print('number : ', count ,', and the combination is', tup)

# number :  1 , and the combination is ('۱', '۲')
# number :  2 , and the combination is ('۱', '۳')
# number :  3 , and the combination is ('۱', '۴')
# number :  4 , and the combination is ('۲', '۳')
# number :  5 , and the combination is ('۲', '۴')
# number :  6 , and the combination is ('۳', '۴')

# ////////////////////////



# شماردن تعداد جایگشت ها
# به ازای هر عدد در درون جایگشت همون تعداد جایگشت ها را میاره

# یعنی ۴ عدد داریم 
# به ازای ۱ جایگشت ۲۴ میشه ۲۴ حالت 
# به ازای عدد ۲ جایگشت  میشه ۲۴ حالت
# به ازای ۳ میشه ۲۴
# به ازای ۴ میشه ۲۴
#  ت۴ا ۲۴ تا میشه ۹۶ تا 

# اما چرا ؟ اسم ریاضیش چیه؟
# فرمول اینه 
#  تعداد کل جایگشت * تعداد اعداد= تعداد کل ترکیب در صف نخست ایستادن هر عدد در کل جایگشت 
 

from itertools import permutations , combinations, pairwise ,product
zia='۱۲۳۴'
zia2=(list(permutations(zia)))

zia3=(list(product(zia,zia2)))
print(zia3)

# [('۱', ('۱', '۲', '۳', '۴')), ('۱', ('۱', '۲', '۴', '۳')), ('۱', ('۱', '۳', '۲', '۴')), ('۱', ('۱', '۳', '۴', '۲')), ('۱', ('۱', '۴', '۲', '۳')), ('۱', ('۱', '۴', '۳', '۲')), ('۱', ('۲', '۱', '۳', '۴')), ('۱', ('۲', '۱', '۴', '۳')), ('۱', ('۲', '۳', '۱', '۴')), ('۱', ('۲', '۳', '۴', '۱')), ('۱', ('۲', '۴', '۱', '۳')), ('۱', ('۲', '۴', '۳', '۱')), ('۱', ('۳', '۱', '۲', '۴')), ('۱', ('۳', '۱', '۴', '۲')), ('۱', ('۳', '۲', '۱', '۴')), ('۱', ('۳', '۲', '۴', '۱')), ('۱', ('۳', '۴', '۱', '۲')), ('۱', ('۳', '۴', '۲', '۱')), ('۱', ('۴', '۱', '۲', '۳')), ('۱', ('۴', '۱', '۳', '۲')), ('۱', ('۴', '۲', '۱', '۳')), ('۱', ('۴', '۲', '۳', '۱')), ('۱', ('۴', '۳', '۱', '۲')), ('۱', ('۴', '۳', '۲', '۱')), ('۲', ('۱', '۲', '۳', '۴')), ('۲', ('۱', '۲', '۴', '۳')), ('۲', ('۱', '۳', '۲', '۴')), ('۲', ('۱', '۳', '۴', '۲')), ('۲', ('۱', '۴', '۲', '۳')), ('۲', ('۱', '۴', '۳', '۲')), ('۲', ('۲', '۱', '۳', '۴')), ('۲', ('۲', '۱', '۴', '۳')), ('۲', ('۲', '۳', '۱', '۴')), ('۲', ('۲', '۳', '۴', '۱')), ('۲', ('۲', '۴', '۱', '۳')), ('۲', ('۲', '۴', '۳', '۱')),
# ('۲', ('۳', '۱', '۲', '۴')), ('۲', ('۳', '۱', '۴', '۲')), ('۲', ('۳', '۲', '۱', '۴')), ('۲', ('۳', '۲', '۴', '۱')), ('۲', ('۳', '۴', '۱', '۲')), ('۲', ('۳', '۴', '۲', '۱')), ('۲', ('۴', '۱', '۲', '۳')), ('۲', ('۴', '۱', '۳', '۲')), ('۲', ('۴', '۲', '۱', '۳')), ('۲', ('۴', '۲', '۳', '۱')), ('۲', ('۴', '۳', '۱', '۲')), ('۲', ('۴', '۳', '۲', '۱')), ('۳', ('۱', '۲', '۳', '۴')), ('۳', ('۱', '۲', '۴', '۳')), ('۳', ('۱', '۳', '۲', '۴')), ('۳', ('۱', '۳', '۴', '۲')), ('۳', ('۱', '۴', '۲', '۳')), ('۳', ('۱', '۴', '۳', '۲')), ('۳', ('۲', '۱', '۳', '۴')), ('۳', ('۲', '۱', '۴', '۳')), ('۳', ('۲', '۳', '۱', '۴')), ('۳', ('۲', '۳', '۴', '۱')), ('۳', ('۲', '۴', '۱', '۳')), ('۳', ('۲', '۴', '۳', '۱')), ('۳', ('۳', '۱', '۲', '۴')), ('۳', ('۳', '۱', '۴', '۲')), ('۳',
# ('۳', '۲', '۱', '۴')), ('۳', ('۳', '۲', '۴', '۱')), ('۳', ('۳', '۴', '۱', '۲')), ('۳', ('۳', '۴', '۲', '۱')), ('۳', ('۴', '۱', '۲', '۳')), ('۳', ('۴', '۱', '۳', '۲')), ('۳', ('۴', '۲', '۱',
# '۳')), ('۳', ('۴', '۲', '۳', '۱')), ('۳', ('۴', '۳', '۱', '۲')), ('۳', ('۴', '۳', '۲', '۱')), ('۴', ('۱', '۲', '۳', '۴')), ('۴', ('۱', '۲', '۴', '۳')), ('۴', ('۱', '۳', '۲', '۴')), ('۴', ('۱', '۳', '۴', '۲')), ('۴', ('۱', '۴', '۲', '۳')), ('۴', ('۱', '۴', '۳', '۲')), ('۴', ('۲', '۱',
# '۳', '۴')), ('۴', ('۲', '۱', '۴', '۳')), ('۴', ('۲', '۳', '۱', '۴')), ('۴', ('۲', '۳', '۴', '۱')), ('۴', ('۲', '۴', '۱', '۳')), ('۴', ('۲', '۴', '۳', '۱')), ('۴', ('۳', '۱', '۲', '۴')), ('۴', ('۳', '۱', '۴', '۲')), ('۴', ('۳', '۲', '۱', '۴')), ('۴', ('۳', '۲', '۴', '۱')), ('۴', ('۳',
# '۴', '۱', '۲')), ('۴', ('۳', '۴', '۲', '۱')), ('۴', ('۴', '۱', '۲', '۳')), ('۴', ('۴', '۱', '۳', '۲')), ('۴', ('۴', '۲', '۱', '۳')), ('۴', ('۴', '۲', '۳', '۱')), ('۴', ('۴', '۳', '۱', '۲')), ('۴', ('۴', '۳', '۲', '۱'))]

count=0
for tup in zia3:
    count+=1
    print('number : ', count ,', and the combination is', tup)
    
# هر عدد ۶ تا جایگشت داره اما چرا؟
# طبق چه فرمولی؟ ایا ریاضی اونو توضیح میده ؟  ترکیبیات هست؟   
#  تعداد کل جایگشت / تعداد اعداد میشه = تعداد اولویت داشتن هر عدد در صف نخست 


# مابقی هم طبق اون اولویت نصف میشه هی . یعنی ۴ حالت یک اولویت اول باشه اون موقع ۲ حالت ۲ اولویت دوم میشه سپس 
# و در اون حالت عدد بعدی ۱ حالت در اولویت بعدی میشه
# اما اسم ریاضی اش چیه؟
# نظریه اولویت؟ !

# ایا می تونیم اینرا در نظریه بازی بکار ببریم یا منطق ترجیح و نظریه تصمیم؟ 
# که بگیم تعدا حالاتی که اون به اون یکی ترجیح بیابد این است
# تعداد حالت هایی که هر دو بازیکن با هم ترجیح بدهند مثلا پارتو اپتیمال را و.... را

# عدد ۱
# number :  1 , and the combination is ('۱', ('۱', '۲', '۳', '۴'))
# number :  2 , and the combination is ('۱', ('۱', '۲', '۴', '۳'))
# number :  3 , and the combination is ('۱', ('۱', '۳', '۲', '۴'))
# number :  4 , and the combination is ('۱', ('۱', '۳', '۴', '۲'))
# number :  5 , and the combination is ('۱', ('۱', '۴', '۲', '۳'))
# number :  6 , and the combination is ('۱', ('۱', '۴', '۳', '۲'))

# number :  7 , and the combination is ('۱', ('۲', '۱', '۳', '۴'))
# number :  8 , and the combination is ('۱', ('۲', '۱', '۴', '۳'))
# number :  9 , and the combination is ('۱', ('۲', '۳', '۱', '۴'))
# number :  10 , and the combination is ('۱', ('۲', '۳', '۴', '۱'))
# number :  11 , and the combination is ('۱', ('۲', '۴', '۱', '۳'))
# number :  12 , and the combination is ('۱', ('۲', '۴', '۳', '۱'))

# number :  13 , and the combination is ('۱', ('۳', '۱', '۲', '۴'))
# number :  14 , and the combination is ('۱', ('۳', '۱', '۴', '۲'))
# number :  15 , and the combination is ('۱', ('۳', '۲', '۱', '۴'))
# number :  16 , and the combination is ('۱', ('۳', '۲', '۴', '۱'))
# number :  17 , and the combination is ('۱', ('۳', '۴', '۱', '۲'))
# number :  18 , and the combination is ('۱', ('۳', '۴', '۲', '۱'))

# number :  19 , and the combination is ('۱', ('۴', '۱', '۲', '۳'))
# number :  20 , and the combination is ('۱', ('۴', '۱', '۳', '۲'))
# number :  21 , and the combination is ('۱', ('۴', '۲', '۱', '۳'))
# number :  22 , and the combination is ('۱', ('۴', '۲', '۳', '۱'))
# number :  23 , and the combination is ('۱', ('۴', '۳', '۱', '۲'))
# number :  24 , and the combination is ('۱', ('۴', '۳', '۲', '۱'))


# عدد ۲
# number :  25 , and the combination is ('۲', ('۱', '۲', '۳', '۴'))
# number :  26 , and the combination is ('۲', ('۱', '۲', '۴', '۳'))
# number :  27 , and the combination is ('۲', ('۱', '۳', '۲', '۴'))
# number :  28 , and the combination is ('۲', ('۱', '۳', '۴', '۲'))
# number :  29 , and the combination is ('۲', ('۱', '۴', '۲', '۳'))
# number :  30 , and the combination is ('۲', ('۱', '۴', '۳', '۲'))

# number :  31 , and the combination is ('۲', ('۲', '۱', '۳', '۴'))
# number :  32 , and the combination is ('۲', ('۲', '۱', '۴', '۳'))
# number :  33 , and the combination is ('۲', ('۲', '۳', '۱', '۴'))
# number :  34 , and the combination is ('۲', ('۲', '۳', '۴', '۱'))
# number :  35 , and the combination is ('۲', ('۲', '۴', '۱', '۳'))
# number :  36 , and the combination is ('۲', ('۲', '۴', '۳', '۱'))

# number :  37 , and the combination is ('۲', ('۳', '۱', '۲', '۴'))
# number :  38 , and the combination is ('۲', ('۳', '۱', '۴', '۲'))
# number :  39 , and the combination is ('۲', ('۳', '۲', '۱', '۴'))
# number :  40 , and the combination is ('۲', ('۳', '۲', '۴', '۱'))
# number :  41 , and the combination is ('۲', ('۳', '۴', '۱', '۲'))
# number :  42 , and the combination is ('۲', ('۳', '۴', '۲', '۱'))

# number :  43 , and the combination is ('۲', ('۴', '۱', '۲', '۳'))
# number :  44 , and the combination is ('۲', ('۴', '۱', '۳', '۲'))
# number :  45 , and the combination is ('۲', ('۴', '۲', '۱', '۳'))
# number :  46 , and the combination is ('۲', ('۴', '۲', '۳', '۱'))
# number :  47 , and the combination is ('۲', ('۴', '۳', '۱', '۲'))
# number :  48 , and the combination is ('۲', ('۴', '۳', '۲', '۱'))


# عدد ۳
# number :  49 , and the combination is ('۳', ('۱', '۲', '۳', '۴'))
# number :  50 , and the combination is ('۳', ('۱', '۲', '۴', '۳'))
# number :  51 , and the combination is ('۳', ('۱', '۳', '۲', '۴'))
# number :  52 , and the combination is ('۳', ('۱', '۳', '۴', '۲'))
# number :  53 , and the combination is ('۳', ('۱', '۴', '۲', '۳'))
# number :  54 , and the combination is ('۳', ('۱', '۴', '۳', '۲'))

# number :  55 , and the combination is ('۳', ('۲', '۱', '۳', '۴'))
# number :  56 , and the combination is ('۳', ('۲', '۱', '۴', '۳'))
# number :  57 , and the combination is ('۳', ('۲', '۳', '۱', '۴'))
# number :  58 , and the combination is ('۳', ('۲', '۳', '۴', '۱'))
# number :  59 , and the combination is ('۳', ('۲', '۴', '۱', '۳'))
# number :  60 , and the combination is ('۳', ('۲', '۴', '۳', '۱'))

# number :  61 , and the combination is ('۳', ('۳', '۱', '۲', '۴'))
# number :  62 , and the combination is ('۳', ('۳', '۱', '۴', '۲'))
# number :  63 , and the combination is ('۳', ('۳', '۲', '۱', '۴'))
# number :  64 , and the combination is ('۳', ('۳', '۲', '۴', '۱'))
# number :  65 , and the combination is ('۳', ('۳', '۴', '۱', '۲'))
# number :  66 , and the combination is ('۳', ('۳', '۴', '۲', '۱'))

# number :  67 , and the combination is ('۳', ('۴', '۱', '۲', '۳'))
# number :  68 , and the combination is ('۳', ('۴', '۱', '۳', '۲'))
# number :  69 , and the combination is ('۳', ('۴', '۲', '۱', '۳'))
# number :  70 , and the combination is ('۳', ('۴', '۲', '۳', '۱'))
# number :  71 , and the combination is ('۳', ('۴', '۳', '۱', '۲'))
# number :  72 , and the combination is ('۳', ('۴', '۳', '۲', '۱'))


# عدد ۴
# number :  73 , and the combination is ('۴', ('۱', '۲', '۳', '۴'))
# number :  74 , and the combination is ('۴', ('۱', '۲', '۴', '۳'))
# number :  75 , and the combination is ('۴', ('۱', '۳', '۲', '۴'))
# number :  76 , and the combination is ('۴', ('۱', '۳', '۴', '۲'))
# number :  77 , and the combination is ('۴', ('۱', '۴', '۲', '۳'))
# number :  78 , and the combination is ('۴', ('۱', '۴', '۳', '۲'))

# number :  79 , and the combination is ('۴', ('۲', '۱', '۳', '۴'))
# number :  80 , and the combination is ('۴', ('۲', '۱', '۴', '۳'))
# number :  81 , and the combination is ('۴', ('۲', '۳', '۱', '۴'))
# number :  82 , and the combination is ('۴', ('۲', '۳', '۴', '۱'))
# number :  83 , and the combination is ('۴', ('۲', '۴', '۱', '۳'))
# number :  84 , and the combination is ('۴', ('۲', '۴', '۳', '۱'))

# number :  85 , and the combination is ('۴', ('۳', '۱', '۲', '۴'))
# number :  86 , and the combination is ('۴', ('۳', '۱', '۴', '۲'))
# number :  87 , and the combination is ('۴', ('۳', '۲', '۱', '۴'))
# number :  88 , and the combination is ('۴', ('۳', '۲', '۴', '۱'))
# number :  89 , and the combination is ('۴', ('۳', '۴', '۱', '۲'))
# number :  90 , and the combination is ('۴', ('۳', '۴', '۲', '۱'))

# number :  91 , and the combination is ('۴', ('۴', '۱', '۲', '۳'))
# number :  92 , and the combination is ('۴', ('۴', '۱', '۳', '۲'))
# number :  93 , and the combination is ('۴', ('۴', '۲', '۱', '۳'))
# number :  94 , and the combination is ('۴', ('۴', '۲', '۳', '۱'))
# number :  95 , and the combination is ('۴', ('۴', '۳', '۱', '۲'))
# number :  96 , and the combination is ('۴', ('۴', '۳', '۲', '۱'))
# حالا چطور فقط اولویت اول را بگیریم ؟ یعنی بگیم مد نظرمون اینه که مثلا ۴ اولویت اول باشه
# کل تعداد حالت هاش میشه ۱ 
# بعد برای اولویت ۳ هم میشه ۱ 
# و به همین ترتتیب
# این اسم ریاضیش چیه؟

# ///////////////////////
# چرخش بین اعضا دو لیست
# چرخیدن  و زیپ کردن
# به اندازه لیست اولی میگرده در دومی و تاپل میکنه 
# تموم که شد میره از اول لیست اولی میگرده 
# تا اخرین کارکاتر لیست دومی
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]

from itertools import cycle
# اگر طول الف بزگرتر از ب بود ای را بگیر با چرخش بی زیپ کن 
# در غیر این صورت 
# چرخش بی را با ای زیپ کن
zip_list = zip(A, cycle(B)) if len(A) > len(B) else zip(cycle(A), B)
print(list(zip_list))
# [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'A'), (5, 'B'), (6, 'C'), (7, 'A'), (8, 'B'), (9, 'C')]


# ///////////////
from itertools import cycle, zip_longest
def zip_cycle(*iterables, empty_default=None):
    cycles = [cycle(i) for i in iterables]
    for _ in zip_longest(*iterables):
        yield tuple(next(i, empty_default) for i in cycles)
for i in zip_cycle(range(2), range(5), ['a', 'b', 'c'], []):
    print(i)
# (0, 0, 'a', None)
# (1, 1, 'b', None)
# (0, 2, 'c', None)
# (1, 3, 'a', None)
# (0, 4, 'b', None)
    
    
# ////////////////////////

from itertools import cycle
# تا بینهایت میچرخه برمیگره از اول
my= cycle('mamad namjoo')
print(my)
print(my)
print(next(my))
# m
# اگر دفعه بعد بیاریم
print(next(my))
# a

# برای پیمایش از 
# for
# استفاده میکنیم


my=[1,2,3]
# print(my)
boro=cycle(my)
# print(next(boro))
for char in boro:
    print(char)
    
# تا بینهایت میده
# 3
# 1
# 2
# 3
# 1
# .
# .
# .
# ////////////////////
# زیپ و چرخش
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]
from itertools import cycle,permutations
# خود زیپ دو تا چیز را میاره  دو به دو میبنده به هم
# حالا میشه یه متد ایتربل باشه اون زیپ کردن

# به اندازه بیشتره میچرخونه
# به اندازه بزرگه میچرخونه
zip_list = zip(A, cycle(B)) 
print(list(zip_list))
# [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'A'), (5, 'B'), (6, 'C'), (7, 'A'), (8, 'B'), (9, 'C')]

# هرکدوم که کوچکتره را در سایکل بزار که اون بچرخه وگرنه بزرگه که ثابته. یعنی برعکسه. 
# معیار اونیکی است

# به اندازه کمتره میچرخونه
# به اندازه کوچیکه میچرخونه
zip_list = zip(cycle(A), (B)) 
print(list(zip_list))
# [(1, 'A'), (2, 'B'), (3, 'C')]



# البته زیپ هم میشه بیاد 
# به اندازه کمتره میچرخونه
# به اندازه کوچیکه میچرخونه
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]
print(list(zip(A,B)))
# [(1, 'A'), (2, 'B'), (3, 'C')]




# ///////
# مساله 
# اگر سه تا یا بیشتر  لیست داشته باشیم که یکیشون تعدادش بیشتر باشه و به تعداد بیشتره بخوایم بچرخه
# باید برای هر کدوم از لیست های دیگه یه سیرکل بنویسیم
# وگرنه به اندازه کوچکترینه میچرخه
m_players=['Human1', 'Human2', 'Human3',]
myplayerlist=['Hossein','Maziar','Akbar'] 


post=['goalkeeper','deffender','modifier','forward'] #'forward'
shuffle(post)
# price= [randint(1,200) for i in (post)] # برای اینکه لیستی رندوم درست کنم به اندازه بزرگتره
print(list(zip((post),cycle(myplayerlist),cycle(m_players))))
# [('modifier', 'Hossein', 'Human1'), ('goalkeeper', 'Maziar', 'Human2'), ('deffender', 'Akbar', 'Human3'), ('forward', 'Hossein', 'Human1')]
# اینجا ۴ تا خروجی درست میکنه ولی اگر سیکل را نمیزاشتم حتی واسه یکی ۳ تا درست میکرد

print(list(zip((post),cycle(myplayerlist),(m_players))))
# [('modifier', 'Hossein', 'Human1'), ('deffender', 'Maziar', 'Human2'), ('goalkeeper', 'Akbar', 'Human3')]

# نکته دیگر اینکه در این خروجی
# [('modifier', 'Hossein', 'Human1'), ('goalkeeper', 'Maziar', 'Human2'), ('deffender', 'Akbar', 'Human3'), 
# ('forward', 'Hossein', 'Human1')]
# برای پست خالی مونده میاد از اول آغاز میکنه و همون اولی ها را میاره دوباره
# یعنی اینجا حسین و هیومن ۱ دوباره میان

# ایا میشه این هم رندوم باشه یعنی از اول نیاد


# حالا اگر سایکل را برای یکی بزنیم که به اندازه بیشترینه باشه 
price= [randint(1,200) for i in (post)] # برای اینکه لیستی رندوم درست کنم به اندازه بزرگتره
print(list(zip((post),cycle(myplayerlist),cycle(m_players))))
# اینجا ۱۲۰ را دوبار زده
print(list(zip((post),cycle(myplayerlist),cycle(m_players),(price))))
# [('deffender', 'Hossein', 'Human1', 120), ('forward', 'Maziar', 'Human2', 123),
# ('modifier', 'Akbar', 'Human3', 120), ('goalkeeper', 'Hossein', 'Human1', 146)]

# ولی در این یک بار زده 
print(list(zip((post),cycle(myplayerlist),cycle(m_players),cycle(price))))
# [('goalkeeper', 'Hossein', 'Human1', 20), ('modifier', 'Maziar', 'Human2', 121), ('forward', 'Akbar', 'Human3', 174), ('deffender', 'Hossein', 'Human1', 86)]




# ////////
# در زیپ  به تعداد کمترین  میاره  حالا اگر دیکشنری ای بسازیک که یکیش را کلید کنیم و بقیه را ولیو 
# قانون ثابته هر که کوچیکتره سیرکل میخوره تا به بقیه برسه
# اگر این لیست باشه
m_players=['Human1', 'Human2', 'Human3','Human4', 'Human5','Human6']
myplayerlist=['Hossein','Maziar','Akbar','pedi', 'shervin','farhad'] 
post=['goalkeeper','deffender','modifier','forward'] #'forward'
shuffle(post)
# تا اینجا پست را تعین کردم
price= [randint(1,200) for i in (myplayerlist)]

# پست کوچکترینشونه پس پست باید بچرخه
def two_list_dict(key_list,value_list):
    mydict={}
    shuffle(key_list)
    shuffle(value_list)    # یا اینجا میتونی تعریف کنی
# پست کوچکترینشونه پس پست باید بچرخه
    for key, value ,j, k in zip((key_list),(value_list),(price),(post)):
            mydict [key]=(value,j,k)
    return mydict
mydict=(two_list_dict(m_players,myplayerlist))
print(mydict)

# اینو میده
# {'Human6': ('farhad', 17, 'forward'), 
# 'Human4': ('Maziar', 161, 'goalkeeper'), 
# 'Human3': ('Akbar', 90, 'modifier'),
# 'Human5': ('shervin', 75, 'deffender')}

#: راهکار
def two_list_dict(key_list,value_list):
    mydict={}
    shuffle(key_list)
    shuffle(value_list)    # یا اینجا میتونی تعریف کنی
    for key, value ,j, k in zip((key_list),(value_list),(price),cycle(post)):
            mydict [key]=(value,j,k)
    return mydict
mydict=(two_list_dict(m_players,myplayerlist))
print(mydict)


# {'Human2': ('Akbar', 188, 'modifier'), 'Human5': ('farhad', 169, 'deffender'), 'Human4': ('pedi', 163, 'forward'), 'Human6': ('Hossein', 104, 'goalkeeper'), 'Human1': ('shervin', 77, 'modifier'), 'Human3': ('Maziar', 56, 'deffender')}

# حالا اگر دوتاش کوچکتر باشه


# ////////////
# زیپ جایگشت
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]
from itertools import cycle,permutations
zip_list = zip(A, permutations(B)) 
print(list(zip_list))
# [(1, ('A', 'B', 'C')), (2, ('A', 'C', 'B')), (3, ('B', 'A', 'C')), (4, ('B', 'C', 'A')), (5, ('C', 'A', 'B')), (6, ('C', 'B', 'A'))]

# ////////
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]
from itertools import cycle,permutations,combinations,pairwise
zip_list = zip(A, pairwise(B)) 
print(list(zip_list))
# [(1, ('A', 'B')), (2, ('B', 'C'))]

# ////////
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]
from itertools import cycle,permutations,combinations,pairwise
zip_list = zip(A, combinations(B,2)) 
print(list(zip_list))
# [(1, ('A', 'B')), (2, ('A', 'C')), (3, ('B', 'C'))]

# /////
A = [1,2,3,4,5,6,7,8,9]
B = ["A","B","C"]
from itertools import cycle,permutations,combinations,pairwise,product
zip_list = zip(A, product(B)) 
print(list(zip_list))
# [(1, ('A',)), (2, ('B',)), (3, ('C',))]

# ////////////
# chain
# پخش میکند ایتریبل ها را 
# مثل لیست و تاپل و استرینگ را 
# لی نه اینتیجر را
from itertools import cycle,chain
# پخس مشکنه اعضا را درون یه لیست دیگر
odds=[1,2,3,4]
enens=[54254]
my=chain(odds,enens)
print(list(my))
# [1, 2, 3, 4, 54254]

# ///////////

from itertools import cycle,chain
# متد فرام ایتریبل . اعضای درونی استرینگ و یا استرینگ درون لیست یا تاپل  را تجزیه ترین میکنه
odds=['1,2,3,4']

my=chain.from_iterable(odds)
print(list(my))
# ['1', ',', '2', ',', '3', ',', '4']


# //////
# اما فرام ایتریبل روی ا اعداد کار نمیکنه
# چون عدد تجزیه نمیشه خودش
odds=[1,2,3,4]
my=chain.from_iterable(odds)
print(list(my))
# TypeError: 'int' object is not iterable

# /////////

# Python code to demonstrate 
# itertools.groupby() method 
  
  
import itertools
  
  
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
  
# Key function
key_func = lambda x: x[0]

for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))
# a : [('a', 1), ('a', 2)]
# b : [('b', 3), ('b', 4)]

# /////////
import itertools
# گروپ بای 

# This method calculates the keys for each element present in iterable. It returns key and iterable of grouped items.
a_list = [("Animal", "cat"), 
          ("Animal", "dog"), 
          ("Bird", "peacock"), 
          ("Bird", "pigeon")]

an_iterator = itertools.groupby(a_list, lambda x : x[0])

for key, group in an_iterator:
    key_and_group = {key : list(group)}
    print(key_and_group)

# {'Animal': [('Animal', 'cat'), ('Animal', 'dog')]}
# {'Bird': [('Bird', 'peacock'), ('Bird', 'pigeon')]}

# ////////
from itertools import groupby
lst = [(1, 'a'), (2, 'b'), (2, 'c'), (3, 'd')]
res = {k: [b for a, b in g] for k, g in groupby(lst, key=lambda x: x[0])}
print(res)
# {1: ['a'], 2: ['b', 'c'], 3: ['d']}

# ///////

# برش زدن دیکشنری
import itertools
test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
 # {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}
print("The original dictionary : " + str(test_dict))
N = 3
out = dict(itertools.islice(test_dict.items(), N))
print("Dictionary limited by K is : " + str(out))
# {'Geeks': 1, 'For': 2, 'is': 3}

# ////////////


# ایترتولز
# دو به دو میاره با هم
from itertools import product

result = product('ab', '12')
list(result)
# [('a', '1'), ('a', '2'), ('b', '1'), ('b', '2')]
# ////////
# تکرار یه چیز 
# با ترکیب و با جایگشت
from itertools import product

product('A', repeat=4)
# A A A A

# ///////////
# تا بینهایت میشماره اگر چیزی ندیم
from itertools import product, count
list(product(count()))


# ///////
# کار با ترکیب
# product
import itertools
letter=('ABCD')
print(itertools.product(letter))
# <itertools.product object at 0x00000213C1D25440>

# پس باید لیست کنی 

# این یه دونه میده پروداکت دو تا چیز باید باشه
import itertools
letter=('ABCD')
print(list((itertools.product(letter))))
# [('A',), ('B',), ('C',), ('D',)]

# //////////
# اینجا دو تا متغیر را با هم اورده 
# ترکیب کرده اعضا را با هم 
# دونه دونه
letter=('ABCD')
letter2=('XOZ')
print(list((itertools.product(letter,letter2))))
# [('A', 'X'), ('A', 'O'), ('A', 'Z'), ('B', 'X'), ('B', 'O'), ('B', 'Z'), ('C', 'X'), ('C', 'O'), ('C', 'Z'), ('D', 'X'), ('D', 'O'), ('D', 'Z')]


# ////////
# میشه خودش رنج هم بزنه عدد بده
# یعنی بشماره

letter=('ABCD')
print(list((itertools.product(letter,range(3)))))
# [('A', 0), ('A', 1), ('A', 2), ('B', 0), ('B', 1), ('B', 2), ('C', 0), ('C', 1), ('C', 2), ('D', 0), ('D', 1), ('D', 2)]

# ///////////
# میشه اولی هم حتی رنج باشه
import itertools
print(list((itertools.product(range(3),range(3)))))
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# /////////////////////////////////////////////////////////////////////////////////////
# /////////

# ///////
# جایگشت
# اعضای یه لیست را با هم مقایسه میکنه
import itertools
def mylist(lst):
    for number in itertools.permutations(lst):
        print(number)    
my=[6,9,10,14] 
print(mylist(my))

# (6, 9, 10, 14)
# (6, 9, 14, 10)
# (6, 10, 9, 14)
# (6, 10, 14, 9)
# (6, 14, 9, 10)
# (6, 14, 10, 9)
# (9, 6, 10, 14)
# (9, 6, 14, 10)
# (9, 10, 6, 14)
# (9, 10, 14, 6)
# (9, 14, 6, 10)
# (9, 14, 10, 6)
# (10, 6, 9, 14)
# (10, 6, 14, 9)
# (10, 9, 6, 14)
# (10, 9, 14, 6)
# (10, 14, 6, 9)
# (10, 14, 9, 6)
# (14, 6, 9, 10)
# (14, 6, 10, 9)
# (14, 9, 6, 10)
# (14, 9, 10, 6)
# (14, 10, 6, 9)
# (14, 10, 9, 6)
# None
# ////////
# اعضای لیست را چند تا چندتا که ما تعین کنیم با هم مقایسه میکنه
# اعضای یه لیست را دو تا دوتا با هم مقایسه میکنه اینجا

import itertools
def mylist(lst):
    for number in itertools.permutations(lst,2):
        print(number)    
my=[6,9,10,14] 
print(mylist(my))
# (6, 9)
# (6, 10)
# (6, 14)
# (9, 6)     تکراری
# (9, 10)
# (9, 14)
# (10, 6)     تکراری با ۶
# (10, 9)     تکراری با ۹
# (10, 14)
# (14, 6)    تکراری  
# (14, 9)   تکرای 
# (14, 10)   تکراری
# None
# ///////////////////

import itertools
def mylist(lst):
    for number in itertools.permutations(lst,2):
        print(number)    
        print(number[0])
# در اینجا به عنصر 
#  n ام 
# اون اشاره می کنیم
# (6, 9)
# 6
# (6, 10)
# 6
# (6, 14)
# 6
# (9, 6)
# 9
# (9, 10)
# 9
# (9, 14)
# 9
# (10, 6)
# 10
# (10, 9)
# 10
# (10, 14)
# 10
# (14, 6)
# 14
# (14, 9)
# 14
# (14, 10)
# 14
# None
my=[6,9,10,14] 
print(mylist(my))
# ///////////
# اینجا یه کاری کردیم با اون چیزها که اشاره شده 
# قدر مطلق اون دو تا را با هم گرفته
import itertools
def mylist(lst):
    for number in itertools.permutations(lst,2):
        print(number)
        # در اینجا قدر مطلق اون دو تا را با هم میگیریم
        print(abs(number[0]-number[1]))
        
# (6, 9)
# 3
# (6, 10)
# 4
# (6, 14)
# 8
# (9, 6)
# 3
# (9, 10)
# 1
# (9, 14)
# 5
# (10, 6)
# 4
# (10, 9)
# 1
# (10, 14)
# 4
# (14, 6)
# 8
# (14, 9)
# 5
# (14, 10)
# 4
# None
my=[6,9,10,14] 
print(mylist(my))

# /////////

import itertools
def sumPairs(lst):
    diffs=[]
    # توجه اگر اینجا ۳ بزنی بجای ۲ سه تا سه تایی مقایسه میکنه
    # ولی اگر تعدادش را بیشتر از اعضای لیست بزنی خروجی اخر ار ۰ میده
    # و جالبه اگر برداریم و هیچی نزاریم به تعداد 
    # اعداد را دونه دونه میاره مثلا اعضا اگر ۳ باشه ۳ تا ۳ تا مقایسه میکنه
    for e in itertools.permutations(lst):
       diffs.append(abs(e[1]-e[0]))
       print(e)
# جفت جفت میاره با هم مقایسه میکنه 
# (6, 9)
# (6, 10)
# (9, 6)
# (9, 10)
# (10, 6)
# (10, 9)
# اینجا هم اومده جمع زده تقسیم بر ۲ کرده تا حالات تکراری را در نظر نیاره
    return int(sum(diffs)/2)
# Driver program
lst = [6,9,10]
print(sumPairs(lst))
# 8
# ////////////////////////////
# البته این کد خلاصه ترشه
# همون کار تابع بالا را میکنه
import itertools
def sumPairs(lst):
    
    diffs = [abs(e[1] - e[0]) for e in itertools.permutations(lst, 2)]
    # فقط پرسش میاد وقتی داشت با 
    # enumerate
    # کار می کرد یه شرط اضافه کرد اگر خودش نباشه
    # اینجا نیاز نیست؟
    return int(sum(diffs)/2)
# Driver program
lst = [6,9,10]
print(sumPairs(lst))
# 8
# ////////////
# برش زدن
# تقسیم کردن

# چگونه یک دیکشنری را به تعداد دلخواه برش بزنیم

# به نصف برش بزنه

from itertools import islice
mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            
my=dict(islice(mydictha.items(),len(mydictha)//2))
print(my)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}

# یا به تعدادی که میگیم برش بزنه
# مثلا ۳ تا

N=2
out = dict(islice(mydictha.items(), N))
print((out))
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286}


# //////
# ?????????/

# iter
# یه چیز را مثلا دیکشنری را به ایتریتور تبدیل میکند

# در نبود ایتر اینگونه برش میزنه

# کاربرد ایتر
# ایتر در حافظه نگه میداره و هر گام فقط یه کار میکنه و باقیشونگه میداره و هر موقع فراخوانی کردیم بهمون میده
# مثل yield

mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            
my=dict(islice(mydictha.items(),len(mydictha)//2))
print(my)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}

my2=dict(mydictha)
print(my2)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}
# یعنی همون اولی را میریزه 


# حالا اگر ایتر کنیم

# میگه یه ابجکته

# اگر از اول بسازیم
mydictha={ 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}            

you=iter((mydictha.items()))

she=dict(islice(you,len(mydictha)//2))
# حواست باشه اینجا لن  دیکشنری اصلی را باید بزنی
print(she)
# {'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75}
# توجه شود که اگر ایتر را درون دیکشنری یا لیست و. .. نریزیم بهمون اینو میده
# <dict_itemiterator object at 0x000001A8FA47D260>


# تا اینجا دیکشنری را برش زدیم
# نصف شده
# حالا در حافظش گذاشته
he=dict(you)
print(he)
# {'soheila': 7.833333333333333, 'ali': 5, 'sarvin': 11.375}
# یه بار یو را داده برش زده و چون یو ایتر بوده 
# سری بعد در حافظش هست که تا کجا چه کرده



# یا اینکه نکست را روی چیزی بیاری
cor = {'mandana': 7.5, 'hamid': 6.066666666666666, 'sina': 11.285714285714286, 'sara': 9.75, 'soheila': 7.833333333333333, 'ali': 5.0, 'sarvin': 11.375}
my=next(iter(cor))
print(my)
# mandana
# این اولین کلید را میده

# حالا اگر روی دیکشنری پاپ کنیم
# حالا اگر روی دیکشنری اصلی پیاده کنیم
key,val=(cor.popitem())
print(key , val)
# sarvin 11.375


# چجوری دونه دونه از اخر بیاد پاپ کنه
# با توجه به اینکه نکست از اوله
# ترکیب اینا چجوریه؟
# ????????????
for k ,v in cor.items():
    print(next(iter(cor)))
# mandana
# mandana
# mandana
# mandana
# mandana
# mandana
# mandana

# /////

# //////

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

# /////////////////////



# A Python program to print all
# combinations of a given length
from itertools import combinations
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)
# Print the obtained combinations
for i in list(comb):
    print (i)

# (1, 2)
# (1, 3)
# (2, 3)


# /////////////////



# A Python program to print all
# combinations of given length
from itertools import combinations
 
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)
 
# Print the obtained combinations
for i in list(comb):
    print (i)

# (1, 2)
# (1, 3)
# (2, 3)
 
# ///////////////

# خودشم میده 
# A Python program to print all combinations
# with an element-to-itself combination is
# also included
from itertools import combinations_with_replacement

# Get all combinations of [1, 2, 3] and length 2
comb = combinations_with_replacement([1, 2, 3], 2)
 
# Print the obtained combinations
for i in list(comb):
    print (i)
    
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 2)
# (2, 3)
# (3, 3)  

# ////////////////

# Python3 code to demonstrate working of
# Extract Combination Mapping in two lists
# using zip() + product()
from itertools import product
  
# initialize lists
test_list1 = [3, 4, 5]
test_list2 = ['x', 'y']
  
# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
  
# Extract Combination Mapping in two lists
# using zip() + product()
res = list(list(zip(test_list1, ele)) for ele in product(test_list2, repeat = len(test_list1)))

# printing result
print("Mapped Combination result : " + str(res))


# The original list 1 is : [3, 4, 5]
# The original list 2 is : [‘x’, ‘y’]
# Mapped Combination result : [[(3, ‘x’), (4, ‘x’), (5, ‘x’)], [(3, ‘x’), (4, ‘x’), (5, ‘y’)], [(3, ‘x’), (4, ‘y’), (5, ‘x’)], [(3, ‘x’), (4, ‘y’), (5, ‘y’)], [(3, ‘y’), (4, ‘x’), (5, ‘x’)], [(3, ‘y’), (4, ‘x’), (5, ‘y’)], [(3, ‘y’), (4, ‘y’), (5, ‘x’)], [(3, ‘y’), (4, ‘y’), (5, ‘y’)]]



# //////////////

# Python3 program for 
# the above approach
  
# Function to check if 
# permutation of one string 
# can break permutation of
# another string or not
def CanBreak(A, B):
  
    # Sort both the strings
    # in alphabetical order
    A = "".join(sorted(A))
    B = "".join(sorted(B))
    ans1 = True
    ans2 = True
  
    # Iterate over the strings
    for i in range(len(A)):
  
        # If any of the string 
        # can break other then 
        # mark ans as false;
        if(A[i] < B[i]):
            ans1 = False
        if(B[i] < A[i]):
            ans2 = False
  
    # If any of the string 
    # can break
    return (ans1 or ans2)
  
# Driver Code
  
# Given string A and B
A = "abc"
B = "xya"
  
# Function Call
if(CanBreak(A, B)):
    print("Yes")
else:
    print("No")
  
# This code is contributed by avanitrachhadiya2155

# Output: 
# Yes


# ///////////////////
# انتخاب بین چند استرینگ در یک لیست
In [1]: import random
In [2]: hello = ['hi', 'hello', 'yo', 'bonjour', 'hola', 'salaam']
In [3]: random.choice(hello)
Out[3]: 'bonjour'

//////////////////
# پخش لیست تودرتو در یک لیست
from more_itertools import collapse
fruits = ['apple','orange', ['pineapple','grapes']]
print(list(collapse(fruits)))
# ['apple', 'orange', 'pineapple', 'grapes']

# حتی یک لیست تودرتوی تودرتو
from more_itertools import collapse
fruits = ['apple','orange', ['pineapple',['jice','mamad'],'grapes']]
print(list(collapse(fruits)))
# ['apple', 'orange', 'pineapple', 'jice', 'mamad', 'grapes']
# https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.collapse


# ////
list(interleave([1, 2, 3], [4, 5], [6, 7, 8]))
# [1, 4, 6, 2, 5, 7]


# //////////
list(zip([player_1],[player_2]))
# [([1, 2, 3, 4], [1, 2, 3, 4])]


# ///////
list(zip(player_1,player_2))
# [(1, 1), (2, 2), (3, 3), (4, 4)]

# /////////
# جایگشت ها را میده به دوتا لیست میکنه
# دولیست را جایگشتشونو میده
# دولیست
player_1 ,player_2 =[1,2,3,4],[1,2,3,4]

list(list(zip(r, p)) for (r, p) in zip(repeat(player_1), permutations(player_2)))
len(permuted) #24

#
# [[(1, 1), (2, 2), (3, 3), (4, 4)],
#  [(1, 1), (2, 2), (3, 4), (4, 3)],
#  [(1, 1), (2, 3), (3, 2), (4, 4)],
#  [(1, 1), (2, 3), (3, 4), (4, 2)],
#  [(1, 1), (2, 4), (3, 2), (4, 3)],
#  [(1, 1), (2, 4), (3, 3), (4, 2)],
#  [(1, 2), (2, 1), (3, 3), (4, 4)],
#  [(1, 2), (2, 1), (3, 4), (4, 3)],
#  [(1, 2), (2, 3), (3, 1), (4, 4)],
#  [(1, 2), (2, 3), (3, 4), (4, 1)],
#  [(1, 2), (2, 4), (3, 1), (4, 3)],
#  [(1, 2), (2, 4), (3, 3), (4, 1)],
#  [(1, 3), (2, 1), (3, 2), (4, 4)],
#  [(1, 3), (2, 1), (3, 4), (4, 2)],
#  [(1, 3), (2, 2), (3, 1), (4, 4)],
#  [(1, 3), (2, 2), (3, 4), (4, 1)],
#  [(1, 3), (2, 4), (3, 1), (4, 2)],
#  [(1, 3), (2, 4), (3, 2), (4, 1)],
#  [(1, 4), (2, 1), (3, 2), (4, 3)],
#  [(1, 4), (2, 1), (3, 3), (4, 2)],
#  [(1, 4), (2, 2), (3, 1), (4, 3)],
#  [(1, 4), (2, 2), (3, 3), (4, 1)],
#  [(1, 4), (2, 3), (3, 1), (4, 2)],
#  [(1, 4), (2, 3), (3, 2), (4, 1)]]

# اولی را ثابت میکنه و دومی را میچرخونه


# /////////

# جایگشت با تکرار

# مشکل permutation
# اینه که خودشو نمزینه
# مشکل combination with replacement
# اینه که   وقتی الف را با ب ترکیب میکنه دیگه ب را با الف ترکیب نمیکنه

# هرچند خودشونو با خودشون میاره . یعنی ضعف پرمیوتیشن را جبران میکنه

# راه حل.
# یا میتونی یه بار از یه لیست پرمیوتیشن بگیری . یه بار از همون کمباینیشن ویت ریپلیس . سپس با هم مرج کنی

# یه راه اینه که یه لیست را دو بار پروداکت کنی

print(equality_list)
# [[1, 2, 3, 4], [1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3], [1, 1, 2, 2], [1, 1, 1, 2], [1, 2, 2, 2], [1, 1, 1, 1]]


db_feature=list(product(equality_list,equality_list))
db_feature
# [([1, 2, 3, 4], [1, 2, 3, 4]),
#  ([1, 2, 3, 4], [1, 1, 2, 3]),
#  ([1, 2, 3, 4], [1, 2, 2, 3]),
#  ([1, 2, 3, 4], [1, 2, 3, 3]),
#  ([1, 2, 3, 4], [1, 1, 2, 2]),
#  ([1, 2, 3, 4], [1, 1, 1, 2]),
#  ([1, 2, 3, 4], [1, 2, 2, 2]),
#  ([1, 2, 3, 4], [1, 1, 1, 1]),
#  ([1, 1, 2, 3], [1, 2, 3, 4]),
#  ([1, 1, 2, 3], [1, 1, 2, 3]),
#  ([1, 1, 2, 3], [1, 2, 2, 3]),
#  ([1, 1, 2, 3], [1, 2, 3, 3]),
#  ([1, 1, 2, 3], [1, 1, 2, 2]),
#  ([1, 1, 2, 3], [1, 1, 1, 2]),
#  ([1, 1, 2, 3], [1, 2, 2, 2]),
#  ([1, 1, 2, 3], [1, 1, 1, 1]),
#  ([1, 2, 2, 3], [1, 2, 3, 4]),
#  ([1, 2, 2, 3], [1, 1, 2, 3]),
#  ([1, 2, 2, 3], [1, 2, 2, 3]),
#  ([1, 2, 2, 3], [1, 2, 3, 3]),
#  ([1, 2, 2, 3], [1, 1, 2, 2]),
#  ([1, 2, 2, 3], [1, 1, 1, 2]),
#  ([1, 2, 2, 3], [1, 2, 2, 2]),
#  ([1, 2, 2, 3], [1, 1, 1, 1]),
#  ([1, 2, 3, 3], [1, 2, 3, 4]),
#  ([1, 2, 3, 3], [1, 1, 2, 3]),
#  ([1, 2, 3, 3], [1, 2, 2, 3]),
#  ([1, 2, 3, 3], [1, 2, 3, 3]),
#  ([1, 2, 3, 3], [1, 1, 2, 2]),
#  ([1, 2, 3, 3], [1, 1, 1, 2]),
#  ([1, 2, 3, 3], [1, 2, 2, 2]),
#  ([1, 2, 3, 3], [1, 1, 1, 1]),
#  ([1, 1, 2, 2], [1, 2, 3, 4]),
#  ([1, 1, 2, 2], [1, 1, 2, 3]),
#  ([1, 1, 2, 2], [1, 2, 2, 3]),
#  ([1, 1, 2, 2], [1, 2, 3, 3]),
#  ([1, 1, 2, 2], [1, 1, 2, 2]),
#  ([1, 1, 2, 2], [1, 1, 1, 2]),
#  ([1, 1, 2, 2], [1, 2, 2, 2]),
#  ([1, 1, 2, 2], [1, 1, 1, 1]),
#  ([1, 1, 1, 2], [1, 2, 3, 4]),
#  ([1, 1, 1, 2], [1, 1, 2, 3]),
#  ([1, 1, 1, 2], [1, 2, 2, 3]),
#  ([1, 1, 1, 2], [1, 2, 3, 3]),
#  ([1, 1, 1, 2], [1, 1, 2, 2]),
#  ([1, 1, 1, 2], [1, 1, 1, 2]),
#  ([1, 1, 1, 2], [1, 2, 2, 2]),
#  ([1, 1, 1, 2], [1, 1, 1, 1]),
#  ([1, 2, 2, 2], [1, 2, 3, 4]),
#  ([1, 2, 2, 2], [1, 1, 2, 3]),
#  ([1, 2, 2, 2], [1, 2, 2, 3]),
#  ([1, 2, 2, 2], [1, 2, 3, 3]),
#  ([1, 2, 2, 2], [1, 1, 2, 2]),
#  ([1, 2, 2, 2], [1, 1, 1, 2]),
#  ([1, 2, 2, 2], [1, 2, 2, 2]),
#  ([1, 2, 2, 2], [1, 1, 1, 1]),
#  ([1, 1, 1, 1], [1, 2, 3, 4]),
#  ([1, 1, 1, 1], [1, 1, 2, 3]),
#  ([1, 1, 1, 1], [1, 2, 2, 3]),
#  ([1, 1, 1, 1], [1, 2, 3, 3]),
#  ([1, 1, 1, 1], [1, 1, 2, 2]),
#  ([1, 1, 1, 1], [1, 1, 1, 2]),
#  ([1, 1, 1, 1], [1, 2, 2, 2]),
#  ([1, 1, 1, 1], [1, 1, 1, 1])]


# ///////////





