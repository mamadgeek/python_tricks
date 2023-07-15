
from itertools import cycle , permutations , pairwise , chain


# تغیر پذیر است لیست


# /////
# کارایی که میشه روی اون انجام داد
dir (list)
print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort']
# //// 
# برش زدن یک لیست
# [50, 70, 30, 20, 90, 10, 50]
Lst = [50, 70, 30, 20, 90, 10, 50]
# این علامت دو نقطه یعنی از اول تا آخر
print(Lst[::])


# //// 
#  . همونه ولی برش دهی را از آخر میزنه
# [50, 70, 30, 20, 90, 10, 50]
Lst = [50, 70, 30, 20, 90, 10, 50]
# میگه از منفی یک شروع کن . تا اخر برو . یکی یکی هم برو
# مثلا میشد بنویسه دوتا دوتا برو
print(Lst[-7::1])



# //// 
# برش می زنه از ایندکس یک تا پنج
# از صفر شروع میکنه پس هفتاد میشه ایندکس یکه . همیشه
# خود عدد اخری هم همیشه خونده نمیشه . اینا اصل هستند
# یعنی تا سر پنج و نه خود پنج 

# پس از صفر آغاز میکنه 
# و یکی از آخر کم میکنه

# [70, 30, 20, 90]
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[1:5])

# ////////
# اگه میخوای خود آخری هم بشه یه به علاوه یک اضافه کن 
# در حلقه زدن لیست چون نمیدونیم بهتره اونو اضافه کنی
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[1:5+1])

# [70, 30, 20, 90, 10]

# ////////////


# البته اگر به آخری میخوای اشاره کنی اصلا ننویسی خودش میاره تا آخر
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[1:])
# [70, 30, 20, 90, 10, 50]



# //// 
# دوتا دوتا برش میزنه 
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(List[3:9:2])
# [4, 6, 8]


# ////
 
# برعکس برش میزنه
List = ['Geeks', 4, 'geeks !']
print(List[::-1])
# ['geeks !', 4, 'Geeks']

# کاراکتر منفی سه را نشون میده 
# یعنی از اخر میشماره میره عقب 

print(List[::-3])
# ['geeks !']

# از منفی دو میره یکی یکی عقب
# اما چرا همونو برگردوند؟
print(List[:1:-2])
['geeks !']

# ////
# مشکل
# out of range


# انواع مقایسه یک لیست با خودش
# هرچیز  با قبلیش و اولی با اخری
player_1 = [4, -1, 0, 3]
player_2 = [-5, -3, 2, 4]

player_1_sorted = player_1
player_2_sorted = player_2

player_1_sorted.sort()
player_2_sorted.sort()
print(player_1_sorted, player_2_sorted)
# [-1, 0, 3, 4] [-5, -5, 2, 4]


# مقایسه یه رشته با خودش
# مشکل
# out of range

# انواع مقایسه یک لیست با خودش

my_list = []
for i, char in enumerate(player_2_sorted):
    print('player_2_sorted[i] is: ', player_2_sorted[i])
    print('player_2_sorted[i-1] is: ', player_2_sorted[i - 1])
    print('player_2_sorted[i]==player_2_sorted[i-1] is : ', player_2_sorted[i] == player_2_sorted[i - 1])
#     the_char=i+1
#     my_list.append(the_char)
# my_list


# [-5, -3, 2, 4]
# player_2_sorted[i] is:  -5
# player_2_sorted[i-1] is:  4
# player_2_sorted[i]==player_2_sorted[i-1] is :  False
# player_2_sorted[i] is:  -3
# player_2_sorted[i-1] is:  -5
# player_2_sorted[i]==player_2_sorted[i-1] is :  False
# player_2_sorted[i] is:  2
# player_2_sorted[i-1] is:  -3
# player_2_sorted[i]==player_2_sorted[i-1] is :  False
# player_2_sorted[i] is:  4
# player_2_sorted[i-1] is:  2
# player_2_sorted[i]==player_2_sorted[i-1] is :  False
#

# هرکدوم با قیبلیش میشه و اولی با اخری میشه
#
# -5 4
# -3 -5
# 2 -3
# 4 -2

# //////

# انواع مقایسه یک لیست با خودش
# بنجامین باتن
# مقایسه دو لیست

player_2=[4,-3,2,1]
# اگر کپی را نزاری لیست دوم هم همون اولی میشه
player_2_sorted=player_2.copy()
print(player_2_sorted)
player_2_sorted.sort()
print(player_2_sorted)
# [-3, 1, 2, 4]


# حالا همینو برعکس کن
player_2_reverse=player_2
print(player_2_reverse)
player_2_reverse.sort(reverse=True)
print(player_2_reverse)

list(zip(player_2_sorted,player_2_reverse))

# [(-3, 4), (1, 2), (2, 1), (4, -3)]

my=[]
for char in list(zip(player_2_sorted,player_2_reverse)):
    my.append(list(char))
my
# [[-3, 4], [1, 2], [2, 1], [4, -3]]

# ////////
# انواع مقایسه لیست با خودش


# ///////////
# دستکاری کردن لیست . یه لیستی را درون اون لیست ما میاره و در کاراکترش میزاره
List = [-999, 'G4G', 1706256, 3.1496, '^_^']
List[2:4] = ['Geeks', 'for', 'Geeks', '!']
print(List)
# اینجا اومده چهار تا حرفو از یک تا چهار میزاره  درون اون لیست فرو میکنه 

# [-999, 'G4G', 'Geeks', 'for', 'Geeks', '!', '^_^']

List[:6] = []
print(List)
# میاد عنصر شیشمی(درحقیقت هفتمی ) را فقط نگه میداره و بجای تا شیش هیچی میزاره
# ['^_^']

# //// 

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = List[:3]+List[7:]
print(newList)
# میاد اول تا سه را برش میزنه و بعد از هفت تا آخر را
# [1, 2, 3, 8, 9]

List = List[::2]+List[1::2]
print(List)
# اول میاد دو تا دوتا میره جلو و بعد اون یکی لیست را از یک شروع میکنه دو تا دوتا میره . یعنی
# میشه اول اعداد فرد و بعد اعداد زوج
# [1, 3, 5, 7, 9, 2, 4, 6, 8]


# //// 
# افزودن به لیست روش دیگر 
l= [1,5,3,'mamad',-1]
l2=[l,'ayda',-1,[1,4,'javid']]
print(len(l2))
#  خود رشته ال پیشین را میافزاید به  ال دو جدیده
# [[1, 5, 3, 'mamad', -1], 'ayda', -1, [1, 4, 'javid']]

# ///////////
# 4
# طول یک رشته را میده . 
l= [1,5,3,'mamad',-1]
l2=[l,'ayda',-1,[1,4,'javid']]
print(len(l2))

# ////////////
# زدن حلقه در طول یک لیست

l= [1,5,3,'mamad',-1]
l2=[l,'ayda',-1,[1,4,'javid']]
# print((l2))

for i in range (len(l2)):
    print(i)
# میاد به تعداد طول نمایش میده 
# یعنی ایندکس را نشون میده
# 0
# 1
# 2
# 3

# //////////
# زدن حلقه
# که اعضا را نشون بده
l2=['ayda',-1,[1,4,'javid']]
for item in l2:
    print(item)

# ayda
# -1
# [1, 4, 'javid']



# //// 
# اعضا و ایندکس را نشون میده
# اعضای درون لیست را دونه دونه نشون میده
# و میگه چندمین ایتم بوده
l= [1,5,3,'mamad',-1]
l2=[l,'ayda',-1,[1,4,'javid']]
# print((l2))
for i in range (0,len(l2)):
    print(i, l2[i])
# 0 [1, 5, 3, 'mamad', -1]
# 1 ayda
# 2 -1
# 3 [1, 4, 'javid']


# /////
l2=['ayda',-1,[1,4,'javid']]
for item in range (len(l2)):
    print(item , l2[item])

# 0 ayda
# 1 -1
# 2 [1, 4, 'javid']

# //////
# برش زدن با حلقه
l2=['ayda',-1,[1,4,'javid']]
for item in range (1, len(l2)):
    print(item , l2[item])

# 1 -1
# 2 [1, 4, 'javid']

# ///////////////
# میشه دوتا لیست را با هم جمع کنه 
# و حتی اگر قبلا تو خودش بوده باشه.
# برای نمونه ال در ال دو بوده
l= [1,5,3,'mamad',-1]
l2=[l,'ayda',-1]

print(l+l2)

# [1, 5, 3, 'mamad', -1, [1, 5, 3, 'mamad', -1], 'ayda', -1]

# ////////
# مقایسه اعضا با بعدی 
# مقایسه اعضا با قبلی
# مساله بررسی اعضا 
# اینکه بگم اون با بعدیش اگر مساوی بود 
# ایندکس ارور میاره 

for char in range (0, len(player_2_sorted)):
    print(player_2_sorted[char],char)
    print(player_2_sorted[char+1])
# list index out of range
# -5 0
# -5
# -5 1
# 2
# 2 2
# 8
# 8 3


# /////////
courses = ['python','kotlin','vuejs','jquery']
print(courses.pop())
print(courses)

# /////////

l2=[[1,5,3,'mamad',-1],'ayda',-1,[1,4,'javid']]
for i in (l2):
    print(i)
# اینم همه ایتم هارا میده 
# [1, 5, 3, 'mamad',
# -1]
# ayda
# -1
# [1, 4, 'javid']

# //// 
# میوتبل بودن لیست ها
# قابل تغیر بودن لیست ها
a=[1,2,3]
print(a)
# [1, 2, 3]
a[0]=4
print(a)
# [4, 2, 3]


# //////////
# تاپلی از لیست ها میشه بده
my_key=['a','b','c' ]
my_val=['1','2','3']
print(my_key , my_val)
# ['a', 'b', 'c'] ['1', '2', '3']

# //////
# ضرب و جمع  کار میکنه در لیست ولی منفی و تقسیم نه
# میشه دوبار یا چند بار تکرار کنه . تابع جمع ضرب اینتیجر در لیست کار میکنه
l= [1,5,3,'mamad',-1]
print(l*2)
# [1, 5, 3, 'mamad', -1, 1, 5, 3, 'mamad', -1]

# ////////
# افزودن به ته لیست 
l= [1,5,3,'mamad',-1]
l.append('neww')
print(l)
# [1, 5, 3, 'mamad', -1, 'neww']

# ////////

# و حتی افزودن یه لیست به ته لیست
l= [1,5,3,'mamad',-1]
l2=['ahha','yeh']
l.append(l2)
print(l)
# [1, 5, 3, 'mamad', -1, ['ahha', 'yeh']]


# ///////
# متدهای اینپلیس
# متد هایی که روی همون لیست قبلی اجرا میشن و اگر هم بریزی توی لیست تازه و یا حتی توی خودشون  خورجی 
# None
# را میدهند
# اینها روی همون لیست قبلی کار میکنند
extend
shuffle



# متد هایی که میشه تو یه متغیر دیگه ریخت

# /////

# میشماره که یه چیز چند بار اتفاق افتاده
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)
# 2

# ////////
# افزودن به لیست با اکستند
#  فرقش با اپند اینه که بازش میکنه و داده های درونشو میریزه
# ولی اپند باز نمیکنه
l= [1,5,3,'mamad',-1]
l2=['ahha','yeh']
l.extend(l2)
print(l)
# [1, 5, 3, 'mamad', -1, 'ahha', 'yeh']


# ////////
# افزودن به لیست . فرقش با اپند و اکستند اینه که در جمع باید بریزی لیست جدید 
# در جمع هیچکدوم تغیر نمیکنه ولی در اپند و اکستند اون دوتا تغیر میکنه

# و حتی افزودن یه لیست به ته لیست
l= [1,5,3,'mamad',-1]
l2=['ahha','yeh']
print(l+l2)
print(l)
# [1, 5, 3, 'mamad', -1, 'ahha', 'yeh']
# [1, 5, 3, 'mamad', -1]



# //////////

# حتی ترکیبی اکستند و جمع هم میشه 
l= [1,5,3,'mamad',-1]
l2=['ahha','yeh']
l.extend(l+l2)
print(l)

# [1, 5, 3, 'mamad', -1, 1, 5, 3, 'mamad', -1,
# 'ahha', 'yeh']




# ////////
# حذف ایندکسی که بهش می دیم

l= [1,5,3,'mamad',-1]
del l[3]
print(l)
# [1, 5, 3, -1]


# ////////
# سورت کردن یک طول

l= [1,5,3,-1]
l.sort()
print(l)
# [-1, 1, 3, 5]
# ////////
# یعنی نه میشه یه ضررب پرینت کرد و نه میشه تو چیز دیگر ریخت . فقط خودش

l= [1,5,3,-1]
l2= l.sort()
print(l2)
# None

# //////
# ولی اگر یه ضرب پرینت بدیم اینجوری میشه:
l= [1,5,3,-1]
print(l.sort())
# None

# ////////
# تفاوت با استرینگ 
# میتوبل بودن
# تغیر دادن یک لیست
# میاد اون لیست ال را برمیداره و هشت را  میزاره بجاش
l= [1,5,3,'mamad',-1]
l2=[l,'ayda',-1,[1,4,'javid']]
# print((l2))
# [[1, 5, 3, 'mamad', -1], 'ayda', -1, [1, 4, 'javid']]
# بعد تغیر میدی
l2[0]=8
print(l2)
# [8, 'ayda', -1, [1, 4, 'javid']]

# //// 
# برداشتن از ته یه لیست

l= [1,5,3,-1]
l.pop()
print(l)
# [1, 5, 3]


# //// 
# میشه برداره و بریزه تو یه متغیر دیگه

l= [1,5,3,-1]
bn= l.pop()
print(l)
# [1, 5, 3]
print(bn)
# -1



# //// 
# حذف میکنه اون  چیزی که میخوای را و برخالف دیلیت که ایندکس را باید میگرفت


l= [1,5,3,-1]
l.remove(3)
print(l)
# [1, 5, -1]


# //// 
# میشه برداره با ایندکس عنصری که بهش می دیم
# پاپ شدشو فقط برمیداره
fruits = ['apple', 'banana', 'cherry']
f2= fruits.pop(1)
print(fruits)
# ['apple', 'cherry']
print(f2)
# banana



# /////////////


# /////////
# این کد هیچی نمیده

def norozi() :
    for i in range(0,3):
        mylist=[]
        mylist=mylist.append(int(input('give me numbers: ')))
        
    return(mylist)

print (norozi())
# give me numbers: 8
# give me numbers: 9
# give me numbers: 9
# None

# ////////////

# این کد فقط اخری را میده
def norozi() :
    for i in range(0,3):
        mylist=[]
        mylist.append(int(input('give me numbers: ')))
        
    return(mylist)

print (norozi())
# give me numbers: 8
# give me numbers: 9
# give me numbers: 9
# 9

# //////////
# ساخت لیست تودرتو
# list comprhention
# لیست کامپرهنشن
# فرمول تک خطی
# ترکیب حلقه و لیست و شرط

[2 taali 1 for sentence] #یک حلقه فور
[3 taali  1 for sentence  2 if moghadam ]] #یک حلقه فور و یک شرط
[[3 taali  2 for sentence2] 1 for sentence] #دو حلقه فور

replaced_list=[  3 tali     2 if moghadam   4 else tali    1 for sentence] # یک حلقه فور و دو شرط

[ [4 tali   3 if moghadam  5 else 'o'  2 for sentence2 ] 1 for sentene] #دو حلقه فور و دو شرط

# مثال
[ [new for new in range( 1,4) ] for num in range(1,4)]
[ ['x' if new %2==0 else 'o' for new in range (1,4) ] for num in range(1,4)]



