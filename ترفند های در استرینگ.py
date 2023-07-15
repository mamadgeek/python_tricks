
# تابع هایی که میشه روی استرینگ انجام بشه را میگه
dir(string)
dir(name_of_string)
# //////////////

# کمک اون تابع را میده
print(help(str.count))

///////
# افزون و ریختن توی خودش. یه علاوه مساوی
# mamad namjoo

name = 'mamad'
name+= ' namjoo'
print(name)

# //////
# فرمت دهی با ٪
name = 'mamad'
print('hello %s ' % name)

# حتی فرمت دهی عدد و قاطی 
# hello mamad midini 31 et shode
name = 'mamad'
sen=31
print('hello %s midini %i et shode' % (name, sen))

# فرمت دهی با اف استرینگ
# hello mamad midini 31 et shode
name = 'mamad'
sen=31
print(f'hello {name} midini {sen} et shode')

# //////
# تعین  نمایش چند رقم اعشار 
# اف استرینگ
# decimal
import math , decimal
a=(math.sqrt(3.5))

# print(a)
# 1.8708286933869707

# تعین تعداد اعشار با 
# اف استرینگ  f''
print("%f" %a)
# 1.870829

# رند به بالا
print("%.f" %a)
# 2

# تا دو رقم اعشار
print("%.2f" %a)
# 1.87
# ////////////////////////////
# این میگه کلش ۹ رقم باشه و ۲ رقم اعشار باشه
# اگر نداشت خالی میده خودش
print("%9.2f" %a)
#      1.87

# //////
# استرینگ و نه فلوت
print("%10s" %a)
# این یعنی هر اسمم ۱۰ تا جا بگیره 
# که اگر کمتر بود اسپیس میزاره

# توجه به روش دیگر نوشتن جادی در فایل ۵.۳ مقدماتی بود
# در یک راستا قرار دادن همه . مرتب تحویل پرینت ادن


from re import sub
from decimal import Decimal

money = '$6,150,593.22'
value = Decimal(sub(r'[^\d.]', '', money))
# 6150593.22

# /////////
    # پس پس از اف استرینگ کردن خودش استرینگ میکنه

    my_list=[4,1,2,19,100]
    # حالا میخوام تابع جذر را روی هر کدوم از کاراکتر ها اجرا کنم و سپس  تا ۴ رقم تحویل بدم
    mylis= list((map(sqrt,my_list)))
    print(mylis)
    # [2.0, 1.0, 1.4142135623730951, 4.358898943540674, 10.0]

    
    my2= [ ('%.4f'%char) for char in mylis]
    # ['2.0000', '1.0000', '1.4142', '4.3589', '10.0000']

    # جالبه که در لیست تک خطی خودش پرینت هم میده نیازی نیست بنویسی پرینت 
    # اگر هم بنویسی نان میزنه
    my2= [ print('%.4f'%char) for char in mylis]
    # ['None','None','None','None','None',]
    
    # و اگر فلوت کنی  دوباره یک رقم بر میگرددونه
    my2= [ float('%.4f'%char) for char in mylis]
    # [2.0, 1.0, 1.4142, 4.3589, 10.0]
    
# ////////////
# برای گفت اورد اوردن این کار را باید کرد
# برای پرینت های حرفه ای هم این کار را می کنیم
print('mohammad said: "hello darling"')

# ////
# یا این روش هم میشه بک اسلش
# mohammad said: 'hello darling'
print('mohammad said: \'hello darling\'')

# ////////////
print("i'm going to be \"adopted\"")
# i'm going to be "adopted"
# /////

# برای اینکه استرینگ در خط بعدی چاپ کنه
# mohammad said:
#  hello darling
print('mohammad said: \n hello darling')



# ///////


# /////

# چسبودندن دو تا استرینگ
# mamadnamjoo
name = 'mamad'
family = 'namjoo'
print(name+family)

/////////

# ////////
# برای گذاشت فاصله
mamad namjoo
name = 'mamad'
family = 'namjoo'
print(name+' '+family)

# /////
# میشه  متغیر گذاشت کنار استرینگ ها 
name = 'mamad'
family = 'namjoo'
print('mamad'+' '+family)


# /////
# /n میاد اینجوری مینویسه پاییش میزنه
List = ['Geeks', 4, 'geeks !']
print("\nOriginal List:\n", List)
# Original List:
# ['Geeks', 4, 'geeks !']

# /////
# فرمت ها  که چه کارهایی میشه کرد را نشون میده

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
# 'translate', 'upper', 'zfill']
name = 'mamad'
sen=31
print(dir(name))

# ////
# بررسی میکنه که ایا یه زیر  مجموعه در اون رشته هست یا خیر
str1 = "Delftstack"
str2 = "Del"
val = str1.__contains__(str2)
print(val)
# True



# //////

# ظاهرا فقط همون جمع میکنه دو استرینگ را
# 30
# 30
n1 = 10
n2 = 20
print(n1 + n2)
print(n1.__add__(n2))

# ////////

# متد 
#  __delattr__(self, name)
#  روی کلاس ها کار میکنه 

# //////////
# برعکس تایتل را انچام میده
# کوچک باشه بزرگ میکنه
# hello, and welcome to my world
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


# تایتل:
# میاد هر واژه را فقط اولشونو بزرگ و کپیتالایز میکنه

txt = "hello, and welcome to my World!"
x = txt.title()
print(x)
# Hello, And Welcome To My World!



# //////////////////////
# اون حرف را میندازه وسط با گرفتن ۲۰ کاراکتر

    #   .banana.
txt = ".banana."
x = txt.center(20)
print(x)

# ///////


# OOOOOOObananaOOOOOOO
txt = "banana"
x = txt.center(20, "O")
print(x)



# /////////////////
# انکود میکنه و اگر انکودی داده نشه utf8 میکنه 
# انگود هم ظاهرا رمز گذاری است که از یه فرمت به فرمت دیگر وارد بشه
# b'My name is St\xc3\xa5le'
txt = "My name is Ståle"
x = txt.encode()
print(x)

# ///////////
# اندازه تبسایز را به اسپیس خالی برمیگردونه
# H e l l o
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)


# ///////////

# H       e       l       l       o
# H       e       l       l       o
# H e l l o
# H   e   l   l   o
# H         e         l         l         o
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# /////////////
# اولین کاراکتر را میگه کی رخ داده در ایندکس چند
# 7
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# ////////


# بین دو تا پوزیشن ۵ و ۱۰ میتونه پیدا کنه چندمین بوده
# 8
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

# ///////////////


# اخرین رخ داد  را پیدا میکنه نخستین واژه را
# 12
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)


# ///////////////
# برمیگردونه طول ۲۰ کاراکتر را و بنانا را قرار میده 

# banana               is my favorite fruit.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# ///////////////



# bananaOOOOOOOOOOOOOO
txt = "banana"
x = txt.ljust(20, "O")
print(x)

# ///////////////

# طبق جایگزین کاراکتر ها را ترجمه میکنه
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


# ///////////////
# جایگزینی میکنه . ترجمه میکنه . پی ها را با اس ها

