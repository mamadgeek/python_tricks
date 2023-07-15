

# تابع ساده تعریف کردن
def greeting ():
    print("Hello")
    print("how are you ?" )
greeting()



# موقع خوندن یک ریترن میشه جلوش پرینت هم گذاشت
# ....
# ....
# ....
# ....
# ....
    # return(print (tup)) 
# give me the number: 256
# (256, 8, [2, 2, 2, 2, 2, 2, 2, 2])

# /////////////
# میشه حتی یه استرینگ نوشت جلوش :
    # /
    # /
    # return('inja ine' ,(tup))

# ('inja ine', (147, 3, [3, 7, 7]))

# ///////////




# /////////////
# پس به جای متغیر میشه اسم گذاشت و بعد پرش کرد
# یا یه کار دیگه کرد باهاش
def greeting(name):
    print("hi", name)
    print("bye", name)
greeting("jadi")
# hi jadi
# bye jadi

# /////
# میشه یه اسم دیگه گذاشت روی متغیر ها  فقط جاگذاریشون باید منطبق باشه
def sum(first,second):
    result=(first+second)
    return(result)
iek=2
do=3
gavab= sum(iek, do)
print(gavab)

# //////

def hoghogh(hur, per):
    if hur > 8 :
        return("to much")
    daranad= (hur*per)
    return(daranad)

print(hoghogh(7,1200))
# 8400
# print("//////")

def f(a):
    return a*5
#فراخانی
print(f(4))
print(f(3))
#20
#15
# /////////////
# میشه اونجا پرینت را گزاشت.. 
# یعنی در تابع نه بازگردانی را... اما نمیشه با پرینت کاری کرد
def sayHello():
    print("hello")
    print("-------------")
# //////////
def print_square_of_7():
    print(7**2)
print_square_of_7()
# 49

# ////
# میشه هم پرینت گذاشت و هم ریترن. ..
def square_of_7():
    # commands
    print("I Am Before Return")
    return 7**2
    print("I Am After Return")
print(square_of_7())
# I Am Before Return
# 49
# /////////
# یه بار که ریترن کرد تموم میشه 
# دیگه دوباره نمیشه پرینت یا ریترن بعدی را بیاره
def square_of_7():
    # commands
    print("I Am Before Return")
    return 7**2
    print("I Am After Return")
    return 7**2
print(square_of_7())
# /////
# میشه درون اون ننوشت..  یعنی 
def add_numbers():
    a = 4
    b = 7
    return a + b

print(add_numbers())

# ////
# هر عددی بود را یه کاری باهاش کن.. یه کار ثابت نه متغیر . مثلا به علاوه شیش
def sum(firstNumber):
    return firstNumber + 6
print(sum(5))
print(sum(9))

# /////
# میشه متغیر گذاشت جای اعداد
def sum(firstNumber, secondNumber):
    return firstNumber + secondNumber
print(sum(19,6))

# /////


# /////
# ترکیب اف استرینگ و تابع

def showFullName(firstName, lastName):
    return f"{firstName} {lastName}"

name = "mohammad"
family = "ordookhani"
person = {
    "name": "mohammad",
    "family": "ordookhani"
}
# پرسشم اینه که اگر نیم و فامیلی را بالا نزده بود ایا نمیومد توی تایع؟
# نه فرق نداره
# این دو تا چیه ؟
print(showFullName(name, family))
# این دومیه میاد از درون یک دیکشنری داده میگیره
# دیکشنری و تابع
print(showFullName(person["name"], person["family"]))
# ///

def divide(num_1, num_2):
    return num_1 / num_2
# print(divide(3,5))
# print(divide(5,3))
# ///
# ترکیب لیست و تابع
#  در یک تابع یه حلقه را وارد لیست میکنه کاری روش انجام میده
myNumbers = [1, 2, 3, 4, 5, 6, 7]  # 16
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
print(sum_odd_numbers(myNumbers))


# ///
# ایا یه خاصیت را داره یا نه 
def is_even_number(number):
    if number % 2 == 0:
        return True
    return False
# print(is_even_number(5))  # false
# print(is_even_number(6))  # true


# ////
# پیشفرض تعریف کردن
def exponent(num, power=2):
    return num ** power
# در حالت غیر پیشفرض دادن 
print(exponent(2, 3))  
# 2 * 2 * 2 = 8
# در حالت پیشفرض که یعنی  هیچی نده میاد به توان دو میرسونه
print(exponent(3)) 
# 3 * 3 = 9
# ////

# ///
#کاربرد اف اسرینگد 
def showFullName(first, last):
    return f"{first} {last}"
print(showFullName("ordookhani","mohammad"))
# اگر همون عنوان تابع را تعیرف کنیم میشه جاش میشینه 
print(showFullName(last="ordookhani", first="mohammad"))
# /////
# وقتی نمیدونیم چند تا متغیر قراره بگیره که یه 
# عملیات را مثلا جمع را روش انجام بده از استارارگز استفاده میکنیم
# میاد یه عملیات تعداد نامشخص را جمع میزنه
def sum_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all_numbers(4,6,8,1))
# 19
print(sum_all_numbers(2,3))
# 5
print(sum_all_numbers(4))
# 4
# //////////
# همون تابع بالا:
# میاد متغیر دیگری هم قرار میده
def sum_all_numbers(name, *args):
    total = 0
    for num in args:
        total += num
    return name , total
print(sum_all_numbers('borrro' , 4,6,8,1))

# که اگر در ریترین name
#   را نزنیم نمیاد
# بورررو


//////
# برای اجرای یه ارگز داخل یه لیست باید در حالت فراخوانی هم 
# پیش از اون متغیر یه ستاره قرار داد
def sum_all_numbers( *args):
    total = 0
    for num in args:
        total += num
    return  total
numbers= [2,5,63,5]
print(sum_all_numbers(*numbers))
# 75

# یعنی 
print(sum_all_numbers('borrro' , *[4,6,8,1]))
# ('borrro', 19)

# ولی
# اگر ستاره نزاریم 
print(sum_all_numbers('borrro' , [4,6,8,1]))
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# منتها اگر لیست نزاریم نیازی باز کارشو انجام میده
print(sum_all_numbers('borrro' , 4,6,8,1))
# ('borrro', 19)


# /////
# تبدیل تابع به دیکشنری 
# وقتی که ندونیم چندتا ایتم میگیره در یک تابع از کیورد ارگز استفاده میکنیم
def showUserInfo(**kwargs):
    return kwargs
print(showUserInfo(name="mohammad", family="orodookhani",
             age=23, email="moh96ordo@gmail.com"))
# {'name': 'mohammad', 'family': 'orodookhani', 'age': 23, 'email': 'moh96ordo@gmail.com'}
# حالا اگر یکی میزاشتیم:
print(showUserInfo(name="mohammad"))
# {'name': 'mohammad'}

# ////////
# تبدیل تابع دیکشنری کی دبلیو ارگز به خروجی استرینگ
# یه حلقه هم میشه روی اون زد
def showUserInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")
showUserInfo(name="mohammad", family="orodookhani",
             age=23, email="moh96ordo@gmail.com")
# name is mohammad
# family is orodookhani
# age is 23
# email is moh96ordo@gmail.com

# ////

# برای خوندن کلید ها هم باید دابل استار را بکار برد
def display_names(name,family):
    print(f"name is {name} and family is {family}")
person = {"name":"sara","family":"moradi"}
display_names(**person)
# name is sara and family is moradi
# ////

# میشه هم استارارگز و هم کی ورد دابل استار و هم متغیر و...
# را یه جا بکار برد در یک تابع 
def display_info(a, b, *args, defPara="defalut", **kwargs):
    return [a, b, args, defPara, kwargs]
print(display_info(1, 2, 6, first_name="mohammad", last_name="ordookhani"))
# [1, 2, (6,),'defalut',{'first_name': 'mohammad', 'last_name': 'ordookhani'}]
# ////////////



print("////////")
# 

# میشه یه برنامه که نوشتیم را تبدیل به تابع کنیم . فقط با یه  دنده دادن و بعد اسم انتخاب کردن 