# ////////////
# ساخت لیست تودرتو
# حلقه زدن تک خطی

numbers=[[1,2,3],[4,5,6]]
[ print(numbers) for charr in numbers]
# [[1, 2, 3], [4, 5, 6]]
# [[1, 2, 3], [4, 5, 6]]

# //////////////

# وقتی لیستی تودرتو بداریم که بخوایم به اعضای درونیش دسترس داشته باشیم
# از دو کاراکتری نمیشه استفاده کرد
numbers=[[1,2,3],[4,5,6]]
for charr  , v in numbers:
    print(v)
# اینجا نمیشه درونشو اشاره کرد
# ValueError: too many values to unpack (expected 2)


# بجاش 
# باید دو حلقه زد
for charr in numbers:
    for v in charr:
        print(v)
# 1
# 2
# 3
# 4
# 5
# 6

# حالا حلثه تودرتوی برای اجرای در لیست تودرتو این میشه
numbers=[[1,2,3],[4,5,6]]
[[print(k) for k in charr]  for charr in numbers]
# 1
# 2
# 3
# 4
# 5
# 6

# //////
# برای این
        for charr in roder:
            while '' in charr:
                charr.remove()
        print(roder)
        
# اما  این اجرا نمیشه
        roder=[ [charr.remove(' ')  while '' in charr] for charr in roder   ]
        # خطا ی سینتکس میده
# ?????????????????????????????//
# پاسخ . جایی نوشته بود برای وایل نمیشه لیست تک خطی زدی
# بجای اون میتونی همینو فور کنی و اونو استفاده کنی
# ///////////


# ////////
# ساخت لیست تودرتو با استفاده از دو لیست جدا

l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
[list(l) for l in zip(l1, l2)]
# [['a', 'd'], ['b', 'e'], ['c', 'f']]

# /////////////


# ساخت لیست تودرتو با استفاده از دو لیست جدا
# عنصر اول ثابت بشه عنصر دوم بره با دونه دونه باهاشون منطبق بشه
# بطوریکه

my_list = ['hat', 'bat']
other_list = ['A', 'B', 'C']

my_list = ['hat', 'bat']
other_list = ['A', 'B', 'C']
new_list=[my_list[0], [f'{my_list[1]}_{e}' for e in other_list]]
new_list
# ['hat', ['bat_A', 'bat_B', 'bat_C']]


# //////////////////////////////
# تبدیل یک لیست به یک لیست تودرتو
data_list = [0,1,2,3,4,5,6,7,8]
new_list = [data_list[i:i+3] for i in range(0, len(data_list), 3)]
# new_list = [ [0,1,2] , [3,4,5] , [6,7,8] ]

# یا
import numpy
new_list = numpy.array(data_list).reshape(-1, 3)


# //////////////
# اگر لیست خالی را درون حلقه بیاری فقط تعدادشو میزنه 
# این کد تعداد شمارنده را میده . اونم فقط اخریشو
def norozi() :
    for i in range(0,4):
        mylist=[]
        i==int(input('give me numbers: '))
        mylist.append(i)
        print(mylist)
    return(mylist)
print (norozi())

# give me numbers: 7
# [0]
# give me numbers: 8
# [1]
# give me numbers: 9
# [2]
# give me numbers: 9
# [3]
# [3]

# //////////////////

# حالا کافیه لیست خالی را بیاری بالا
# این کد هم میاد فقط شمارنده را میاره نه محتواش را
def norozi() :
    mylist=[]
    for i in range(0,4):
        i==int(input('give me numbers: '))
        mylist.append(i)
        # print(mylist)
    return(mylist)
print (norozi())

# give me numbers: 8
# give me numbers: 5
# give me numbers: 3
# give me numbers: 9
# [0, 1, 2, 3]
# //// 
# این کد اضافه میکنه با اپند 
# هرکدوم از محتواها را میریزه تو لیست
def norozi():
    mylist=[]
    for i in range(0,4):
        i=int(input('give me numbers: '))
        mylist.append(i)
        # print(mylist)
    return(mylist)
print (norozi())
# give me numbers: 3
# give me numbers: 9
# give me numbers: 7
# give me numbers: 2
# [3, 9, 7, 2]


# //////////
# این کد هرکدوم از محتوا ها را یه لیست میکنه درون لیست بزرگتر میریزه
def norozi():
    mylist=[]
    for i in range(0,4):
        i=int(input('give me numbers: '))
        mylist.append([i])
        # print(mylist)
    return(mylist)
print (norozi())
# give me numbers: 8
# give me numbers: 7
# give me numbers: 8
# give me numbers: 5
# [[8], [7], [8], [5]]



# ////////
# متد انومریت در لیست
# ایندکس و کاراکترا بهش دسترسی داریم
B = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']
for index , char in enumerate(B):
    print(index , char)

# 0 N1
# 1 N2
# 2 N3
# 3 N4
# 4 N5
# 5 N6
# 6 N7


# ////////////
# شببه جایگشت میشه درست کنه
# بیاد دونه دونه دو حلقه را اضافه کنه دومی را و به تعداد هر کددوم از داده های 
# درون لیست یهلیست تازه بسازه و بریزه تو لیست جدیده
# دو حلقه با هم که اپند کنه و پاپ کنه. 


fruit = [['Orange','Fruit'],['Banana','Fruit'], ['Mango', 'Fruit']]
consume = ['Juice', 'Eat']
possible = []
print(possible)
# Iterating item in list fruit
for item in fruit :
    # Inerating use in list consume
    print('item mishe',item)
    for use in consume :
        # میاد به ازای هر ایتمی که در فروت هست هر ایتمی که در کانسیوم هست را در نظر میگیره
        item.append(use)
        # بعد میاد اون ایتم کانسیوم را که اسمش یوز هست را به ایتم اضافه میکنه
        # (اما چرا نه به فروت؟)
        print('item use mishe: ',item)
        possible.append(item[:])
        # بعد میریزه توی پاسیبل از اول تا اخرشو
        print('possible mishe: : ',possible)

        item.pop(-1)
        # بعد از ایتم میاد یکی کم میکنه. چون لیست بهم نریزه و 
        # لیست مون دست نخورده بمونه که دفعه بعد کار کنه . 
        print('item hazf karde mishe: ',item)
        
print(possible)

# جواب آخر:
# [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'],
#  ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat'],
#  ['Mango', 'Fruit', 'Juice'], ['Mango', 'Fruit', 'Eat']]


# جواب دونه دونه :
# []
# item mishe ['Orange', 'Fruit']
# item use mishe:  ['Orange', 'Fruit', 'Juice']
# possible mishe: :  [['Orange', 'Fruit', 'Juice']]
# item badi:  ['Orange', 'Fruit']
# item use mishe:  ['Orange', 'Fruit', 'Eat']
# possible mishe: :  [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat']]
# item badi:  ['Orange', 'Fruit']
# item mishe ['Banana', 'Fruit']
# item use mishe:  ['Banana', 'Fruit', 'Juice']
# possible mishe: :  [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'], ['Banana', 'Fruit', 'Juice']]
# item badi:  ['Banana', 'Fruit']
# item use mishe:  ['Banana', 'Fruit', 'Eat']
# possible mishe: :  [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'], ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat']]
# item badi:  ['Banana', 'Fruit']
# item mishe ['Mango', 'Fruit']
# item use mishe:  ['Mango', 'Fruit', 'Juice']
# possible mishe: :  [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'], ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat'], ['Mango', 'Fruit', 'Juice']]
# item badi:  ['Mango', 'Fruit']
# item use mishe:  ['Mango', 'Fruit', 'Eat']
# possible mishe: :  [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'], ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat'], ['Mango', 'Fruit', 'Juice'], ['Mango', 'Fruit', 'Eat']]
# item badi:  ['Mango', 'Fruit']
# [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'], ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat'], ['Mango', 'Fruit', 'Juice'], ['Mango', 'Fruit', 'Eat']]
# # //// 




# # //// 


# تابعی که روی اون کار میکنه
# ماکسیمم یا مینیمم را میاره
l= [1,444,464554,4]
print(max(l))
# 464554

# ////

# //// 
# حتی ترکیبی میشه کار کرد. یعنی یه ضرب مین و ماکس را گرفت
# یه عملیات دیگه روش پیاده کرد.
inter = [7, 6, 54]
blur= max(inter) - min(inter)
# 48

# /////////////

# تابعی که روی اون کار میکنه
# جمع میکنه  اعداد  ها را 
l= [1,444,464554,4]
print(sum(l))
# 465003


# //// 
# تبدیل لیست به استرینگ
l2=['jadi',"bechasboon"]

l3= "+".join(l2)
print(l3)
# jadi+bechasboon
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



# ////////
# یه ضرب تبدیل کردن 
 my_list=[4,1,2,19,100]
    # حالا میخوام تابع جذر را روی هر کدوم از کاراکتر ها اجرا کنم و سپس  تا ۴ رقم تحویل بدم
    mylis= list((map(sqrt,my_list)))
    print(mylis)
    # [2.0, 1.0, 1.4142135623730951, 4.358898943540674, 10.0]
    # جالبه که در لیست تک خطی خودش پرینت هم میده نیازی نیست بنویسی پرینت 
    # اگر هم بنویسی نان میزنه
    my2= [ ('%.4f'%char) for char in mylis]
# //// 
# تبدیل استرینگ به لیست
# اینکه باید چیزی بنویسی وگرنه داخل اسپلیت خخالی که باشه نمیزنه چیزی را

txt = "welcome to the jungle"
x = txt.split()
print(x)
# ['welcome', 'to', 'the', 'jungle']



# //////
# می تونه هر جا که بی دید جدا کنه
l= ('jadi bechasboon')
print(l.split('b'))
# ['jadi ', 'echas', 'oon']
# ///////
# لیست میکنه ولی اسپیس ها را هم کاراکتر میگیره
enterance =('3 6 9')
enterance.split(' ')
print(list(enterance))
# ['3', ' ', '6', ' ', '9']

# انگار که اسپلیت نداشت
# لیست میکنه ولی اسپیس ها را هم کاراکتر میگیره
enterance =('3 6 9')
print(list(enterance))
# ['3', ' ', '6', ' ', '9']


# /////////
# برای اینکه متد اسپلیت کار کنه باید بریزی تو یه متغیر دیگه
enterance =('3 6 9')
ent2= enterance.split()
print(ent2)
# ['3', '6', '9']


# /////////
# اسپلیت
# نمیشه تبدیل بشه کلش بلکه باید استرینگ نباشه
enterance =('3 6 9')
(ent2)=int(enterance.split()) 
print(ent2)
(ent2)=int(enterance.split())
# TypeError: int() argument must be a string, a bytes-like object or a real number,
# not 'list'

# ///////////////
# برای این تبدیل اعداد از استرینگ به اینتیجر باید در حلقه بندازی یا در لیست کامپرهنشن

# با کامپرهشن میاد در ایپسلیت میکنه 
# یه تعداد اعداد را و بعد درون لیست میریزه اینتیجر میکنه
# اینپوت هم توی همونه
inter= [int(i) for i in input('give me: ').split()]
print(inter)
# give me: 4 5
# [4, 5]

# نه اپند نیازه نه یه لیست جدانوشتن و نه 

# اما پرانتز نزاری برای اسپلیت خطا میده
ghad=[int(i) for  i in (input('give me the ghad numbers: ').split)]

print (ghad) 
# TypeError: 'builtin_function_or_method' object is not iterable

# ////////////
# برای حلقه کردن این تبدیل
# نمیشه بلکه هر قسمت را جدا میکنه
# باید روش دیگری برگزید
enterance =('3 6 9')
for char in enterance:
    ent2=char.split()
    print(ent2)
# ['3']
# []
# ['6']
# []
# ['9']

# روش های دیگر هم نمیشه

enterance =('3 6 9')
for char in enterance:
    inter=int (char)
    print(inter)

# ValueError: invalid literal for int() with base 10: ' '


# یا
enterance =('3 6 9')
for char in enterance:
    inter=int(enterance.split())
    print(inter)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'


# یا
enterance =('3 6 9')
for char in enterance:
    inter=int(char.split())
    print(inter)

# TypeError: int() argument must be a string, a bytes-like object or
# a real number, not 'list

# اما یا اول باید متد را در ورودی بگذاری
# نمیشه تبدیل بشه بلکه باید استرینگ نباشه
enterance =('3 6 9').split()
print(enterance)
# ['3', '6', '9']

# یا
enterance =('3 6 9')
ent2= enterance.split()
print(ent2)
# ['3', '6', '9']

# حالا استرینگ را تبدیل به اینتیجر کنی
for char in enterance:
    inter=int (char)
    print(inter)
# 3
# 6
# 9

# اما این خودش لیست نیست

# برای حل این مشکل 
# که لیستی از استرینگ هارا به لیستی از اعداد تغیر بده

# این نمیشه
for char in enterance:
    list(enterance)=int (char)
    print(inter)


# یا این هم نمیشه
for char in enterance:
    (inter)=int(char)
    print(list (inter))
    
    
# باید یه لیست درست کنی و اپند بشه
ent3=[]
for char in enterance:
    ent3.append((int(char)))
    print(ent3)

# اما این روش طولانی میشه 
# بلکه یه ضرب بهتر بود که لیست کامپرهنشن بود یعنیی این
# هم اسپلیت میکنه هم اینتیجر میکنه هم لیست میکنه
inter= [int(i) for i in input('give me: ').split()]
print(inter)
# give me: 6 9 10
# [6, 9, 10]

# البته خلاصه تر ولی ناقص ترش  در دو مرحله اینه:
enterance =input().split()
results = [int(i) for i in enterance]
print(enterance)

# ///////
# تغیر دادن یه لیست . وقتی یه چیزی را میگی عنصر ان اوم اون لیست بشه قبلی را حذف میکنه و این یکی را جایگزین میکنه
a= [1,2,3]
print(a)
# [1, 2, 3]
a[0]='no'
print(a)
# ['no', 9, 10]

# ////////////
# اسم استعاری گذاشتن
# وقتی دو چیز را مساوی هم میگیری تغیر در یکی تغیر در دیگری میشه
# اونی که سمت راست هست ریخته میشه . تغیر دهنه است. اونی که سمت چپ مساوی است تغیر کننده است
# ا و ب را هر دو را به یه چیز اشاره میدیم

a= [1,2,3]
b=[8,9,10]
a=b 
print(b)
# [8,9,10]
print(a)
# [8,9,10]
a[0]='no'
print(b)
# ['no', 9, 10]
a[0]='yes'
print(a)
# ['yes', 9, 10]
print(b)
# ['yes', 9, 10]


# /////////
# لیست تک خطی
# ترکیب لیست و حلقه
# اگر میخوای به اندازه یک عدد در یک  لیست تک خطی چیزی را  بپرسه حتما اونرا در رنج قرار بده
numbers= [  int(input('give me the number to cosidering: ')) for N_time in range (figure())]   

# ///////////////
# موقعی که ان تا باید ورودی بگیریم و هر ورودی هم وای تا باشه و بعد اون عنصر وای ها با هم مقایسه بشن از لیست تو در تو استفاده میکنیم
# لیست تو در تو
# در اینجا به ازای هر کدوم از ورودی ها که میدم دو تا لیست میسازه . 
# لیست کامپرهنشن
# به اندازه اعداد ورودی لیست میسازه
# یعنی اگر سه تا ورودی بزنیم اونم سه تا میسازه اگر دو تا ورودی بزنیم دو تا لیست کپی میسازه از اون
enter=int(input('give me number of laptop: '))
biglist=[]
for char in range (enter):
    listha= input('give me list: ').split()
    listha=[int(char) for char in listha]
    print(listha)
    for sublist in listha:
        biglist.append(listha)
        print(biglist)