# Hello PamP!
txt = "Hello SamS!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# ///////////////


# تبدیل تاپل ای از استرینگ میکنه . اون کلمه را . قبلیشو و بعدیشو
# ('I could eat ', 'bananas', ' all day')
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# ///////////////

# تبدیل فرمت میکنه 
# For only 49.00 dollars!
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# We have 5.000000e+00 chickens.
txt = "We have {:e} chickens."
print(txt.format(5))


# سایر فرمت ها:
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%      Percentage format


# ///////////////////////////

# blibbbbekonbrtes
sentence='alibabaekonartes'
print(sentence.replace('a', 'b'))
# /////////////
entereance = 'ideoAufghji'
# dfgh
# sub= 'e' or 'a' or 'o' or 'u' or 'i'
ent2=entereance.replace('e' and 'i','.' )
print(ent2)
# از لحاظ سینتکس کار میکنه ولی از لحاظ کارایی کار نمیکنه
# .deoAufghj.
# ////////
# 
# به مشکل جایگزینی:
# alibabaekonartes.
sentence='alibabaekonartesu'
sen=sentence.replace('a', '.')
sen=sentence.replace('e', '.')
sen=sentence.replace('i', '.')
sen=sentence.replace('o', '.')
sen=sentence.replace('u', '.')
print(sen)



# اینکه بعد از هر بار متغیر جدید را عملیات روش اجرا کنه مه متغیر اولی را
# .l.b.b..k.n.rt.s
sentence='alibabaekonartesu'
sen=sentence.replace('a', '.')
sen1=sen.replace('e', '.')
sen2=sen1.replace('i', '.')
sen3=sen2.replace('o', '.')
sen4=sen3.replace('u', '.')
print(sen4)


# /////////

print()

# //////////
# تعداد را میشماره
# 5
sentence=('dorod')
print(len(sentence))

# /////////
# عنصر دومی را میده
# r
sentence=('dorod')
print(sentence[2])

# /////
# از شروع تا ۲ 
# do
sentence=('dorod')
print(sentence[0:2])


# ////////
# برش از  دومی تا اخر
# rod
sentence=('dorod')
print(sentence[2:])

# برش های پیچیده تر:
#یه حرف که پیدا کرد از اون به بعد را برش بزنه

# از اون چیزی که پیدا کرد برش میزنه
sentence=('dohrod')
# خود حرفه را میاره از
print(sentence[sentence.find('h'):])
# hrod

# از پس از اون حرفه میاره
print(sentence[sentence.find('h')+1:])
# rod


# پیش از اون حرفو برش میزنه
print(sentence[:sentence.find('h')])
# do

# //////
# دوتا دوتا از سومین عنصر  برش میزنه کنار هم میزاره
# rd
sentence=('dorod')
print(sentence[2::2])

# 
# عنصر اخر را بهمون میده 
# d
sentence=('dorod')
print(sentence[-1])


# /////
# از شروع تا -۱
# doro
sentence=('dorod')
print(sentence[:-1])

# ////
# اسم مستعار گذاشتن. الیاسینگ

# bedrod
# bedrod

sentence=('dorod')
sentence2=('bedrod')
sentence1= sentence2
print(sentence1)
print(sentence2)

# ////
# تبدلی به اینتیجر 
# متغیر تبدیل نمیشه باید اون سمت راستی را تبدیل کنی
enterance =('3 6 9')
int(ent2)= enterance.split()
print(ent2)
# ['3', '6', '9']

# /////////////
# برعکس از اخر چاپ میکنه
# عنصر اخر را نمیاره
# ahdoro
sentence=('dorodha')
print(sentence[:0:-1])

sentence=('dorodha')
print(sentence[:2:-1])
# ahdo

#  کلا برعکس میکنه
txt = "Hello World"[::-1]
print(txt)
# dlroW olleH
# ///////
# اینم به یه روش دیگه برعکس میکنه
reversed_num = "".join(reversed(num_string))
# ////////////
# از اونجایی که ایمیوتبل هست باید برای تغیر در متغیر دیگر ریخت
# Morodha
sentence=('dorodha')
gomleh='M'+sentence[1:]
print(gomleh)

# حتی توی خودش ریخت
# Morodha
sentence=('dorodha')
sentence='M'+sentence[1:]
print(sentence)

# ////
# متد بزرگ کردن 
# DOROD
sentence=('dorod')
print(sentence.upper())

#  کوچک کردن
sentence=('dorRod')
print(sentence.lower())


# ///////////
# کاربرد توابع درونی با تعریف تابع بیرونی
# جالبه هر بار که میخوای یه چیزی را کوچک کنی درون یه تابع باید بریزی توی یه چیز تازه . هرچند به همون اسم پیشین
# وگرنه کاری نمیکنه روش

def smalize (xapital_word):
    xapital_word.lower()
    return xapital_word
# خروجی:
# .D.f.G.l.K.s

def smalize (xapital_word):
    xapital_word=xapital_word.lower()
    return xapital_word
# خروجی:
# .d.f.g.l.k.s
# //////////
#  یه حرف  خاص چندبار بکار رفته
# میشماره
# 2
sentence=('dorod')
print(sentence.count('d'))

# //////////

# عنصر چندمه؟
# 0
sentence=('dorod')
print(sentence.find('d'))
# ///////////
# دوطرف را میاره کم میکنه

# dorod
sentence=('    dorod  ')
print(sentence.strip())


# ///////////

# True
sentence=('dorod')
print(sentence.startswith('d'))

# /////////
# تبدیل استرینگ به لیست
# تبدیل یه جمله یا کلمه به لیست . 
# ['this', 'is', 'a', 'hero', 'here']
name = ' this is a hero here'
print(name.split())

# ///////
# راه دیگه سورتت هستش


# ////
# میشه بگیم هر جا یه کلمه خاص بود ببریم
# [' thi', ' i', ' a hero here']
name = ' this is a hero here'
print(name.split('s'))

# /////////
# تبدیل لیست به استرینگ
# برگردوندن یک لیست استرینگی به یه استرینگ  . برعکس اسپلیت
# this-is-a-hero-here
name2= ['this', 'is', 'a', 'hero', 'here']
name3= (('-').join(name2))
print(name3)
# this-is-a-hero-here
# //////////
# برای اجرای یک متد جوین روی یه استرینگ میشه این کار را کرد
a='sdfghjklrtyrty'
for char3 in [a]:
    a=('.').join(char3)
print(a+'.')
# s.d.f.g.h.j.k.l.r.t.y.r.t.y
# /////////
# ترکیب دو تابع درونی با هم مانند جوین و ریورسد
reverse = 'mehdibabam'
print( '.'.join((reversed(reverse))))
# m.a.b.a.b.i.d.h.e.m

# //////////////////////////
# ترکیب اسپلیت و جوین

print(self.history) #1995/02/03
self.history =''.join(history.split('/')) #19950203

# ////////
# تبدیل تاپل به استرینگ
# John#Peter#Vicky
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