def isprime(num):
    num = int(input(""))
    if num > 1: # این شرط زده بزرگتر از 1 که اعداد منفی و صفر نباشه 
        # اینجا نیاز داره بگرده همه اعداد را 
        for i in range(2, num):   # همه اعداد به خودش و یک که تقسیم
            # میشن حتی نات پرایم ها ... پس باید
            # از بعد از 1 اغاز کرد و تا خود قبل اون 
            # عدد که عملا رنج این کار ا انجام میده
            if (num % i) == 0:
                # اینجا اگر در اون رنج عددی را پیدا کرد که تقسیم عدد
                # مدنظر ما بر اون باقیموندش صفر شد پس عدد ما اول نیست
                print("not prime")
                # به این دلیل میشکونه 
                # حلقه را میاد بیرون که یه دونه پیدا کرد و کافیه
                break
        else:
            # اگه همچیین عددی پیدا نکرد در حلقه پس اوله
            print("prime")
    else:
        # در غیر این صورت میشه اگر عدد منفی بود یا صفر بود پس اول نیست 
        print("not prime")

print(isprime(45))

# این برنامه اون برنامه بود:


# num = int(input(""))
# if num > 1:  
#     for i in range(2, num):  
#         if (num % i) == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("not prime"

print("////////")

# نکته : جالبه اگر داخل تابع یه چیز بزنیم اون موقع موقع 
# فراخانی باید یه چیز بزاری توش حتی اگر خالی باشه

# چجوری بیاد برعکس را چجوری پیدا کنه بریزه ؟
def reverse_string(sentence):
    sentence= input(' give me the sentence: ')
    sentence_reverse=''
    sen2 = len(sentence)-1
    while sen2 >= 0 :
        print("iaftam",sentence[sen2])
        sentence_reverse += sentence[sen2]
        print("ta hala gomle hast:",sentence_reverse)
        sen2 -= 1
    return("akhar gomleh hast",sentence_reverse)
    # باگ این برنامه اینه که میاد اخرین حرف را میریزه و یه اپند یا مثل اون نداره . چجوری میشه اضافه کرد؟
    # با به علاوه مساوی در یک کانت
reverse_string()
# این ارور را میده
# TypeError: reverse_string() missing 1 required positional argument: 'sentence'
#  حالا اگر هر چیزی مسخره هم بزنیم برنامه کار میکنه:
reverse_string("fsadad")
# حتی اگز متغیر استرینگ را بدی ارور میده. مگر 

# حالا اگر هیچ چیزی هم تعریف نکنیم بازهم میره 
# رو خط بعدی و میشه در فراخوانی هیچ چیز ننوشت
def reverse_string():
    sentence= input(' give me the sentence: ')
    sentence_reverse=''
    sen2 = len(sentence)-1
    while sen2 >= 0 :
        print("iaftam",sentence[sen2])
        sentence_reverse += sentence[sen2]
        print("ta hala gomle hast:",sentence_reverse)
        sen2 -= 1
    return(sentence_reverse)
    # باگ این برنامه اینه که میاد اخرین حرف را میریزه و یه اپند یا مثل اون نداره . چجوری میشه اضافه کرد؟
    # با به علاوه مساوی در یک کانت


reverse_string()
print("////////")


# راه ۲ اینه که خود تابع را بزاریم :
sent2 = input(' give me the sentece2: ')
if reverse_string() == sent2:
    print ('Palindrom')
else:
    print ('not Palindrom')

#  فراخانی یا در یک حلقه :
for i in reverse_string():
    print(i)

# ///////
# بکار بستن دو تا تابع با هم دیگه
def duble(number):
    number*=2
    return(number)
def reverse (number):
    num_str =str(number)
    number= num_str[::-1]
    number = int(number)
    return number
# برای اینکه دو تا تابع را با هم بکار ببریم در فراخوانی
# اونی که بعدش میخواد بکار بره را اول می نویسیم . 
a = duble(reverse(765))
print(a)
# 1134
# /////////
# یا بدون اینپوت گرفتن : 
myNumbers = [1, 2, 3, 4, 5, 6, 7]  
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
print(sum_odd_numbers(myNumbers))
# 16
# اینجا بجای نامبرز خود  مای نامبرز را گذاشته و یه ضرب هم پرینت کرده .. 
# یعنی نه اینتپوت گرفته نه موقغ فراخانی داخل متغیر دیگه ای ریخته

# میشه فقط متغیرشو نوشت و داخل شرط یا حلثه 
# یا  حتی میشه یه متغیر را مقایسه با خودش کرد که فاکنشی روش پیاده شده

sen1= input('give me the sen1: ')
print(sen1)
if reverse_string(sen1) == sen1:
    print ('Palindrom')
else:
    print ('not Palindrom')


print("////////")

# نکته : یک داده درون تابع را نمیشه بیرون از اون تابع بکار برد

print("////////")

# میشه داخل تابع متغیر را ننوشت و رفت پایین  و درون اون تابع ورودی گرفت:
def reverse_string():
    sentence= input(' give me the sentence: ')
    
# میشه داخلش از اول گرفت:
def reverse_string(sentence= input(' give me the sentence: ')):

# یا میشه هر دو :
def reverse_string(sentence):
    sentence= input(' give me the sentence:' ) 

# اما در حالت هایی که میای متغیری میزنی باید در خود فراخانی هم متغیری بریزی
sen1='hggv'
if reverse_string(sen1) == sent2:
# هرچند وقتی که یک بار درون تابع اینپوت دادی دیگه جلو هم یک بار استرینگ دادی 
# حالا کدوم را حساب میکنه ؟ استرینگ را
# یا اینپوت را  . یا حتی موقع فراخانی هم میشه دوباره اینپوت گرفت؟

# پاسخ: استرینگ را حساب نمیکنه که چی گرفته فقط اون چیزی که درون تابع بوده
# ..هرچیزی هم که تو استرینگ بریزی فرق نداره
sen1='hggv' 
if reverse_string(sen1) == sent2:
    print ('Palindrom')
else:
    print ('not Palindrom')
    
# ورودی تابع را موقع اینپوت فراخانی درون تابع دادیم:
#  give me the sentece2: aba
#  give me the sentence:aba

# و اون درون تابع ملاکه و نه hggv
# کما اینکه در این کد این را دادیم که طبق داده 
# بیرونی پالیندروم هست ولی طبق داده تابع نیست و 
# ملاک را تابع درونی گرفته 
# give me the sentece2: aba
# give me 3: aba
#  give me the sentence:kjil
# not Palindrom


# ///////////////
# در تابع از اول اینپوت دادن و موقع فراخوانی خودش میخواد
def divisibility(a= int(input('give me maghsum alie:')),b= int(input('give me mghsum: '))):
    if a%b ==0:
        return ('divisible')
    else:
        return('notdivisible')
print (divisibility())
# give me maghsum alie:10
# give me mghsum: 5
# divisible



print("///////")


print("////////")

# زیپ

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)  # Holds an iterator object

# این ارور نیست . زبون خود کامپیوتره

# zip object at 0x7fa4831153c8>
type(zipped)
# <class 'zip'>
print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')]

# /////////////////////////////////////
# زیپ کردن یه لیست و دو تا لیست تو در تو
player1=[['a'],['b'], ['c'] ,['d']]
player2=['A','B','C' ,'D']
print(list(zip(player1 , player2)))

# [(['a'], 'A'), (['b'], 'B'), (['c'], 'C'), (['d'], 'D')]

# ///////////
# ترکیب دو تا رنج در زیپ و لیست کردن اونا

list(zip(range(5), range(100)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# ////////
# ترکیب رنج با یه حروف الفبا در زیپ 

from itertools import izip
zipped = izip(range(3), 'ABCD')
zipped
# <itertools.izip object at 0x7f3614b3fdd0>
list(zipped)
# [(0, 'A'), (1, 'B'), (2, 'C')]



# ////////////

# //حلقه و لیست دوتایی

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
print(f'Letter: {l}')
print(f'Number: {n}')
# Letter: a
# Number: 0
# Letter: b
# Number: 1
# Letter: c
# Number: 2


# ////////////////
#  سترکیب زیپ و حلقه در لیست
# سه تایی
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')
 
# Letter: a
# Number: 0
# Operator: *
# Letter: b
# Number: 1
# Operator: /
# Letter: c
# Number: 2
# Operator: +


# //////////////////
# ترکیب زیپ و دیکشنری
# دوتا دیکشنری
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
      print(k1, '->', v1)
      print(k2, '->', v2)
 
# name -> John
# name -> Jane
# last_name -> Doe
# last_name -> Doe
# job -> Python Consultant
# job -> Community Manager

# ///////////////
# جدا کردن یه دوتایی با برعکس کردن زیپ .

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
numbers
(1, 2, 3, 4)
letters
# ('a', 'b', 'c', 'd')


# /////////////
# سورت کردن دوتا لیست زیپ شده
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
data1
# [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
data1.sort()  # Sort by letters
data1
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]
data2 = list(zip(numbers, letters))
data2
# [(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
data2.sort()  # Sort by numbers
data2
# [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]


# //////////////////




letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data = sorted(zip(letters, numbers))  # Sort by letters
data
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]