# give me number of laptop: 2
# give me list: 1 3 5
# [1, 3, 5]
# [[1, 3, 5]]
# [[1, 3, 5], [1, 3, 5]]
# [[1, 3, 5], [1, 3, 5], [1, 3, 5]]
# give me list: 1 4
# [1, 4]
# [[1, 3, 5], [1, 3, 5], [1, 3, 5], [1, 4]]
# [[1, 3, 5], [1, 3, 5], [1, 3, 5], [1, 4], [1, 4]]


# البته میشه برای مقایسه از حلقه استفاده کرد اما لیست بهتره

# این حلقه ناقصه و بعدا کاملش کن

enter1= int(input('give me numbers of laptob: '))        # this gets numbers of laptob. example 3 laptob for compare
last_laptop=[0,0]
print('irsa at first is poor')

poor_irsa=True
for char in range(enter1):
    price_and_quality= input('price and quality:').split()
    print(price_and_quality)
    price_and_quality=[int(characters) for characters in price_and_quality ]
    print(price_and_quality)
    last_laptop=price_and_quality
    if (price_and_quality[0]< last_laptop[0]) and (price_and_quality[1]> last_laptop[1]):
        print('lastly irsa has bacome happy')
        poor_irsa=False
        break
    else:
        print('irsa is steel poor')
        print('the last laptob would be:',last_laptop)
if poor_irsa==True:
    print('poor irsa')
elif poor_irsa==False:
    print('happy irsa')
    

# //////////////////////////////////////////////////////////////
# زدن حلقه در لیست و لیست تو در توی داشته
list = [["Rohan", 60], ["Aviral", 21], 
        ["Harsh", 30], ["Rahul", 40],
        ["Raj", 20]]
  
# looping through nested list using indexes
for names in list:
    print(names[0], "is", names[1],
          "years old.")
# Rohan is 60 years old.
# Aviral is 21 years old.
# Harsh is 30 years old.
# Rahul is 40 years old.
# Raj is 20 years old.

# ////////////////

ofword=[int(x)for x in input('').split()]
print(ofword)
# اینکه صافی درست کردن و فیلتر کردن
# میگه اگر چیزی کوچکتر بود بیارش در لیست 
# ببا کاربرد لیست کامپرهنشن

shart =[i for i in ofword if i<3 ]
print(shart)

# روش دیگر همونه 
# با حلقه ها صافی درست کنیم از یه لیست
# صافی کردن
shart=[]
for num in range(ofword):
    a=(int(input('give me times tha player:')))
    if a<=2:
        shart.append(a)