# //////
# ترکیب کردن دو تا متغیر با هم 

# True
sentence=('dorod')
print(sentence.upper().startswith('D'))



# ////
# این برنامه میبینه که اگر هر کدام از این حروف در این جمله بودند  هر کدام از ای ها را به علاوه ای دیگری میکنه .add()#  
# اما چجوری فقط همون ای را بهش اشاره کنم که اون عنصر را داره؟
# sentence=('dorod')
# for i in sentence:
#     if i== "a" or "e" or "i" "o" or "u":
#         print (i+i)
#     else:
#         print('no')

# //////////

# d
# o
# r
# o
# d
sentence=('dorod')
# input(' give me the sentence')
for i in range (0, len (sentence)):
    print(sentence[i])

# //////
# d
# o
# r
# o
# d
sentence=('dorod')
for i in sentence:
    print(i)


# //////
# 0 d
# 1 o
# 2 r
# 3 o
# 4 d
sentence=('dorod')
for i in range(0,len(sentence)):
    print(i ,sentence[i])
# //////
#  از دومی برش میزنه در حلقه
# 2 r
# 3 o
# 4 d
sentence=('dorod')
for i in range(2,len(sentence)):
    print(i ,sentence[i])

# /////////////
# میشماره چند تا الف داره اون رشته
# tedad hast  2
sentence=('dorod')
count = 0
for i in sentence:
    if i == 'o':
        count+=1
print('tedad hast ', count)

# /////////////

# میشماره چندتا ای داره تو جمله هه
# 7
sentence = ' go away asshloe am a promramer here . i can rule your life . '
count = 0
for character in sentence:
    if character=='a':
        count += 1
print(count)


# حالا با تابع هم میشه
# 7
print(sentence.count('a'))


print("////////////////////////")
# result 569
mRa = 569.34643865
print("result %1.0f" %mRa)

print("////////////////////////")
# حذف یک کاراکتر در همه جای استرینگ 
sentence=  "alibabaekonartes"
for i in sentence:
    if i == 'a' :
        set2= sentence.replace(i, '')
print(set2)
#  به روز کردن متغیر 
# حالااگر همون جمله را یک کاراکتر تازه بزنیم میاد 
# رو قبلیه میریزه پس باید جدیده را روی قبلی بریزیم:
    elif i =='e':
        set2= sentence.replace(i, '')
        sentence=set2
        
print("////////////////////////")
# این سینتکس هم میشه کار کنه در جایگزینی
        del_word=del_word.replace(xhar,('.'+xhar))
# یعنی پیش از هر حرف یه نقطه بزن همون حرف را بیار

# /////////
# با وجود میوتبل بودن میشه با همون نام  نام تازه را
entereance = 'ideoAufghji'
entereance= entereance.replace('o', '?')
print(entereance)
# ide?Aufghji

# //////////////
# جایگزینی در حلقه =
# تغیر یک استرینگ درون یک حلقه
# میخوام اگه ماندانا بود بنویسه ممد

# ['mandana', '5', '7', '3', '15', '', '', '', '', '', '', '', '', '', '', '']
# ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1']
# ['sina', '19', '10', '19', '6', '8', '14', '3', '', '', '', '', '', '', '', '']
# ['sara', '0', '5', '20', '14', '', '', '', '', '', '', '', '', '', '', '']
# ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7', '', '', '']
# ['ali', '1', '9', '', '', '', '', '', '', '', '', '', '', '', '', '']
# ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8', '', '', '', '', '', '', '']
# []
# []
# []
        for char in my_vorodi:
            # print(char[0:1]) # پرینت کار میکنه 
            # if char[0:1] ==['mandana']:
            for c in char[0:1]:
                print(c)
                # حالا چطور ماندانا را تغیر بدم به ممد یا....؟
                # یا چیزی را بررسی کنه ؟
                # بعد بریزه توی فایل تازه؟
                if c == 'mandana':
                    print('c is',c)  #c is mandana
                    c= c.replace(c, 'mamad')
                    print('c is',c)  #c is mamad
                    
                    # ولی مساله اینه که هنوز عوض نشده
                 #   چطور یک استرینگ را که درون یک لیست قرار دارد تغیر بدم ؟ 
                    # :این میتونه تغیر بده
                    if c == 'mandana':
                        print('c is',c)
                        char[0]='mamad'
                    # ['mamad', '5', '7', '3', '15', '', '', '', '', '', '', '', '', '', '', '']
                    # یا
                    if c == 'mandana':
                    char[0]=c.replace(c, 'mamad')
                    print('c is',c)
                    # ['mamad', '5', '7', '3', '15', '', '', '', '', '', '', '', '', '', '', '']
                    # ////////////////////

# حذف یک کاراکتر از درون لیست
char=['fdas','rfed','','','vfadc','']
            while (''in char):
                # print(True)
                char.remove('')
            MY.append(char)

# //////

# حذف یک کاراکتر خالی درون یک لیست
# در حلقه
# Python3 code to demonstrate
# removing empty strings
# using remove()
 
# initializing list
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]
 
# Printing original list
print("Original list is : " + str(test_list))
 
# using remove() to
# perform removal
while("" in test_list):
    test_list.remove("")
 
# Printing modified list
print("Modified list is : " + str(test_list))
# Original list is : ['', 'GeeksforGeeks', '', 'is', 'best', '']
# Modified list is : ['GeeksforGeeks', 'is', 'best']

# ///////////////
# روش دوم لامبدا و فیلتر
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]
 
# Printing original list
print("Original list is : " + str(test_list))
 
# using lambda function
# لامبدا هایی را میگه بیار که طول ایکسشون بزرگتر از صفر باشه 
# و چون کاراکتر خالی بزرگتر از صفر نیست فیلتر میشه
test_list = list(filter(lambda x: len(x) > 0, test_list))
 
# Printing modified list
print("Modified list is : " + str(test_list))
# Original list is : ['', 'GeeksforGeeks', '', 'is', 'best', '']
# Modified list is : ['GeeksforGeeks', 'is', 'best']

# ////////////
# نکته: اگر اعداد  را از اول بدیم اونرا جمع میکنه
# و بعد میریزه تو لیس ولی اگر اینپوت بگیریم جدا میکنه
# ورودی داده : 1+3+4+1
# خروجی:['1', '3', '4', '1']
teacher=str(input("give me the number:" ))
teach2= teacher.split('+')
print(teach2)
#  اما:
# جمع میکنه میریزه
# چرا ؟ و چطور باید ورودی ثابت را ریخت؟
# ['10']
teacher=str(1+2+4+3)
teach2= teacher.split('+')
print(teach2)

print("////////////////////////")
# برعکس میکنه که اگر بزرگ باشه کوچک و اگر کوچک باشه بزرگ میکنه

# GeeKSforGEEKS
string = "gEEksFORgeeks"
print(string.swapcase())

print("////////////////////////")
# یک کلمه را میگیره و مثل نوشتن اسم ها عمل میکنه.
# یعنی همه حروف را کوچک و اولی را بزرگ میکنه
# Geeksforgeeks
string = "gEEksFORgeeks"
print(string.capitalize())