# ////////////
# دوتا ورودی را دادن . بعد عملیات وارد کردن یکی بر دیگری .
# اینجا اولی را منهای دومی میکنه . عنصر اولی لیست اول را منفهای عنصر اولی لیست دومی میکنه
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')

# Total profit: 5200.0
# Total profit: 5100.0
# Total profit: 4800.0



# /////////////
# تبدیل لیست به دیکشنری با زیپ کردن عنصر ها

fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
a_dict
# {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}

# //////////////
# بروز کردن دیکشنری با زیپ 
new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
a_dict
{'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}


# //////////////


# اگر زیپ یشه باید به همون تعداد یکسان باش ه . اوما در این مورد میشه خودش جاهای خالی را پر کنه

from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
list(zipped)
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

# اگر زیپ یشه باید به همون تعداد یکسان باش ه .
# اوما در این مورد میشه خودش جاهای خالی را پر کنه

from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
list(zipped)
[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

# /////////////////////

# تابع های تو در تو

def function1(): # outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()
function1()
# Hello from outer function
# Hello from inner function
# /////////////////////


# اینجا میاد تو در تو را میاره ولی نفهمیدم چرا
# و چگونه دومی را نسبت داد؟
def num1(x):
    def num2(y):
        return x * y
    return num2
res = num1(10)
print(res(5))
# 50

# //////////
def wage(x):
    return x*25
print(wage(8))
# 200
def bonus(per_hour):
    # اینجا باید یکی  باشه اون متغیره که به هم ربط بده
    return wage(per_hour)+50
print(wage(8), bonus(10) )

# 200 300
# ۲۰۰ را همون ویج را میگیره
# ۳۰۰  را امیاد هر ساعت را ۱۰ میگیره و بعد ضربدر ۲۵ از
# تابع ویج میکنه و بعد به علاوه ۵۰ که میشه 

# پس عملیات ۲ تابع را میاره اول داخل تابع اولی حساب میکنه و نتیجه را میاد در تابع دومی

# ///////

# دوتا کد را ترکیب کردم. یکی تعداد بازی ها 
# در لیگ فوتبال
# را میپرسه و در اون یکی بکار میبره و فقط 
# در تابع دیگر تا همون تعداد میپرسه
def tedad_bazi (number= int(input(' give me numbers of all teams of the ligue:'))):
    count1 = (number-1)*2
    return count1
print(tedad_bazi())

# تابعی که تعداد برد  و باخت را میشماره .
def win():
    wining=0
    draw= 0
    lose= 0
    for i in range(tedad_bazi()):
        d= int(input('emtiaz chand shod?: '))
        if d== 3:
            wining+=1
        elif d==0:
            lose+=1
        elif d ==1:
            draw+=1
    return wining , lose , draw
            
print(win())


# 4
# emtiaz chand shod?: 1
# emtiaz chand shod?: 3
# emtiaz chand shod?: 0
# emtiaz chand shod?: 3
# (2, 1, 1)

# //////


# ترکیب دو تابع وقتی که برونداد یک تابع را
# در یک حلقه چند بار تکرار میکنیم  و برونداد میگیریم 
# و بعد اون برونداد ها ی تاپلی را با هم مقایسه می کنیم
def counter_prime (num):
    numx=num
    counter_num = 0
    list_of_primes= []
    for i in range(2, num+1):
        # print(i)
        while num % i == 0:
            # print(i,'is prime')
            # print('num is ',num,'and i is ',i,)
            list_of_primes.append(i)
            counter_num += 1
            # print('counter name is ', counter_num ,'list is')
            num = num/i
            # print('now num would be',num)
            # باگ این برنامه اینه که اگر به عدد اول رسید نمیاد اضافه کنه
            # خوب چطور اضافش کنم ؟
        # elif num%i != 0:
    return numx , counter_num , list_of_primes 

# مقایسه برونداد یک تابع که چند بار ورودی بگیره 
# . و بعد اینجا اونی که بزرگتره را میده
def biger_def():
    # برای مقایسه تاپل باید صفر بدی که جایگزین بشه . به تعداد گمون کنم
    tup = (0,0,0)
    for i in range(1, 3):
        num2 = int(input(' give me the number: '))
        # print (((counter_prime(num2))))
        # اینجا درون یه تابع دیگر یه تابع را بکار بردم که همن تابع دوم هستش. 
        # که اگر صرفا دو تاپل بود num2 همون naaam میشد
        naaam =(((counter_prime(num2))))
        if naaam[1] > tup[1]:
            tup=naaam
        elif naaam[1]== tup [1]:
            if naaam[0]>tup[0]:
                tup=naaam
    return('behtarin ine: ',tup)
print(biger_def())

# /////////////
def small():
    zi=input('')
    lowerer= [char.lower() for char in zi]
    return lowerer 
# در حلقه فور اون اسمال را دوباره بکار بردم
def empty():
    empty=''
    small = 'edaoif'
    vowl = ['a','e','o','i','u']
    for char in small():
        # name=''.join(lowerer)
        if char not in vowl:
            empty += char
    return (empty)

# ///////////////

    

# df



# /////////////////


# تابع تودرتو چگونه بکار میره؟

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# اینجا به تابع میک مقدار ۳ داده
# Multiplier of 3
times3 = make_multiplier_of(3)

# اینجا به تابع میک مقدار ۵ داده
# # Multiplier of 5
times5 = make_multiplier_of(5)


# اینجا چون به تابع تایم ۳ دداده بود و الان ۹ داده ۹ میره جای تابع داخلی
# # Output: 27
print(times3(9))

# به همین ترتیب ۳ میره جای تابع داخلی...
# # Output: 15
print(times5(3))

# یعنی اونی که دوم داده میره جای تابع داخلی 
# و ما تابع داخلی را مستقیم ارجاع نمیدیم


print(times5(times3(2)))
# # Output: 30

# اینجا تایمز ۳ میشه ۳ داخلیش میشه ۲ میشه ۶
# حالا تایمز ۵ میشه ۵ ضربدر داخلیش که ۶ هست میشه ۳۰

# نکته . نمیشه تابع دوم را خارج از اون تابع صدا کرد
# یعنی فقط تابع اول را میشه 

# دوم اگر داخل بجای ایکس بزنیم مساوی و بعد اینتپوت بگیریم فقط ضرب میکنه 

def make_multiplier_of(n= int(input(' give me the  first number: '))):
    def multiplier(x= int(input('give me the second number: '))):
        return x * n
    return multiplier
a =(make_multiplier_of())
print(a)
# <function make_multiplier_of.<locals>.multiplier at 0x000001C813EED790>
# حالا چجوری خروجی بگیریم؟


# /////////
# ایا همینو میشه به داخلش هم ارجاع داد و نوشت ؟
# ایا همینو میشه در دو تابع نوشت؟
# //////////////
# بازی کن باهاش



# //////
# Python program to count number of items
# in a dictionary value that is a list.
def main():
    # defining the dictionary
    d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'B': 34,
         'C': 12,
         'D': [7, 8, 9, 6, 4]}
    # using list comprehension
    print(sum([len(d[x]) for x in d if isinstance(d[x], list)]))
if __name__ == '__main__':
    main()

# /////////////////////////

# چطور یه لیستی از فانکشن ها را صدا بزنه 
# اول همه را داخل یه لیست کن
functions = [function_one, function_two, function_three, ...]
# تعداد فانکشن ها را نوشته اینجا

n = int(input('Number: '))
for i in range(n):
    functions[i]()
# اینجا فانکشن اي ام را صدا میزنه 

# حالا
# اپراتور ماجول درصد را بکار بردن:
# گمون کنم میاد از عقب میره جلو
n = int(input('Number: '))
for i in range(n):
    functions[i % len(functions)]()
# ///////////////////////////////////////////////

    
# /////////////



# /////////

print('//////////')
# چجوری باید یه عدد را که از تابع میگیریم لیست کرد؟
# def f(a):
#     return a*5
# #فراخانی
# print(list(f(5))
# print(list(f(4))


print('//////////') #map
#[2, 4, 6]
#وقتی یه تابع را بخوایم رولیست اجرا کنیم نمیشه و باید مپ بیاریم
def double(a):
    return a*2
x=[1,2,3]
y=list(map(double, x))
print(y)


print('////////////')
#دوتا ورودی گرفتن
#200
def f(a,b):
    return a*b
print(f(100,2))

print('////////////')#lamda
#30
def add(x, y):
      return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 0

print(do_twice(add, a, b))

# ////////
#20
g=lambda a:a*5
print(g(4))

print("////////")#lamda
#دوتا متغیر
#200
g=lambda a,b:a*b
print(g(100,2))


print("////////")

x = lambda a : a + 10
print(x(5))


print("////////")

x = lambda a : a + 10
print(x(5))

print("////////")

x = lambda a, b : a * b
print(x(5, 6))

print("////////")

def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
print(mydoubler(11))

print("////////")


def myfunc(n):
    return lambda a: a * n
mytripler = myfunc(3)
print(mytripler(11))

print("////////")


# 2
# 3
# 4
# 5
# 6
# 7
# 8

def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

print("////////")
#کلید دیکشنری را برابر لامبدا قرار داده
#بنابر کوچکترین به بزرگترین سورت میکنه . در values ha
    # lambda is: {'e': 12, 'a': 23, 'g': 67, 45: 90}

    my_dict = {'a': 23, 'g': 67, 'e': 12, 45: 90}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    print("Sorted dictionary using lambda is : ", sorted_dict)



# ///////////
# اگر بجای پرینت بزاریم ریترن اون موقع به اولین ریترینی که خورد بر میگردونه 
# یعنی اصلا دیگه کار نمیکنه
def find_biggest ():
    what= int(input('give me the number: '))

    while what != -1:
        biggest=0
        the_second= 0
        if what > biggest :
            the_second=biggest
            biggest= what
            return ('the second is ',the_second ,'the biggest is', biggest)
        elif what< biggest and what > the_second:
            the_second=what
            print ('the second of elif ',the_second ,'the biggest of elif  is', biggest)

        what= int(input('give me the number2: '))
    return ('the big number is ', biggest , 'and sec number is : ',the_second)

print (find_biggest())



# ///////////

# نکته در تابع های چند تایی نباید دوباره صدا بزنی .
# یه بار فقط صدا میخوره اگر سلسله زنجیر وار هستشش

# def(1)
# def(2)
# def(3)

print(def3)
# برای فراخوانی کافیه فقط ۳ را
# صدا بزنی و اون موقع
# اگر ۳ به یک و دو متصل باشه میاد پشتش


# //////////
# ونکته 
# اگر یه عالمه تابع پشت سر هم داشتیم می تونیم تابع را
# بیاریم اینپوت داخل یکیشون بیاریم ولی تا وقتی که
# یکیشو صدا نزدیم هیچکدوم فراخوانی نمیشن


# ///////////////////////

# تابع معیار گیری واژه ها در یک استرینگ تازه 
# روش ایجابی
# اون واژه هایی که معیار است را دور میندازه

def p_criterion (criterion  ,test_item ):
    positive_Gained=''
    for char in test_item:
        if char not in criterion:
           positive_Gained += char
    return (positive_Gained)
# فراخوانی
test2='rtyuieop'
cri2='a','o','i','u'
a= p_criterion(cri2,test2)
print(a)
# rtyep

# تابع معیار گیری واژه ها در یک استرینگ تازه 
# روش سلبی
# اون واژه هایی که معیار است را دور میندازه

def n_criterion (criterion ,test_item ):
    for char in test_item:
        if char in criterion:
            # ریپلیس میتونه یه متد حذف کردن هم باشه .
            # یعنی بگیم جایگزین کن با هیچی یعنی حذف میشه دیگه
           test_item =test_item.replace(char,'')
    return (test_item)

test2='rtyuieop'
cri2='a','o','i','u','e'
a= n_criterion(cri2,test2)
print(a)
# rtyp

# ///////////////////////////////////


# تابع معیار گیری واژه ها در یک استرینگ تازه 
# بصورت سلبی
# اون واژه هایی که معیار است را نگه میداره

def su_criterion(critorion,test_item ):
    for char in test_item:
        if char not in critorion:
            test_item=test_item.replace(char, '')
    return(test_item)

right_test= 'ahhelllouu'
wrong_test= 'hlelo'

criterion= 'hello'


from criterion_function import p_criterion , n_criterion, su_criterion

p= p_criterion(criterion,right_test)
print(p)

su= su_criterion(criterion,right_test)
print(su)

# hhelllo
# ////////////////


# نکته:
    # پس میشه فقط معیار ها را داد . و بعد کدش و حلقه و... شونو ریخت و بعدا 
    # موقع فراخوانی بهشون مقدار بدیم
def n_criterion (criterion  ,test_item ):
    negative_Gained=''
    for char in test_item:
        if char not in criterion:
           negative_Gained += char
    return (negative_Gained)
# فراخوانی
test2='rtyuieop'
cri2='a','o','i','u'
a= n_criterion(cri2,test2)
print(a)
# rtyep



# //////////////////////////////////////////////////////////
# نکته
# اگر  
# درون یه پازیتیو گیند بریزیم فقط یه دونشو میاره .
# باید داخل خودش ریپلیس کنیم تا همشو برگردونه
def n_criterion (criterion ,test_item ):
    positive_Gained=''
    for char in test_item:
        if char in criterion:
           test_item =test_item.replace(char,'')
    return (test_item)

test2='rtyuieop'
cri2='a','o','i','u','e'
a= n_criterion(cri2,test2)
print(a)
# rtyp


# /////////
# صدا زدن یک فانکشن از فایل دیگری که پیشتر ساختیم
# باید فایل کنار فایل ای که داریم میازیم باشه . توی همون فولدر
# بعد صداش بزنیم  
# from
# اسم فایل
# سپس
# import کن
# تابع را 

from criterion_function import p_criterion , n_criterion
test2='rtyuieop'
cri2='a','o','i','u'
# اینجا هم صداش میزنیم که متغیر هایی که توی همین فایل تعریف کردیم را
# بهش می دیم و میریزیم توی یه متغیر دیگر تا پرینت کنیم
p= p_criterion(cri2,test2)
print(p)
n= n_criterion(cri2,test2)
print(n)
# rtyep
# rtyep


# ////////////
# نکته میشه اسم یه پارامتر در تابع یه چیز باشه 
# در فراخوانی یه چیز دیگر
# /ولی باید همون ساختار را داشته باشه


def su_criterion(critorion,test_item):
    for char in test_item:
        if char not in critorion:
            test_item=test_item.replace(char, '')
    return(test_item)
su_criterion(apple,bnana)

# //////////////
# میشه در یه حلقه از وسط برش بزنه بقیه استرینگ را بره


# ////////////////
# تابع ها و اسم مستعار گذاشتن
# عوض میشه 
# نکته جادی را ببین . اخر درس لیست ها
# رابطه فانکشن و لیست
# تابع و لیست

# //////////
# کی یک تابع را در خروجی می ده NoNE? 

# //////////
# فراخوانی و نوشتن تابع . میشه ورودی را در خود تابع گذاشت و فراخوانی را اجرا کرد که بعد خودش  بعدا ورودی بگیره
def bigger_number (number1=int(input('Give me the first number:')) , number2=(int(input('give me the second number:')))):
    if number1>number2:
        return (number1)
    else:
        return(number2)

print(bigger_number())

# ////////////////////////
# اگر در فراخوانی حتی اگر ورودی بدیم هم  اونی که قبلا نوشته شده را مد نظر قرار میده
def bigger_number (number1=int(input('Give me the first number:')) , number2=(int(input('give me the second number:')))):
    if number1>number2:
        return (number1)
    else:
        return(number2)

print(bigger_number(2,8))
# Give me the first number:45
# give me the second number:32
# 8
# در اینجا ۲ و ۸ را معیار میده و نه ۴۵و ۳۲ را. 

# ///////////////
# اگر پرینت را در خود تابع نوشته باشی دیگه نیاز نیست پرینت را بنویسی در  فراخوانی و خود تابع فراخوانی شده را در متغیر دیگر بنویسی 

def age_of__the_person(age):
    if age >0 and age <6:
        print('khordsal')
    elif age >= 6 and age < 10:
        print('koodak')
    elif age >=10 and age <14:
        print('nojavan')
    elif age >= 14 and age < 24:
        print('javan')
    elif age >=24 and age <40:
        print('bozorgsal')
    elif age >= 40 :
        print('miansal')
age_of__the_person(13)

# تازه اگر پرینت بزنی خروجی none  میده
print (age_of__the_person(13))
# nojavan
# None


# ///////////
# میشه بجای پرینت  از اول ریترن را گذاشت که بعدش در فراخوانی هیچی نمیاره حتی اوناسترینگ که چاپ کرده را
def age_of__the_person(age):
    if age >0 and age <6:
        return('khordsal')
    elif age >= 6 and age < 10:
        return('koodak')
    elif age >=10 and age <14:
        return('nojavan')
    elif age >= 14 and age < 24:
        return('javan')
    elif age >=24 and age <40:
        return('bozorgsal')
    elif age >= 40 :
        return('miansal')
(age_of__the_person(13))
# اینجا هیچی پرینت نمیکنه

# باید پرینت گذاشت
# تا بتونه ریترن های درون تابع را پرینت کنه .
print((age_of__the_person(13)))
# nojavan
# ///////////

# اگر درون تابع پرینت هستش دیگه نباید پرینت گذاشت در فراخوانی 
# چون 
# none 
# میده
# وگرنه اگر ریترن هست باید پرینت کنی .
def compare_function():
    compered='hello'
    if naked() == compered:
        print('NO')
    else:
        print('YES')
# وضع پرینت و فراخوانی . اگر پرینت بزاری  نان میده چون در بالا یه بار دادی
# پس نباید پرینت بزاری اینجا
(compare_function())

# ////////////
# //////////////////////////////////////

# فراخوانی از فایل دیگر
from file import function
function(a, b)

# اگر میخوای دو تا  تابع در فایل دیگر را بیاری
def f():
      return 1

def g():
  return 2
from file_a import f, g

# ////////////

# اگر در فایل ها و پکیج های دیگر بود
com.my.func.DifferentFunction

def add(arg1, arg2):
    return arg1 + arg2

def sub(arg1, arg2) :
    return arg1 - arg2

def mul(arg1, arg2) :
    return arg1 * arg2

from com.my.func.DifferentFunction import *
# یا هر کدومو جدا تعریف کن
from com.my.func.DifferentFunction import add, sub, mul


# ////////////
# مشکلی که داره اینه که  دوبار میاد ورودی را میاره
#  یه بار خود ورودی و یه بار برای پرینت . ولی ما نمیخوایم به محض ورود بیاره بخونه میخوام فراخوانی کنیم
from excersise5 import bigger
print(bigger())
پاسخ 
# چون توی فایل شما کل فایل را اوردی  اگر پایین تعریف اون تابع دو بار اون تابع را اورده باشی ( حتی برای فراخوانی ) 
# اون موقع دو بار هم بالا میاره در این یکی فایل 

# ///////////////////////////
# کاربرد دو تابع  در دو فایل جدا با هم در یک فایل سوم
# second_big : with the method of 2 functions
from excersise4 import secound
from excersise3 import biggest

# print(secound())
# print(biggest())
# اینجا تعین میکنی فقط خروجی دو تابع را بررسی کنه   
if secound()> biggest():
    print('second')
else:
    print('biggest')
    
# ////////

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

# //////////////////

def main():
       print("calling function from for loop")

# for loop
for i in range(5):

   # python function call from for loop
   main()
# calling function from for loop
# calling function from for loop
# calling function from for loop
# calling function from for loop
# calling function from for loop

# ////////////////////////////////////////////
# کاربرد تابع در حلقه وایل

def main():
   print("calling function from while loop")
num = 0https://www.golinuxcloud.com/wp-admin/admin.php?page=eos_dp_by_post_type
# while loop
while num<5:
   # python function call from for loop
   main()
   # increase num
   num +=1
# calling function from for loop
# calling function from for loop
# calling function from for loop
# calling function from for loop
# calling function from for loop

# ////////////
# خواندن یه تابع در یک حلقه
# این سه بار  همون یک چیز را چاپ میکنه
mylist=[]
a=prime_number()
for i in range (3):
    mylist.append(prime_number())
    print(mylist)
# [(672, 24)]
# [(672, 24), (672, 24)]
# [(672, 24), (672, 24), (672, 24)]

# //////////////
# کاربرد  تابع درون حلقه که اعضای حلقه را مقایسه کنه
# نکتش اینه که نباید توی تابع بنویسی بلکه باید بیرون از تابع و زیرش بنویسی
def prime_number ():
    number= int(input('give me the number for testing: '))
    The_Number=number 
    
biggest=[0,0]
for i in range (2):
    a= prime_number()
    print(a[1])
    if a[1] > biggest[1]:
        biggest=a
    print('the biggest is',biggest , 'yet')

# give me the number for testing: 672
# 24
# the biggest is (672, 24) yet
# give me the number for testing: 148886
# 16
# the biggest is (672, 24) yet

# توجه شود که  فقط هر بار که فراخوانی یه
# تابع میاد خودش  میخونه حتی اگر برای پرینت باشه.add()پس بهتره همون اول اونو تو یه متغیر بریزی مثل 
# a در بالا
# یعنی بجای بالا اگر اینو مینوشتیم باید این ورودی را میدادیم
biggest=[0,0]
for i in range (2):

    print(prime_number()[1])
    if prime_number()[1] > biggest[1]:
        biggest=prime_number()
    print('the biggest is',biggest , 'yet')
# give me the number for testing: 68
# 6
# give me the number for testing: 569
# give me the number for testing: 444
# the biggest is (444, 12) yet
# give me the number for testing: 415
# 4
# give me the number for testing: 551
# the biggest is (444, 12) yet


# ///////////////////
# کاربرد سلسله ای تابع ها

def clean (the_word,compare_word=['i','j','o','u','e','a']):
    for i in the_word:
        for j in compare_word:
            if i== j:
                the_word=the_word.replace(i,'' )
    return(the_word)

def del_word(del_word):
    for xhar in del_word:
        del_word=del_word.replace(xhar,('.'+xhar))
    return(del_word)

def smalize (xapital_word):
    xapital_word=xapital_word.lower()
    return xapital_word
# چطور می تونم به ساده ترین حالت سلسله ای بکار ببرم؟
my_word='DfaGeloKisu'
my_word_2=(clean(my_word))
my_word_3= (del_word(my_word_2))
my_word_4= (smalize(my_word_3))
print(my_word_4)

# یا راه ساده تر
# راه حل اینه که از اخر به اول بیاری . یعنی اونی که میخوای پس از همه بکار بیوفته را اول بنویسی و در دل اون اونیکی تابع را 
# بیاری که بگی خروجی این تابع بشه ورودی اون تابع
my_word_5=smalize(del_word(clean(my_word)))
print(my_word_5)
# .d.f.g.l.k.s

# /////

# اگر میخواستیم همونو تو یه تابع بیاریم چی؟ یعنی زنجیر میشدن و ترکیب ماژول نمیشدن چی؟
# میتونی به عنوان پیشفرض تعریف کنی
my_word='DfaGeloKisu'
def clean (the_word,compare_word=['i','j','o','u','e','a']):
    for i in the_word:
        for j in compare_word:
            if i== j:
                the_word=the_word.replace(i,'' )
    return(the_word)
# my_word_2=(clean(my_word))

def del_word(del_word=clean(my_word)):
    for xhar in del_word:
        del_word=del_word.replace(xhar,('.'+xhar))
    return(del_word)


def smalize (xapital_word=del_word()):
    xapital_word=xapital_word.lower()
    return xapital_word

print(smalize())
# //////////

# یه راه دیگه اینه که بیایم پیشفرض تعریف نکنیم 
# بلکه اون تابع را مساوی قرار بدیم درون تابع دیگر با یه متغیر
# تابع حذف حروف بی صدا
def clean (the_word,compare_word=['i','j','o','u','e','a']):
    for i in the_word:
        for j in compare_word:
            if i== j:
                the_word=the_word.replace(i,'' )
    return(the_word)
# my_word_2=(clean(my_word))

# فقط به شرط اینکه به اسمهمون متغیر بیاری 
# اینجا مای ورد بود بعد متغیر هم به همون اسم باشه که بتونه یکی بشه
def del_word():
    del_word=clean(my_word)
    for xhar in del_word:
        del_word=del_word.replace(xhar,('.'+xhar))
    return(del_word)


def smalize ():
    xapital_word=del_word()
    xapital_word=xapital_word.lower()
    return xapital_word
my_word='DfaGeloKisu'
# اگر این اسم مای ورد هرچیز دیگری بود باز نمیشد . فقط همون اسمی که توی کاربرد تابع کلین  بالا گذاشتی 
print(smalize())


# //////

# ترکیب دو تابع با هم 
# اینجوری که میاد دو تابع را میاره . هر کدوم 
a= '3+2+1+4'  #input('give it to me: ')
def sort_eliminate(sentence_number):
    sentence_number=sorted(sentence_number.replace('+','' ))
    return sentence_number
print(sort_eliminate(a))

def join_sort(number_list):
    number_list='+'.join(number_list)
    return number_list

# یعنی درون تابع سوم ترکیب دو تا دیگه را میاره
# حالا در این تابع ترکیب دو تابع را اجرا می کنیم
# تابع اجرای ترکیب
def somaie(my_sentence):
    somaie= (join_sort(sort_eliminate(my_sentence)))    
    return(somaie)
# اینجا اخری را فراخوانی میکنیم . اخری درون خودش بقیه را داره
# و جالبه درون خود این تابع تابع دیگری میاد که اون تابع هم تابع دیگری داره 
# اون تابع دیگر داده اولی را میگیره که در تابع اخری نوشته

# مای سنتس درون سورت الیمینیت هست . و سورت الیمینیت که جوین سورت را داره 
print(somaie(a))

# /////////////////

def standard ():
    names_list=[]
    for i in range(1,3):
        name=input('give me the name: ')
        # جالبه نیازه که یه تابع درون یه 
        # تابع دیگه ریخته بشه تا کپیتالایز بشه ولی اگر 
        # دو تا تابع روش اچرا کنی نیاز نیست بریزی تو یکی دیگه
        # یعنی این نیاز نیست:
        # name=name.capitalize()
        # names_list.append(name)
        # بحاش همین یک خط میتونه راه بندازه
        names_list.append(name.capitalize())
    return names_list
# ////////
# توجه بشه که نمیشه اینجوری اینپوت را بنویسی به گمونم

def standard ():
    names_list=[]
    for i in range(1,3):
# توجه بشه که نمیشه اینجوری اینپوت را بنویسی به گمونم
        names_list.append(name=input('give me the name: ').capitalize())
    return names_list



# //////////

# نکته اگر در اینتپوت خود تابع دیگر را بنویسی خود واژه های اسمشو  پرینت میکنه 
# ولی چیزی که میخوام اینه که بیاد درون اون تابع را برگدونه . لیست اونو 
def bulid_in_function (myfunction = input('give me the function to invert a list: ')):
    for every in myfunction:
        print(every)
bulid_in_function()
# give me the function to invert a list: standard()
# s
# t
# a
# n
# d
# a
# r
# d
# (
# )

# یک راهش اینه:
# درون یه تابع  تابع دیگر را فراخوانی دادن
def bulid_in_function (a):
    myfunction=a
    for every in myfunction:
        print(every)
# یعنی بجای داده درون بیلد این فانکشن خود تابع را بنویسی
bulid_in_function(standard())
# give me the name: ghjnHUBJN
# give me the name: gbhjnGBHJN
# Ghjnhubjn
# Gbhjngbhjn


# باز مشکل حل نشده . من تابعی را میخوام که تابع بگیره
# ////////


# میشه متغیری را درون یه تابع دوباره در تابع دیگر بکار برد
# اینجا فرست را داد .
def counterer(first):
    big_count=0
    small_count=0
    for character in first:
        if character ==character.upper():
            # print(character,'iaftam')
            big_count+=1
        else:
            small_count+=1
    return big_count , small_count


# میشه متغیری را درون یه تابع دوباره در تابع دیگر بکار برد
# حتی با نام دیگر 
# در اینجا ما نام فرست را دادیم سک و باز هم کار کرد
def big_smaler(sec):
    # این نوع نوشتن میشه در تاپل ها هم باشه . متغیر نخست اون تاپل با متغیر دوم مقایسه بشه
    if counterer(sec)[0] >counterer(sec)[1]:
        sec = sec.upper()
    else:
        sec = sec.lower()
    
    return sec

# حتی میشه اسم سومی هر دو را داد. 
# یعنی فرست همون سک است و ای همون فرست و سک در کاربرد
a='HasTam'

print(big_smaler(a))


# ////////////
# print (my_reverse(half_string(vorodi)[1]))
# میشه در یک تابع خروجی دو تابع را با هم مقایس کرد.
# حتی بخشی از خروجی دو تابع را مقایسه کرد
# حتی یه  بخش تابع از یه فایل دیگر را با یه
# الزامی نیست که اسم های متغیر ها یکی باشه. فقط جاشون باید درست باشه
vorodi='madam'
def half_string (ino):
    if (len(ino)) %2==0:
        # print('even')
        my_half1=ino[len(ino)//2:]
        my_half2=ino[:len(ino)//2]
        return my_half2 , my_half1
    else:
        # print('odd')
        my_half1=ino[len(ino)//2:]
        my_half2=ino[:len(ino)//2+1]
        return my_half1,  my_half2


# print(half_string(vorodi))
# از یه فایل ایمپورت بگیر که کنارشه
# from excersise9 import my_reverse
# این همونه که در فایل دیگر است
# def my_reverse(my_string):
#     my_string=my_string[::-1]
#     return (my_string) 



# print (my_reverse(half_string(vorodi)[1]))
# میشه در یک تابع خروجی دو تابع را با هم مقایس کرد.
# حتی بخشی از خروجی دو تابع را مقایسه کرد
# حتی یه  بخش تابع از یه فایل دیگر را با یه
# الزامی نیست که اسم های متغیر ها یکی باشه. فقط جاشون باید درست باشه
def compare (the_word):
    
    # حتی میشه بگی از یه تابع یه تابع دیگر را بیار یه کاری رو متغیرش انجام بده
    # تابع های تودرتو
    if half_string(the_word)[0]== my_reverse(half_string(the_word)[1]):
        print('palindrom')
    else:
        print('not palindrom')
 
compare(vorodi)
       

# ////////////

# انگار نمیشه ورودی یه تابع همون خروجی تابع دیگر باشه . 
# یعنی این شکلی
def ghadr_motlagh(norozi()):
# پس یا
# باید بیاری درون تابع و یه متغیر تعریف کنه  

def ghadr_motlagh():
    alfa=norozi()
# اگر در ترکیب دو تابع خروجی تابع نخست که باید در تابع دو استفاده بشه یک لیست باشه
# دیگه نباید نوشت 
# alfa()[]
# بلکه باید نوشت
# alfa[1]
    first =alfa[1]-alfa[0]
    second=alfa[2]-alfa[1]
    ghadr = first+second
    return ghadr
print (ghadr_motlagh())


# ///////////
# اگر هم بیای تابع را درون خودش یه هم تعریف کنی 
# هر بار که بر بخوره  که یه تیکشو بکشه بیرون دوباره اجراش میکنه
# یعنی
# منتها اگر متغیر داده باشی  درون پرانتز مستقیم میشه

def ghadr_motlagh():
    first =norozi()[1]-norozi()[0]
    second=norozi()[2]-norozi()[1]
    ghadr = first+second
    return ghadr
print (ghadr_motlagh())
# give me: 6 9 10
# give me: 6 9 10
# give me: 6 9 10
# give me: 6 9 10
# 4


# ///////
# برای اجرای یک تابع درونی برای مپ  و ابس
# فقط یه بار میاره
a= norozi()
print (list(map(abs,a)))
# [6]


# ///////////

# انگار نمیشه ورودی یه تابع همون خروجی تابع دیگر باشه . 
# def ghadr_motlagh(norozi()):
# پس یا
# باید بیاری درون تابع و یه متغیر تعریف کنه  

# /////////////
# سعی کن بیشتر تابع پیشین را به عنوان متغیر تعریف کنی درون خود تابع 
# و هم خود تابع را معمولا خالی بزار
def checking():
    my_list=tedad()
    
# ////////////

# ترکیب فایل با تابع 
# تابع های دو تایی در اول
import csv
# نوع دیگ  اوردن فایل و خروجی گرفتن
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as fi:
    
    # یعنی میشه ادرس فایل را در تابع نوشت
    # ترکیب تابع و کار با فایل ها
        khandan = csv.reader(fi)
        with open(output_file_name, 'w', newline='') as nomre:

# ورودی تابع اولی میشه که همون ورودی و خواندن فایل اولی است
# خروچی چی؟
# چرا رید را در اولی ننوشته ؟
# چرا تابع خروجی را در  همون اول نوشته ؟ چون متا معمولا ریترن میکنیم تازه اونم معلوم نیست




# /////////////////
# کار با فایل ها در تابع 
def kar(input_file):
    with open (input_file,'a+' ) as my_file:
        my_file.write('hello')
        return ((my_file.read()))
print(kar('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\mean.txt')()) 
# اینو در پرینت خطا میده ولی در  فایل کارشو انجام میده
# TypeError: 'str' object is not callable

# ////////////
# توجه اگر ریترن نکنی 
# none 
# میده

# ////////////
import csv
def moadel(input_adress):
    with open (input_adress,'r') as vorodi:
        new_vorodi=csv.reader(vorodi)
        return new_vorodi
print(moadel('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\csv-mean.csv'))
# <_csv.reader object at 0x0000024CAF4E2A40>

#  محتوای فایل را بهمون برنمیگردونه 
# ///////////
# اگر در حلقه هم بندازیم میاد اولی را فقط برمیگردونه 

import csv
def moadel(input_adress):
    with open (input_adress,'r') as vorodi:
        new_vorodi=csv.reader(vorodi)
        for char in new_vorodi:
            return char
        # return new_vorodi
print(moadel('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\csv-mean.csv'))
# ['mandana', '5', '7', '3', '15', '', '', '', '', '', '', '', '', '', '', '']

# /////////////
# ولی اگر پرینت کنیم نشون میده 
# منتها بقیه خالی ها را هم کاراکتر میگیره

# پس باید در حلقه بندازی تا در تابع نشون بده
import csv
def moadel(input_adress):
    with open (input_adress,'r') as vorodi:
        new_vorodi=csv.reader(vorodi)
        for char in new_vorodi:
            print (char)
        # return new_vorodi
print(moadel('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\csv-mean.csv'))

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
# []
# []
# []
# []
# []
# []
# None

# ///////////////////////////
# اگر در حلقه نندازیم 
import csv
def moadel(input_adress):
    with open (input_adress,'r') as vorodi:
        new_vorodi=csv.reader(vorodi)
        print(new_vorodi)
        # return new_vorodi
print(moadel('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\csv-mean.csv'))
# <_csv.reader object at 0x0000024080CAF1C0>
# None

# ////////
# کدهای عددی چیه در فراخوانی ریترن یک فایل ؟
# 604

# ////////

# میشه یه تابع دف را 
# به عنوان ارگومان تابع  درونی  گرفت
# و برعکس؟

def remove_empty_strings(string):
    return string != ""
 
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]
# در اینجا تابع درونی که تشخیص هرچیزی که خالی است هستش
# روی تست لیست میره
# و بعد اونو فیلتر میکنه فیلتر
filtered_list = filter(remove_empty_strings, test_list)
print(list(filtered_list))  # Output: ['GeeksforGeeks', 'is', 'best']


# ////////


# ازمایش 
# این کار نمیکنه
# در تابع دوم کار نمیکنه میگه باید بهم اسم فایل بدی 
# این مساله ای برای تابع ها است
# راهکار ها جلوتر
import csv
from statistics import mean

def calculate_averages(input_file_name):
    with open (input_file_name, 'r') as Reader :
        my_Reader= csv.reader(Reader)
        roder=list(my_Reader)
        return(roder)
def dictionary_av():
    roder=calculate_averages()
    my={}
    for charr in roder:
        while '' in charr:
            charr.remove('')
        for harf in charr:
            my[charr[0]]=mean(list(int(x) for x in charr[1:]))
    return (my)
def csw_writter(output_filename):
    with open (output_filename,'w',newline='') as neveshtan:
        khandan= dictionary_av()
        mywrit=csv.writer(neveshtan)
        mywrit.writerows(khandan.items())

calculate_averages('E:\.python and every thing\codes and projects\exer\csv-mean.csv')
csw_writter('E:\.python and every thing\codes and projects\exer\csv-mean6.csv')


# راهکار
# ایا میشه که بیایم بالاترش بدیم بهش؟
# یعنی بالای تابع ؟
# بازهم
#نمیشه میگه نه و انگار چیزی بهش ندادی
# TypeError: calculate_averages() missing 1 required positional argument: 'input_file_name'

import csv
from statistics import mean
def calculate_averages(input_file_name):
    with open (input_file_name, 'r') as Reader :
        my_Reader= csv.reader(Reader)
        roder=list(my_Reader)
        return(roder)
calculate_averages('E:\.python and every thing\codes and projects\exer\csv-mean.csv')
def dictionary_av():
    roder=calculate_averages()
    my={}
    for charr in roder:
        while '' in charr:
            charr.remove('')
        for harf in charr:
            my[charr[0]]=mean(list(int(x) for x in charr[1:]))
    return (my)


# اما اینم اگه اینجوری بنویسی هم باز همون خطا را میده
a='E:\.python and every thing\codes and projects\exer\csv-mean.csv'
calculate_averages(a)
# TypeError: calculate_averages() missing 1 required positional argument: 'input_file_name'
#
# 
# اما این  کار میکنه
# یعنی درون تابع دوم بدی 
def calculate_averages(input_file_name):
    # ..........

a='E:\.python and every thing\codes and projects\exer\csv-mean.csv'
def dictionary_av():
    roder=calculate_averages(a)



# یا اینکه ادرس را درون دومی بنویسی
# که بازهم فرقی نداره
# و این کار میکنه
def calculate_averages(input_file_name):
    with open (input_file_name, 'r') as Reader :
        my_Reader= csv.reader(Reader)
        roder=list(my_Reader)
        return(roder)
def dictionary_av():
    roder=calculate_averages('E:\.python and every thing\codes and projects\exer\csv-mean2.csv')
    my={}
# و ادامه



# یا اگر اینم اینجوری بنویسی باز خطا میده میگه چنین چیزی وجود نداره
def calculate_averages(input_file_name):
    with open (input_file_name, 'r') as Reader :
        my_Reader= csv.reader(Reader)
        roder=list(my_Reader)
        return(roder)

def dictionary_av():
    roder=calculate_averages(input_file_name)
    # اینجا میگه 
    # input_file_name
    # وجود نداره

# نکته 
# جالبه اگر بلاایی را بهش چیزی داده باشی پایین درون تابع دیگر میتونی خالی بزاری و همون را میخونه 
# همونجوری که اگر درون تابع دوم ادرس فایل را بزاری دیگه درون تابع اول دیگه نیاز نیست  ادرس را بدی بلکه درون فایل اول خالی بازر
# تا حالا دانش من اینه



# پس باید برای هر کدام بالاش تعریفش کره باشی که پایین میرسه اونو اجرا کنه
# میتونی همون اول بنویسی ادرس فایل را یا اینپوت کنی
# در صورتی که بالا اینپوت کردی دیگه نیاز نیست پایین اینپوت بشه
import csv
from statistics import mean
def calculate_averages(input_file_name=input()):
    with open (input_file_name, 'r') as Reader :
        my_Reader= csv.reader(Reader)
        roder=list(my_Reader)
        return(roder)

def dictionary_av():
    roder=calculate_averages()
    my={}
    for charr in roder:
        while '' in charr:
            charr.remove('')
        for harf in charr:
            my[charr[0]]=mean(list(int(x) for x in charr[1:]))
    return (my)
def csw_writter(output_filename):
    with open (output_filename,'w',newline='') as neveshtan:
        khandan= dictionary_av()
        mywrit=csv.writer(neveshtan)
        mywrit.writerows(khandan.items())
calculate_averages ()
csw_writter('E:\.python and every thing\codes and projects\exer\csv-mean6.csv')


# نکته معیار عمل را با فایل بالاتر قرار میده 
# یعنی پایین را میتونی اسم فایل بدی یا حتی خالی بدی فرق نداره اونی که بهش بالا دادی را حساب میکنه
# 

# نکته اگر مقدار پیشفرض هم بازری در مورد فایل ها و ادرس دان فایل ها کار نمیکنه
calculate_averages ('E:\.python and every thing\codes and projects\exer\csv-mean.csv')

# و موقع فراخوانی بدی 2
calculate_averages ('E:\.python and every thing\codes and projects\exer\csv-mean.csv')

# اون موقع  فایل ۱ را میاره اجرا میکنه توی خروجی نه فایل ۲ را

# /////
# یعنی واقعا نمیشه در بالا اسم متغیر کلی داد و فایل را بعدا بهش داد؟
# //////////
# تغیر داده پیشفرض
# ایا ادرس پیشفرض دادن میشه؟ یعنی بالا اونو بخونه ولی پایین که میاد عوضش کنه؟
# اینجا اسم مارک را به عنوان پیشفرض لست نیم تعریف کرده
def student(firstname, lastname='Mark', standard='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')


# 1 keyword argument
student(firstname='John')

# 2 keyword arguments
student(firstname='John', standard='Seventh')

# 2 keyword arguments
# اینجا لست نیم را چیز دیگر گذاشته
student(lastname='Gates', firstname='John')
John Mark studies in Fifth Standard
John Mark studies in Seventh Standard
John Gates studies in Fifth Standard
# ////////////
# حالا ایا میشه داده پیشفرض تعریف کرد ولی اگر همه چی درست باشه همون پیشفرض را بده و از ما بپرسه کدومو میخوای عوض کنی
# و سپس عوض کنه



# //////////
# این کد دو بار  از ما میپرسه  هرچند زده رنج ۳
# بخاط راینکه دو بار فراخوانی کردی یه بار درون کلاس یه بار بیرون از کلاس
class A:
    def __init__(self,ghad,vazn,sen):
        self.ghad=ghad
        self.vazn=vazn
        self.sen=sen
# کدی که بیاد به اندازه تعداد اعضا را درون لیست کنه
    @staticmethod
    def miangin():
        # mynumber=int(input('give me the number:'))
        for i in range(3):
            ghad=[int(i) for  i in input('give me the ghad numbers: ').split()]
            vazn=[int(i) for i in input('give me the vazn: ').split()]
            sen=[int(i) for i in input('give me the sen: ').split()]
            print ('',ghad,'\n',vazn,'\n',sen )  
    miangin()
    
A. miangin()

# /////////////

# نکته 
# باید ترتیب ها را درست نوشت در یک تابع  مثلا اگر
# به ترتیب ورودی میگیری باید در ریترن هم به ترتیب ورودی بدی

from statistics import mean
class A:
    def __init__(self,ghad,vazn,sen):
        self.ghad=ghad
        self.vazn=vazn
        self.sen=sen
    @staticmethod
    def miangin():
        mynumber=int(input('give me the number of whole:'))
        # for i in range(3):
        sen=mean([float(i) for i in input('give me the sen: ').split()])
        ghad=mean([float(i) for  i in input('give me the ghad numbers: ').split()])
        vazn=mean([float(i) for i in input('give me the vazn: ').split()])
        return (ghad,vazn,sen)  
class B(A):
    pass

# ترتیب را از پیش از این بهم میریزه کلاس
# من اول سن را وارد میکنم بعد قد را بعد وزن را 
# اون چیزی که اول میده بیرون 
# اول قده بعد وزنه بعد سنه
# چکار کنم که اینو بیاد درست کنه؟

my_A=A
my_aa=(my_A.miangin())
my_Aa=dict(enumerate(my_aa))
print(my_Aa)

my_B=B
myBb=(my_B.miangin())
mybb=dict(enumerate(myBb))
print(mybb)

def comparable():
    if my_Aa[1]> mybb[1]:
        print('A') 
    else:
        if my_Aa[1]==mybb[1]:
            if my_Aa[2]<mybb[2]:
                print('A')
            else:
                if my_Aa[2]>mybb[2]:
                   print('B') 
                else:
                    print('Same')
                print('B')
        else:
            print('B')

            
for charA  in my_Aa:
    print(my_Aa[charA])
for charB  in mybb:
    print(mybb[charB])

# اینجا خروجی را نوشتم درسته که به ترتیب سن و قد و وزن میزنیم ولی بعد به ترتیب نمیاد
# give me the number of whole:5
# give me the sen: 16 1
# 7 15 16 17
# give me the ghad numbers: 180 175 172 170
# 165
# give me the vazn: 67
# 72 59 62 55
# {0: 172.4, 1: 63.0, 2: 16.2}
# give me the number of whole:5
# give me the sen: 15 1
# 7 16 15 16
# give me the ghad numbers: 16 156 168 170 1
# 62
# give me the vazn: 45
# 52 56 58 47
# {0: 134.4, 1: 51.6, 2: 15.8}
# 172.4
# 63.0
# 16.2
# 134.4
# 51.6
# 15.8

comparable()
# A

# پاسخ
# موقع  گرفتن درسته که ردست گرفته بودیم ولی در ریترن ترتیب را جابجا زده بودیم
def miangin():
        mynumber=int(input('give me the number of whole:'))
        # for i in range(3):
        sen=mean([float(i) for i in input('give me the sen: ').split()])
        ghad=mean([float(i) for  i in input('give me the ghad numbers: ').split()])
        vazn=mean([float(i) for i in input('give me the vazn: ').split()])
        return (sen,ghad,vazn)  
    # بجای 
    # return (ghad,vazn,sen)

# //////////
post=y
price=x
# جاالبه درون تابع اگر متغیری را تعریف نکرده باشی
# میتونی بعدش درون تابع دیگر استفاده کنی حتی اگر جزو ورودی اول تابع  دوم نباشه
def two_list_dict(key_list,value_list):
    # ببین اینجا فقط دو تا ورودی گرفته ولی فقط از این دو تا استفاده نکرده بلکه متغیر های دیگری هم استفاده کرده
    
    mydict={}
    shuffle(key_list)
    shuffle(value_list)  
    # پرایس و  پست را در ورودی تابع نیاوردیم ولی چون بالاتر در خط های ساده 
    # یعنی به غیر از درون تابع  بیاریم میشه تعریف بشه
    # ولی اگر این دو تا درون تابع ای باشند که فقط خروجی میده و اون خروجی پرایس و پست نباشند نمیشه استفاده کرد درون تابع
    
    # پس ما میتونیم هر متغیر معمولی را هم از بالای تابع بگیریم
    for key, value ,j, k in zip((key_list),(value_list),(price),(post)):
            mydict [key]=(value,j,k)
    return mydict
mydict=(two_list_dict(m_players,myplayerlist))
print(mydict)

# ////////////////////////////////////
# decorator







# ////////
# ؟؟؟؟؟؟؟؟؟؟؟
# تغیر داده های پیشفرض
def database_builder(host='localhost' ,user='root', password='mamad951219644002@',databasename=input('give me the name of database: ') ):
    import mysql.connector
    db=mysql.connector.connect(host= 'localhost', user='root', password='mamad951219644002@')
    mycursor=db.cursor()
    mycursor.execute(f'CREATE DATABASE {databasename}')
database_builder()
# حالا چطور باید اون مقادیر پیشفرض را عوض کنم
# یعنی همیشه این باشه ولی یک بار مثلا اسم یوزر را عوض کنم و یا اسم پسورود را عوض کنم
