# شمارش طول یه لیست
# روش ها برای دسته بندی .. که طول را بشماری 
# و ببینی ۵ تا چند دسته سه تایی است؟
print(len(shart)//3)
# اینم همونه با حلقه . طول یک لیست را میشه حساب کرد و
# بعد  ببینی ۵ تا چند تا دسته سه تایی است
num=0
for number in shart:
    num+=1
print(num//3)

# /////

# درست کردن لیست
# ولی جندبار همونو تکرار میکنه 
def norozi():
    mylist=[]
    yours=(input())
    for number in yours:
        mylist.append(yours.split())
        
    return mylist
print(norozi())        
# 6 8 0
# [['6', '8', '0'], ['6', '8', '0'], ['6', '8', '0'], ['6', '8', '0'], ['6', '8', '0']]



# ///////

# به تعداد رنج ازت لیست میگیره
def norozi():
    mylist=[]
    for number in range(0,5):
        yours=(input('give me: '))

        mylist.append(yours.split())
        
    return mylist

# give me: 7 8 9
# give me: 44 4 5 8
# give me: 5 9
# give me: 5
# [['7', '8', '9'], ['7', '8', '9'], ['44', '4', '5', '8'], ['5', '9'], ['5']]

# /////////


# درست کردن لیست
# این یه لیست تو در تو میسازه
# ولی استرینگه
def norozi():
    mylist=[]
    for number in range(1):
        yours=(input('give me: '))

        mylist.append(yours.split())
        
    return mylist
print(norozi())  
# give me: 77  6 7
# [['77', '6', '7']]

# /////////
# اسپلیت میکنه ولی لیست نمیکنه
def norozi():
    # mylist=[]
    yours=(input('give me: '))

    yours.split()
        
    return yours
print(norozi())  
# give me: 6 77 8
# 6 77 8


# //////////
# تابع ها و اسم مستعار گذاشتن
# عوض میشه 
# نکته جادی را ببین . اخر درس لیست ها
# رابطه فانکشن و لیست
# تابع و لیست


# //// 
# تقسیم و زدن تو کمرش. یه ضرب نصف کنی و هر کدوم را درون لیست دیگری بریزی
list = [11, 18, 19, 21]
length = len(list)
middle_index = length // 2
first_half = list[:middle_index]
second_half = list[middle_index:]
print(first_half)
print(second_half)

# [11, 18]
# [19, 21]

# //// 

#  تقسیم به ایکس بخش که خودمون میخوایم
import numpy as np
listA = [11, 18, 19, 21, 29, 46]
splits = np.array_split(listA, 3)
for array in splits:
    print(list(array))
# [11, 18]
# [19, 21]
# [29, 46]


# //// 
# فقط عنصر اولشو اونجایی که میخوایم را میتونیم اشاره کنیم برداره

l = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
[i.split('\t', 1)[0] for i in l]

# میگه به ازای هر عنصری که در اون لیسته هستش اون عنصر را اسپلیت کن 
# اینکه به عنصر صفرم اش اشاره کرده . و به اون علامته که میگه با اون رسیدی ببر .
# ولی نمیفهمم عدد یک چیه
# اگر ماکس اسپلیت هستش چرا یک داده و برای همه کار کرده؟
# اسپلیت دوتایی یعنی چی؟



# ['element1', 'element2', 'element3']

# //// 
# اینم همونه با حلقه
for i in l:
    newList.append(i.split('\t')[0])


# //// 



# //// 

# اعضای لیست را به اینتیجر تبدیل کردن

for i in range(len(list)):
    list[i] = int (list[i])


# //////////////
# ورودی را گرفتن به صورت تبدیلی با حرف خاصی
#
# میاد ورودی را که گرفته  جدا میکنه میریزه تو لیست
# مهم نیست که مثبت باشه یا منفی

t = [int(i) for i in input("give me the numbers: ").split("+")]
print(t)
# [12356]
# اما تبدیل اینتیجر لیست کامپرنشن به معمولی چطوره؟
# ///////
# سورت میکنه
print(list.sort())
# سورت برعکس میکنه لیست را 
list.sort(reverse = True)
# هرچند اینم هون نتیجه را میده 

# print(teach2.sort(reverse=False))

# /////////
# بنجامین باتن
# اگر از یه لیست بخوایم سورت و برعکس سورت همزمان بگیریم
player_2=[4,-3,2,1]
# اگر کپی را نزاری لیست دوم هم همون اولی میشه
player_2_sorted=player_2.copy()
print(player_2_sorted)
# [4, -3, 2, 1]

player_2_sorted.sort()
print(player_2_sorted)
# [-3, 1, 2, 4]


# حالا همینو برعکس کن
player_2_reverse=player_2
print(player_2_reverse)
# [4, -3, 2, 1]

player_2_reverse.sort(reverse=True)
print(player_2_reverse)
# [4, 2, 1, -3]





# ///////////////


# به تعداد مشخصی مثلا ۱۰ تا ورودی میگیره و بعد میریزه توی لیست 
#به توان دو میرسونه عدد قبلی در لیست را

pow2 = []
for x in range(10):
   pow2.append(2 ** x)
print(pow2)
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# /////////////

# ////////
# این کد ضعفی داره که فقط دوبار میپرسه
# و شعف دیگه اینه که عدد دوم را وارد نمیکنه
# یعنی ورودی را لیست کنه و نمیشه لیست را لیست کنه با این روش . واگر نامبرز را لیست نکنیم و مای لیست را کنیم خط و نقطه میزنه

my_list=[]
numbers= int(input(' adad bede ta berizam toie listet: '))
for num in [numbers]:
    my_list.append(num)
    numbers= int(input("adad bede ta berizam toie listet again:" ))    # بدون این نمیشه دوباره و یه بینهایت میشه 
    print(my_list) 


# adad bede ta berizam toie listet: 4
# adad bede ta berizam toie listet again:3
# [4] 

print("////////////")


# ////////
# حالا اگر میخوای وابسته به عدد یا چیزی که
# هر موقع تو بهش دستور بدی ورودی بگیره باید اینجوری بنویسی یا وایل./
numbers= int(input('give it to me: '))
pow2=[]
while (numbers != (-1)) :
    for num in [numbers]:
        pow2.append(num)
        numbers= int(input('give it to me again: ' ))
        print(pow2)
        
# give it to me: 4
# give it to me again: 5
# [4]
# give it to me again: 6
# [4, 5]
# give it to me again: 3
# [4, 5, 6]
# give it to me again: 2
# [4, 5, 6, 3]
# give it to me again: 5
# [4, 5, 6, 3, 2]
# give it to me again: 6
# [4, 5, 6, 3, 2, 5]
# give it to me again: 7
# [4, 5, 6, 3, 2, 5, 6]
# give it to me again: -1
# [4, 5, 6, 3, 2, 5, 6, 7]
        
print("////////////")

# لیست تو در تو
# لیست کامپرهنشن
# ورودی بگیره  به تعداد ورودی اول لیست تو در تو بسازه و بعد همه اون لیست های تو در تو را بریه توی لیست کلی تر
enter=int(input('give me number of laptop: '))
biglist=[]
for char in range (enter):
    listha= input('give me list: ').split()
    listha=[int(char) for char in listha]
    biglist.append(listha)
    print(biglist)
# give me number of laptop: 2
# give me list: 1 3
# [[1, 3]]
# give me list: 4 2
# [[1, 3], [4, 2]]
# //////////

pow2 = [2 ** x for x in range(10)]
print(pow2)
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

print("////////////")
# شرط میزاره بالای پنج را فقط به توان میرسونه
# [64, 128, 256, 512]
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

print("////////////")

# ترکیب میکنه اون دو تا را دو به دو .... مثل جایگشت ریاضی
pow= [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(pow)
# ['Python Language', 'Python Programming', 'C Language', 'C Programming']


# میشه اینجوری هم نوشت:
pow= [
    x+y 
for x in ['Python ','C '] 
for y in ['Language','Programming']]
print(pow)

print("////////////")
# I like apple
# I like banana
# I like mango
for fruit in ['apple','banana','mango']:
    print("I like",fruit)

# //////////
# سورت کردن داخل یه لیست از الفبا
# به ترتیب حروف الفبای کوچک به بزرگ
# ['arancia', 'mela', 'Pera', 'UVA']
my_list = ['Pera','mela','arancia','UVA']
my_list.sort(key=str.lower)
print(my_list)


# ///////
# تفاوت سورت و سورتت
# فکر کنم تفاوت سورتت و سورت در اینپلیس کردنشونه 
# وگرنه اگر در سورت بریزی تو یه متغیر دیگه نمیریزه
# مینویسه نان

my_list = ['Pera','mela','arancia','UVA']
my_sorted_list = sorted(my_list,key=str.lower)

# یعنی : سورت را نمیشه داخل متغیر دیگری ریخت
# None 
['Pera', 'UVA', 'arancia', 'mela']
my_list = ['Pera','mela','arancia','UVA']
my2= my_list.sort(key=str)
print(my2)


# اگر طبق حروف کوچک سورت کنیم
my_list = ['Pera','mela','arancia','UVA']
my_sorted_list = sorted(my_list,key=str.lower)

# //////////
# سورت کردن داخل یه لیست از الفبا
# به ترتیب اول حروف بزرک و بعد کوجک
# ['Pera', 'UVA', 'arancia', 'mela']
my_list = ['Pera','mela','arancia','UVA']
my_list.sort(key=str)
print(my_list)
# /////

# جمع کردن درون لیست:
# [0, 2, 4, 5, 8, 11]
d = [2, 4, 5, 8, 11]
[0] + d

# //////
# فریز کردن لیست
# ایمیوتبل کردن لیست
# نمیزاره تغیر کند لیست
# شابه مجموعه بر میگردونه با این تفاوت که تغیر نمیکند
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

# frozenset({'apple', 'cherry', 'banana'})
x[1] =  "strawberry"
# نمیشه تغیر کند
# TypeError: 'frozenset' object does not support item assignment

# در صورتی که لیست به غیر از اون تغیر پذیر بود
mylist[1] =  "strawberry"
print(mylist)
# ['apple', 'strawberry', 'cherry']
# /////



# //////////
# به اندازه هر عدد درون لیست  دوم
# ازعدد لیست اول را برش میزنه تیکه میکنه
# اولین عنصر ۵ است پس میاد  ۵تا برش میزنه میشه
# 93011
# بعد عدد بعدی ۲۰ است که 
# بقیشو برش میزنه 
# و چون 
# null
# ۴ تا است 
# ۱۶ تا اسپیس میره جلو
s = "93011NULL                5011005874          A0000000000010000000000001JKL00000000NULL                                              00000000A63"
d = [5,20,20,1,16,9,3,8,50,8,1,2]
# Convert sizes to indexes
d = [sum(d[:i+1]) for i in range(len(d))]
print(d)
# [5, 25, 45, 46, 62, 71, 74, 82, 132, 140, 141, 143]``
splits = [s[i:j] for i, j in zip([0]+d, d+[None])]
print (splits)
# ['93011', 'NULL                ', '5011005874          ', 'A', '0000000000010000', '000000001', 'JKL', '00000000', 'NULL                                              ', '00000000', 'A', '63', '']


# //////////
# میبینه چند بار تیچ منطبق شده با یس

list_one = ['con good', 'con good', 'tech', 'retail', 'con good',
           'con good', 'retail', 'finance', 'finance', 'retail',
           'retail', 'finance', 'tech', 'retail', 'tech',
           'finance', 'con good', 'tech', 'con good', 'tech']
list_two =      ['yes', 'yes', 'yes', 'no', 'no',
                 'no', 'no', 'yes', 'yes', 'yes',
                 'yes', 'yes', 'yes', 'no', 'no',
                 'no', 'no', 'yes', 'yes', 'no']
tech = 0
for i in range(len(list_one)):
    if list_one[i] == 'tech' and list_two[i] == 'yes':
        tech = tech+1
print (tech)



# //////////






print("////////////")
#اجرای یک متد در یک دیکشنری . که values هاش یک لیست هستند.
#اینجا اومده از داده های درون یک لیست هرکدوم میانگین گرفته
# 7.5
# 6.066666666666666
# 11.285714285714286
# 9.75
# 7.833333333333333
# 5.0
# 11.375
cor={'mandana': [5.0, 7.0, 3.0, 15.0], 'hamid': [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0],
     'sina': [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0], 'sara': [0.0, 5.0, 20.0, 14.0],
     'soheila': [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0], 
     'ali': [1.0, 9.0], 'sarvin': [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0]}
for value in cor.values():
    print(mean(value))

print("////////////")

cor={'mandana': [5.0, 7.0, 3.0, 15.0],
     'hamid': [3.0, 9.0, 4.0, 20.0, 9.0, 1.0, 8.0, 16.0, 0.0, 5.0, 2.0, 4.0, 7.0, 2.0, 1.0], 
     'sina': [19.0, 10.0, 19.0, 6.0, 8.0, 14.0, 3.0], 
     'sara': [0.0, 5.0, 20.0, 14.0],
     'soheila': [13.0, 2.0, 5.0, 1.0, 3.0, 10.0, 12.0, 4.0, 13.0, 17.0, 7.0, 7.0], 
     'ali': [1.0, 9.0], 
     'sarvin': [0.0, 16.0, 16.0, 13.0, 19.0, 2.0, 17.0, 8.0]}
for esm in cor.items():
    print(esm)

print("////////////")
# {'name': 'mohammad', 'family': 'ordookhani', 'age': 24, 'email': 'moh96ordo@gmail.com'}
# {'name': 'mohammad', 'family': 'ordookhani', 'age': 24, 'email': 'moh96ordo@gmail.com'}

me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}

copy_me = me.copy()
print(me)
print(copy_me)


print("////////////")
# تبدیل دیکشنری به لیست
# دیکشنری را به لیست تبدیل میکنه 
# [('ali', 5.0), ('hamid', 6.066666666666666), ('mandana', 7.5)]
corlist= [ ((value)) for key,value in sorted(cor.items())]
    print(corlist[:-4])


print("////////////")
# کدی که میبینه یه حرف خاص اگر درون اون واژه بود اونرا فقط به لیست میافزاید

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
# ['apple', 'banana', 'mango']

# همون میشه . بدون اپند
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# ['apple', 'banana', 'mango']

# فرمول کلی اینه
# فیلتر کردن اعضای لیست
newlist = [expression for item in iterable if condition == True]


# ///////////
# لیست و دیکشنری
for this_one in list(cor.keys()):
    print(this_one, cor[this_one])
      
print("////////////")
# هر کدوم از اعضا را داخل یه لیست جدا میریزه
# خودکار به اینتر حساسه موقع نوشتن تا اینتر خورد قطع میکنه وگرنه به اسپیس میزنه میره جلو
for i in input(' give me the 3 point: ').split():
    print(list(i))
# give me the 3 point: 4 5 6
# ['4']
# ['5']
# ['6']
# //////////////
# یه استرینگ  که اعداد جدا داره را لیست میکنه هرکدومش را
# ولی استرینگ میده نه اینتیجر
def norozi():
    yours=(input('give me: '))
    yours= list(yours.split())
    return yours
print(norozi())  
# give me: 7 8 99
# ['7', '8', '99']

# /////////
# این کد میاد یه رشته جدا را به اینتیجر تبدیل میکنه  
def norozi():
    yours= (input('give me: '))
    yours= list((yours.split()))
    my=[]
    for char in yours:
        my.append(int(char))
    return my
print(norozi())  
give me: 4 5 6
[4, 5, 6]

# /////////
# به همون تعدادی که دادیم میپرسه ازمون که بعد میریزه توی یه لیست
# یه نکته اینه که رنج را از صفر اغاز میکنه تا اون عدد که خود اون عدد اخر را نمیاره بنابراین تعداد همون میشه مثلا سه
# بدیم اون صفر را حساب میکنه یک را و دو را .. پس میشه سه . بنابراین همون میشه بازم
enterance = int(input('give me the members:'))
# give me the members:3
print(enterance)
# 3
mylist=[]
for num in range(enterance):
    mylist.append(int(input('give me times tha plaayer:')))
print(mylist)

# give me times tha plaayer:4
# give me times tha plaayer:5
# give me times tha plaayer:9
# [4, 5, 9]

# ////////

# برنامه ای که  یه عضو را به یه تعداد  درون لیست میاره
#tedade ozvhaie darune list : 3
#2
#[2, 2, 2]
N=int(input('tedade ozvhaie darune list : '))
ozvlist=[int(x) for x in (input(''))  for i in range(N)]
print(ozvlist)

print("////////////")

#  برنامه ای که تعدادی لیست درون یک لیست میچینه و اعضای اون را با اسپیس جدا میکنه 

tedadlist= int(input('chandta list mikhai dakhele liste aslit? '))
# میگه به ازای هرعددی که دادی در رنج هر کدوم را لیست کن
ozv_har_list = [list(int(x) for x in input(' har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : ').split()) for i in range(tedadlist)]
print('liste aslimun in mishe ',ozv_har_list)
#chandta list mikhai dakhele liste aslit? 3
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : 3 4
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : 2 5 6
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : 2 3 5 6
#liste aslimun in mishe  [[3, 4], [2, 5, 6], [2, 3, 5, 6]]
# حالا اگر جای لیست میزاشتیم تاپل میومد تاپل میکرد داخل لیست را

# اینم همونه ولی در حلقه 
enter=int(input('give me number of laptop: '))
biglist=[]
for char in range (enter):
    listha= input('give me list: ').split()
    listha=[int(char) for char in listha]
    biglist.append(listha)
    print(biglist)


# حالا اگر میخواستیم مثلا یه لیست بسازیم که فقط ۳ تا لیست داره و هر کدوم دقیقا یه اندازه
# داده بدارن مثلا ۴ تا عضو بدارن چجوری باید می نوشتیم؟

print("////////////")

# اینم همونه فقط توی یه خط:

entr = [list(int(x) for x in input(' har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : ').split()) for i in range(int(input('chandta list mikhai dakhele liste aslit? ')))]
print(entr)
#chandta list mikhai dakhele liste aslit? 3
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : 4 5 66
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : 65 2 2 1 6
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : 4321
#[[4, 5, 66], [65, 2, 2, 1, 6], [4321]]
print("////////////")

## اینم همونه فقط توی یه خط:
# یعنی برنامه ای که میاد به ازای هر عدد که دادیم لیست درست میکنه و بعد اگر اسپیس دید پارامتر جدا میسازه
entr = [list((x) for x in input(' har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : ').split()) for i in range(int(input('chandta list mikhai dakhele liste aslit? ')))]
print(entr)
#chandta list mikhai dakhele liste aslit? ۳
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : bfda nasd dsa
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : sdffhd
# har kodom az lista be tartib ozvashun chi(ba space dune dunashono goda kon) : dddfje e rdde ddke
#[['bfda', 'nasd', 'dsa'], ['sdffhd'], ['dddfje', 'e', 'rdde', 'ddke']]


print("////////////")
# برنامه ای که تعداد اعدا را درون یک لیست میاره به تعداد تعین شده 
#اما اسپیس وسط را هم جدا مینکه و هم درون لیست میزاره

cases = [input("khob bad: ").split() for x in range(int(input('bede:')))]
flatList = [int(item) for elem in cases for item in elem]
print(flatList)
#bede:3
#khob bad: 2 3 4
#khob bad: 2 4 6
#khob bad: 2 5  8
#[2, 3, 4, 2, 4, 6, 2, 5, 8]

print("////////////")

#برنامه ای که لیست های جدا درست میکنه به تعداد
tedad= int(input('chandta list mikhai dakhele liste aslit? '))
for x in range(tedad):
    case=input('adadhaie liste avl ra BEDE: ').split()
    [int(x)for x in case]
    case= [int(i) for i in case]
    print(case)
#chandta list mikhai dakhele liste aslit? 3
#adadhaie liste avl ra BEDE: 2 3 4
#[2, 3, 4]
#adadhaie liste avl ra BEDE: 2 3 5
#[2, 3, 5]
#adadhaie liste avl ra BEDE: 23 1 1 1 1
#[23, 1, 1, 1, 1]
print("////////////")

# برنامه ای که میاد هرکدوم از داده های عددی را داخل  یک یگانه لیست میریزه 
#adad ra bede : 3 4 56
#[3, 4, 56]
ofword=[int(x)for x in input('adad ra bede : ').split(" ")]
print(ofword)

print("////////////")

#برنامه ای که میاد هرکدوم از داده ها را داخل یه پارامتر میریزه 
#adad ra bede : ali ia zahra
#['ali', 'ia', 'zahra']
ofword=[x for x in input('adad ra bede : ').split(" ")]
print(ofword)

print("////////////")

# به تعداد نامشخصی  ورودی میگیریم. یعنی هرقدر بخوایم که بعد 
# با اسپیس هرجا دیدجدا شده را میگیره میریزه تلیست
aa=list(input(' give me the any point: ').split())
print((aa))
#  give me the any point: 654 67565 34 978 23 2 gf
# ['654', '67565', '34', '978', '23', '2', 'gf']
    

# ////////////

#به تعداد محدودی مشخصی ورودی گرفتن
# این فقط عدد های جدا میده
# 344 343 22

ofword=string1, string2, string3= input("").split()
results = [int(i) for i in ofword]
print((results))
# [344, 343, 22]
print("////////////")

# فقط به یه تعداد که گرفته اسم میگیره و میریزه توی یه لیست حالا گر در هر اسم یه
# اسپیس دید اونو یه پارامتر دیگه میکنه  منتها داخل همون لیست
#tedad ra bede : 3
#ali
#hasan hosin
#mitra
#[['ali'], ['hasan', 'hosin'], ['mitra']]
tedadesm=int(input("tedad ra bede : "))
string=[list(input().split())  for adad in range(tedadesm) ]
print(string)

print("////////////")

# ونه دونه از حرفا را یه عضو میکنه تو
# یک لیست میزاره منتها به تعدا ماره ها یه زیر لیست میگیره
tedadesm=int(input("tedad ra bede : "))
string=[list(input('esme badi che?'))  for adad in range(tedadesm) ]
#tedad ra bede : 3
#ali hasan
#reza
#dariush
#[['a', 'l', 'i', ' ', 'h', 'a', 's', 'a', 'n'], ['r', 'e', 'z', 'a'], ['d', 'a', 'r', 'i', 'u', 's', 'h']]

print("////////////")

#یه تعداد میگیره و به ازای اون تعداد بار اسم میپرسه
# و هر اسم را یه پارامتر میکنه داخل یه لیست واحد

tedadesm=int(input("tedad ra bede : "))
string=[(input())  for adad in range(tedadesm) ]
print(string)
#tedad ra bede : 3
#ali vaghe
#nads
#javad
#['ali vaghe', 'nads', 'javad']
print("////////////")

#یه لیست را میگیره هر کاراکتر را (حتی اسپیس را  ) داخل یه پراامتر میریزه

tedadesm=int(input("tedad ra bede : "))
string=[list(input())  for adad in range(tedadesm) ]
print(string)
#tedad ra bede : 3
#ali
#hsio ra
#boao
#[['a', 'l', 'i'], ['h', 's', 'i', 'o', ' ', 'r', 'a'], ['b', 'o', 'a', 'o']]
print("////////////")

#لیست میکنه تا ان عدد را 

chandta= int(input("chandta adad mikhai: "))
adadbede=[ i for i in range(chandta)]
print(adadbede)
#chandta adad mikhai: 3
#[0, 1, 2]
print("////////////")


chandta= int(input("chandta adad mikhai: "))
adadbede=[list(int(i)  for i in range(chandta))]
print(adadbede)
#chandta adad mikhai: 4
#[[0, 1, 2, 3]]

# حالا اگر بازه را بخوایم لیست کنیم چی؟

print("////////////")

#برنامه ای که یه عد میگیره و
# به ازای اون عدد عدد میخواد و بعد همه را تو یه نستت لیست میریزه
chandta= int(input("chandta adad mikhai: "))
adadbede=[list((int(input("adad chie: ")))  for i in range(chandta)) ]
print(adadbede)

# chandta adad mikhai: 4
# adad chie: 7
# adad chie: 32
# adad chie: 645
# adad chie: 3
# [[7, 32, 645, 3]]

print("////////////")

# اول یه عدد میگیره و بعد به ازای اون عدد همه را داخل یه لیست واحد میریزه 
chandta= int(input("chandta adad mikhai: "))
adadbede=[ x for x in list(int(input("adad chie: "))  for i in range (chandta))  ]
print(adadbede)

# chandta adad mikhai: 4
# adad chie: 34
# adad chie: 31
# adad chie: 5
# adad chie: 6
# [34, 31, 5, 6]

print("////////////")

#ترکیب فور و ماژول ها . یعنی به ازای هر کدم میریزه تو ماژول
# یه لیست را میگیره و هر کدام را جذرشونو حساب میکنه 

# کار روی محتوای لیست ها و لیست های تو در تو
adadbede=[23, 54, 45]
print(adadbede)
import math
for i in adadbede:
    adad=math.sqrt(i)
    print(adad)

# [23, 54, 45]
# 4.795831523312719
# 7.3484692283495345
# 6.708203932499369

print("/////////")
#
# دیکشنری که ولیو هاش لیست هستند
data = {'CNN': [5.89, 2.34], 'BBC': [6.78, 4.45]}
for k, v in data.items():
     print (k, v)

print("/////////")

print("//////////")# zip
#کار با zip میاد یه لیست را یک به یک درون با عضو دیگ از ای لیست جفت میکنه
X=[1,2,3]
Y=['a','b','c','d','E']
koolac=list(zip(X,Y))
print(koolac)
# [(1, 'a'), (2, 'b'), (3, 'c')]
for x, y in zip(X,Y):
    print(x,y)
# 1 a
# 2 b
# 3 c
# فقط این روش اگر دو لیست اندازه یکسانی نداشته باشند میاد کوچکترین را میگیره
# برای روش های دیگه به ITERTOOLS باید رفت
print("//////////")# zip
#متناظر کرد سه لیست.

p=["A","B","C","D","E"]
x=[1,2,2,3,3]
y=[1,1,2,1,2]
koolac=list(zip(p,x,y))
print(koolac)
#[('A', 1, 1), ('B', 2, 1), ('C', 2, 2), ('D', 3, 1), ('E', 3, 2)]


# ریختن در یک لیست همه ی موارد را
people=[]
for x, y ,z in zip(X,Y,Z):
    people.append(x,y,z)
print(people)
# TypeError: append() takes exactly one argument (3 given)

# راه حل اینه. یه پرانتز درون اون اپند هم بزار
# تبدیل سه لیست به تاپل هایی از یک لیست
people=[]
for x, y ,z in zip(X,Y,Z):
    people.append((x,y,z))
print(people)
# [(18, 'a', 'mamd'), (19, 'b', 'milad'), (14, 'c', 'javid'), (12, 'd', 'gali'), (5, 'E', 'javad')]

print("//////////")
# *zip
#جدا کند یک لیست را به سه تا سه تایی  و هرکدوم را درن یه تاپل یا هرچی بزاره


z= [(1, 'A'), (2, 'B'), (3, 'C')]
x,y=zip(*z)
print(x)
print(y)
# (1, 2, 3)
# ('A', 'B', 'C')

print("//////////")
#   عناصر یه لیست را میکنه و به یک لیست تبدیل میکنه
# جدا میکنه از زیب

z= [(1, 'A'), (2, 'B'), (3, 'C')]
x,y=((zip(*z)))
print (list (x))
print(y)
#[1, 2, 3]
#('A', 'B', 'C')
print("//////////")
#ترکیب حلقه for وzip  یعنی به ازای یه تعدادی

list1=[1,2,3,4,5,6,7,8,9]
list2=[4,6,8,2,3,7]
list3=[7,3,9,1,4,6,8,2]
for item1,item2,item3 in zip(list1,list2,list3):
    print(str(item1)+','+str(item2)+','+str(item3))
# 1,4,7
# 2,6,3
# 3,8,9
# 4,2,1
# 5,3,4
# 6,7,6

print("//////////")
# داخل لیست  را خروجی هم تاپلی ار لیست ها میکنه

list1=[1,2,3,4,5,6,7,8,9]
list2=[4,6,8,2,3,7]
list3=[7,3,9,1,4,6,8,2]
print (list(zip(list1,list2,list3)))
#[(1, 4, 7), (2, 6, 3), (3, 8, 9), (4, 2, 1), (5, 3, 4), (6, 7, 6)]


print("//////////")
# لیست به دیکشنری
#حالا دو لیست را به عنوان دیکشنری در میاریم با استفاده از zip
#a_dict = {'name' : 'Monty', 'age' : 42, 'food' : 'spam'}

keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']
dictionary = dict(zip(keys, values))
print(dictionary)



# ////////
# مساله 
# زیپ کردن رندوم
# وقتی که عنصر سوم یا دوم یک بازه رندوم باشه مشکل ایجاد میشه
from random import shuffle,choice,randint,randrange
from itertools import cycle
m_players=['Human1', 'Human2', 'Human3',]
myplayerlist=['Hossein','Maziar','Akbar'] 

post=['goalkeeper','deffender','modifier','forward'] #'forward'
shuffle(post)
# تا اینجا پست را تعین کردم
# چجوری باید عددی بین رنج را به بازیکن ها اختصاص بدم؟

price= randint(1,200)
print(price)
print(list(zip((post),(myplayerlist),(randint(1,1000)))))
# [('forward', 'Hossein'), ('modifier', 'Maziar'), ('goalkeeper', 'Akbar'), ('deffender', 'Hossein')]
# TypeError: 'int' object is not iterable


# پاسخ نهایی
price= [randint(1,200) for i in post]
print(list(zip(post,myplayerlist,m_players,price)))
# [('forward', 'Hossein', 'Human1', 61), ('goalkeeper', 'Maziar', 'Human2', 134), ('modifier', 'Akbar', 'Human3', 125)]


# ///////
# زیپ کردن تعداد نامشخصی از لیست ها






print("//////////")

#فقط یه عنصر خاص را n ام بهمون میده. مثلا فقط عنصر اول که با ایندکس 0 در پایتون
# معلوم میشه را بهمون میده که بعد باهاش کرا کنیم

a= [[1,2],[3,4],[5,6],[7,8]]
for line in a:
    print(line[0])
# 1
# 3
# 5
# 7

print("//////////")
# یه لیست را دونه دونه اینتر میزنه 

My_List_1 = [3, 16, 5, 4, 2, 1]
print(*My_List_1, sep='\n')
#
# 3
# 16
# 5
# 4
# 2
# 1
print('\n')

My_List_1.sort()
print(*My_List_1, sep='\n')

#همون لیست را سورت میکنه اینتر میزنه
# 1
# 2
# 3
# 4
# 5
# 16


print("//////////")
#یه لیست را از آخر برعکس میکنه ولی به ازای اون عددی که بهش دادیم
# برعکس کردن لیست
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
print("The original list : " + str(test_list))
K = 6
res = test_list[-K:][::-1]
# The original list : [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
print("The sliced list : " + str(res))
# The sliced list : [18, 16, 15, 12, 9, 3]



print("//////////")
# تبدیل دیکشنری به لیست
# ساخت یک لیست از دیکشنری ها که اول کلید ها میاد و بعد ولیو ها

test_dict = {"Gfg": 1, "is": 3, "Best": 2}
print(" " + str(test_dict))
# {'Gfg': 1, 'is': 3, 'Best': 2}
res = list(test_dict.keys()) + list(test_dict.values())
print(" : " + str(res))
# : ['Gfg', 'is', 'Best', 1, 3, 2]



print("//////////")


print("//////////")
# وارونه چاپ میکند


from itertools import islice
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
print("The original list : " + str(test_list))
K = 6
res = list(islice(reversed(test_list), K))
print("The sliced list : " + str(res))
# The original list : [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
# The sliced list : [18, 16, 15, 12, 9, 3]
print("//////////")
# نوشته بود موقعی که دو تا حلقه فور بکار میرن همونجوری هستند که در نستد اوپ هستند.
for i in conversion:
    for f in glob.glob(i):
        print(os.path.getsize(f))

[os.path.getsize(f) for i in conversion for f in glob.glob(i)]

////

# نوشته بود این دو تا یکی هستند:
# اول اون چیزی که اضافه بشه را می نویسیم و دیگه نیاز
# نداریم اخر بنویسیم اپند بشه . مابقی ترتیب ها همونه
uppercase_letters = []
for name in screencasts:
    for char in name:
        if char.isupper():
            uppercase_letters.append(char)
# یکیه
uppercase_letters = [
    char
    for name in screencasts
    for char in name
    if char.isupper()
]
# ////
# یعنی این دو تا یکی هستند

mylist= [1,2,3,4]
my2=[]
for i in mylist:
    my2.append(i**2)
print(my2)

my3=[
    i**2
    for i in mylist
]
print(my3)


print("//////////")


word = 'geeks, for, geeks, pawan'
  
# maxsplit: 0
print(word.split(', ', 0))
# داره میگه هیچکدوم از اونا را تکه نکن وقتی رسیدی . همه را یه استرینگ جدا کن
['geeks, for, geeks, pawan']

# maxsplit: 4
print(word.split(', ', 4))
# ['geeks', 'for', 'geeks', 'pawan']
#   چهار بار این کار را کن

# maxsplit: 1
print(word.split(', ', 1))
# ['geeks', 'for, geeks, pawan']
# داره میگه یکبار این کار را کن
print("//////////")
# هم اعضای درونی لیست را دسترسی پیدا میکنه و هم  اعضای درون درون
biglist=[[1, 10], [7, 3]]
for char in biglist:
    print(char)
    for i in char:
        print(i)
# [1, 10]
# 1
# 10
# [7, 3]
# 7
# 3
# /////////
biglist=[[1, 10], [7, 3]]
for char in biglist:
    print ([char][0])
# [1, 10]
# [7, 3]


# ////////
# فقط عنصر اولی در هر لیست تو در تو را بداریم
biglist=[[1, 10], [7, 3],[4,5]]
for char in biglist:
    print ([char][0][0])
# 1
# 7
# 4

# یا
# داری میگی عنصر اولی کاراکتر ها را بده
biglist=[[1, 10], [7, 3],[4,5]]
for char in biglist:
    print(char[0])
# 1
# 7
# 4


print("//////////")
# مقایسه همزمان دو فاکتور 
biglist=[[1, 10], [7, 3],[3,8]]
for char in biglist:
# چجوری بگم کاراکتر اول اونی که کمتر از بقیه بود و هم کاراکتر دوم بیشتر از همون بود؟ 
# این فرق داره با اینی که بگم اونی که کاراکتر اول کمتر بود. و اونی که کاراکتر دوم بیشترین بود... 
# ما ترکیبی میخوایم... 
    
    
#    /////
# چجوری موقعی که پیدا کرد بگه این بود



print("//////////")

# code
# LIST
list = [["Rohan", 60], ["Aviral", 21], 
        ["Harsh", 30], ["Rahul", 40],
        ["Raj", 20]]
  
# looping through nested list using multiple 
# temporary variables
for name, age in list:
    print(name, "is",
          age, "years old.")
# Rohan is 60 years old.
# Aviral is 21 years old.
# Harsh is 30 years old.
# Rahul is 40 years old.
# Raj is 20 years old.

print("//////////")
# میخوام به عنصر اول کاراکتر دسترسی داشته باشم

# این روش دوبار پرینت میکنه . به تعداد کاراکتر  !که نمیخوام
biglist=[[1, 10], [7, 3]]
for char in biglist:
    for i in char:
        print (char[0])
# 1
# 1
# 7
# 7



print("//////////")


# مقایسه کردن دو لیست جدا تودرتو با هم در یک حلقه
x= [['1', 'a', 'b'], ['2', 'c', 'd']]
y = [['1', 'z', 'x'], ['4', 'z', 'x']]

def find_match(x, y):
    match = []
    for i in x:
        for j in y:
            if i[0] == j[0]:
                match.append(j)
    return match
match = find_match(x, y)
print(match)
# [['1', 'z', 'x']]


print("//////////")
# تفاوت های یک لیست را در نستد لیست در میاره
lst = [[1, 2], [3, 4], [1, 2], [5, 6], [8, 3], [2, 7]]
sublst = [[1, 2], [8, 3]]
diff  =[x for x in lst if x not in sublst]
print(diff)
# diff = [[3, 4], [5, 6], [2, 7]]


# یا با لامبدا
filter(lambda x:x not in sublst,lst)
# [[3, 4], [5, 6], [2, 7]]

# یا تاپل
def tuples(lst): return [tuple(l) for l in lst]
print (set(tuples(lst)) - set(tuples(sublst)))
# set([(5, 6), (2, 7), (3, 4)])

print("//////////")

# مقایسه جایگشتی 
# در لیست تودرتو
# اول عنصر اول اولی را با  عنصر اول دومی میاره
# بعد عنصر اول اولی را با عنصر اول سومی میاره
# فقط عنصر دومی به بعد با خودشون هم مقایسه میشه
# اگر میزاشتیم لن صفر اولی هم با خودش مقایسه میشد
biglist=[[1, 10], [7, 3],[4,5]]
for i in range(len(biglist)):
        # print(biglist[i])
        # [1, 10]
        # [7, 3]
        # [4, 5]
    for j in range(1,len(biglist)):
        print('biglist[i][0] is',biglist[i][0])
        print('biglist[j][0] is',biglist[j][0])
# biglist[i][0] is 1
# biglist[j][0] is 7

# biglist[i][0] is 1
# biglist[j][0] is 4

# biglist[i][0] is 7
# biglist[j][0] is 7

# biglist[i][0] is 7
# biglist[j][0] is 4

# biglist[i][0] is 4
# biglist[j][0] is 7

# biglist[i][0] is 4
# biglist[j][0] is 4

#
# ۱اگر صفر باشه بجای اون طول 
#   یا چیزی ننویسیپیشفرض صفر میگیره

        for j in range(0,len(biglist)):
            print('biglist[i][0] is',biglist[i][0])
            print('biglist[j][0] is',biglist[j][0])
# biglist[i][0] is 1
# biglist[j][0] is 1

# biglist[i][0] is 1
# biglist[j][0] is 7

# biglist[i][0] is 1
# biglist[j][0] is 4
# ///////
# biglist[i][0] is 7
# biglist[j][0] is 1

# biglist[i][0] is 7
# biglist[j][0] is 7

# biglist[i][0] is 7
# biglist[j][0] is 4
# ////////
# biglist[i][0] is 4
# biglist[j][0] is 1

# biglist[i][0] is 4
# biglist[j][0] is 7

# biglist[i][0] is 4
# biglist[j][0] is 4

# /////////////
# توجه شود که اگر لیست را میخوای ایتربل کنه باید
# range
# را بکار ببری 
def determinatio():
    number = int(input('give me the number: '))
    my_list=[]
    # یعنی در اینجا وگرنه خطا میده
    for num in range (number) :
        mie= input('give me the price: ')
        my_list.append(mie)
        
    return my_list

# /////////////

def determinatio():
    number = int(input('give me the number: '))
    my_list=[]
    for num in range (number):
        # توجه اینجا نمیشه همونجوری به اینتیجر تبدیل کنه 
        mie= int(input('give me the price: ').split())
        my_list.append(mie)
    return my_list
print(determinatio())

print("//////////")
# یک لیست تو در تو درست میکنه
twdad=int(input(""))
keifoghei= [list(int(x) for x in (input('')).split()) for char in range(twdad)]
print(keifoghei)

# زدن حلقه تک خطی در یک حلقه معمولی
# حالا همینه فقط در حلقه و طولانی تر هست
twdad=int(input('give me number of laptop: '))
keifoghei=[]       # a prepare this empy list for add to 
for char in range (twdad):    # in the number of taking this loop ask from agetn how many laptob doyou need?
    sublist= input('give me list: ').split()   #get input from agent for example 
    some_sublist=[int(char) for char in sublist]   #invert a string to intiger
    keifoghei.append(some_sublist)   #to add whole of nested list in a biger list(parent list)
    print(keifoghei)


# حتی این خلاصه تره
# twdad=int(input(""))
keifoghei= [list(int(x) for x in (input('')).split()) for char in range(int(input()))]
print(keifoghei)
# 2
# 3 4
# 5 6
# [[3, 4], [5, 6]]
print("//////////")
# شماردن اینکه یه متغیر چند بار در یه لیست بکار رفته 
from collections import Counter
my_powers=[2,2,2,2,2,3]
print(Counter(my_powers))
# Counter({2: 5, 3: 1})

# یا شماردن 
l = ["a","b","b"]
[[x,l.count(x)] for x in set(l)]
# [['a', 1], ['b', 2]]
#  یا روش دیگر
dict((x,l.count(x)) for x in set(l))
# {'a': 1, 'b': 2}

print("//////////")
# ضرب کردن اعداد با هم در یک لیست
a = [2, 3, 4]
total = 1
for i in a:
    total *= i
print(total)

print("//////////")
# استفاده و ترکیب تابع و لیست ها . مقایسه دو لیست که یک تابع است و یک  لیست ساده است
# فرض کن خروجی تابع اینه:
# return([number , total])
# [672, 24]
print(prime_number(672)[1])
# 24
biggest=[0,0]
print(biggest[0])
# 0
print(prime_number(672)[1] >biggest[0])
# True

if prime_number(672)[1] >biggest[0] :
    print('true')
# true




print("//////////")

# تبدیل یه استرینگ به لیست ای از شماره ها و تعداد حروف اون استرینگ

# Using split() + loop

# اینجا کلشو یه لیست میکنه
test_str='ok im here for explanation of your context'
print((test_str))

delim="_"
temp= test_str.split(delim)
print(temp)
# ['ok im here for explanation of your context']

# ولی  با افزودن این تیکه در اولش هر واژه را یه لیست میکنه
test_str = 'gfg_is_best_for_geeks'
print("The original string is : "
      + str(test_str))
 # The original string is : gfg_is_best_for_geeks 
 
delim = "_"
temp = test_str.split(delim)
print(temp)
# ['gfg', 'is', 'best', 'for', 'geeks']



print("//////////")
# تابعی که درون لیست میگه اون  متغیر درون لیست چندمی هست
# enumerate  تابع درونی
# built in
a=["Mohammad","Ali","Hasan","Hossein"]
print(list(enumerate(a)))
# [(0, 'Mohammad'), (1, 'Ali'), (2, 'Hasan'), (3, 'Hossein'), (4, 'Sajjad')]
# 
# حالا اگر بخوایم اندیس گذاری را از ۱ آغاز کنه اینگونه میشه 
# . باید بجای پیشفرض صفر بزاری ۱ 
print(list(enumerate(a,1)))
# [(1, 'Mohammad'), (2, 'Ali'), (3, 'Hasan'), (4, 'Hossein')]


print("//////////")
# کاربرد 

# در حلقه و لیست 
# مقایسه اعضای درونی یک لیست با هم در یک حلقه
def sumPairs(lst):
    diffs = []
    for i, x in enumerate(lst):
        print('x is: ',x)
        for j,y in enumerate(lst):
            if i != j:
                print('y is: ',y)
                diffs.append(abs(x-y))
                print('x , y is',x , y)
                print('diffs is now: ',diffs)
    print(diffs)   # 16
    # به این دلیل تقسیم بر ۲ میکنه چون که در 
    # دو حلقه دو بار بررسی میکنه . یه بار ۶ را با ۹ و یکبار ۹ را با ۶
    # پس باید تقسیم بر ۲ هم کرد که فیلتر کنه
    return int(sum(diffs)/2)
lst = [6, 9, 10]
print(sumPairs(lst))
# 8
print("//////////")

import itertools
def sumPairs(lst):
    diffs=[]
    # diffs = [abs(e[1] - e[0]) for e in itertools.permutations(lst, 2)]
    # میگه برای هر ای که در لیست هست 
    # جایگشت اون ای را بگیر
    # اما اون ۲ برای چی هست؟
    for e in itertools.permutations(lst,3):
        # بعد قدر مطلق اون ای با عضو دیگر را بگیر 
        # اضافه کن و بریز توی دیففس
        # اما چرا ای صفر و ای ۱
        # جالبه اگر بالا را ۳ بزنی اینجا میتونی ۲ بزنی 
       diffs.append(abs(e[1]-e[2]))
    #    اینجا اینتیجر میکنی . جمع اعداد لیست را
    # #چون  بعضی موارد مثل ۶ با ۹ را میاره . یه بار هم ۹ با ۶ را میاره 
    return int(sum(diffs)/2)
# Driver program
lst = [6,9,10]
print(sumPairs(lst))
# 8
# ////////////
# کار بدون اپند و ساخت لیست خالی
import itertools
def sumPairs(lst):
    diffs=[]
    for e in itertools.permutations(lst):
       diffs.append(abs(e[1]-e[0]))
    return int(sum(diffs)/2)
lst = [6,9,10]
print(sumPairs(lst))
# 8

# این هموه بدون اپند و بدون ساخت لیست خالی
# لیست تو در تو
import itertools
def sumPairs(lst):
    # این تیکه کد به معنای اینه که  هم اپند بشه اون تیکه پشت حلقه 
    # هم یه لیست خالی خودش ساخته که میریزه توش
    # تازه . یعنی دیگه نیاز نیست هی متغیر تعریف کنیم خود عملیات را میشه درون تابع ریخت حساب کنه
    diffs = [abs(e[1] - e[0]) for e in itertools.permutations(lst, 2)]
    return int(sum(diffs)/2)
lst = [6,9,10]
print(sumPairs(lst))
# 8
# //////////////
# هرکدوم از اعضا را به لیست میبره با اینتیجر
[int(i) for i in str(12345)]
# [1, 2, 3, 4, 5]
# ////////////ت
my_list=[]     
for i in input().split():
    my_list.append(int(i))
print(my_list)
# 3 2 5 4
# [3, 2, 5, 4]   
# /////////
# ولی این نمیشه چون از قبل یه لیست تبدیل کرده
my_list=[]     
for i in range (2):
    min=input().split()
    my_list.append(int(min))
print(my_list)

# ////////
# ////////////
def tedad():
    member =int(input('give me the number of member of players:'))
    mine=[]
    # اینکه اعضای درونی یک داده را با فاصله دادیم را جدا کنه به لیست بیاره یه ضرب
    for each in (input('give me your number: ')).split():
# تبدیل اسپلیت به اینتیجر در حلقه
# بجای اینکه در حلقه جدا بنویسیم
        mine.append(int (each))
        print(mine)
tedad()
# این حلقه هر بار یکیو بر میداره میریزه تو ی لیست ما
# [4]
# [4, 5]
# [4, 5, 6]
# [4, 5, 6, 7]

# ////

# تبدیل لیست به استرینگ
# برگردوندن یک لیست استرینگی به یه استرینگ  . برعکس اسپلیت
# this-is-a-hero-here
name2= ['this', 'is', 'a', 'hero', 'here']
name3= (('-').join(name2))
print(name3)
# this-is-a-hero-here
# /////

# خطا های ارور در لیست

# subscriptable   # اشتراک پذیر
# ///////////////////////////////////
# لیست به دیکشنری
# تبدیل لیست تودرتو به دیکشنری
# عنصر های اول لیست تو در تو میشه کلید
# عنصر های دوم میشه ولیو
mylist=[[1,10],[7,3]]
my_dict={}
for k in mylist:
    my_dict[k[0]]=k[1]
print(my_dict)
# {1: 10, 7: 3}

# ///////////
# میگرده به ترتیب میده
# iter
x = iter(["apple", "banana", "cherry"])
print(type(x))   #<class 'list_iterator'>
print(next(x))
# apple
print(next(x))
# banana
print(next(x))
# cherry
# //////////////
# حلقه زدن در لیست 
from collections import defaultdict
test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]
print("The original list is : " + str(test_list))
# The original list is : [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]
res = defaultdict(list)
print((res))
# defaultdict(<class 'list'>, {})
for i, j in test_list:
    res[i].append(j)

# //////////////////
# جایگزینی
# '''شیوه های جایگزینی یک عنصر لیست با دی=عنصر دیگر '''
# Replace Values in a List using indexing
# define list
l = [ 'Hardik','Rohit', 'Rahul', 'Virat', 'Pant']
# replace first value
l[0] = 'Shardul'
# print list
print(l)
# ['Shardul', 'Rohit', 'Rahul', 'Virat', 'Pant']


# /////////////////////////////////////
# به وسیله حلقه جایگزین می کنیم
# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
  
for i in range(len(l)):
  
    # replace hardik with shardul
    if l[i] == 'Hardik':
        l[i] = 'Shardul'
  
    # replace pant with ishan
    if l[i] == 'Pant':
        l[i] = 'Ishan'
  
# print list
print(l)
# ['Shardul', 'Rohit', 'Rahul', 'Virat', 'Ishan']

# ///////////////////
# جایگزینی با حلقه وایل

# اصلا روش هم ارزی فور و وایل هم همینه 
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant'] 
i = 0
while i < len(l):
    # replace hardik with shardul
    if l[i] == 'Hardik':
        l[i] = 'Shardul'
  
    # replace pant with ishan
    if l[i] == 'Pant':
        l[i] = 'Ishan'
  
    i += 1
  
# print list
print(l)
# ['Shardul', 'Rohit', 'Rahul', 'Virat', 'Ishan']

# /////////////////
# جایگزینی یک عنصر لیست  با دیگری با لامبدا
# جالبه که وقتی متدی برای استرینگ است میشه با لامبدا برای لیست هم بکارش برد
# Replace Values in a List using Lambda Function
  
# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
  
# replace Pant with Ishan
l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))
  