print("////////////////////////")
# یک کلمه را پیدا میکنه در رشته
# فرقش با فایند اینه که فایند منفی ۱ بر میگردونه
# 5
txt = "Hello, welcome to my world."
x = txt.index("o")
print(x)

# بین بازه ۵ تا ۱۰ را میگرده میاره

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

# //////
# پیدا کردن
# find

vorodi='ABBA'
# اینو که تیکه هست پیدا نمیکنه درونش
# و در نتیجه هم درون شرط هم نمیره
# اما چرا؟
if vorodi.find('AB'):
    print('iaftam')
# هیچی نمیاره

print("////////////////////////")
# این کد میاد از اون حرف به بعد را میبره . تا اون حرف را دید میبره
# say hello sara: bnbmnhklk
# bnbmnhklk
# nbmnhklk
# mnhklk
# klk
geting = (input(' say hello sara: '))
for i in range(0,len(geting)):
    if(geting.find('h')):
        geting=geting[i:]
        print(geting)
        


# چرخیدن و اجرا روی استرینگ و پیاده کردن فایند نیاز 
# به لن داره و نمیشه با جستجوی ساده بیاد
# این ارور میده
# geting = (input(' say hello sara: '))
# for i in geting:
#     if(geting.find('h')):
#         geting=geting[i:]
#         print(geting)


print("////////////////////////")
# یه روش برش زدن با همون فایند میشه فقط ایندکس برمیگردونه 

# vorode= mmnmhdfdenmmn
# 4
# 8
print(vorodi)
x =vorodi.find('h')
print(x)
x_1 = vorodi.find('e', x+1)
print(x_1)


# ////////
# دوتایی هم بیاره حرف اولی که یافت را شماره کاراکترشو میاره
vorodi='bhello'
x =vorodi.find('he')
print(x)
# 1

# ولی اگر کل کاراکتر که بهش دادی را نداشته باشه میزنه -۱


print("////////////////////////")
# میشه برش زدن را بجای ایندکس متغیر و خود عملگر  و عمل راگزاشت
# بجای 
# vor[1:]
# یا
# vor[i:]
# میشه:
str = str[str.find("harfe morednazar")+1:]

print("////////////////////////")

vorodi = "ahhelllllOou"
print(vorodi)      #ahhellllloou
vorodi2 = vorodi[vorodi.find("h"):]   #hhelllllOou     این خود حرفو میاره 
vorodi3 = vorodi[vorodi.find("h")+1:]   #hellllloou   این از اون به بعد را میاره خود حرفی که پیدا کردن را نمیاره


print(getting[:getting.find('h')])    #a    این قبلشو میریزه


print("////////////////////////")
# پرسش: موقع برش زدن  چجوری متغیر جدید را تعریف کنم در اون جدیده که از اون به بعد را حساب کنه 
vorodi2 = vorodi[vorodi.find("h"):]   #hhelllllOou


print("////////////////////////")
# اضافه کردن یک حرف به رشته خالی دونه دونه
string = input("")
kalame= ""
if 'h' in string:
    #print ('peida kardam h ra')
    kalame = kalame + "h"

print("////////////////////////")
# برش زدن یکه رشته با لوپ
# P
# y
# t
# h
# o
# n
string_to_iterate = "Python Data Science"
for char in string_to_iterate[0 : 6 : 1]:
   print(char)


print("////////////////////////")
# با حلقه فور برعکس چاپ میکنه
# g
# n
# i
# n
# r
# a
# e
# L

string_to_iterate = " Learning"
for char in string_to_iterate[ :  : -1]:
   print(char)

# /////////
# با حلقه وایل برعکس چاپ میکنه

string_to_iterate = " Learning"
char_index = len(string_to_iterate) - 1
# یکی قبلش قرار میده یعنی ۹ کاراکتر هست هسشتا میزاره
# چون شمردن از صفر شروع میکنه و ولی طول را از یک  
# اگر نزاره در ارور ۹ تایی میده در بعد از خط وایل اوت او رنج
# (اما چرا؟)
while char_index >= 0:
    # به این دلیل میاد مساوی صفر میزاره که اولین کاراکتر صفر هستش
   print(string_to_iterate[char_index])     
#    این میاد میگه ایندکس کاراکتره را از اون رشته را پرینت کن
   char_index -= 1                           
#    وگرنه تا بینهایت میره # بعد منهای یکی کرد که برعکس بره تو اون لوپ تا برسه به صفر    

# //////

# چجوری بیاد برعکس را چجوری پیدا کنه بریزه ؟

sentence_reverse=''
sen2 = len(sentence)-1
while sen2 >= 0 :
    print("iaftam",sentence[sen2])
    sentence_reverse += sentence[sen2]
    print("ta hala gomle hast:",sentence_reverse)
    sen2 -= 1
print("akhar gomleh hast",sentence_reverse)
# باگ این برنامه اینه که میاد اخرین حرف را میریزه و یه اپند یا مثل اون نداره . چجوری میشه اضافه کرد؟
# با به علاوه مساوی در یک کانت
    

# //////

# n
# o
# h
# t
# y
# P

//////////
# برش زدن یک استرینگ طبق داده های درون یک لیست
# 93011
# NULL
# 5011005874
# A
# 0000000000010000
# 000000001
# JKL
# 00000000
# NULL
# 00000000
# A
# 63

s = "93011NULL                5011005874          A0000000000010000000000001JKL00000000NULL                                              00000000A63"
d = [5,20,20,1,16,9,3,8,50,8,1,2]
start=0
for x in d:
    print (s[start:start+x])
    start += x

# ///////
# خروجی لیست دادن با زیپ
# ['93011', 'NULL                ', '5011005874          ', 'A', '0000000000010000', '000000001', 'JKL', '00000000', 'NULL                                              ', '00000000', 'A', '63', '']
s = "93011NULL                5011005874          A0000000000010000000000001JKL00000000NULL                                              00000000A63"
d = [5,20,20,1,16,9,3,8,50,8,1,2]
# Convert sizes to indexes
d = [sum(d[:i+1]) for i in range(len(d))] #از آی به بعد را جمع میکنه با قبلی یعنی آی. 
splits = [s[i:j] for i, j in zip([0]+d, d+[None])]  
# یه تریک جالبه که مساوی با نان قرار میده چون خود اخری را حساب نمیکنه 
print (splits)

# ////

# این کد میاد به تعداد ۴ بار اون رشته را پرینت میکنه چون در لیستا ۴ تا عدد هست
# boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon
# boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon
# boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon
# boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon

aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[:])
    
# /////


# حالا اگر متغیر را تعریف کنیم
# میاد عدد درون اون لیست را میخونه و به تعداد اون رشته را برش میزنه
# bor
# boro
# boro inja
# boro inj
motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[motaghaier:i])
  
    
# //////

# این برنامه میاد متغیر را یک عدد لیست میگیره به علاوه قبلی میکنه میریزه تو متغیر
# 3
# 7
# 16
# 24
motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    # print(aba[motaghaier:motaghaier+i])
    motaghaier+=i
    print(motaghaier)