# print list
print(l)
# ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Ishan']

# //////////////
# جایگزینی با روش برش زدن

# Replace Values in a List using Slicing
  
# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
  
# find the index of Rahul
i = l.index('Rahul')
#   اینجا اومده میگه پیش از آی را و پس از ای را بیار .  این یعنی خود ای را که قبلا بود را نیار اینبار  بجاش کلمه جدیده را بیار
# replace Rahul with Shikhar
l = l[:i]+['Shikhar']+l[i+1:]
  
# print list
print(l)
# ['Hardik', 'Rohit', 'Shikhar', 'Virat', 'Pant']
# //////////////////

# در مقایسه  دیکشنری و لیست 
# به روش لن که بالا برای جایگزینی اشاره کردیم
# مثلا میخوایم بگیم که هر کدوم از کلید ها که در لیست بود را با ولیو اون کلید در لیست جایگزین کن

# روش حلقه بدون رنج اصلا جایگزینی صورت نمیگیره با اون ۴ چوب باید از 
# len
# استفاده کرد
sentence=['you','say','to','i','guy','hello']
my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
new_sentence=[]
for char in range (len(sentence)):                  #   وقتی لیست  تغیر ناپذیره چجوری جمله  را تغیر بدم
    for my_vazhenameh[klid] in range(len(my_vazhenameh)):              #
        # اگر بخوایم  یه دیکشنری و یه حلقه را مقایسه کنیم برای اشاره به لن اون
        # همون شکلی است که اشاره کنیم ولیو اون چند است.. واسه همین هم اصلا ایندکس را نیاوردن
        # این خطا میده
        if sentence[char] == klid:



# مشکل تفاوت لن و حلقه زدن
# راه حلش اینه از انومریت کمک بگیریم
# داری میگه که  اگر همون بود  با انومریتش جایگزین کنه
def replace(list, dictionary):
    for idx, val in enumerate(list):
        if i in k:
           list[idx] = dictionary[list[idx]]
    return list
print replace(input_file,curaw_dict)

# //////////////////

# مزیت لیست تک خطی اینه که یه ضرب مینویسی و دیگه نیاز نیست اپند کنی
# جایگزینی 

import collections
def requaired_sentence():
    # my_vanameh=converter_lt_2_d()
    my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
    my_vazhenameh=collections.OrderedDict(((my_vazhenameh.items())))
    print(my_vazhenameh) 
    # sentence=input('give me the sentence for translating: ').split()
    sentence=['you','say','to','i','guy','hello']
# ساخت لیست یک خطی و بررسی شرطی که اگر نبود خودشو بزاره و اگر بود جایگزین اون ولیو اون کلید را بزاره
    # داره میگه هر کدوم از اعضایی که در جمله هستند را به عنوان ایکس در نظر بگیر
    # اگر اون ایکسه در کلید های دیکشنری نبود خودشو جایگزین کن وگرنه ولیوشو جایگزین کن
    replaced_list=[ x if x not in my_vazhenameh  else my_vazhenameh[x]  for x in sentence]
    return (replaced_list)
# ['tu', 'say', 'to', 'man', 'guy', 'dorod']




# ////////
# فرمول تک خطی
replaced_list=[  3 tali     2 if moghadam   4 else tali    1 for x in sentence]

# ///////

# برای اجرای یک حلقه در لیست تودرتو
# در صورتی که این درست
# بود
L = [[0,[1,1.0]],
     [0,[2,0.5]],
     [1,[3,3.0]],
     [2,[1,0.33]],
     [2,[4,1.5]]]
for k , (v ,c) in L:
    print('d[k]',d[k])
    print('k',k)



# حالا اگر اینرا برای لیستی که کار میکنه اضافه کنیم اینو میده

for k , v ,c in L:
    print('d[k]',d[k])
    print('k',k)
# ValueError: not enough values to unpack (expected 3, got 2)



# حالا اگر اولی را هم اینجوری بزنیم 
my_members= [['2022-01-16', ['9', '1']], ['2022-01-23', ['14', '1']]]

# درست میشه
for main_key ,val in my_members:
    print(val)
# ['9', '1']
# ['14', '1']

# پس باید لیست تو در تو به اندازه متغیر های درون حلقه باشه

# ///////////
# حلقه زدن در یک لیست تو در تو
# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# سینتکس حلقه تودرتو
# در لیست تک خطی
flatten_matrix = [val for 1 for 2]
flatten_matrix = [val for sublist in matrix for val in sublist]

# //////////
# برش لیست میشه که در خود حلقه لحاظ بشه . از اول به اونها فقط 
# یه لیست تودرتو
# که بعد کاراکتر هم میاد اشاره میکنه 
# به برش
# تبدیل لیست برش خورده به دیکشنری
    for char in (my_members[5:]):
        dict[char[0]]= char[1] ,char[2]
# {'2022-01-16': ('9', '1')}

# //////////

#  تبدیل یک لیستی از تاپل های تودرتو به دیکشنری
# عنصر اول تاپل اول میشه کلید عنصر های دوم میشه ولیو ها
# اینجا حتی میشد لیست تودرتو باشه .یه لیست کلی - یه لیست دو مادر - یه لیست فرزندان که هر فرزد دو کاراکتر داره 


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
        
        
        
# /////////
# عنصر های اولشو جدا میکنه 
# عنصر های دوم هر لیست را به اینتیجر تبدیل میکنه
# [['mandana', '5', '7', '3', '15'], ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], ['sina', '19', '10', '19', '6', '8', '14', '3'], ['sara', '0', '5', '20', '14'], ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], ['ali', '1', '9'], ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8'], [], [], [], [], [], [], [], [], []]
        roder=list(my_Reader)
        my=[]
        for charr in (roder):
            while '' in charr:
                charr.remove('')
            cha =[int(k) for k in charr[1:]]
            my.append(cha)
            my.append((charr[0:1]))
# [[5, 7, 3, 15], ['mandana'], [3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1], ['hamid'], [19, 10, 19, 6, 8, 14, 3], ['sina'], [0, 5, 20, 14], ['sara'], [13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7], ['soheila'], [1, 9], ['ali'], [0, 16, 16, 13, 19, 2, 17, 8], ['sarvin'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# ///////////////
# اینم نمیشه
# تاپل اضافه میکنه دردل لیست خالی
       for charr in roder:
            while '' in charr:
                charr.remove('')

            # my.append((list(int(x) for x in charr[1:])))
            my.append([x for x  in(charr[0:1]) ] )
            my.append([ tuple(int(x) for char in my for x in char[1:0])])
# [['mandana'], [()], ['hamid'], [()], ['sina'], [()], ['sara'], [()], ['soheila'], [()], ['ali'], [()], ['sarvin'], [()], [], [()], [], [()], [], [()], [], [()], [], [()], [], [()], [], [()], [], [()], [], [()]]
#
#
# ///////////
# insert
# به عنصر اول 
# اینو اضافه کن
lis = ['Geeks', 'Geeks']
lis.insert(1, "For")
print(lis)

# ///////
# افزودن به لیست
list5 = [[], [(1,2,3,4), 2, 5]]
print(list5)
# [(1, 2, 3, 4), 2, 5]]

# این جایگزینی هم داره
# میگه به جای عنصر صفرم لیست
# اینو اینسرت کن در عنصر صفرم
list5[0].insert(0, (2,5,6,8))
print(list5)
# [[(2, 5, 6, 8)], [(1, 2, 3, 4), 2, 5]]
            
list5.insert(0, (2,5,6,8))
# [(2, 5, 6, 8), [], [(1, 2, 3, 4), 2, 5]]  
# /////////
# برش میزنه 
# عنصر اول ها را اولین لیست میکنه
# عنصر های بعدی را لیست دومی
# لیست اول:
# [['mandana', '5', '7', '3', '15'], ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], ['sina', '19', '10', '19', '6', '8', '14', '3'], ['sara', '0', '5', '20', '14'], ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], ['ali', '1', '9'], ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8'], [], [], [], [], [], [], [], [], []]

        for charr in (roder):
            while '' in charr:
                charr.remove('')
            cha =[int(k) for k in charr[1:]]
            my.append((charr[1:]))
            my.insert(0,charr[0:1])
# [[], [], [], [], [], [], [], [], [], ['sarvin'], ['ali'], ['soheila'], ['sara'], ['sina'], ['hamid'], ['mandana'], ['5', '7', '3', '15'], ['3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], ['19', '10', '19', '6', '8', '14', '3'], ['0', '5', '20', '14'], ['13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], ['1', '9'], ['0', '16', '16', '13', '19', '2', '17', '8'], [], [], [], [], [], [], [], [], []]


# اینم جلوش اضافه میکنه
# تغیر میده ولی جلوش اضافه میکنه
# قبلی را حذف نمیکنه
        for charr in roder:
            while '' in charr:
                charr.remove('')
            for k in charr[1:]:
                charr.append(int(k))
                
# [['mandana', '5', '7', '3', '15', 5, 7, 3, 15], ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1', 3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1], ['sina', '19', '10', '19', '6', '8', '14', '3', 19, 10, 19, 6, 8, 14, 3], ['sara', '0', '5', '20', '14', 0, 5, 20, 14], ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7',
# 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7], ['ali', '1', '9', 1, 9], ['sarvin', '0', '16', '16',
# '13', '19', '2', '17', '8', 0, 16, 16, 13, 19, 2, 17, 8], [], [], [], [], [], [], [], [], []]
# None



# //////////
# برش زدن و خالی کردن یک لیست
        for charr in roder:
            while '' in charr:
                charr.remove('')
            for adad in charr[1:]:
                
                charr[1:]= adad.replace(adad,'')
                
# [['mandana'], ['hamid'], ['sina'], ['sara'], ['soheila'], ['ali'], ['sarvin'], [], [], [], [],
# [], [], [], [], []]    

# ////////
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# اما چطور یه لیست تو در تو را برش بزنم عنصر اولش باقی بمونه استرینگ و بقیه اینتیجر بشن؟


# دیکشنری شدنش اینجوری میشه
        my={}
        for charr in roder:
            # print(charr)
            while '' in charr:
                charr.remove('')
            for harf in charr:
                # harf=int(harf)
                my[charr[0]]= (list (int(x) for x in charr[1:]))