# ////////////////
 
# bor     سهه حرف میاره
# 3
# o in سه و چهار میشه هفت .پس هفت حرف میاره 
# 7
# ja bazi n
# 16
# akon pes
# 24
motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[motaghaier:motaghaier+i])
    motaghaier+=i
    print(motaghaier)

/////
# حال برنامه ای که فقط به اندازه عدد بعدی میاره و نه اینکه جمع کنه
# bor
# 0
# boro
# 0
# boro inja
# 0
# boro inj
# 0
motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[motaghaier:motaghaier+i])
    # motaghaier+=i
    print(motaghaier)



////
# این هفتمین حرف و چهارمینو ... امین حرف را میاره
# نه نمیدونم چیه
# bor
# 3
# o
# 7
# ja
# 16

# 24
motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[motaghaier:i])
    motaghaier+=i
    print(motaghaier)


//////
# برنامه ای که از اولین  به بعد را فقط حساب میکنه و از اون به بعد را برش میزنه میاره
# bor
# 3
# o in
# 4
#  inja baz
# 9
#  bazi na
# 8

motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[motaghaier:motaghaier+i])
    motaghaier=i
    print(motaghaier)
# //////
# برنامه ایکه بازه ای
# را برش میزنه که  از اون عدد قبلی تا عدد جدیده را میاره نشون میده

# bor
# 3
# o
# 4
#  inja
# 9

# 8

motaghaier= 0
aba= 'boro inja bazi nakon pesar . gomsho goloie kharabshodeie khodeeton bazi kon'
lista=[3,4,9,8]
for i in lista:
    print(aba[motaghaier:i])
    motaghaier=i
    print(motaghaier)

# /////
# میبینه که ایا یه حرف کوچک است یا خیر و اگر کوچک بود میریزه توی کانت کوچیک
count_big= 0
count_small=0
    for i in sentence:
        # یه چیزی میخوام که بررسی کنه که اونی که میبینه بزرگه یا کوچیکه
        if i.isupper():
            print(i)
            count_big +=1
            print(f'count_big is {count_big} ')
        else:
            print(i)
            count_small+=1
            print(f'count_small is {count_small} ')

# //////////////
# برای کار کردن لوور و آپر باید بریزی تو یه متغیر دیگه یا همون وگرنه نمیشه یه راس
'sentence=sentence.lower()'




# //////////////


# /////////

# پیش از ای چون جای خالی میگیره همه را جایگزین میکنه

# AcAAAmABAjABAAAoAlA
give= 'cAmBjBAol'
print(give.replace('','A'))


# /////////
# به تعداد مشخص مثلا ۲ بار فقط جایگزین میکنه نه بیشتر
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
y = txt.replace("one", "three")
print(x)
print(y)


# /////

# تا اونجایی که ای را پیدا کرد و جایگزین نمیکنه ای از اون به بعد را 
# cmBjBAol
give= 'cAmBjBAol'
print(give.replace('A','',give.find('A'),))
# این همون متد تعداد 
# ریپلیس هستش فقط بهش میگیم اولی چیزی که پیدا کردم. به تعداد همون

# ////////////////////
# ترتیب جایگزینی
def compare( ):
    my_sentence= 'ahhellllloo'     #input('give me the sentence: ')
    compare='hello'
    my=''
    for sen in my_sentence:

            if sen not in compare:
                my_sentence=my_sentence.replace(sen, '')
    return my_sentence

print(compare())

# خروجی ریپلیس مهمه که این اون کاراکتر را با هیچی جایگزین میکنه
# hhellllloo

# //////////////////


def compare( ):
    my_sentence= 'ahhellllloo'     #input('give me the sentence: ')
    compare='hello'
    my=''
    for sen in my_sentence:

            if sen not in compare:
                my_sentence=my_sentence.replace('', sen)
    return my_sentence

print(compare())

# ولی این میاد هرجا هیچی پیدا کرد با اون کاراکتر یعنی 
# a
# جایگزین میکنه
# یعنی پیش و پس از هر کاراکتر . یعنی اونجا را خالی تشخیص میده
# aaahahaealalalalalaoaoa                 
    
    
    
    
# //////////////

# همه ای ها را جایگزین میکنه
# cmBjBol
give= 'cAmBjBAol'
print(give.replace('A',''))


# /////////////
# کدی میخوام که بیاد بگه از اون به بعد که پیدا کردی بجای اولیش بزار 


# ///////////

# اگر کل متغیر را بنویسی  میاد به تعداد فور به تعدادش
# اون کار را میکنه ولی باید به تعدادآی و ایکس بزنه
vowl= 'euoai'
entereance = 'ideoafghji'
ent2=''
new_str = ''
for i in entereance:
    for x in vowl:
        if x == i:
            # print(' i found ' , word)
            new_str += i.replace(i, x)
#             # print('now ebterance is',entereance)
            # print( ' now new_str is ', new_str)
print(new_str)
# نکته الزامی نیست که از کاراکتر دومی استفاده کنی
# یعنی ایکس .. میشه دوتا حلقه زد 
# ولی یکیشو گذاشت و اون یکی را یه چیز دیگر گذاشت مثلا یه استرینگ

# اینجوری:
for i in entereance:
    for x in vowl:
        if x == i:
            entereance=entereance.replace(i, '')



# ///////////

# ای را از 5 تا 10 پیدا میکنه 
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# که اگرچیزی نزنی تا اخر حساب میکنه
# ۸
txt = "Hello, welcome to my world."
x = txt.find("e", 5)
print(x)
# ////////////
#  ترتیب بندی کردن .خودش استرینگ را میگیره سپس لیست میکنه میده
a='xcvbnm'
b=sorted(a)
print(b)
# ['b', 'c', 'm', 'n', 'v', 'x']


# ///////////
# ترتیب دهی استرینگ
# ترکیب دو متد با هم در استرینگ
for number in enter:
    # print(number)
    # print(enter)
    saver=(enter.split('+'))
    saver2=(''.join(sorted(saver)))
print(saver)
print(saver2)


# //////////

# از اون حرفی که پیدا کرد را برش میزنه 
# ولی خود حرفه را نمیاره و برای اینکه حرفه را بیاره باید مثبت یک را برداری
# mBjBAol
print(give[give.find('A')+1:])

# /////////////
# میشه در شرط عم متد گذاشت
for char in criterion :
    print(char)
    if right_test.find(char):
        print(char)
        

# ////////////
# متد ریپلیس تعدا جایگزنی را معلوم میکنه . اگر ۲ تا باشه ۲ بار جایگزین میکنه

# three three was a race horse, two two was three too.
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 3)
print(x)

# /////////////////
# اگر یک زیر رشته باشه که خودش رشته باشه اولین عنصر را به عنوان فایند میشناسونه
# 1 ایندکس را بر میگردونه
give4='BABAB'  
give5 = give4.find('AB')
print(give5)