# میشه بعد کلید را عنصر نخست لیست کنم و بقیه را پخش کنم توی  مابقی لیست؟


# این کد به عنصر اولی اضافه میکنه فقط همه را
for charr in roder:
            while '' in charr:
                charr.remove('')
            my.append((list(int(x) for x in charr[1:])))
            my[0].insert(0,(charr[0:1]))
# [[ ['sarvin'], ['ali'], ['soheila'], ['sara'], ['sina'], ['hamid'], ['mandana'], 5, 7, 3, 15]   , [3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1], [19, 10, 19, 6, 8, 14, 3], [0, 5, 20, 14], [13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7], [1, 9], [0, 16, 16,
# 13, 19, 2, 17, 8], [], [], [], [], [], [], [], [], []]



# //////////
# این  هم این مشکلو داره
        for charr in roder:
            while '' in charr:
                charr.remove('')

            # my.append((list(int(x) for x in charr[1:])))
            two=[x for x  in(charr[0:1]) ]
            print('two is',two)
            one= [(int(x)) for x in charr[1:]]
            print('one is',one)
            three=list(zip(one,two))
            print('three is',three)
# میاد فقط به اندازه زیپ میکنه مابقیشو نمیریزه
# two is ['mandana']
# one is [5, 7, 3, 15]
# three is [(5, 'mandana')]
# two is ['hamid']
# one is [3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1]
# three is [(3, 'hamid')]
# two is ['sina']
# one is [19, 10, 19, 6, 8, 14, 3]
# three is [(19, 'sina')]
# two is ['sara']
# one is [0, 5, 20, 14]
# three is [(0, 'sara')]
# two is ['soheila']
# one is [13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7]
# three is [(13, 'soheila')]
# two is ['ali']
# one is [1, 9]
# three is [(1, 'ali')]
# two is ['sarvin']
# one is [0, 16, 16, 13, 19, 2, 17, 8]
# three is [(0, 'sarvin')]


# ///////

# اگر زیپ  سایکل کنیم هم اینجوری میده
# لیستی از تاپل ها میده که اون اسمه هی تکرار میشه
        my=[]
        for charr in roder:
            while '' in charr:
                charr.remove('')
            # my.append((list(int(x) for x in charr[1:])))
            name=[x for x  in(charr[0:1]) ]
            # print('name is',name)
            num= [(int(x)) for x in charr[1:]]
            print('num is',num)
            myr=(zip((num),cycle(name)))
            my.append(list (myr))
        print(my)

# [[(5, 'mandana'), (7, 'mandana'), (3, 'mandana'), (15, 'mandana')], [(3, 'hamid'), (9, 'hamid'), (4, 'hamid'), (20, 'hamid'), (9, 'hamid'), (1, 'hamid'), (8, 'hamid'), (16, 'hamid'), (0, 'hamid'), (5, 'hamid'), (2, 'hamid'), (4, 'hamid'), (7, 'hamid'), (2, 'hamid'), (1, 'hamid')], [(19, 'sina'), (10, 'sina'), (19, 'sina'), (6, 'sina'), (8, 'sina'), (14, 'sina'), (3, 'sina')], [(0, 'sara'), (5, 'sara'), (20, 'sara'), (14, 'sara')], [(13, 'soheila'), (2, 'soheila'), (5, 'soheila'), (1, 'soheila'), (3, 'soheila'), (10, 'soheila'), (12, 'soheila'), (4, 'soheila'), (13, 'soheila'), (17, 'soheila'), (7, 'soheila'), (7, 'soheila')], [(1, 'ali'), (9, 'ali')], [(0,
# 'sarvin'), (16, 'sarvin'), (16, 'sarvin'), (13, 'sarvin'), (19, 'sarvin'), (2, 'sarvin'), (17,
# 'sarvin'), (8, 'sarvin')], [], [], [], [], [], [], [], [], []]
# //////////
# این کد دونه دونه هر عنصر را اضافه میکنه به تهش
# یا اگر جابجا مینوشتیم به اولش
        for charr in roder:
            while '' in charr:
                charr.remove('')

            my.append((list(int(x) for x in charr[1:])))
            my.append([x for  x in charr[0:1]] )
# [[5, 7, 3, 15], ['mandana'], [3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1], ['hamid'], [19, 10, 19, 6, 8, 14, 3], ['sina'], [0, 5, 20, 14], ['sara'], [13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7], ['soheila'], [1, 9], ['ali'], [0, 16, 16, 13, 19, 2, 17, 8], ['sarvin'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# من میخوام بریزه تو همون لیسته به عنوان عنصر اول لیست
# ////////



# ///////


# اگر برای برش زدن این خطا اومد 
charr[0]
# میتونی بیای 
print(charr[0:1])

# البته این همونه 
print(charr[:1])

# ////////

# این چیزیه که میخوام . 
# هر چند کدش بهینه نیست

# کدی که اگر کناریش تکراری بود که چون سورت شده فقط کناری هاش تکراری هستند 
# میاد عنصر ایندکسشو میزاره 
# چون ایندکس ها از صفر میزارن وگرنه ایندکس را از یک میزاره
player_2=[-5,-5,2,8]
mylist=[]
my_second=[]
for char in range (0, len(player_2)):
    if player_2[char] not in mylist:
        mylist.append(player_2[char]) 
        my_second.append(char+1)
    else:
        print('reapeat',player_2[char])
        my_second.append(char)
print(mylist)
print(my_second)

# reapeat -5
# [-5, 2, 8]
# [1, 1, 3, 4]

# ////////
# این کد  میاد یه لیست 
# [['mandana', '5', '7', '3', '15'], ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], ['sina', '19', '10', '19', '6', '8', '14', '3'], ['sara', '0', '5', '20', '14'], ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], ['ali', '1', '9'], ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8'], [], [], [], [], [], [], [], [], []]
# 
# به این تبدیل میکنه
# [['mandana', 5, 7, 3, 15], ['hamid', 3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1], ['sina', 19, 10, 19, 6, 8, 14, 3], ['sara', 0, 5, 20, 14], ['soheila', 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7], ['ali', 1, 9], ['sarvin', 0, 16, 16, 13, 19, 2, 17, 8], [], [], [], [], [], [], [], [], []]

        roder=list(my_Reader)
        my=[]
        # این لیست اصلی را باز میکنه . یک بار باز میکنه 
        # دومین باز کردن در پایین است
        for charr in roder:
            # این وایل میاد همه کاراکتر های اضافه را حذف میکنه
            while '' in charr:
                charr.remove('')
                # این تیکه میاد کاراکتر  اول را میکنه تو یه لیست جدا
            name=[x for x  in(charr[0:1]) ]
            # print('name is',name)
            # این تیکه میاد اینتیجر میکنه یک به بعد را
            num= [(int(x)) for x in charr[1:]]
            # print('num is',num)
            # این تیکه هم پخش میکنه اعضای دو لیست را و بعد لیست میکنشون میریزه تو یه لیست اصلی
            my.append(list(chain((name),(num))))
            # چون خودش درون یهحلقه بالا است هر بار جدا این کار را میکنه 
            # و بنابراین لیست جدا درست میکنه

# اما چطور باید لیست های خالی را حذف کنیم؟
# در بالا چند تا لیست بود
# ////////////
# تبدیل اعضا به اینتیجر
# کلا برای اجرای هر فانکشن در لیست از مپ استفاده میکنیم
a = ["1", "2", "-3"]
print(list(map(int, a)))
# [1, 2, -3]

# ///////

# این خطا میده
# attribute error
string = "1234567"
string.insert(10, 1)
print(string)
# میگه استرینگ نداره 
# //////
# اضافه کردن 
# بیفور المنت
# Python3 program for Insertion in a list  
# before any element using insert() method 
  
list1 = [ 1, 2, 3, 4, 5, 6 ]
  
# Element to be inserted 
element = 13 
  
# Element to be inserted before 3
beforeElement = 3 
  
# Find index
myindex = list1.index(beforeElement) 
  
# Insert element at beforeElement 
list1.insert(myindex, element) 
print(list1)
# [1, 2, 13, 3, 4, 5, 6]

# /////////
list1 = [ 1, 2, 3, 4, 5, 6 ]
  
# tuple of numbers
num_tuple = (4, 5, 6)
  
# inserting a tuple to the list
list1.insert(2, num_tuple)
  
print(list1)


# ////////
# تکرار  ها در لیست
list1 = [['a','b']] * 3
for item in list1:
  item.append("Hello")
print (list1)
# [['a', 'b', 'Hello', 'Hello', 'Hello'], ['a', 'b', 'Hello', 'Hello', 'Hello'], ['a', 'b', 'Hello', 'Hello', 'Hello']]


# ///////
# تکرار در لیسست ها
x = [['a', 'b'] for i in range(0, 3)]
x
[['a', 'b'], ['a', 'b'], ['a', 'b']]
x[0].append('Hello')
x
# [['a', 'b', 'Hello'], ['a', 'b'], ['a', 'b']]

# ////
xs = [[1] * 4] * 3

# xs == [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]] 

# ////
xs[0][0] = 5
# xs == [[5, 1, 1, 1], [5, 1, 1, 1], [5, 1, 1, 1]]  

# /////////
# تکرار کردن در لیست های تودرتو

[[1]*4 for _ in range(3)]
print([[1]*4 for _ in range(3)])
# [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

# //////////
# مشکل ایجاد یه متد روی لیست تک خطی
# این را خطا میده
from statistics import mean
my_list=mean[float (i) for i in input().split()]
# ولی اینو درست میده
my_list=mean([float (i) for i in input().split()])

# /////////////



# ساخت یک  رشته  بطوریکه عنصر اول با عنصر اخر لیست دوم یکی بشه
# و  نان را حساب نکنه
# مقایسه دو لیست در حلقه
# “An apple a day keeps the doctor away”

list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']

def merge_list(list1, list2):
    resultant_data = []
    list2.reverse()
    # اینجا لیست را برعکس میکنه
    # بعد دو حلقه را با هم زیپ میکنه
    # اشاره ای و جی به ترتیب برای حلقه اول و دوم است که حلقه بیاد بگرده درون  اعضای اونها
    for i,j in zip(range(0, len(list1)), range(0, len(list2))):
        if list2[j] is not None:
            s = list1[i]+list2[j]
        else:
            s = list1[i]
        resultant_data.append(str(s))

    return ' '.join(resultant_data)

# ازمون کردن خروجی
#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
# “An apple a day keeps the doctor away”

# ///////

# تبدیل رندوم دو لیست به یک دیکشنری 
# بطوریکه عضو یکی بشه کلید و عضو یاعضو های دیگر بشه ولیو
# کد مرتب:
# https://stackoverflow.com/questions/40298116/python-how-to-merge-two-lists-into-a-dictionary-in-a-total-random-order

# ساخت یک دیکشنری از دو لیست




# میاد اعضای یه لیست را ترتیبشونو بهم میزنه هر بار یه چیز میده
from random import shuffle
import random
A = ['SW1', 'SW2', 'SW3', 'SW4']
B = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']
def randomize_to_dictionary(a, b):
    # اینجا یه کپی از لیست اول و دوم میگیره
    # این چه معنی داره؟
    copy_a = a[:]
    copy_b = b[:]

    print(copy_a)
    print(copy_b)
    
# ['SW1', 'SW2', 'SW3', 'SW4']
# ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']
    
    # اینجا میاد شافل میکنه که ترتیب را هر بار  بهم بزنه
    random.shuffle(copy_a)
    random.shuffle(copy_b)
    print(copy_a)
    print(copy_b)
    
# این دو نمونه هر بار تغیر میکنند فقط میخواستم ترتیب بهم ریختگی را نشون بدم
# ['SW4', 'SW3', 'SW2', 'SW1']
# ['N4', 'N6', 'N7', 'N1', 'N2', 'N3', 'N5'] 
   
    # اینجا تعداد اعضای هر لیست را میشماره
    length_a = len(copy_a)
    length_b = len(copy_b)
    print(length_a)  #4
    print(length_b)  #7

    # یه دیکشنری خالی تعریف میکنه
    dictionary = {}

    # اغاز را برابر با صفر میزاره اول که بعد تغیر بده
    start = 0
    # بعد اعضای لیست را با ایندکس و عضو در حلقه میزنه
    # کاربرد متد انومریت در لیست
    for index, key in enumerate(copy_a):
       
        # اینجا میاد به ترتیب ایندکس ها را میاره و عضو را جلوش میاره در متد انومریت
# این نمونه هر بار تغیر میکننه
# 0 SW4
# 1 SW3
# 2 SW2
# 3 SW1
# پایان را منفی یک میکنه اول
        end = -1
        print('end is ',end ,'and start is ',start)
        # در هر بار حلقه دوباره منفی یک میکنش از اول
        # هرچند بعد که رندوم شد 
        # جلوتر اند میشه چیزی که بریزه توی استارت
        # اگر ایندکسه کوچکتر از تعداد طول منهای یک بود
        # دفعه اول ایندکس صفره و طول هم ۴ هست که منهای یک میشه سه
        # پس کار رو میبره جلو
        # چرا این کار را میکنه؟ یعنی ایندکس را معیار میگیره؟؟؟؟؟؟
        # چرا طول آ را یکی کم میکنه
                # اما چرا منفی یک ؟؟؟؟؟؟؟؟؟

            # چرا بازه را اینجوری تعریف میکنه؟
        print('index < length_a - 1 IS ' ,(index < length_a - 1) )
        if index < length_a - 1:
            print('lenght_a -1 is',length_a - 1)
            # این ایندکس و تعداد ثابته
            # مساله اون شافل کردنشونه که جابجا میکنشون
            # متد رندوم بین دو بازه یک عدد میده
            # دوباره بین  اغاز  به علاوه ۱ که میشه ۱
            # بعد اونم میشه ۳ که از ۳ تا ۱ را اند میده
            end = random.randint(start + 1, length_b - (length_a - index))
            
            print('length_b is ',length_b)
            print('length_a is ',length_a)
            print('index is ',index)
            print('length_a - index ',length_a-index)
            print('length_b - (length_a - index) ',length_b - (length_a - index))
            
            
            print('start +1 ',start + 1)
            print('end is',end)
    # ساخت دیکشنری از دو لیست
    # sw3 را اول میده
    #  بود میزاره کلید دیکشنری  
    # مثلا عنصر  صفر که 
    # استارت  است 
    # n1
    # تا اند که شد ۱ 
    # که چون برش را یکی قبل حساب میکنه پیش از ۱ میشه صفر 
    # پس همون عنر 
    # n1
    # فقط میشه 
    # اگر اند را مثلا ۲ میزاشت میشد 
    # n1 ,n7
    
    # برش زده را برابر ولیو قرار میده

    # استارت شده بود ۱ که میشه  
    # n4
    # اند هم شده بود ۱ که میشه همون ان ۴
    # پس میزنه
        dictionary[key] = copy_b[start:end]
        # اینجا کلید را از 
        # sw
        # برمیداره ولی ولیو اونرا که ریخته بود توی کلیده 
        # که  در دیکشنری سازی این همون کار را میکنه
        # دو عنصر را میاره
        # مثلا چون دفعه اول استارت شده بود یک میره عنصر یک شافل را میاره
        print('dictionary key is', key)
        print('copy_b[start:end] is', copy_b[start:end])
        print('dictionary[key] is',dictionary[key])
        print('dictionary is',dictionary)

        
        print('start is ',start , 'end is',end)
        # بعد اند را میریزه توی استارت که دفعه بعد از اون اغاز کنه
        # اینجا اند شد ۱ که یعنی استارت را از ۱ اغاز کنه 
        # یعنی از n7
        start = end
        print(' now start is ',start , 'end is',end)
    # dictionary is {'SW4': ['N2', 'N4', 'N5'], 'SW3': ['N7'], 'SW1': ['N6'], 'SW2': ['N1']}
    return dictionary

print(randomize_to_dictionary(A, B))

randomize_to_dictionary(A,B)


# ['SW1', 'SW2', 'SW3', 'SW4']
# ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']
# ['SW3', 'SW1', 'SW2', 'SW4']
# ['N1', 'N7', 'N3', 'N5', 'N6', 'N2', 'N4']
# 4
# 7
# end is  -1 and start is  0
# index < length_a - 1 IS  True
# lenght_a -1 is 3
# length_b is  7
# length_a is  4
# index is  0
# length_a - index  4
# length_b - (length_a - index)  3
# start +1  1
# end is 1
# dictionary key is SW3
# copy_b[start:end] is ['N1']
# dictionary[key] is ['N1']
# dictionary is {'SW3': ['N1']}
# start is  0 end is 1
#  now start is  1 end is 1
# end is  -1 and start is  1
# index < length_a - 1 IS  True
# lenght_a -1 is 3
# length_b is  7
# length_a is  4
# index is  1
# length_a - index  3
# length_b - (length_a - index)  4
# start +1  2
# end is 2
# dictionary key is SW1
# copy_b[start:end] is ['N7']
# dictionary[key] is ['N7']
# dictionary is {'SW3': ['N1'], 'SW1': ['N7']}
# start is  1 end is 2
#  now start is  2 end is 2
# end is  -1 and start is  2
# index < length_a - 1 IS  True
# lenght_a -1 is 3
# length_b is  7
# length_a is  4
# index is  2
# length_a - index  2
# length_b - (length_a - index)  5
# start +1  3
# end is 5
# dictionary key is SW2
# copy_b[start:end] is ['N3', 'N5', 'N6']
# dictionary[key] is ['N3', 'N5', 'N6']
# dictionary is {'SW3': ['N1'], 'SW1': ['N7'], 'SW2': ['N3', 'N5', 'N6']}
# start is  2 end is 5
#  now start is  5 end is 5
# end is  -1 and start is  5
# index < length_a - 1 IS  False
# dictionary key is SW4
# copy_b[start:end] is ['N2']
# dictionary[key] is ['N2']
# dictionary is {'SW3': ['N1'], 'SW1': ['N7'], 'SW2': ['N3', 'N5', 'N6'], 'SW4': ['N2']}
# start is  5 end is -1
#  now start is  -1 end is -1
# {'SW3': ['N1'], 'SW1': ['N7'], 'SW2': ['N3', 'N5', 'N6'], 'SW4': ['N2']}
# ['SW1', 'SW2', 'SW3', 'SW4']
# ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']
# ['SW1', 'SW4', 'SW3', 'SW2']
# ['N1', 'N4', 'N3', 'N6', 'N7', 'N5', 'N2']
# 4
# 7
# end is  -1 and start is  0
# index < length_a - 1 IS  True
# lenght_a -1 is 3
# length_b is  7
# length_a is  4
# index is  0
# length_a - index  4
# length_b - (length_a - index)  3
# start +1  1
# end is 1
# dictionary key is SW1
# copy_b[start:end] is ['N1']
# dictionary[key] is ['N1']
# dictionary is {'SW1': ['N1']}
# start is  0 end is 1
#  now start is  1 end is 1
# end is  -1 and start is  1
# index < length_a - 1 IS  True
# lenght_a -1 is 3
# length_b is  7
# length_a is  4
# index is  1
# length_a - index  3
# length_b - (length_a - index)  4
# start +1  2
# end is 3
# dictionary key is SW4
# copy_b[start:end] is ['N4', 'N3']
# dictionary[key] is ['N4', 'N3']
# dictionary is {'SW1': ['N1'], 'SW4': ['N4', 'N3']}
# start is  1 end is 3
#  now start is  3 end is 3
# end is  -1 and start is  3
# index < length_a - 1 IS  True
# lenght_a -1 is 3
# length_b is  7
# length_a is  4
# index is  2
# length_a - index  2
# length_b - (length_a - index)  5
# start +1  4
# end is 4
# dictionary key is SW3
# copy_b[start:end] is ['N6']
# dictionary[key] is ['N6']
# dictionary is {'SW1': ['N1'], 'SW4': ['N4', 'N3'], 'SW3': ['N6']}
# start is  3 end is 4
#  now start is  4 end is 4
# end is  -1 and start is  4
# index < length_a - 1 IS  False
# dictionary key is SW2
# copy_b[start:end] is ['N7', 'N5']
# dictionary[key] is ['N7', 'N5']
# dictionary is {'SW1': ['N1'], 'SW4': ['N4', 'N3'], 'SW3': ['N6'], 'SW2': ['N7', 'N5']}
# start is  4 end is -1
#  now start is  -1 end is -1

# ////
# ساخت دو لیست  بطور تصادفی از اعضای دو لیست
# ساخت دو لیست از اعضای یک لیست
# انتخاب تصادفی اعضای یک لیست
# جمع اعضای یک لیست
A = ["A1","A2","A3","A4"]
B = ["101","102","103","104"]
print(A+B)
# ['A1', 'A2', 'A3', 'A4', '101', '102', '103', '104']
P1=sample(A+B ,4)
print(P1)
# ['102', 'A1', '103', '101']
# حالا اگر بخوایم  به اندازه برابر بریزیم توی  دو تا لیست
# کد بالا میاد دوباره از اول میاره
my2=list(filter(lambda x: x  not in P1 , A+B))
print(my2)
# ['A2', 'A3', 'A4', '104']

# لیست اصلی این بود
['A1', 'A2', 'A3', 'A4', '101', '102', '103', '104']

# پس  دو لیست ما این میشه
['102', 'A1', '103', '101']
['A2', 'A3', 'A4', '104']

# البته تیکه دوم کد را هم میشه اینجوری نوشت
new_list = []

for x in A+B:
    if x not in P1:
        new_list.append(x)
        
P2 = random.sample(new_list, 4)

# /////

# تقسیم یک لیست به سه لیست با تعداد برابر
# راه ۱
listt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

sample = random.sample(listt, 5 * 3)
sample[0:5]
['h', 'm', 'i', 'k', 'd']
sample[5:10]
['a', 'b', 'o', 'j', 'n']
sample[10:15]
['c', 'l', 'f', 'e', 'g']

# ////
# زیپ کردن لیست تودرتو
# این کد به ازای هر عنصر در لیست اول کل لیست تودرتوی دوم 
# را میاره
assignment = ['Title', 'Project1', 'Project2', 'Project3']
grades = [ ['Jim', 45, 50, 55], \
           ['Joe', 55, 50, 45], \
           ['Pat', 55, 60, 65] ]
print(list(zip(assignment,grades)))
# [('Title', ['Jim', 45, 50, 55]), ('Project1', ['Joe', 55, 50, 45]), ('Project2', ['Pat', 55, 60, 65])]


////
# زیپ کردن لیست تودرتو
# این کد به ازای هر عنصر اول لیست تودرتو را باز میکنه و همه را در یک تاپل میزاره
# همه عنصر های اول  حتی اگر داخل یه لیست باشند  
# را میاره
# استار
# انپک میکنه لیست تودرتو را
assignment = ['Title', 'Project1', 'Project2', 'Project3']
grades = [ ['Jim', 45, 50, 55], \
           ['Joe', 55, 50, 45], \
           ['Pat', 55, 60, 65] ]
print(list(zip(assignment,*grades)))
# [('Title', 'Jim', 'Joe', 'Pat'), ('Project1', 45, 55, 55), ('Project2', 50, 50, 60), ('Project3', 55, 45, 65)]

# ///////
# اینم فقط اولی را انپک میکنه
assignment = ['Title', 'Project1', 'Project2', 'Project3']
grades = [ ['Jim', 45, 50, 55], \
           ['Joe', 55, 50, 45], \
           ['Pat', 55, 60, 65] ]
print(list(zip(*assignment,grades)))
# [('T', 'P', 'P', 'P', ['Jim', 45, 50, 55]), ('i', 'r', 'r', 'r', ['Joe', 55, 50, 45]), ('t', 'o', 'o', 'o', ['Pat', 55, 60, 65])]

# ///
# انپک کردن
# آنپک کردن لیستی که عنصر های اول باشه ولی یکیشون عنصر اخر  تودرتو هستش

a = [['a', '0', 'b', 'f', '78']]
b = [['3', 'w', 'hh', '12', '8']]
c = [['g', '7', '1', 'a0', '9'], ['45', '4', 'fe', 'h', 'k']]

import itertools
z = list(zip(*itertools.chain(a, b, c)))
print(z)
# [('a', '3', 'g', '45'), ('0', 'w', '7', '4'), ('b', 'hh', '1', 'fe'), ('f', '12', 'a0', 'h'), ('78', '8', '9', 'k')]
#
# ///////
# بدون استار همون کد
a = [['a', '0', 'b', 'f', '78']]
b = [['3', 'w', 'hh', '12', '8']]
c = [['g', '7', '1', 'a0', '9'], ['45', '4', 'fe', 'h', 'k']]

import itertools

z = list(zip(itertools.chain(a, b, c)))
print(z)
# [(['a', '0', 'b', 'f', '78'],), (['3', 'w', 'hh', '12', '8'],), (['g', '7', '1', 'a0', '9'],), (['45', '4', 'fe', 'h', 'k'],)]
# //

# به ترتیب
# سورت کردن لیستی از تاپل ها
# سورت کردن لیست تودرتو
# سورت کردن لیست با عنصر دوم
[('abc', 121),('abc', 231),('abc', 148), ('abc',221)]
sorted(
    [('abc', 121), ('abc', 231), ('abc', 148), ('abc', 221)],
    key=lambda x: x[1] , reverse=False

)
# حالا اگر بخوایم برعکس از بزرگ به کوچک چاپ کنه فالس را میزنیم ترو
# پیشفرض هم خودش فالس است یعنی از کوچک به بزرگ میاره

# حالا اگر شرط بزاریم یعنی اگر شرط اول برابر شد بره سراغ عنصر دومی مثلا وزن

# سورت کردن با شرط
# سورت کردن با چند شرط
def biggest_height(anycursor):
    best=sorted(anycursor,key= lambda x:(x[3], x[2]) ,reverse=True )
    print(best)

# که اینجا در صورت برابری طبق بعدی سورت میکنه
# [(2, 'Mahdi', 90, 190),
# (1, 'Amin', 75, 180),
# (3, 'Mohammad', 75, 175)]
# (4, 'Ahmad', 60, 175),


# /////
# سورت کردن برعکس
# منفی لامبدا
# حالا اگر بخوایم بعدی را برعکس بیاره یعنی طبق کوچک به بزرگ کافیه قبلش یه منفی بزاری

def biggest_height(anycursor):
    best=sorted(anycursor,key= lambda x:(x[3], -x[2]) ,reverse=True )
    print(best)
# [(2, 'Mahdi', 90, 190),
# (1, 'Amin', 75, 180),
# (4, 'Ahmad', 60, 175),
# (3, 'Mohammad', 75, 175)]



# /////////
# سورت کردن اول طبق بزگری و پس از اون مثلا طبق طول و ....
sorted_by_length = sorted(list_,
                         key=lambda x: (x[0], len(x[1]), float(x[1])))


# چاپ برعکس با منفی بدون ریورس
def biggest_height(anycursor):
    best=sorted(anycursor,key= lambda x:-x[3]  )
    for char in best:
        print (char[1],char[3],char[2])
biggest_height(mycursor)

# اگر منفی نداشت
# Mohammad 175 75
# Ahmad 175 60
# Amin 180 75
# Mahdi 190 90


# حالا که منفی داره یعنی برعکس
# Mahdi 190 90
# Amin 180 75
# Mohammad 175 75
# Ahmad 175 60
# //////
# کار با یک لیست تودرتو
# لیست اصلی را به اعضاش تقسیم میکنه
# جدا کردن عناصر درون رشته‌ی اول
new=[['گوشی موبايل سامسونگ مدل گلکسی A32 4G دو سیم کارت - ظرفیت 128 گیگابایت - رم 6 گیگابایت', '10,495,000تومان', '128', '6.4', '64', '5000'], ['گوشی موبايل سامسونگ مدل گلکسی A32 4G دو سیم کارت - ظرفیت 128 گیگابایت - رم 6 گیگابایت', '10,495,000تومان', '128', '6.4', '64', '5000'], ['گوشی موبایل شیائومی Redmi Note 11 ظرفیت 128 گیگابایت - رم 6 گیگابایت', '8,729,000تومان', '128', '6.43', '50', '5000']]
second_new = []
for item in new:
    # جدا کردن عناصر درون رشته‌ی اول
    # چون specs چندتا داره تقسیم میشه
    # اینجا سه تا عنصر داره ایتم دونه دونه درون لیست های جدا میریزه
    product, price, *specs = item
    # جایگزینی کاراکترهای خاص با کاما
    product = product.replace(' - ', ',').replace(' مدل ', ',').replace(' دو سیم کارت ', ',').replace(' 4G ', ',')
    # اضافه کردن عناصر به لیست دومی
    second_new.append([product, *specs, price])
print(second_new)
# [['گوشی موبايل سامسونگ,گلکسی A32,دو سیم کارت,ظرفیت 128 گیگابایت,رم 6 گیگابایت', '128', '6.4', '64', '5000', '10,495,000تومان'], ['گوشی موبايل سامسونگ,گلکسی A32,دو سیم کارت,ظرفیت 128 گیگابایت,رم 6 گیگابایت', '128', '6.4', '64', '5000', '10,495,000تومان'], ['گوشی موبایل شیائومی Redmi Note 11 ظرفیت 128 گیگابایت,رم 6 گیگابایت', '128', '6.43', '50', '5000', '8,729,000تومان']]

# /////////////////
# تقسیم یه لیست تودرتو به اجزاش



# /////////

# لیست کامپر هنشن حلقه تو  در تو با حلقه معمولی 
# لیست سه بعدی 
# لیست تو در تو

all_forms= list(list(zip(r, p)) for (r, p) in (zip    (repeat(player1_payoff), permutations(player2_payoff))  ))
    permuted=[]
    for char in all_forms:
        my_char=[]
        for sub_char in char:
            my_char.append(list(sub_char))
        permuted.append(my_char)
    return (permuted)
Forms(player_1,player_2)


# این همونو میده 
all_forms= list(list(zip(r, p)) for (r, p) in (zip    (repeat(player1_payoff), permutations(player2_payoff))  ))
    permuted=[ [[sub_char]for sub_char in char ] for char in all_forms]
    return (permuted)
Forms(player_1,player_2)

# خروجی شبیه اینه برای هر دو
# [[[(1, 1)], [(2, 2)], [(3, 3)], [(4, 4)]],
#  [[(1, 1)], [(2, 2)], [(3, 4)], [(4, 3)]],
#  [[(1, 1)], [(2, 3)], [(3, 2)], [(4, 4)]],
#  [[(1, 1)], [(2, 3)], [(3, 4)], [(4, 2)]],
#  [[(1, 1)], [(2, 4)], [(3, 2)], [(4, 3)]],
#  [[(1, 1)], [(2, 4)], [(3, 3)], [(4, 2)]]]

# مساله اینه که نتونستم تاپل داخل را به لیست تبدیل کنم ولی با بالاییه میشه


# ///////
# برگردوندن به شکل پیامد بازیکن ها  
list (zip(*my))
# [(-2, -3, -2, -4), (0, -3, -2, -1)]