# آیا برنامه و کدی میشه نوشت که اون بازه را بنویسه مثلا ۳-۵ ؟ که بگه تو اون بازه هست؟


# /////////

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

# //////////

# اراسپلیت از آخر یعنی راست میزنه

word = 'geeks@for@geeks'
print(word.rsplit('@', 1))
# ['geeks@for', 'geeks']



# ////////
# کار با رشته ها بود ولی در لیست میاره 
input_word = [myword.lower() for myword in input()] # read input_word in terminal

# //////////////////

# نکته نخست اینکه توی لیست بزاریم راحت تر  میشه
# هرچند الزامی نیست 
targ_word = ['a','e','i','o','u']
print("Enter word:") # example: shahram yalameha
input_word = [myword.lower() for myword in input()] # read input_word in terminal
output_charc = ''
output_nosplit= ''
print("Split input word is:", input_word)
# نکته دوم اینکه میشه کاراکتر سوم ساخت و درونش ریخته
# فقط اضافه بهش میشه کرد . 
# حتی میشه کوچیکش کرد 
# یعنی یه به علاوه کرد  و بعد با اون 
# یعنی اول خالی هستش. بعد که در دور بعد به علاوه ی نبودن کاراکتر ها میشه میندازه توی اون 
# و دونه دونه میاره تو اون
# و نکته جالب اینه که استثنا گرفتن ها بود. که اگر نبود در... ها را هم میشه در نظر گرفت در حلقه و پایتون
for myword in input_word:
   if myword not in targ_word:
     output_charc = (output_charc + '.' + myword.lower())
     output_nosplit =(output_nosplit  + myword.lower())
   
print("Split output word is",list(output_nosplit))
print("=============================================")
print("Result:",output_charc)
print("=============================================")


# //////////////////////////////////////////////////////////////////

# زدن حلقه در رشته
# کار با رشته ها
# استرینگ در لیست کامپرهنشن
vowl = 'aeiuo'
ent= input()
# این به ازای تعداد اون همه را میده ولی من میخوام یه بار بده
lowerer= [ ent.lower() for char in ent]

# این یکی هر کاراکتر را کوچیک میکنه میریزه توی لیست
# نباید متغیر بگیره
# چون در متغیر داری میگی متغیر را کلشو عوض کن 
# ولی اینجا میگی کاراکتر یعنی مای ورد را عوض کن
lowerer = [ myword.lower() for myword in input()]
# ['s', 'd', 'f', 'g', 'h', 'j', 'k', 't', 'y', 'u', 'v', 'b', 'n', 'm', 'r', 't', 'y', 'u', 'i']
print(lowerer)

# این هم نا معتبره
lowerer = [ myword.lower() for myword in vorodi= input()]

# حتی اینم اگر اینتیجر بزنی نمیاره
# یعنی اخر سر تعداد همون کاراکتر ها را بزنی 
# و در دادن تعداد اینتیجر هم اثر نداره
bn='gbhGBHNbhn'
an= int(2)
lowerer= [bn.lower() for (an) in bn]
print(lowerer)


# حتی اگر خود استرینگ  را بزنی هم میشه/
# vowl = 'aeiuo'
lowerer= [char.lower() for char in 'inpFVGBHN()']
print(lowerer)
# ['i', 'n', 'p', 'f', 'v', 'g', 'b', 'h', 'n', '(', ')']

# و اگر هم متغیر را بزنی باز میشه ولی کاراکتر را باید کوچیک کنی
zi='gfdDCTFGVcde'
lowerer= [char.lower() for char in zi]
print(lowerer)
# ['g', 'f', 'd', 'd', 'c', 't', 'f', 'g', 'v', 'c', 'd', 'e']


# حتی اینپوت را خارج از اون میشه زد یعنی درون یه متغیر 
# زدن حلقه در رشته
# کار با رشته ها
# vowl = 'aeiuo'
zi=input('')
lowerer= [char.lower() for char in zi]
print(lowerer)
# ['d', 'r', 't', 'f', 'v', 'g', 'b', 'h', 'g', 'v', 'b', 'h', 'j', 'n', 'v', 'g', 'b', 'h', 'j', 'n']





# ////////////
# اجرای دو متد استرینگ در کامپرهنشن
names= [input().capitalize() for name in range(3)]







# //////////////////
# Geeksforgeeks
string = "gEEksFORgeeks"
print(string.capitalize())

# //////////////////
# طول  رشته را ۱ میده اگر ویرگول بزاری 
vorodi='madam',
print(len(vorodi))
# 1

# یعنی پس از هر ویرگول را یه کاراکتر در نظر میگیره. مثل لیست !
vorodi='madam','ddffdfd'
print(len(vorodi))
# 2

# حالا اگر تقسیم / کنیم اینجوری میده
print(len(vorodi)/2)
# 2.5

# برای اینکه تقسیم رند باشه باید // بدیم
print(len(vorodi)//2)
# 2

# اما اگر تعداد حروف  فرد باشه  مشکل ایجاد میکنه یعنی دقیق نمیده
# اما اگر زوج باشه تعداد حروف  مشکلی پیش نمیاد

# /////
# برش زدن استرینگ
# توی بالا روش های برش زدن را دیدیم
# حالا میخوایم از وسط برش بزنیم با len

# این از وسط تا اخر برش میزنه

vorodi='madam'
# داره میگه طول رشته را تقسیم بر دو رند کن بده . محتواشو نه تعدادشو .
print(vorodi[len(vorodi)//2:])
# dam
# اینم از اول تا وسط برش میزنه
print(vorodi[:len(vorodi)//2])
# ma

# حالا چون فرد هست مشکل ایجاد میکنه
# چون یکیشو سه تا میده یکیشو ۲ تا


# اگر هم یه دونه ای تقسیم کنیم از اول خطا میده
vorodi='madam'
print(vorodi[:len(vorodi)/2])
# ma
# TypeError: slice indices must be integers or None or have an __index__ method

# یه ایده اینه که بزنی +۱ کنی یکیشونو
# یه ایده اینه که 
# منها کنی تا نصف بده
# ////////////////
# برش زدن استرینگ
enter= 'Madam'
str0=slice(enter[0],enter,enter[-1])
print(str0)
# slice('M', 'Madam', 'm')
str1 =(slice(0, len(enter)//2))
print(str1)
# slice(0, 2, None)


# //////////
# تعداد زوج بودن کاراکتر و یا فرد بودن تعداد کاراکتر در استرینگ
# تقسیم کردن و نصف کردن کاراکتر ها
# در صورت زوج و فرد بودن
s=  'madam'
s.lower()
if len(s)%2 != 0:
    print('odd')
    new1= s[:(len(s)//2)+1]
    print(new1)
    new2=s[len(s)//2:]
    print(new2)
else :
    print('even')
    s1 = s[:len(s)//2]
    print(s1)
    s2 = s[len(s)//2:]
    print(s2)

# dam

# /////////////////////////////////
# همیشه جایگزین اولی چیزیه که داریم . با چیزی که میخوایم جایگزین میشه
# اگر نباشه چیزی اون که اول بود را دوباره مینویسه.. به انتفاع مقدم
enter7='ABA'
enter8='ABBA'

alef=enter7.replace('AB','.')
be=alef.replace('BA','.') 
print(alef)
print(be)


# /////////////////////////////////////

# روش برش زدن استرینگ با توجه به معیار.
# هم با معیار مقایسه میکنه و هم برش میزنه
# دفعه اول همون ورودی را مقایسه میکنه دفعه های بعد برش زده اش را مقایسه میکنه
right_test= 'ahhelllouu'
wrong_test= 'hlelo'
# اولین بار تست را میزاره رایت تست
# اما دفعه های بعد  برش زده را قرار میده
test= right_test
criterion= 'hello'
empty=''

# if 'h' in right_test:
#     right_test= right_test[right_test.find('h')+1:]
# print(right_test)
new=''
for char in criterion:
    print('char in for is ',char)
    if char in test:
        print('char in if is',char)
        new+=char
        print('new is',new)
        # روش برش زدنکاراکتر که بعدشو بیاد انجام بده
        test=test[test.find(char)+1:]
        
        print('now test would be',test)

print(new)
print(test)
# //////////////////
# برش زدن
name='my name is'
# print(name[-1:])
# s
print(name[:-1])
# my name i
print(name[0:-1])
# my name i
print(name[-1:0])
# هیچی
for char in name:
    print(char[-1:0])
# هیچی


# //////////////////////////

print(('add') in 'jadi')
False

# ///////////
# پیدا کردن. میگه ایا هست . اولیشو پیدا میکنه و ایندکس را میده
a='kjghfgjf'

print(a.find('j'))
# 1
#  بعد میگی از اون به بعد مثلا از سومی به بعد کجاست میگه تو شیشمی هست(شیشمی از اول کل)
print(a.find('j',3))
# 6
# ///////////////////

# شیوه نوشتن یه استرینگ هم اینجوری میشه. 
# بگو اون متن اصلی به علاوه ی اون استرینگ . که معلوم کنه تمیز که خروجی چی میشه
test_str = 'gfg_is_best_for_geeks'
print("The original string is : "
      + str(test_str))
 # The original string is : gfg_is_best_for_geeks 
 



# ///////////////
# یه نکته . موقع برش زدن 
# اگر از چپ اولی را بزنی برش میزنه از وسط به اخر
# چپ از وسطه
ino='madam'
my_half1=ino[len(ino)//2:]
# dam
# اگر از راست بزنی برش میزنه تا وسط 
# راست تا وسطه
my_half2=ino[:len(ino)//2]
# mad


# ///////////
# ارائه خروجی با استرینگ 
res = dict()
# using loop to reform dictionary with splits
# انومریت یعنی میشماره اون لیست تمپ را
for idx, ele in enumerate(temp):
    res[idx] = ele
    
# در این تیکه اول چیزی را مینویسی که ببین خروجی شما اینه:
# هم برای خوندن کد راحت تر است
print("Dictionary after splits ordering : "
      + str(res))
# //////
# خروجی دادن  در هر خط بطور جدا

# ('name', 'mamad')
# ('sen', '29')
# ('ghad', 167)
d={'name':'mamad', 'sen':'29','ghad':167}
print(*d.items(), sep='\n')

# ////////
# متد نوشتن خروجی
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) 
# For only 49.00 dollars!

# /////////////////////////////////////////////////////////
# escape کردن

# نمایش در خیلی جاهای کامپیوتر با 
# اینتر میشه :
\n
# است

# بک اسلش یعنی \
# معنی زایی میکنه 
# hello\jadi 
# یعنی اسپیس
# hell jadi


\t
# tab  را نشون میده که 
# ۴ اسپیس پایتون است یا 
# ۸ تا اسپیس جاهای دیگر

# ////////////
# تریپل کوت
# یعنی هر چیزی بنویسی و حتی بری در پرینت بگیری میشه بره خط پایین

a='''dsdsddd
dffd
dfscdsc
dscx'''

# که این برای سینگل و دابل کوت نمیشه
b='
sddsdsdsdddssd
'

# ///////////////////////
a='''ssddsd
ddafc
adfscxdvcx
dcx         

'''
# این متد از هر دو طرف اسپیس ها را بر میداره
a=a.strip()

print(a)
# ssddsd
# ddafc
# adfscxdvcx
# dcx
# ////////////////////////
# این متد اسپیس ها را فقط از چپ بر میداره
a='''                                ssddsd
ddafc
adfscxdvcx
dcx                          '''
a=a.lstrip()

print(a)
# ssddsd
# ddafc
# adfscxdvcx
# dcx
# /////////////////////////
# از راست میچسبونه اگر اسپیس وجود داشته باشه
a=a.rstrip()
# ssddsd
# ddafc
# adfscxdvcx
# dcx

# /////////////////////


# در حلقه انداختن که پرینت
# end ... 
# به این معنی است که هر جا که دیدی رسید به اند ختم کن
    for lin in f:
        print(lin,end='') 
        # اینجا  اند که اورده درست کار کرده
# mandana,5,7,3,15
# hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
# sina,19,10,19,6,8,14,3
# sara,0,5,20,14
# soheila,13,2,5,1,3,10,12,4,13,17,7,7
# ali,1,9
# sarvin,0,16,16,13,19,2,17,8
# ////////////////////////////////////////////////////
# شیوه ارائه 

Dict = { }
print("Initial nested dictionary:-")
print(Dict)
# Initial nested dictionary:-
# {}

# ///////////
# در دو خط گرفت وررودی

def readCSV(filename= input('give me the file name and format like this: csv-mean\n : ')):
# give me the file name and format like this: csv-mean
#  : csv-mean


# //////////
# شیوه نوشتن اف استرینگ در توابع ارث برده شده
class Computer :
    def __init__(self,cpu,ram,graphic):
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue   
    
# اینجا تابعی تازه تعریف میکنیم که فرق داره  یعنی روی ولیو های بالایی کار میکنه
# ولی یه تغیراتی که ما بخوایم را روش انجام میده
class laptob(Computer):
    def arzesh(self):
        print(f'arzeshe in hastesh {self.value()*2}')
# سینتکس درست همینه توجه بشه که اگر سلف خالی بزنی
# نمیاره چیزی باید یه متدی را بیاری روش کار کنی یا متغیر

mylap=laptob(2.6,8,16)
# اینجا بدون اینکه واسه بالایی چیزی تعری کنیم همونو میده
print(mylap.value())
# 26.6
(mylap.arzesh())
# arzeshe in hastesh 53.2

# ////

# ساخت لیستی از اعضا که فقط عددشون تغیر کند

# چگونه لیستی از اعضا درست کنم که اسم 
# اولشون ثابت باشه ولی عدد بعدیشون در حلقه تغیر کند
# این خطا را نده
# can only concatenate str (not "int") to str

# راه ۱
m_players=[]
for i in range(3):
    m_players.append(f"'player'{i}")
print(m_players)
# چگونه لیستی از اعضا درست کنم که اسم اولشون ثابت باشه ولی عدد بعدیشون در حلقه تغیر کند
# ["'player'0", "'player'1", "'player'2"]


# راه ۲
m_players=[]
for i in range(3):
    m_players.append(('player',str(i)))
print(m_players)
# [('player', '0'), ('player', '1'), ('player', '2')] 

# راه ۳
m_players=[]
for char in range(3):
    name='player'
    m_players.append (('%s,%i'%(name,char)))
print(m_players)
# ['player,0', 'player,1', 'player,2']

# راه ۴
# حالا اگر میخوایم اون کاما نباشه از اول توی درصد ها نزار
m_players=[]
for char in range(3):
    name='player'
    m_players.append (('%s%i'%(name,char)))
print(m_players)
# ['player0', 'player1', 'player2']  

# حالا اگر میخوایم از ۱ اغاز کنه
m_players=[]
for char in range(1,4):
    name='player'
    m_players.append (('%s%i'%(name,char)))
print(m_players)
# ['player1', 'player2', 'player3']  

# راه دیگه اینه
'player'+str(i)
# مثلا
# ساخت یک دیکشنری بصورت رندوم
def random_dict():
    my_dict={}
    for i in range(10):
        # نوشتن یک  کلید  استرینگی در لید دیکشنری
        my_dict['key'+str(i)]=randrange(10)
    return my_dict
print(random_dict())
# {'key0': 3, 'key1': 1, 'key2': 9, 'key3': 6, 'key4': 7, 'key5': 4, 'key6': 1, 'key7': 3, 'key8': 2, 'key9': 6}
      
# /////
# میشه در سه خط جدا بنویسیم و در سه خط هم بیاره
a='''
dsdfdfsfdsf
dsfsdf
dsfsdf '''
print(a)

# dsdfdfsfdsf
# dsfsdf
# dsfsdf

# ////

# تبدیل یک استرینگ به چند استرینگ
input_str = '32,6.52,8,5000'

# تابع split() را با کاما به عنوان جداکننده روی رشته ورودی اجرا کرده و یک لیست از رشته‌ها ساخته می‌شود
output_list = input_str.split(',')
print(output_list)  # ['32', '6.52', '8', '5000']

# از لیستی که در مرحله قبلی ساخته شده، با استفاده از join() و کاما به عنوان
# جداکننده، یک رشته جدید به وجود می‌آید که درون گیومه قرار دارد
output_str = ','.join(["'"+x+"'" for x in output_list])
print(output_str)  # '32','6.52','8','5000'


# این کد بدون کامپرهنشن است
# تقسیم رشته ورودی به چند رشته جداگانه
input_str = '32,6.52,8,5000'
output_list = input_str.split(',')

# تبدیل هر رشته به صورت یک رشته با کاما و داخل نقل قول تکی
output_str = []
# میگه به ازای هر ایکس که  ایکسه را یه دونه رشته بده
for x in output_list:
    x = "'" + x + "'"
    output_str.append(x)
# ["'32'", "'6.52'", "'8'", "'5000'"]
# یا این
for x in output_list:
    x = ''+ x + ''
    output_str.append(x)
print(output_str)


# ادغام رشته‌های تکی با کاما
final_str = ','.join(output_str)

# با هیچی یعنی دوباره در یک رشته  کلی ببر
final_str = ''.join(output_str)

# چاپ نتیجه نهایی
print(final_str)


# منظور از

"'" + "32" + "'"  # output: "'32'"

# /////////

s = '32,6.52,8,5000'

# ابتدا رشته s را با استفاده از کاما به چند رشته کوچکتر تقسیم می‌کنیم و آن‌ها را در یک لیست ذخیره می‌کنیم.
split_result = s.split(",")
print(split_result)  # ['32', '6.52', '8', '5000']

# سپس رشته‌های کوچکتر حاصل از تقسیم را با استفاده
# از کاما و نقطه توسط رشته "',' " به یکدیگر وصل می‌کنیم.
join_result = "','".join(split_result)
print(join_result)  # 32','6.52','8','5000

# در نهایت با استفاده از نقل قول تکی، رشته ایجاد شده در مرحله قبل
# را درون نقل قول دوتایی قرار داده و به عنوان خروجی نهایی چاپ می‌کنیم.
result = "'" + join_result + "'"
print(result)  # '32','6.52','8','5000'

# /////

words = "ABCD abcd AB55 55CD A55D 5555"
' '.join(s for s in words.split() if not any(c.isdigit() for c in s))
# 'ABCD abcd'

# این کد تا جایی که به جوین ربط داره
mylist=[]
for s in words.split():
        if not any(c.isdigit() for c in s):
            mylist.append(s)
# mylist
# ['ABCD', 'abcd']

# که حالا اگر میخوای داده های درون یک لیست را که از رشته ها تشکیل شده را به یک رشته تبدیل کنی
''.join(mylist)
# 'ABCDabcd'

# حالا اگر میخوای تیکه تیکه اش کنی باز
' '.join(mylist)
# 'ABCD abcd'
# یعنی یه اسپیس بزار درونش
# //////////
# تبدیل استرینگ به لیست از اینتیجر یا فلوت
s = "32,6.52,8,5000"
result = [int(x) if '.' not in x else float(x) for x in s.split(',')]
print(result)
# [32, 6.52, 8, 5000]


input_str = '32,6.52,8,5000'
output_list = []
for number_str in input_str.split(','):
    output_list.append(int(float(number_str)))

print(output_list)
# خروجی: [32, 6, 8, 5000]

# //////
# replace
# شبیه رجکس کار میکنه
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

# روش دیگر جایگزینی
# اگر عدد داشت حذفش کن یا اگر حروف داشت حذفش کن و عد خالصشو بهمون بده
data=['6.43in', '6.43in', '1.77', '6.43in', '1.77', '1.8', '6.43', '1.77']
# به این تبدیل میکنه
# ['643', '6.43', '1.77', '643', '1.77', '1.8', '6.43', '1.77']
ram=[]
for char in data:
    # for the_ram in char[1][0]:
    if 'in' in (char):
        char = ''.join([i for i in char if  i.isdigit()])
        # ram.append(char) # اگر اینو بیاریم  به اندازه اون ها که در بالا داشتیم تعداد اضافه میکنه
        # ['643', '643', '6.43', '1.77', '643', '643', '1.77', '1.8', '6.43', '1.77']
    ram.append(char)
print(ram)

# ///////////////////////
s = '12abcd405'
result = ''.join([i for i in s if not i.isdigit()])
# 'abcd'
# /////////
# میشه یع متغیر را جایگزین کنیم با یه رشته
for title in data:
    # اینجا برای اینکه مشکل تایپی باعث نشه که گوشی های موبایل که متفاوت نوشته شده اند
    # را برای برچسب زدن ماشین متفاوت تشخیص بده با یک چیز جایگزین کردم
    title[0][0]=title[0][0].replace(title[0][0],'گوشی موبایل') # میشه یع متغیر را جایگزین کنیم با یه رشته
    product.append(title[0][0])
# ///////////


