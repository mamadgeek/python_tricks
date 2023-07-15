# کد بزن 
# کد را توضیح بده
# حالت های مختلف را بزن

# ولی کتاب ننویس

# //////////
# ////////
# claass Attribute که بهش 
# variable  هم میگن 

# instance Attribute

# class method  = یعنی @decorator , @classmethod
# instance  method    = def self

# /////////

# ابجکت ها نمونه ای از کلاس هستند . اینستنس اون کلاس هستند
# کلاس مفهوم کلی است و ابجکت مصداق است
# فقط ما میسازیم انها را

# ////
# یه حالت  تعریف کلاس - تعریف ابجکت  یا همون اینستنس - تعریف اتریبیوت اینه
# شیوه افزایش خارج از دامنه کلاس
# کلاس خالی اینگونه تعریف میشه
class Human:
    pass    #بطور کلی هر کلاس که خالی باشد اینگونه تعریف میشه 
# تعریف ابجکت بر اساس کلاس  
p1= Human()
print(p1)
# <__main__.Human object at 0x00000194245702E0>
# میگه ابجکت ی از نوع کلاس داریم که 
# نشانی اش در حافظه اینه و فعلا 

# دادن خصوصیت  یا مشخصه
# atribute 
# به اون آبجت 
# اینگونه میشه

p1.name='ali'
print(p1.name)
# ali

# حالا
#  اگر شاخص را بدون تعریف ابجکت ارائه کنی خطا میده
p2.name='mamad'
print(p2.name)
# NameError: name 'p2' is not defined. Did you mean: 'p1'?

# قبلش باید تعریف کنیم
p2=Human()
p2.name='mamad'
print(p2.name)
# mamad

# ///////////
# حالا اگر اتربیوت را در خود کلاس تعریف کنیم 
# برای هر دو اعمال میشه و نیاز نیست دونه دونه باشه
# مننجر خصوصیت است . خصوصیت برای کل کلاس است
class Human:
    manager='vakili'
p1= Human()
print(p1)

p1.name='ali'
print(p1.name)

p2=Human()
p2.name='mamad'
print(p2.name)

print(p2.manager)
# vakili
print(p1.manager)
# vakili

# ولی اگر  در اتریبیوت پایین تر یکیشونو عوض کنیم فقط برای اون یکی عوض میشه
print(p2.manager)
# vakili


p1.manager= 'rahimi'
print(p1.manager)
# rahimi

# ولی پرینت نمیشه یه ضرب
# print(p1.manager= 'rahimi')


# /////////////


# شیوه دیگر کار با کلاس 
# تعریف شاخص بطور کلی 
# شیوه افزایش درون دامنه کلاس
# name یک اتربیوت است
class Human:
    def __init__(self,name):
        self.name=name

p1=Human('ali')
print(p1)
# <__main__.Human object at 0x000001830CC80130>
# اینجا یه ابجکت خالی تعریف کردی و هیچ اتریبیوت ندادی بهش

print(p1.name)
# ali


# //
# در اینجا در تعریف سلف اینگونه عملی میشه مثلا
class Human:
    def __init__(p1,name):
        p1.name=name



# //
class classname:
    
    def magic method(object,atribute):   #this is method. object varieble
        object.atribute=the atribute 
# ////////////

# نکته تفاوت متد ها و اتربیوت ها
class Human:
    def __init__(self,name,family):
        self.name=name
        self.family=family
    def fullname(self):
        return self.name +' '+ self.family
    
    # نکته ۱ 
    #  در اختصاص متد ها به اتریبیوت ها باید سلف دات را بزنی پشت اتربیوت ها
    # فراخوانی خصوصیت یا اتربیوت 
    # Attribute
    # در استفاده اتربیوت کلاس باید اسم کلاس را همه جا پشتش وارد کنی حتی درون  دامنه کلاس
    
# اگر اتربیوت اینیت دو تا بود باید در فراخوانی هم 
# ‍دوتا  چیز بدی  و این به همون ترتیب بهت برمیگردونه
p1=Human('ali','yari')
print(p1.name)
# ali
print(p1.family)
# yari


# ۲ نکته  فراخوانی متد یا تابع یا رفتار
#  تابع دیگر به غیر از اینیت میشه متد نه اتربیوت برای فراخوانی هم باید جلوش پرانتز بدی

print(p1.fullname())
#    ali yari     

# یعنی نمیشد مثل  فراخوانی بر روی اتریبیوت ها اینگونه بیاری:
print(p1.fullname)
# <bound method Human.fullname of <__main__.Human object at 0x0000022AC0FE0370>>
# مگر اینکه اونو به عنوان پراپرتی دکوریتر درست کرده باشیش

# حالا اگر مانند متد های خود پایتون اگر ورودی هم بخواد بهش ورودی میدیم
# یعنی این
    def fullname(self,a):
print(p1.fullname(5))

        
# نکته ۳ 
# در تعریف مشخصه ها اگر لحظه نمونه سازی مقدار را از کاربر بگیریم در 
# __init__
# میدیم ولی اگر پیشفرض باشه اون مشخصه ها 
# یا خودکار انجام بده و بقیه برنامه اجرا بشه 
# به عنوان کلاس وریبل میزنیم
class Human:
# اینها خصوصیات هستند برای کل
        name='mamad'
        family='namjoo'
# روش دوم همون تابع اینیت است
# که درون اون مینویسیم

# برای فراخوانی اول باید نمونه سازی کنیم یهنی اینستنس   را بسازیم
Java_Man=Homo_erectus('java man',1170000)
# که کلاس همو اراکتوس را که ساخته بودیم این نمونه جاوا من اسمش جاوا هستش قدمتش هم ای اندازه است
# حالا برای فراخوانی خصوصیت 

# اما برای فراخوانی رفتار یا همون متد یا تابع از 

# بکار میبریم

# ///////////
# نکته ۴
def 
# ها رفتاری هستند که سلف ها انجام میدن 
# روی نمونه ها اجرا میشن
# رفتارش در قبال فلان چیز چی است؟
# //////
# تفاوت فراخوانی و تعریف خصوصیت ها 
# خصوصیت های کلاس که برای همه نمونه ها مشترکه
# خصوصیت های اون نمونه
# تابع ها

# این اسم کلاس
class Computer : 
    # این مشخصه کل کلاس 
    # میتونه ویژگی هایی را داشته باشه که همه نوع اون کلاس داشته باشند
    # مثلا ساخت امریکا بودن
    mark='lenovo'
    def __init__(self,cpu,ram,graphic):
        # اینا مشخصه هایی هستند که برای  یک نمونه استفاده میشن 
        # مثلا لپتاب وای هفتصد 
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    
    def value (self):
        # این رفتاری است که اون داره 
        # مثلا قیمتش اینجوری حساب میشه
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue   


y700=Computer(1.4,15,8)
print(y700.ram)
# 15
mycamp=Computer.mark
print(mycamp)
# lenovo

# حالا فراخوانی تابع یا رفتار یا متد روی اون نمونه از کلاس
print(y700.value())
# 24.4
# ////////////



# نکته اگر اینیت را با داندر یهعنی دو تا آندراسکور نزنی این خطا را میده
from datetime import datetime
class current_age :
    
    def __iniit__(self,history):

        history=history.split('/')
        print(history)

the_date= current_age('1995/02/03')
# TypeError: current_age() takes no arguments


# ////////






# ///
# تعریف کلاس پیچیده تر
# ساختار کلاس ها  .
# ساختار اولیه کلاس ها  اینه
class Homo_erectus:
    sub_species=0
    def __init__ (self,name, ):
        self.name=name
        self.era= era

def __init__  
# اغازگر ابجکت هستش که ابجکت ها با اون اغاز میشن

# متغیرعمومی 
(self)
# که درون تابع اینیت باشه


# اما این به تنهایی اجرا نمیشه 
# باید متد یا همون فانکشن واسش تعریف کنی 
# همانطور که  لیست ها متد  مثلا سورت داشتند

# برای تعریف متد ها باید از 
self 
# استفاده کنی 
# که مشترکشون کنه و بچسبونه به کلاس اول
    def mymethod_name(self):
        # که اینجا تعریفشون میکنی
        # اول اسن اون بعد اون کاری که با اینستنس میکنی 
        print(self.name)
# بعد برای استفاده باید فراخوانی کنی 
 
# البته اگر 
        print(name)
#  کنی خطا میده و باید در هر تابع هم سلف را بدی 
 
 
# فراخوانی کلاس و استفاده از کلاس
# اول اون اینستنس را ایجاد میکنیم
Java_Man=Homo_erectus('java man',1170000)

# بعد اون متد را روش ایجاد میکنیم
# با اسم اون 
Java_Man.mymethod()

# طبق قوانین تابع
# که اگر پرینت را درون خود تابع قرار داده بودی 
# نیازی نیست دوباره در فراخوانی  متد کلاس پرینت بزاری

# ولی اگر قرار ندادی باید پرینت را بزاری  در فراخوانی تا پرینت کنه

 

# پس اولین  برنامه کلاس اینه 
class Homo_erectus:
    # import time
    sub_species=0
    def __init__ (self,name,era):
        self.name=name
        self.era= era
    def period(self):
        print(self.era)
    # سوال ایا باید همیشه هر متغیر مثل 
    # era 
    # را در فانکشن بالایی هم داشته باشم یا میشه نباشه؟
    # ؟؟؟؟؟؟؟؟؟؟؟
    
     
    
Java_Man=Homo_erectus('java man',1170000)
Java_Man.period()
# خروجی اینو میده تابع
# 1170000

# ////////


# میتونیم از درون تابع یه تابع دیگر را بیاریم تغیر بدیم

    ..........
    def period(self):
        print(f' the era of {self.name} is {self.era} ')
        # range(2000000,117000)
    def period_1(self):
        self.era= self.era+1
        print(f'{self.era} is ')
        
        
Java_Man=Homo_erectus('java man',500000)
Java_Man.period()
Java_Man.period_1()
#  the era of java man is 500000
# 500001 is

# ///////////







# //////////////////////

# ابجکت وریبل
# کلاس وریبل 

# تفاوت ابجکت وریبل و کلاس وریبل

# یک اینه که ابچکت درون تابع به سلف اختصاص میابند
 def __init__ (self,name,era):
        self.name=name
        self.era= era
    def period(self):
        print(self.era)

# ///////////////
# تفاوت ابجکت وریبل و کلاس وریبل

    def __init__ (self,name,era):
        self.name=name
        self.era= era
        Homo_erectus.sub_instance
# این وریبل  از کلاس گرفته ولی اونها از سلف گرفتند


# ////////
# بطور کامل اینگونه میشه
class Homo_erectus:
    # import time
    sub_instance=0
    # در دل تابع اینیت تعریف کرد 
    # یه تابع درست کرد که گفت هم میشه
    # با سلف بهش داد هم سلف را بهش نداد
    def __init__ (self,name,era):
        self.name=name
        self.era= era
    # **************
        Homo_erectus.sub_instance=Homo_erectus.sub_instance+1
        # اینجا در دل تابع اینیت بازهم تعریف میکنیم
    def period(self):
        print(f' the era of {self.name} is {self.era} ')
        # range(2000000,117000)
    def period_1(self):
        self.era= self.era+1
        print(f'{self.era} is ')
    
   
    # اینجا تابعی برای کلاس وریبل تعریف میکنیم 
    # این بالا می تونیم بزنیم سلف یا نزنیم
    
    def my_count(self):
            # فرقش با بقیه اینه که دیگه اینجا نمیزنیم  سلف ! 
        print (Homo_erectus.sub_instance)
        
        
        
Java_Man=Homo_erectus('java man',500000)
Java_Man.period()
Java_Man.period_1()
#  the era of java man is 500000
# 500001 is

# برای بازخوانی ها سلف را دیگه نمیاریم
Peking_man=Homo_erectus('Peking Man',70000)
Peking_man.period()

lantian_man=Homo_erectus('lantian man',163000000)
lantian_man.period()

yuanmu_man=Homo_erectus('yuanmu man',17000000)
yuanmu_man.period()

# ///////
# بطور خلاصه
class Homo_erectus:
    # import time
    sub_instance=0

    def __init__ (self,name,era):
        # self.name=name
        # self.era= era
        Homo_erectus.sub_instance=Homo_erectus.sub_instance+1
    def my_count(self):
        # فرقش با بقیه اینه که دیگه اینجا پایین نمیزنیم  سلف ! 
        print (Homo_erectus.sub_instance)
# این گونه بازخوانی میشه
(yuanmu_man.my_count())
# 4
# که بهمون میده اون کل اینستنس ها چند بار بکار رفتن
# یعنی میاد تفکیک میکنه کل اینستنس ها چند بار بکار رفته و برای خود اون اینستنس  نیست
# یعنی یه بار جاوا یه بار لانتیان یه بار یوانمو یه بار پکیننگ 


#  اگر سلف را نزاریم هم میشه در تابع یعنی
    def my_count():
            # فرقش با بقیه اینه که دیگه اینجا نمیزنیم  سلف ! 
        print (Homo_erectus.sub_instance)

# بعد برای فراخوانی  باید اسم کلاس را فراخوانی کنی 
# طبق کلاس فراخوانی کنی نه طبق اینستنس ای که دادیم

(Homo_erectus.my_count())
# 4
# ولی پرسش چرا فقط یه اینستنس را اسم برده و همه را اورد؟
# چرا درون تابع اینیت تعریف کرد در بالا اگر  کلاس وریبل بود

# در حالت اول
# چرا دوباره سلف را داد؟

# چرا تابع تعریف کرد واسش؟
# ایا نمیشد همونجا بشماره بقیه اینستنسها را؟


# //////////////
# توجه  
# وقتی خصوصیت را صدا میزنیم پرانتز نمیزاریم
# وقتی متد را صدا میزنیم پرانتز میزاریم



# انواع تعریف کلاس ها

class a(object):
class myClass():
class Homo_erectus:


# ////////

# دادن پیشفرض هم برای کلاس ها کار میکنه
class Computer :  
    mark='lenovo'
    def __init__(self,cpu=1.4,ram=4,graphic=256):
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue   

# اگر چیزی ندیم و تغیرش ندیم
y700=Computer()
print(y700.ram)
# 4

# اگر به پیشفرض چیزی بدیم و تغیرش بدیم
y700=Computer(1.4,15,8)
print(y700.ram)
# 15


# ////////////
# استفاده از کلاس  به عنوان ماژول در فایلی دیگر
# کتابخانه

# فرض کن در فایلی به اسم 
from excersise8 import Computer
# حالا 
# در  فایلی به اسم 
# excersise9
# این کلاس را استفاده میکنیم
y700=Computer(1.4,15,8)
print(y700.ram)
# 15

# کلاس  نوشتیم با متد هاش
# البته باید فایلش کنارش باشه

# برای کار با فایل ها و فایل 
ven
# به اموزش فصل ۲ جنگو نگاه شود

# ////////
# مجیک متد
# مجیک متد های اینتیجر اینه
print(dir(2))    

# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__',
#  '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__',
#  '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__',
#  '__int__', '__invert__', 
# '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
# '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
# '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
# '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length',
# 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# بعنی بجای 
print(2+3)
# 5

# میشه زد :
print((2).__add__ (3))
# 5

# حتما نقطه و پرانتز وجود داشته باشه

# ///////
# مجیک متد داندر استی ار
overwrite 
# حالت برگشت رشته را عوض کنه
ــstr__
# //////////
# بجای این خودش چیزی که ما میخوایم را برگردونه
class homo:
    def __init__(self,name):
        self.name=name
        
myname=homo('mamad')
print(myname)
# <__main__.homo object at 0x00000237873C0130>      

# میشه بزنیم
# مجیک متد

class homo:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name +' is the object'
    
myname=homo('mamad')
print(myname)
# mamad is the object
# بجای اینکه جای حافظه را بده

# ///////////
# ارث بری 
# ارث بری شباهت کامل 
# ارث بری شباهت با کاستی 
# ارث بری شباهت با افزودن


# //////
# شباهت کامل 
# کافیه 
# pass
# کنی 


class Computer :
    def __init__(self,cpu,ram,graphic):
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue
# اینجا یه نمونه از اون کلاس پرنت ما میسازیم
my_computer=Computer(2.6,4,8)
print(my_computer.value())
# 14.6

# شیوه نوشتن اینه مادر در دل دختر
# اول دختر پرانتز دختر

class laptob(Computer):
    pass
# این کلاس دختر همون مادر است ولی اسمشون فرق داره انگار یه کپی صد درصد ژنتیکی انجام شده
# یعنی همه ویژگی های داشته اش را دارد 
my_laptob=laptob(3.6,16,4)
print(my_laptob.value())
# 23.6


# /////////

# حالا اگر بخوایم معیاری را زیاد کنه 

#
# 1 -میتونیم با روش ساده خارج از دامنه کلاس چیزی بهش بدیم همانجوری که  در دادن اتربیوت به کلاس ها در شیوه ۱ دادیم
#مثل این: 
# p1.name='ali'
# print(p1.name)
# 
class laptob(Computer):
    pass
my_laptob=laptob(3.6,16,4)
print(my_laptob.value())
my_laptob.size=13
print(my_laptob.size)
# 13
print(my_laptob.cpu)
# 3.6
# همونجور که میتونستیم به سی پی یو دسترس داشته باشیم
# ولی مساله اینه که انگار پس از سایز اضافش نمیکنه به مای لپتاب
print(my_laptob.value())
# 23.6

# برای حل این  ۱ راه اینه که بیایم فقط تابع ولیو را بنویسیم و اضافه کنیم به کلاس
# نیازیه به تابع  اینیت نیست فقط

# این روش چیزی اضافه نکرده بلکه روی متد ای که در کلاس مادر بوده کار کرده
class laptob(Computer):
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic+self.size
        return itsvalue
my_laptob=laptob(1.4,6,5)
my_laptob.size=12
print(my_laptob.value())
# 24.4
# یعنی به تعداد قبلی بزن و اینجا یه چیز اضافه کن بهش


# /////////
# منتها اگر اینجوری بنویسی خطا میده که چیزی به اسم سایز نداشت اون تابع بالا
class laptob(Computer):
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic+self.size
        return itsvalue
my_laptob=laptob(1.4,6,16,4)
print(my_laptob.value())

# TypeError: Computer.__init__() takes 4 positional arguments but 5 were given
# حالا اگر یه عددشو کمتر بدیم یعنی ه
my_laptob=laptob(1.4,6,16)
# اینو میده
# 'laptob' object has no attribute 'size'

# هرچند اینو میده یعنی عملا به روز رسانی نکردی
class laptob(Computer):
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue
my_laptob=laptob(1.4,6,16)
print(my_laptob.value())

# که دقیقا همون 
class laptob(Computer):
    pass
# هستش


# ///////

# متد  اینیت کانستراکتور است
constructive

# اما متد مخرب هم داری
destructive

def __del__(self):
    # بگیم هر موقع دیلیت کردی یه کاری کن

# مثال دیلیت
# Python program to demonstrate
# __del__
  

class Example: 
    # Initializing
    def __init__(self): 
        print("Example Instance.")
    # Calling destructor
    def __del__(self): 
        print("Destructor called, Example deleted.") 
obj = Example() 
del obj 
# Example Instance.
# Destructor called, Example deleted.
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟/


# خود جادی اشتباه کرده
# کل این شیوه این میشه ولی پرسش چرا کار نمیکنه
class Computer :
    # اینجا کلاس وریبل را میاری
    count=0
    def __init__(self,cpu,ram,graphic):
        Computer.count+=1
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
        # اینجا درون تابع میاریش
        
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue   
    # اینجا تابعشو اضافه میکنی
    def __del__(self):
        Computer.count -=1
# حالا اگر بخوایم معیاری را زیاد کنه 

class laptob(Computer):
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic+self.size
        return itsvalue
    
my_computer=Computer(2.6,4,8)
print(my_computer.value())
# 14.6


# حالا اینجا متد دیلیت را بیاریم
del my_computer


my_laptob=laptob(1.4,6,5)
my_laptob.size=12
print(my_laptob.value())
# 24.4
# ولی هر دوشون خروجیشون تغیر نکرد بازهم
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟

# پاسخ:


# ////////
# متد 
# دیلیتر
# دیلتر
https://www.geeksforgeeks.org/python-__delete__-vs-__del__/


# //////
# حالا افزودن  به وسیله نوشتن تابعی دیگر
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
# arzeshe in hastesh 5.2


# /////

# .........

class Computer :
    def __init__(self,cpu,ram,graphic):
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue
class laptob(Computer):
    def arzesh(self):
        print(f'arzeshe in hastesh {self.cpu*2}')
# کار روی متغیر   مادر  یا حتی روی تابع دیگر
# با وجود اف استرینگ
mylap=laptob(2.6,8,16)
print(mylap.value())
# 26.6
(mylap.arzesh())
# arzeshe in hastesh 5.2
# ///////
# توجه اگر اسم است باید استرینگ بدی وگرنه متغیر میشناسه و میگه تعریف نشده
y700=laptop_lenovo('y700',21)
# و نه
y700=laptop_lenovo(y700,21)
# //////
# بجای اون تیکه پایینی
# یا حتی روی تابع دیگر و تابع بالایی اون کلاس را 
    def arzesh(self):
        print(f'arzeshe in hastesh {self.value()*2}')
# کار روی متغیر   مادر  یا حتی روی تابع دیگر
# با وجود اف استرینگ
mylap=laptob(2.6,8,16)
print(mylap.value())
# 26.6
(mylap.arzesh())
# arzeshe in hastesh 53.2


# ///////

# میشه رفتار و ویژگی خصوصی ایجاد کرد
# میشه بدون ایینیت تعریف کرد
class calculator:
    def sum(self,a,b):
        return a+b
mysum=(calculator ().sum(3,4))
print(mysum.sum(3,4))
# 7
# پس اینیت چه کاربردی داره؟
# ////////
 
# تعریف روی زیر کلاس که فقط به این کلاس برمیگرده
class laptob(Computer):
    mark='lenovo'
    def arzesh(self):
        print(f'arzeshe in hastesh {self.cpu*2}')

mylap=laptob(2.6,8,16)
(mylap.arzesh())
# arzeshe in hastesh 53.2
# حالا تعریف روی کلاس وریبل این میشه

print(mylap.mark)
# lenovo

# ///////
# سوپر
# استفاده از یک تابع مادر درون تابع دختر  
#  مثلا یه کاربرد اینه که اسم اون تابع تغیر کند درون تابع تازه
class Computer :
    def __init__(self,cpu,ram,graphic):
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    def value (self):
        itsvalue=self.cpu+self.ram+self.graphic
        return itsvalue   
    
# سوپر
# تعریف روی زیر کلاس که فقط به این کلاس برمیگرده
class laptob(Computer):
    def arzeshham(self):
       return super().value()
mylap=laptob(3.5,4,5)
print(mylap.arzeshham())
# 12.5

# انگار که داری تابع بالایی را میگیری
# در این وهله تفاوتی ایجاد نمیکنه

mycamp=Computer(3.5,4,5)
print(mycamp.value())
# 12.5

# توجه اینجوری یه ضرب نمیاره
mycamp=Computer.value()

# ولی
mycamp=Computer(3.5,4,5).value()
# خطا نمیده
# حتی اگر ارگومان اولی در کلاس هم خالی باشه باید برای فرراخوانی کلاس را با پرانتز فراخوانی کنی

# حتی میشد یه ضرب پرینت کرد بدون اینکه در متغیری بریزی
print(Computer(3.5,4,5).value())
# 7


# یعنی اگر این هم بود
class Computer :
    def __init__(self):
mycamp=Computer()
# باید با پرانتز  فراخوانی کنی
# ضمن اینکه میشه هیچ متغیری درون کلاس تعریف نکرد

# /////////
# انجام یه عملیات روی یکی از ورودی های کلاس
# میشه اینستنس یه لیست باشه
# که عملیاتی را در کلاس روی اون پیا ده کنه


from statistics import mean
class A:
    def __init__(self,agelist):
        self.agelist=agelist
        # self.heightList=heightList
        # self.weightlist=weightlist
    
    def list_age(self):
        age_average=float(mean(self.agelist))
        print(age_average)
        
        # self.heightAve = float(mean(self.heightList))
        
# اینجا شی به عنوان یک موجود نیست 
# مثلا یک دانش آموز مدرسه که صفت هایی مثل قد و وزن و سن داشته باشه
# بلکه
# اینجا یک مجمعه از نفرات یک مدرسه را به عنوان یک شی تلقی کرده
# که صفت هر کدام از اون مدرسه لیستی از قد ها است یعنی یک صفت خودش شامل چند چیز است
# هرچند در نهایت اخر سر میاد با میانگین گرفتن اونها را به یک چیز واحد تبدیل کرده
# صفت دیگر  لیستی از وزن ها است


myage=[16,17,15,16,17]
my_A=A(myage)
my_A.list_age()
# 16.2

# پرسش 
# ایا
# میشه یه سری ویژگی چندین نفر را یک شی تلقی کرد؟
# مثلا مجموعه ی همه قد ها یک شی باشن

# /////////
# ارث بری 
class laptob_Aser(laptob_lenovo):
    pass
legion5_wa=laptob_Aser()
# اگه پس بدی که همون قبلی را میزنه
# یعنی رم و سی پی یو و...



# حالا اگر یه متغیر اضافه داشت اون کلاس تازمون
# چند راه داریم 

# اگر کلاس مادر ما این باشد 
class laptob_lenovo:
    def __init__(self,ram):
        self.ram=ram
y700=laptob_lenovo(128)
print(y700.ram)
# 128

# و این کلاس دختر باشه که از مادر به ارث ببره
class laptob_Aser(laptob_lenovo):
    def __init__(self,graphic):
        self.graphic=graphic

legion5_wa=laptob_Aser(256,24)
print(legion5_wa.graphic)

# TypeError: laptob_Aser.__init__() takes 2 positional arguments but 3 were given
# خود این خطا میده به ما ولی راه های دیگه هست که بشه انجام بشه)


# اینجا خطا میده با اینکه ازش ارث رده ولی چون اینیت دیگه تعریف کردیم همونو نمیاره
print(legion5_wa.ram)
# ypeError: laptob_Aser.__init__() takes 2 positional arguments but 3 were given

# یعنی نه مادر را میشناسه نه دختر را

# 1راه:
# سوپر
class laptob_Aser(laptob_lenovo):
    def __init__(self,model,cpu,ram,hard,year,graphic):
        super().__init__(model,cpu,ram,hard,year)
        self.graphic=graphic

legion5_wa=laptob_Aser('my',2.6,8,256,1,2012)
print(legion5_wa.graphic)
# 2012
# اومده طبق کلاس دختر اخرین گزینه هرچی بود همونو میاره
print(legion5_wa.ram)

# ضعف به نظر عینا همه متغیر های بالا را باید دوباره بنویسی در اینیت پایین 
# خوب یه خط ر ا هم کپی کنیم دیگه  
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟/
# دوم اینکه انگار فقط میشه به کلاس دختر چیزی افزود نمیشه یه متغیر را کم کرد که در مادر هست  و در دختر نباشه 
#  این خطا را میده اگر 
#  مثلا سی پی یو را نزاریم
class laptob_Aser(laptob_lenovo):
    def __init__(self,model,ram,hard,year,graphic):
        super().__init__(model,ram,hard,year)
        self.graphic=graphic

legion5_wa=laptob_Aser('my',8,256,1,2012)
print(legion5_wa.graphic)
#  TypeError: laptob_lenovo.__init__() missing 1 required positional argument: 'year_made'
# 





# راه ۲ بازنویسی متغیر اینیت

class laptob_Aser(laptob_lenovo):
    def __init__(self,model,cpu,ram,hard,year,graphic):
        laptob_lenovo.__init__(self,model,cpu,ram,hard,year)
        self.graphic=graphic

legion5_wa=laptob_Aser('my',8,8,1,2012,256)
print(legion5_wa.graphic)
# 256

print(legion5_wa.ram)
# 256
# 8

# هرچند همون مشکلات کم نشدن را داره
# انگار فقط زیاد میشه 


# میتونه رفتارشو یا تابعشو به ارث ببره
legion5_wa=laptob_Aser('my',8,8,1,2012,256)
(legion5_wa.show())
# made in:  USA, year_made is 11



# //////////

# اینکه خود تایپ کلاس دختر را چی فرض میکنه
print(type(mycamp))
# <class '__main__.Computer'>
# میگه ارجاع میده به کلاس اصلی و اولی

# چیزی دوتا اندرلاین داشته باشه میشه مین

# /////////
# توجه شود که اگر خود متغیری که کلاس را بهش دادیم را پرینت کنیم جای حافظه را میده
class laptob:
    mark='lenovo'
    def __init__(self,cpu,ram):
        self.ram=ram
        self._pasword='123'
        self.cpu=cpu
    def  login(self,gotPasword):
        if self._pasword == gotPasword:
            print('your in')
        else:
            print('wrong password')
my=laptob(1.4)
print(my)
# <__main__.laptob object at 0x0000023012650130>
# برای رفع این یا باید اتربیوت را بدون پرانتز پرینت کنی 
# یا باید تابع را که در کلاس نوشتی را فراخوانی کنی
my=laptob(1.4,2)
print(my.cpu)
# 1.4
# حالا میشه بجای پرینت اون جای حافظه چیزی که ما میخوایم برگردونه را برگردونه 

# دو روش دارد:
    # ۱- متد repr
    
# مثلا وقتی اینو بدیم
class laptob_lenovo:
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,graphic) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)

print(y700)
# <__main__.laptob_lenovo object at 0x0000018F177A02E0>

# حالا برای اینکه خودمون چیزی که میخوایم را بده
# مجیک متد 
# __repr__
class laptob_lenovo:
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,graphic) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
    def __repr__(self):
        return (f' mark hast {laptob_lenovo.Mark_name} ,\n model hast {self.name} ,\n ram hast {self.ram} ,\n,cpu hast {self.cpu} ')
    
        
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)

print (y700)
#  mark hast Lenovo ,
#  model hast y700 ,
#  ram hast 8 ,
# ,cpu hast 2.4
    
# ۲- 

# ///////
# class atribute



# /////////













# /////////
# تفاوت  در  نام ها متد های و متغیر ها کلاس

name
# //////////

# چون مثل بعضی دیگر از زبان ها پرایویت 
# private
# نداریم 
# پس یه دونه آندرلاین میزاریم تا بقیه برنامه نویس ها بفهمن ما  منه
_name

# این کانونشن است قرار داد است

# /////////////
ــname
# name mangaling
# وقتی چیزی را با داندر لفت مینویسیم 
# نمیتونیم  مستقیما با نوشتن اون بهش دسترسی داشته باشیم
class laptob:
    mark='lenovo'
    def __init__(self,cpu):
        self.__massage='hi this is first class'
        self.cpu=cpu
        
my=laptob(1.4)
print(my.__massage)
# AttributeError: 'laptob' object has no attribute '__massage'

# اینجا میگه نداریم 
# برای این باید اینگونه نوشت تا بیاد
# یه دونه آندرلاین سپس اسم کلاس سپس دوتا اندرلاین سپس مسج
my=laptob(1.4)
print(my._laptob__massage)
# hi this is first class


# name mangaling در ارث بری
# کاربرد : در کلاس های ارث برده شده که هر دو یه چیز مشخصه را داشته باشند
class laptob:
    mark='lenovo'
    def __init__(self,cpu):
        self.__massage='hi this is first class'
        self.cpu=cpu
# حالا پیام مسیج را هر دودارن
class Computer(laptob):
    def __init__(self):
        self.__massage='this is secound class'

my=laptob(1.4)
print(my._laptob__massage)
# hi this is first class   

you=Computer()
print(you._Computer__massage)
# this is secound class   

# /////////////
# ما خودمونم میتونیم مثل سایر کلید های داندر از این استفاده کنیم
__name__

# خود پایتون  از این استفاده کرده



# /////
# مجیک متد ها
# مجیک متد 
# __dict__
# میاد در وریبل ها میگه چه اتربیوت هایی داره
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 256}

# یا برای کلاس وریبل ها
print(laptob_lenovo.__dict__)

# {'__module__': '__main__', 'made': 'USA', 'Mark_name': 'Lenovo', 
# 'numbers_of_laptp': 0, 'permited': ['y700', 'legion5_wa', 'Legion5_Pro-AC'],
# 'Wherehouse': [], 
# '__init__': <function laptob_lenovo.__init__ at 0x000001628A5A7D90>,
# '__dict__': <attribute '__dict__' of 'laptob_lenovo' objects>, 
# '__weakref__': <attribute '__weakref__' of 'laptob_lenovo' objects>,
# '__doc__': None}
# به غیر از اونها که ما بهش دادیم هم چیزهایی را میاره
# ////

# مجیک متد رپر
__repr__

# //////////////////////////
# مجیک متد 
__len__

# /////
# مجیک متد
__str__

# /////////
# میشه درون  دامنه اینیت متغیری را وارد نکنیم و بعدش استفاده کنیم ازش
class laptob:
    mark='lenovo'
    def __init__(self,cpu):
        self._pasword='123'
        self.cpu=cpu
    # اینجا تعریف شد ولی مشکلی نداشت 
    # برای سلف بود ولی جزو دامنه اولیه نیاز نیست بهش بدیم    
    # فقط متغیر نباید داد بهش 
my=laptob(1.4)
print(my.cpu)
# 1.4
# هرچند بعدش میتونیم استفاده کنیم ازش در تابعی دیگر
class laptob:
    mark='lenovo'
    def __init__(self,cpu):
        self._pasword='123'
        self.cpu=cpu
    def  login(self,gotPasword):
        if self._pasword == gotPasword:
            print('your in')
        else:
            print('wrong password')
my=laptob(1.4)
my.login(456)
# wrong password

# //////////
# اجرای شرط درون کلاس 
class laptob:
    mark='lenovo'
    def __init__(self,cpu):
        self._pasword='123'
        self.cpu=cpu
    def  login(self,gotPasword):
        if self._pasword == gotPasword:
            print('your in')
        else:
            print('wrong password')
my=laptob(1.4)
my.login(456)
# wrong password
# //////////////////



# ///////
# تعریف یافتن یه زیرر شته در یک رشته با کلاس ها
class myClass():
    def __init__(self, name):
        self.name=name
    def __contains__(self, substr):
        if substr in self.name:
            return True
        else:
            return False
ob = myClass("latracal")
print ('latra' in ob)   
print ('Latra' in ob)
# True
# False

# ///////

class a(object):
    
    d = 'ddd'

    def __contains__(self, m):
        if self.d: 
            return True

b = a()

'd' in b
True


# ///////////
# خروج و ورود کل نمونه های کلاس 
# کدی که تعداد ورودی و خروجی لپ تاب را داشته باشه 
# از طریق کلاس
# بعد ایسوز و... از اون ارث بری کنند 
# بعد با هم مقایسه بشن دو تا لپ تاب

class laptop_lenovo:
    laptob_number=0
    mark='lenovo'
    def __init__ (self,model,price):
        self.name=model
        self.price=price
        laptop_lenovo.laptob_number+=1
    def out(self):
        laptop_lenovo.laptob_number-=1
        print(f'{self.name} is out' )
         
        # اینجا باید اتربیوت را بیاری نه عنوان را یعنی 
        # name
        # و نه مدل
        # model
        
y700=laptop_lenovo('y700',21000)
print(y700.mark)
# lenovo
legion5_wa=laptop_lenovo('legin_5_wa',55.500)
print(legion5_wa.mark)
# lenovo
# اینجا چون متغیر کلاس است پس میگه از این کلاس این تعداد اومدن
print(laptop_lenovo.laptob_number)
# 2  میگه دو تا وارد شده اند

# برای خارج شدن باید تابع را بیاری ولی برای وارد شدن چون جزو سلف بوده نیاز نیست
y700.out()
# y700 is out     اینو خودش در کد بالا داده و هر وقت خارج بشه چیزی خودش اینجا میاره که اون چیز خارج شده
# دوباره پس از این میشماره
print(laptop_lenovo.laptob_number)
# 1    میگه دو نمونه وارد شده اند


# ههمین کد را میشه به عنوان تابع تعریف کرد فقط طولانی تر میشه موقع فراخوانی
class laptop_lenovo:
    laptob_number=0
    mark='lenovo'
    def __init__ (self,model,price):
        self.name=model
        self.price=price
    def daron(self):
        laptop_lenovo.laptob_number+=1
    def out(self):
        laptop_lenovo.laptob_number-=1
        print(f'{self.name} is out' )

y700=laptop_lenovo('y700',21000000)
y700.daron()
legion5_wa=laptop_lenovo('legion5_wa',55500000)
legion5_wa.daron()
print(laptop_lenovo.laptob_number)
# 2 
# چون دو تا اینستنس بهش داده

legion5_wa.out()
print(laptop_lenovo.laptob_number)
# 1 که فقط همون وای هفتصد است


# البته این هم میشد 
y700=laptop_lenovo('y700',21000000).daron()
# که تابع را پیش از همه اینا وارد کنی
# فقط در اون صورت دیگه اینا کار نمیکنه
print(y700.mark)

# ///////////////////////
# ایجاد ارور در کلاس ها
# raise ValueError('')
# کدی که میگه اگر اون اسم لپتاب در ان لیست ما نبود مثلا مارک دیگر بود 
# خطا وارد کن
# کنترل ورودی اینستنس ها
# گرفتن فقط یه سری مقادیر
class laptop_lenovo:
    laptob_number=0
    mark='lenovo'
    mylaptopnames=['y700','legion5_wa','Legion_5_Pro-AC']
    def __init__ (self,model,price):
        self.name=model
        self.price=price
        # توجه شود که همه متغیر های کلاس را اولش اسم کلاس را وارد کنی اینجا لپتاب لنوو
        # یعنی صرفا اسم لیست نباشه
        if self.name not in laptop_lenovo.mylaptopnames:
            raise ValueError(f' {self.name}  is not in my list of lenovo laptops')
    def daron(self):
        laptop_lenovo.laptob_number+=1
    def out(self):
        laptop_lenovo.laptob_number-=1
        print(f'{self.name} is out' )

y700=laptop_lenovo('y700',21000000)
y700.daron()
legion5_wa=laptop_lenovo('legion5_wa',55500000)
legion5_wa.daron()
print(laptop_lenovo.laptob_number)
legion5_wa.out()
print(laptop_lenovo.laptob_number)

IdeaPad_3=laptop_lenovo('IdeaPad_3',1000000)
IdeaPad_3.daron()
# ValueError:  IdeaPad_3  is not in my list of lenovo laptops
#

# /////
# ایا میشه به درون کلاس چیزی افزود؟؟
# مثلا تا این وارد شد خودش بره داخل اون اپند بشه؟
# از بیرون اون کلاس؟؟؟؟؟؟؟؟؟؟؟؟؟

# ////////
# کد انبار
# نمونه هایی که وارد میشن درون اون ساخته میشن اونا
# که خارج میشن  از درون اون لیست خارج  میشن

# تعریف کلاس
class laptop_lenovo:
    # اینجا کاونتر را صفر قرار میدیدم تا وقتی اینستنسی زیاد یا کم شد تغیر کنه
    laptob_number=0
    # این برای همه لپتاب ها است
    mark='lenovo'
       # توجه شود که لپتابی ممکن است در  لیست اصلی باشد ولی هیچوقت وارد انبار ما نباشد 
        # هرچند اجازه دارد که وارد شود
    mylaptopnames=['y700','legion5_wa','Legion 5 Pro-AC']
    # بالایی لیستی از همه لپ تاب های مجاز به ورودی انبار است
    warehouse=[]
    # اینجا لیست انبارمون هستش که اول خالیه و هرچیز که به انبار میره به این وارد میشه
    # این پایین هم  نمونه ها را تعریف میکنه چه ویژگی ای دارند 
    # مثلا هر نمونه مدل داره  قیمت داره و...
    def __init__ (self,model,price):
        self.name=model
        self.price=price
        # توجه شود که همه متغیر های کلاس را اولش اسم کلاس را وارد کنی اینجا لپتاب لنوو
        if self.name not in laptop_lenovo.mylaptopnames:
            raise ValueError(f' {self.name} is not in my list of lenovo laptops')
        # اگر اینستنسه جزوی از اون لیست   مجاز لنوو باشه 
        # نباشه خطا بده و اگر باشه
        # اون موقع که حاضرش کردی به درون اون انبار ما بریز
        # هرچند میشه در درون متد 
        # def daron(self):
        # هم بریزیش  و از اونجا فراخوانی کنی
        laptop_lenovo.warehouse.append(self.name)
    # متد افزودن به تعداد شماره
    def daron(self):
        laptop_lenovo.laptob_number+=1
        # چیزی خارج بشه با اون متد فراخوانی میشه
    def out(self):
        laptop_lenovo.warehouse.remove(self.name)
        laptop_lenovo.laptob_number-=1
        print(f'{self.name} is out')

y700=laptop_lenovo('y700',21000000)
y700.daron()
# اینانبارمونه که بالا تعریف کردیم
print(laptop_lenovo.warehouse)
# ['y700']

legion5_wa=laptop_lenovo('legion5_wa',55500000)
legion5_wa.daron()
print(laptop_lenovo.warehouse)
# ['y700', 'legion5_wa']
# حالا دوتا داریم
print(laptop_lenovo.laptob_number)
legion5_wa.out()
print(laptop_lenovo.warehouse)
# ['y700'] حالا که دوباره خالی شد اونو اوردیم

print(laptop_lenovo.laptob_number)
print(laptop_lenovo.warehouse)
# ['y700', 'legion5_wa']
# 2
# legion5_wa is out
# ['y700']
# 1
# ['y700']

# ///////
# نکته
#  اگر ما اینستس را فراخوانی کنی برای یه پروپرتی
# با اینکه کلاس را فراخوانی کنیم هر دو را یکی میدونه؟
print(y700.mylaptopnames)
# ['y700', 'legion5_wa', 'Legion 5 Pro-AC']

print(laptop_lenovo.mylaptopnames)
# ['y700', 'legion5_wa', 'Legion 5 Pro-AC']
# یعنی هم از اینستنس به اون ویژگی دسترسی داریم هم از خود کلاس

# بخاطر اینه که ایدی حافظشون یکی است همون جای کلاس است

print(id(y700.mylaptopnames))
# 2626528359424
print(id(laptop_lenovo.mylaptopnames))
# 2626528359424

# هرچند ای دی خود کلاس فرق داره
print(id(laptop_lenovo))
# 2035682249904

# هرچند ای دی خود اینستنس فرق داره
print(id(y700))
# 2035687686096


# پس این آی دی اون ویژگی در اون کلاس است


# //////////
# کلاس اتریبیوت
# تفاوت  در اینستنس اتربیوت و کلاس اتربیوت
# class atribute
# اپند کردن روی یه   ویژگی کلاس
# اضافه کردن با مساوی روی یه ویژگی کلاس
# نکته 
# حالا اگر اپند کنی روی اینستنس هم روی کلاس اضافه میشه 

print(y700.mylaptopnames)
# ['y700', 'legion5_wa', 'Legion 5 Pro-AC']

print(laptop_lenovo.mylaptopnames)
# ['y700', 'legion5_wa', 'Legion 5 Pro-AC']

# اینجا اپند کنی
y700.mylaptopnames.append(['mamad','asghar'])
print(y700.mylaptopnames)
['y700', 'legion5_wa', 'Legion 5 Pro-AC', ['mamad', 'asghar']]

laptop_lenovo.mylaptopnames.append(['mamad','asghar'])
print(laptop_lenovo.mylaptopnames)
# ['y700', 'legion5_wa', 'Legion 5 Pro-AC', ['mamad', 'asghar']]

# /////
# ولی اگر = کنی  به اینستس تاثیری در کلاس نمیزاره
# و افزایش نمیده در کلاس اصلی 
y700.mylaptopnames=['mamad','asghar']
print(y700.mylaptopnames)
['mamad', 'asghar']
# که افزایش پیدا نمیکنه در کلاس اصلی
print(laptop_lenovo.mylaptopnames)
['y700', 'legion5_wa', 'Legion 5 Pro-AC']


# ولی برعکس میده  یعنی مساوی کردن برای 
# # اما در این حالت میاد جایگزاری میکنه یعنی داشته قبلی اون کلاس را حذف میکنه
laptop_lenovo.mylaptopnames=['mamad','asghar']
print(y700.mylaptopnames)
# ['mamad', 'asghar']
print(laptop_lenovo.mylaptopnames)
# ['mamad', 'asghar']

# پس کلاس را تغیر بدی با مساوی روی اینستنس تغیر میابه ولی 
# اگر اینستس را تغیر بدی با مساوی روی کلاس تاثیر نداره

# پس اگر چه به اینستنس اپند کنی روی کلاس هم اپند میشه و چه به کلاس اپند کنی به اینستنس تاثیر داره  و اپند میشه 
# برای فهم به جلسه اردوخانی ۶۳
# ////////

# کلاس متد
# مانند چیزی که قبلا بکار میبردیم
# dict.fromkeys()
# فقط خودمان میسازیم 

# classmethod
# اجرای متد یا فانکشن روی اتربیوت های کلاس و نه اینستنس
class laptob_lenovo:
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,graphic) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
        # اینجا باید بیاری اضافه کنه یا در یک تابع تا به بالا اضافه کنه
        laptob_lenovo.numbers_of_laptp+=1
    def out(self):
        laptob_lenovo.numbers_of_laptp-=1
    # این دکوریتر کلاسمتد موجب میشه که به اتربیوت کلاس دسترسی داشته باشیم و یه تابعی ازش یا روش پیاده کنیم
    @classmethod
    def Active_laptop(cls):
        print(cls.numbers_of_laptp)
        
# بجای سلف میزنیم سی ال اس و پس از اون اسم اتربیوت کلاس را میاریم
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)


# برای فراخوانی  متد کلاس هم اسم کلاس پس از اون اسم تابع پس از اون پرانتز
laptob_lenovo.Active_laptop()
    #2 

# /////
# اما 
#  برای اینکه متد کلاس  از یه  متد اینستنس اجرا
# بشه و نه از اتربیوت اینستنس باید موقع فراخوانی 

class laptob_lenovo:
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,graphic) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
    def _in(self):
        laptob_lenovo.numbers_of_laptp+=1
    def out(self):
        laptob_lenovo.numbers_of_laptp-=1
    # این دکوریتر کلاسمتد موجب میشه که به اتربیوت کلاس دسترسی داشته باشیم و یه تابعی ازش یا روش پیاده کنیم
    @classmethod
    def Active_laptop(cls):
        print(cls.numbers_of_laptp)
        
# باید اسم تابع را فراخوانی کنی 
# در جلوی هر اینستنس
# تابع اینستنس متد را تا تغیر ایجاد کنه در اتربیوت و اون اتربیوت از 

y700=laptob_lenovo('y700',2.4,8,256)._in()
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)
laptob_lenovo.Active_laptop()
    #1

# ///////////////

# انبار داری با کلاس متد
# فرق انبار داری با روش  دسترسی به اتربیوت از اینستنس متد در فراخوانی است
# laptob_lenovo.Active_laptop()
# بجای اینکه اینستنس را بگی
# print(laptop_lenovo.laptob_number)

# در این کلاس هم مثل قبل چیزی اضافه شد میاد

# اگر اضافه شد وارد میکنه اگر کم شد با یه تابع دیگر کم میکنه از انبار
class laptob_lenovo:
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,graphic) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.graphic=graphic
        laptob_lenovo.numbers_of_laptp+=1
        laptob_lenovo.Wherehouse.append(self.name)
    def out(self):
        laptob_lenovo.numbers_of_laptp-=1
        laptob_lenovo.Wherehouse.remove(self.name)
        # اینجا کلاس متد را فراخوانی میکنیم
    @classmethod
    def Active_laptop(cls):
        print(cls.Wherehouse)
    # بعد سلف کلاس را که به کلاس اشاره داره را میاریم
    # در اون کلاس متغیر ورهاوس را یا همون انبار را میاریم که نشون بده
    
    
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)
laptob_lenovo.Active_laptop()
# اینجا اسم کلاس متد از کلاس را فراخوانی میکنیم

#['y700', 'legion5_wa']
# که دو تا انباری داشته درون ورهوس

# این مثال نشون میده روی کلاس وریبل کار انجام میشه به وسیله کلاس متد
# //////
    

# ///////
# اما کار وقتی که یک یا دوتا متغیر داشته باشیم چطور است؟
# ?????????????///
# https://www.geeksforgeeks.org/classmethod-in-python/
# فایل ۶۴

    @classmethod
    def anonymus (cls,from_model):
        mydate= cls.from_model
        return 

# موقع فراخوانی 
laptob_lenovo.from_model

# ///////////////////
# /؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟////////////////
# ساخت کلاس متد

class geeks:
    # اینجا وریبل ای تحت عنوان کورس داریم
    course = 'DSA'

    def purchase(obj):
        print("Purchase course : ", obj.course)
        # اما این ابجکت کورس به چه معنیه؟
        # تابعهه ابجکت را پرینت میکنه
        
# print(geeks.purchase())
# این خطا میده
# geeks.purchase() missing 1 required positional argument: 'obj'

print(geeks.purchase)
# <function geeks.purchase at 0x0000023949337D90>


# حالا اگر کلاس متد را اجرا کنی و بریزی تو یه متغیر 
# اون تابع را اجرا میکنه
# متد گیک پرچس را درون کلاس متد میاره
# که بعد متد را به کلاس متد تبدیل میکنه
# بعد اون فانکشن پرچس را بدون افریدن اینستنس یا همون ابجکت میسازه
geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
# Purchase course :  DSA

# ////////

# instance variable
# class variable
# تفاوت اینستنس وریبل و کلاس وریبل


# instance variable:
class laptob_lenovo:
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,graphic) :
        self.name=model
        self.cpu=cpu
        self.ram=ram

# در اینجا 
# 2.4 و 8 و    'y700'
# اینستنس وریبل هستند
# یعنی برای اون اینستنس هستند
# فقط برای اون اینستنس هستند نه برای اینستنس دیگر 
# مثلا برای لپتاب لجیون یه وریبل دیگر اون وریبل  وای هفتصد کار نمیکنه
# رمش فرق داره یا....

y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)

# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# پرسش اگر رم دو تا لپتاب یکی بود یعنی وریبل مشترک داشتند چی؟

# ////////
# class variable
# کلاس وریبل ها درتمام اینستنس ها مشترک هستند یعنی در تمام اینستنس ها بکار میرن
# فایدشون اینه که نیازی نیست برای هر اینستنس اون را تغیر بدیم

# اگر بخوایم ساخته کجا را یا مارک را برای هر اینستنس جدا بنویسیم زیاد میشه مثلا
class laptob_lenovo:
    # بجای اینکه ساخته را آمریکا در کلاس لپتاب لنوو بزنیم بیایم دونه دونه در اینستنس ها وارد کنیم
    # made='USA' 
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.made=made
y700=laptob_lenovo('y700',2.4,8,256,'USA')
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128,'USA')

# ///
# میتونمی کلاس وریبل بنویسیم
class laptob_lenovo:
    # بجای اینکه ساخته را آمریکا در کلاس لپتاب لنوو بزنیم بیایم دونه دونه در اینستنس ها وارد کنیم
    made='USA' 
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        print(f'{self.name} made in {laptob_lenovo.made}  ')
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)
# این پرینت را داره
# y700 made in USA
# legion5_wa made in USA

# یا اینکه دسترسی به کلاس وریبل
# در اینجا مید برای کلاس است بدون اینکه بنویسیم در اینستنس ولی در اون متغیر دسترسی داره
print(y700.made )

# همانطور که وریبل اینستنس را دسترسی داریم
print(y700.ram)
# 8


# ///////
# تفاوت نوشتن کلاس وریبل و اینستنس وریبل 
# اوردن کلاس وریبل با سلف 
class laptob_lenovo:
    made='USA' 
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        # میتونستیم اینجا از طریق سلف هم بهش دسترسی داشته باشیم
        print(f'{self.name} made in {self.made}  ')
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)

# اما اینجا  با اینکه سلف دادیم میاره توی کلاس و نه اینستنس 

print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 256}

#  میاره برای کلاس وریبل ها
print(laptob_lenovo.__dict__)

# {'__module__': '__main__', 'made': 'USA', 'Mark_name': 'Lenovo', 
# 'numbers_of_laptp': 0, 'permited': ['y700', 'legion5_wa', 'Legion5_Pro-AC'],
# 'Wherehouse': [], 
# '__init__': <function laptob_lenovo.__init__ at 0x000001628A5A7D90>,
# '__dict__': <attribute '__dict__' of 'laptob_lenovo' objects>, 
# '__weakref__': <attribute '__weakref__' of 'laptob_lenovo' objects>,
# '__doc__': None}

# /////////////
# تغیر یه اینستنس وریبل از کلاس وریبل
# مثلا یه لپتاب در چین تولید شده باشه
class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard


y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)

# حالا در تابع دیگر که نوشتیم اینستنس را تغیر میدیم
# اینجا مساوی چیزی دیگر میگیریم
y700.made='CHINA'

print(y700.made)
# CHINA
# حالا اینو میاره
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 256, 'made': 'CHINA'}


# در صورتی که برای سایر بپتاب ها همون قبلی یعنی کلاس وریبل هستش
print(legion5_wa.made)
# USA

# و جالبه که اونا که تغیر دادیم جزوی از اینستنس وریبل اون هستش  و در
# دیکشنری اینستنس وریبل میاره 
# ولی برای اونا که تغیر پیدا نکردند  جزوی از  کلاس وریبل هستند و در
# دیکشنری وریبل ها نمیاره
# حالا اینو میاره
print(legion5_wa.__dict__)
# {'name': 'legion5_wa', 'cpu': 2.8, 'ram': 16, 'hard': 128}


# ولی اگر مزدیم روی کلاس تغیر میدادیم

laptob_lenovo.made='CHINA'

print(y700.made)
# CHINA
# حالا اینو میاره
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 256, 'made': 'CHINA'}


# در صورتی که برای سایر بپتاب ها همون قبلی یعنی کلاس وریبل هستش
print(legion5_wa.made)
# USA

# و جالبه که اونا که تغیر دادیم جزوی از اینستنس وریبل اون هستش  و در
# دیکشنری اینستنس وریبل میاره 
# ولی برای اونا که تغیر پیدا نکردند  جزوی از  کلاس وریبل هستند و در
# دیکشنری وریبل ها نمیاره
# حالا اینو میاره
print(legion5_wa.__dict__)
# {'name': 'legion5_wa', 'cpu': 2.8, 'ram': 16, 'hard': 128}



laptob_lenovo.made='CHINA'

print(y700.made)
# CHINA
# حالا اینو میاره
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 256}


# در صورتی که برای سایر بپتاب ها همون قبلی یعنی کلاس وریبل هستش
print(legion5_wa.made)
# CHINA
# {'name': 'legion5_wa', 'cpu': 2.8, 'ram': 16, 'hard': 128}


# یعنی در کل کلاس تغیر می کرد
print(laptob_lenovo.__dict__)
# {'__module__': '__main__', 'made': 'CHINA', 'Mark_name': 'Lenovo', 'numbers_of_laptp': 0, 'permited': ['y700', 'legion5_wa', 'Legion5_Pro-AC'], 'Wherehouse': [], '__init__': <function laptob_lenovo.__init__ at 0x000002B76A7D7D90>, '__dict__': <attribute '__dict__' of 'laptob_lenovo' objects>, '__weakref__': <attribute '__weakref__' of 'laptob_lenovo' objects>, '__doc__': None}
# PS E:\.python and every thing\codes and projects>

# هرچند برای اپند در لیست اینگونه نبود بلکه کلش عوض میشه 




# اما با تابع نوشتن
class laptob_lenovo:
    made='USA' 
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        
    def change(self):
        return (f'made in:  {laptob_lenovo.made} ')
    
y700=laptob_lenovo('y700',2.4,8,256)
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128)

# در صورتی که تغیر نکرده با سلف
print(y700.change())
# made in:  USA

# حالا که تغیر بدیم
y700.made='china'
print(y700.change())
# made in:  china

# حالا اگر بکلی اون سلف بالا را تغیر بدیم به کلاس
# یعنی بجای سلف بدیم کلاس را
    # def change(self):
    #     return (f'made in:  {laptob_lenovo.made} ')

# با وجود تغیر هم میده  آمریکا که قبلش بود
print(y700.change())
# made in:  USA 

# باز هم همون میشه
y700.made='china'
print(y700.change())
# made in:  USA

# با این حال در خودش تغیر میکنه
print(y700.made)
# china

# /////////










# ///////////
# انواع متد در کلاس ها
# متد 
# class method
# decorator
# دکوریتور

    instancemtthod
    @classmethod
    @staticmethod



# ///////
instancefunction

# برای نمونه های یا همون اینستنس ها هستند
# در اونها اجرا میشن


    @classmethod
# برای کلاس هستند و در متغیر های کلاس اجرا میشن

    @staticmethod
# تابع های معمولی هستند که نه برای نمونه هستند بطور مستقیم و نه برای کلاس 
# بلکه درون کلاس هستند بیشتر برای تمیز بودن کد


# مثال ۲ 
    @classmethod
# اینستنس کلاس
import datetime
import jdatetime

class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard,year_made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        self.year_made=year_made
    def show(self):
        return (f'made in:  {laptob_lenovo.made} ')
    
    @classmethod
    def era(cls,model_name,cpu,ram,hard,age_year):
        age=cls(datetime.datetime.now().year)-age_year
        return age

        
legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128,2021)
    

y700=laptob_lenovo('y700',2.4,8,25,2014)
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 25, 'year_made': 2014}
# اینجا اینستنس را فراخوانی میکنه

# حالا اگر میخوایم تابع به کلاس بره بهتره این جوری بنویسیم

y700=laptob_lenovo.era('y700',2.4,8,25,2014)
print(y700)
# 9
# میره تفاوت را میزاره حساب میکنه

# /////////
# اما اگر cls  را فراخوانی کنیم
# خود کلاس را که صدا می زنیم اینیت فعال میشه
# و باید مقادیر را هم دوباره بفرستی 
# یعنی بجای

# فایده ۱- میاد روی متغیر های کلاس تغیرات انجام میده
# ۲- ابجکت برمیگردونه با 
# cls
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# ولی منظور اینو نفهمیدم وقتی اینستنس هم ساختیم اونا هم ابجکت بودند دیگه

@classmethod
    def era(cls,model_name,cpu,ram,hard,age_year):
        age=cls(datetime.datetime.now().year)-age_year
        return age
# اینا خاموش هستند شما تعریف کردی ولی کاری باهاش نکردی

# باید
@classmethod
    def era(cls,model_name,cpu,ram,hard,age_year):
        age=cls(model_name,cpu,ram,hard,datetime.datetime.now().year-age_yea)
        return age

# حالا کاملش
# اینستنس کلاس
import datetime
import jdatetime

class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard,year_made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        self.year_made=year_made
    def show(self):
        return (f'made in:  {laptob_lenovo.made}, year_made is {self.year_made}')
    
    @classmethod
    def era(cls,model_name,cpu,ram,hard,age_year):
        age=cls (model_name,cpu,ram,hard,datetime.datetime.now().year-age_year)
        return age


legion5_wa=laptob_lenovo('legion5_wa',2.8,16,128,2021)


y700=laptob_lenovo('y700',2.4,8,25,2014)
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 25, 'year_made': 2014}

y700=laptob_lenovo.era('y700',2.4,8,25,2014)
print(y700.__dict__)

# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 25, 'year_made': 9}
# جالبه که در همه اینا با اینکه تغیر داده در تابع ولی اسمی که در اینیت بود را داده
# year_made
# در صورتی که برای  کلاس ولیو بود 
# age_year
# هرچند در فراخوانی محاسبشو انجام داده

# اگر لپتاب را هم دوباره بایریم همون اولی را میاره
y700=laptob_lenovo('y700',2.4,8,25,2014)
print(y700.__dict__)
# {'name': 'y700', 'cpu': 2.4, 'ram': 8, 'hard': 25, 'year_made': 2014}


# حالا 
y700=laptob_lenovo.era('y700',2.4,8,25,2014)
print(y700.show())
# made in:  USA, year_made is 9

# دلیلش اینه که میره اینستنس را میکنه در کلاس 
# بعد اونجا حساب میکنه میبره در اینیت
# بعد تابع 
show
# هم از اینیت میخونه
# یعنی میره پایین بعد میره بالا

# ??????????????/
# به نظر کار مسخره ای میاد چون با سلف هم از پسش بر میاد 
# و الکی اومده یه عالمه متغیر معرفی کرده با سلف هم همون خروجی را میتونیم بدیم
# مثال
class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard,year_made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        # توجه درون خود تابع اینیت هم میشه اتوماتیک محاسبه انجام بده و خروجی بده
        self.year_made=datetime.datetime.now().year-year_made
    def show(self):
        print (f'made in:  {laptob_lenovo.made}, year_made is {self.year_made}')
    
    # @classmethod
    # def era(cls,model_name,cpu,ram,hard,age_year):
    #     age=cls (model_name,cpu,ram,hard,datetime.datetime.now().year-age_year)
    #     return age
y700=laptob_lenovo('y700',2.4,8,25,2014)

(y700.show())
# made in:  USA, year_made is 9

legion5_wa=laptob_lenovo('y700',2.4,8,25,2020)
(legion5_wa.show())
# made in:  USA, year_made is 3
# یعنی اومده حساب کرده چند سالشه این لپتاب
# از طریق اینستنس
# ///

# ////

@staticmethod
# یه تابع ساده که فقط درون کلاس میره
# یعنی نه 
self
# نه 
cls
# میگیره که به کلاس کار بداره
# ربطی کلی به کلاس داره ولی از اونا استفاده نمیکنه

import datetime
import jdatetime

class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permited=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard,year_made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        self.year_made=datetime.datetime.now().year-year_made
    def show(self):
        print (f'made in:  {laptob_lenovo.made}, year_made is {self.year_made}')
    
    @classmethod
    def era(cls,model_name,cpu,ram,hard,age_year):
        age=cls (model_name,cpu,ram,hard,datetime.datetime.now().year-age_year)
        return age
    
    # این استاتیک متد میگرده اگر لوکیشنی که میخواد بود ادرسشو میده بهش
    @staticmethod
    def seller(location):
        Sales_representative={'tehran':'gomhori','shiraz':'golsar','rasht':'darvaze ghoran'}
        if  location in Sales_representative:
            print(Sales_representative[location])
# فقط باید بگی فروشنده اش کجاست            
laptob_lenovo.seller ('tehran')
# gomhori
# اینجا نه از سلف گرفت نه از کلاس
# ولی یه جورایی هم ربط داشت به کلاس هم چون کد را شی گرایانه نوشتیم نخواست جدا کنه
#
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
#     # کلاس متد روی کلاس ها اجرا میشه نه اینستنس
    # ولی مسخره به نظر میاد چون عملا میاد از اینستنس ها استفاده میکنه 
    # یا اینستنس ها هم میاد 
    # یعنی انگار هیچ کاری نیست که کلاس متد انجام بده و اینستنس نتونه کنه
# 
# //////

# ///////////////////

# ?????????????
# ایا در ارث بری اینو داریم که بشه خودمون فروشنده هاشو عوض کنیم 
# یا بروز کنیم 

# /////
# ارث بری 
# اینجا میخوام ارث ببره هر چیز که داره را ولی یه چیزاییش عوض بشه
class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permitted=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard,year_made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        self.year_made=datetime.datetime.now().year-year_made
        if self.name not in laptob_lenovo.permitted:
            raise ValueError (f'{self.name} is not in {laptob_lenovo}')
    def show(self):
        print (f'made in:  {laptob_lenovo.made}, year_made is {self.year_made}')
    @classmethod
    def era(cls,model_name,cpu,ram,hard,age_year):
        age=cls (model_name,cpu,ram,hard,datetime.datetime.now().year-age_year)
        return age
    
    @staticmethod
    def seller(location) :
        Sales_representative={'tehran':'gomhori','shiraz':'golsar','rasht':'darvaze ghoran'}
        if  location in Sales_representative:
            print(Sales_representative[location])

y700=laptob_lenovo('y700',2.4,8,1,2016)
print(y700.ram)


class laptop_Aser( laptob_lenovo):
    pass

Nitro_17=laptop_Aser('Nitro_17_VN7',4.7,8,1,2017)
print(Nitro_17.ram)
# ValueError: Nitro_17_VN7 is not in <class '__main__.laptob_lenovo'>

# نخست از همه این نمیخوام توی لپتاب لنوو باشه چون ایسر هست
# دوم میخوام ساخت تایوان باشه
# سوم میخوام لیست اون عوض بشه و در بررسی هم بره جای اون بگذاره یعنی یک کد را دوبار ننویسم فقط اسمشون عوض بشه
# و خطا نده
# بعدشم برخی متد هاش عینا اجرا بشه روشون
# مثلا استاتیک 
# فقط لیست فروشگاهاش عوض بشه

# ////
# نکته اگر خطا نمیداد میتونست اون تابع را حساب کنه جون به ارث برده بود
Nitro_17.show()
# made in:  USA, year_made is 6
# یا اون کلاس اتربیوت را
print(Nitro_17.Mark_name)
# Lenovo
# نخستین مشکل اینه که نمیخوام لنوو را بده باید تغیراتی بدم درش که اونو یکی دیگه بده 
# یا خودش اتومات از چیزی بخونه و بده به ما که ایسر است

# ///////////////////////
# چطور مانع تغیر کلاس شویم؟ توسط کاربر و فراخوانی؟
# validation
# ۱-
import datetime
import jdatetime
# کدی که اگر عدد کمتر وارد شد را نزاره
# و عوض کنه با چیزی که میخوایم
# فیلتر کردن کد- بررسی ورودی کلاس و تغیر ورودی اگر نا مناسب بود 
# /
from datetime import datetime
class mohasebe_sen:
    def __init__(self,history):
        self.history=history
        if self.history =='1995/02/03':
            self.history=0
        else:
            self.history=history
        
my_date=mohasebe_sen('1995/02/03')
print(my_date.history)
# 0

# حالا مساله اینه 
my_date=mohasebe_sen('1995/02/03')
print(my_date.history)
# 0

my_date.history='1995/02/03'
print(my_date.history)
# 1995/02/03
# بعدش که تغیر بدیم تغیر میکنه یعنی هرچند توی
# ورودی اول تنظیم شده ولی توی تغیر ورودی  معیار را درنظر نمیگیره

# //////

# راه ۱
# ۱- گتر و ستر را خود بسازیم
# getattr , setter


# گام ۱
from datetime import datetime
class mohasebe_sen:
    def __init__(self,history):
        # self.history=history 
        # برای تنظیم دیگه دوباره این بالاییه را ننوشته
        # بلکه یه ضرب رفته توی  شرط 
        # و تازه  سلف را مساوی نگرفته بلکه خود متغیر را نوشته
        if history =='1995/02/03':
            self.ـhistory=0
        else:
            self.ـhistory=history
        
        # def get_history(self):
            
my_date=mohasebe_sen('1995/02/03')
print(my_date.history)
# AttributeError: 'mohasebe_sen' object has no attribute 'history'. Did you mean: 'ـhistory'?

# بعدش این ارور را میده چون ما اندرلاین هیستوری 
# را اوردیم که کاربر دسترسی نداشته باشه بهش


# گام ۲-
from datetime import datetime
class mohasebe_sen:
    def __init__(self,history):
        # self.history=history 
        if history =='1995/02/03':
            self._history=0
        else:
            self._history=history
        # حالا تابع گت را میاریم که کاربر اون تابع را بخونه 
        # نه در چیزی که خودش میخواد
    def get_history(self):
        return self._history
    # این یه عنصر میگیره که تنظیم کنه اونرا یعنی در این چهارچوب بگیره
    def set_history(self,newhistory):
        if newhistory=='1995/02/03':
            self._history=0
        else:
            self._history=newhistory
                
my_date=mohasebe_sen('1995/02/03')
# my_date._history='1995/02/03'   
# جالبه اگر این بالایی را ندیم همه را صفر میده وگرنه همه را همون تاریخ غلط را میده
# یعنی اینو میده
# print(my_date._history)     
#1995/02/03
# بخاط این مشکل از اول اومد اندرلاین را دا که کاربر گول بخوره و نیمه خصوصی بشه واسش
# یعنی مثلا کاربر نمیدونه که  باید
# my_date._history
# را بنویسه و نه
# my_date.history
# که اگر این یکی بالایی را بنویسه  خطا میده بهش
# AttributeError: 'mohasebe_sen' object has no attribute 'history'. Did you mean: 'ـhistory'?

# حالا برای اولی بخاطر شرطی درون ایینت این صفر را میده
print(my_date._history)     
# 0

# بعد این هم پرینتش میکنه ورودی را دریافت میکنه 
# اما توجیه اینو نفهمیدم - ما در پراپرتی میدونیم که اتربیوت میده ولی در این که توجیه نداشه
# ؟؟؟؟؟؟؟؟؟؟؟؟؟؟
print(my_date.get_history())
# 0
# پاسخ در پایین تر گام ۴


# این یکی هم تنظیمش میکنه
my_date.set_history('1995/02/03')
# 0
print(my_date.get_history())
# 0

# پاسخ
# گام ۴

        # یعنی اگر گتر نباشه  ستر خونده نمیشه 
        # چون ستر تنظیم گره و نه خواننده 
        # و هر بار که میدی ستر را میگه ورودی بهم بده
# یعنی
class mohasebe_sen:
    def __init__(self,history):
        # self.history=history 
        if history =='1995/02/03':
            self._history=0
        else:
            self._history=history

    def get_history(self):
        return self._history
    def set_history(self,newhistory):
        if newhistory=='1995/02/03':
            self._history=0
        else:
            self._history=newhistory
            
my_date=mohasebe_sen('1995/02/03')

print(my_date._history)     
# 0
# print(my_date.get_history())
# 0
my_date.set_history('1995/02/03')
# 0
# print(my_date.get_history())
# 0

# پاسخ شاید این باشه که این باعث میشه که ستر را بخونه
# یعنی اگ اینرا بدیم
print(my_date.set_history)
# <bound method mohasebe_sen.set_history of <__main__.mohasebe_sen object at 0x0000023631710370>>

# ولی با گتر اینو میخونه و اجرا میکنه
print(my_date.get_history())
# 0





# /////
# راه حل ۲
# ۳- گتر و ستر دکوریتور متد
# getattr , setter
@property
@functione name.setter

# مشکلی که در فراخوانی داشتیم این بود که اومدیم دو تابع را فراخوانی کردیم تا تنظیم کنه
# مساله اینه که ما نمیخوایم 
print(my_date.set_history)
# <bound method mohasebe_sen.set_history of <__main__.mohasebe_sen object at 0x0000023631710370>>

# ولی با گتر اینو میخونه و اجرا میکنه
print(my_date.get_history())
# 0

# بلکه یه بار فراخوانی کنیمش





# //////
# گام ۲
# توضیح پراپرتی گتر و ستر
class mohasebe_sen:
    def __init__(self,history):
        # نکته حتما در اینیت باید اون اتربیوت را به  
        # سلف اتربیوت اختصاص بدی تا بعدش بتونی باهاش یه کاری کنی 
        # وگرنه اگر اینشکلی باشه خطا میده
        if history =='1995/02/03':
            self._history=0
        else:
            self._history=history 
   # پس اسم هر دو فانکشن و اسم ستر دکورتیر  باید یکی باشند با هم در اینجا گت هیستوری
    @property
    def get_history(self):
        return self._history
    @get_history.setter
    def get_history(self,newvlue):
        if newvlue =='1995/02/03':
            self._history=0
        else:
            self._history=newvlue
            # توججه شود که دیگه اینجا نیاز نیست ریترن بشه یه بار در گتر ریترن شده
'1995/02/03'
myname=mohasebe_sen('2023/12/18')
# نکته باید برای فراخوانی اسم تابع را بیاری فراخوانی کنی  
# اگر میخوای  میتونی به اسم همون اتربیوت  اینیت باشه
# یعنی شما داری
get_history
# را بجای
self._history
# قرار میدی

print(myname.get_history)
# 2023/12/18

# اینجا اگر تاریخ غلط را واردکنیم که مقیدش کریدم نکنه دیگه اونو نمیاره بلکه چیزی که ما میخوایم را برمیگردونه
myname.get_history='1995/02/03'
print(myname.get_history)
# 0




# ////



# کار با پراپرتی
# میاد یه فانکشن را تبدیل به متغیر میکنه و دیگه نیاز نیست پرانتز بزاریم
class laptob_lenovo:
    made='USA'
    Mark_name='Lenovo'
    numbers_of_laptp=0
    permitted=['y700','legion5_wa','Legion5_Pro-AC']
    Wherehouse=[]
    def __init__(self,model,cpu,ram,hard,year_made) :
        self.name=model
        self.cpu=cpu
        self.ram=ram
        self.hard=hard
        self.year_made=datetime.datetime.now().year-year_made
        # if self.name not in laptob_lenovo.permitted:
        #     raise ValueError (f'{self.name} is not in {laptob_lenovo}')
    @property
    def show(self):
        print (f'made in:  {laptob_lenovo.made}, year_made is {self.year_made}')
    


y700=laptob_lenovo('y700',2.4,8,1,2016)
# print(y700.ram)

class Acer(laptob_lenovo):
    pass

Nitro_5=Acer('Nitro_5',2.4,16,512,2019)
 
# read only است prooerty
(Nitro_5.show)
# made in:  USA, year_made is 4

# این فقط میخونه 
# برای ست کردن باید این کار را کرد
    @property
    def show(self):
        print (f'made in:  {laptob_lenovo.made}, year_made is {self.year_made}')
    @show.setter
    def show(self,varshow):
        pass
# ست کرد و چیزی قرار داد

# ///
# فایده گتر و ستر
# گتر
# وقتی که نخوایم یه تابع را دوباره فراخوانی کنیم و میخوایم روی همون  پراپرتی که داده کار کنه
#یعنی در تابع دیگر تنظیم نکنه 
# از گتر استفاده میکنیم

# ستر 
# برای اینکه ورودی را کنترل کنه و تنظیم کنه بر معیاری که ما میخوایم 
# و تغیر ورودی را کنترل میکنه 
# نه اینکه ورودی را کنترل کنه  تا
#  هر ورودی ای نشه داد
# مثلا
my=class('str')
my.name= 345
# ستر میاد ۳۴۵ را کنترل میکنه که مثلا اینتیجر نشه نه اینکه از اول استرینگ را نده
# یعنی موقع تغیر اون تابع فعال میشه نه موقع ورودی اول در کلاس


    # در حقیقت پراپرتی باعث میشه که اون اتربیوت در اینیت یه اندرلاین بخوره
    # اما چرا؟ چرا پرایویت میکنیم و چه فایده داره؟
    @property 
    def name (self):
        return self.ـname

# سوال اما اینجا چرا نیو ولیو را میزنه . اصن چیه ایا متغیر جدیده ؟
# ایا نمیتونستیم همینجا ست کنیمش؟ بدون پراپرتی
    @name.setter
    def name(self,newvalue):
        if #......
# این نیو ولیو متغیر تازه است که بعدا اولی را تغیرش داده


        

# مثال 
# کار گتر و ستر تنظیم کردن است بر داده ورودی
# گتر و ستر 
# مکانیسمشو نفهمیدم ولی کاری که میکنه را فهمیدم
# هرچند برای کد نویسی میتونم در اون محدوده بکارش ببرم ولی خلاقیت نمیتونم بدارم
class Persson:
    def __init__(self,name):
        # نخست پرایتویت میکنیم. پروتکتد میکنیم
        # اما چرا و چه کاربردی داره؟
        # ؟؟؟؟؟؟؟؟؟؟؟
        # برای اینکه از حالت عمومی بودن دربیاد و راحت بهش دسترسی نداشته باشه
        # اما چه ارتباطی داره و کجا درست میشه؟ :
        self.ـname=name

    
    # به اسم اتربیوت  بدون پرایویت یه اتربیوت میسازیم   
    # چه کاربردی داره؟
    # برای اینه که در ستر بکار بره ؟؟
    @property   
    def name (self):
        return self.ـname
    # تا به شکل اتربیوت کار کنه
    # یعنی پرانتز نداشته باشه 
    # اما چه فایده ای داره این پرانتز نداشتن؟
    # پاسخ اینه که اگر تابع باشه باید دوبار مقدار بدیم
    # و یک بار نام را فراخوانی  گت میکنه و یکبار ست   میدده
    
    # اینجا ستر است 
    # اسم همون متد باشه و چون هم نام میشه باید پراپرتی بیاری به عنوان ستر 
    # ستر تنظیم میکنه یا اصلاح میکنه
    # یا خطا میده ورودی  در فراخوانی اینستنس را 
    # کارش همینه
    @name.setter
    def name(self,myvalue):
        if not isinstance (myvalue,str):
            raise ValueError ('adad manfi hastesh')
        self._name=myvalue
        # مای ولیو اون چیز است که جدیده متغیر جدید
        
name1=Persson('mamad')
print(name1.name)

# name1.name=123

# این کار را که بکنیم و بخوایم عدد بدیم
# اینو میده که تعریف کردیم
# ValueError: adad manfi hastesh

# جالبه الان عوض نکرد
name1.name='ali'
print(name1.name)
# mamad
# mamad
# و جالبتر اینکه در لیترالش این علی را میاره
# (property) name: Literal['ali']

# جالبه که الان اومد وارد کرد اگر به اندرلاین بدیم
name1.ـname=123
print(name1.name)
# 123


name1.name='ali'
print(name1._name)
# الان علی را تغیر ایجاد میکنه


# پاسخ مشکل اینجا بود که 
name1.ـname
# فرق داره با 
name1._name
# موقع فارسی نویسی اینو وارد کرده بودیم


    

# //////////
# انوا ع حالات ارث بری 
# بین سه کلاس
# 1- 
A
B
C(A,B)

# 2-
A
B(A)
C(A)

# 3-
A
B(A)
C(B)

# 4-

# /
# ارث بری بین ۴ کلاس




# ///////
# انواع حالات ارث بری متغیر ها
# ارث بری وقتی که متغیری اضافه بشه به سلف های فرزند۱- 


# ۲- ارث بری وقتی که چیزی از سلف فرزند کم بشه که در مادر نبود


# ۳-  ارث بری وقتی که متغیری در کلاس مادر جاشو عوض میکنه یا نقششو عوض میکنه 


# در مورد اتربیوت ها
# ۴-۱

# ۴-۲

# ۴-۳


# //////////
# در مورد توابع اینستنس
# ۵-۱

# ۵-۲

# ۵-۳


# در مورد توابع کلاس
# ۶-۱

# ۶-۲

# ۶-۳

# //////

# حالت ۱-۱ 
# ارث بری چند گانه 


# ارث بری چندگانه 
class Person:
    def __init__(self, name):
        print("Person Init")
        self.name = name

    def sayHello(self):
        return f"hello {self.name} in Person Class"

    def sayBye(self):
        return f"goodbye {self.name}"
    
class User:
    def __init__(self, name):
        print("User Init")
        self.name = name

    def sayHello(self):
        return f"hello {self.name} in User Class"

# ترتیب اینجوریه که میاد از اینییت کلاس اول یعنی چپ ترین داخل پرانتز ارث بری میکنه
class Admin(Person, User):
    def __init__(self, name):
        super().__init__(name)
        
p1=Admin('mohammad')
print(p1.sayHello())
# hello mohammad in Person Class
# هرچند میشه تابع ای درون کلاس دوم را هم داشته باشه
print(p1.sayBye())
# goodbye mohammad
# این از کلاس دوم بود با اینکه در اینیت اولی را فراخوانی کرد میشه از اینیت دوم هم بیاره

# ////////
# موقعی که در دو کلاس دو نام مشترک اما کار متفاوت داشتیم
# اگر هر دو یه متغیر داشته باشند و دو تا اینیت را در کلاس سوم بخوایم فراخوانی کنیم راه حلش 
# name mangaling 
# است
class Person:
    def __init__(self, name):
        print("Person Init")
        # در اینجا تعریفش میکنی تا بعد فراخوانی کنی درون تابع ای
        self.__name = name

    def sayHello(self):
        # اینجا نیم منگلینگ میکنه تا اگر دو چیز به یه اسم باشند در دو کلاس دو کار متفاوت را کنند
        return f"hello {self._Person__name} in Person Class"

    def sayBye(self):
        return f"goodbye {self._Person__name}"


class User:
    def __init__(self, name):
        print("User Init")
        self.__name = name

    def sayHello(self):
        return f"hello {self._User__name} in User Class"

# اینجا از هر دو اینیت استفاده میکنه
class Admin(Person, User):
    def __init__(self, name):
        print("Admin Init")
        print(f'got name is {name}')
        # super().__init__(name)
        User.__init__(self, 'user name')
        Person.__init__(self, 'person name')


person_1 = Admin('mohammad')


print(person_1._Person__name)
# person name
print(person_1._User__name)
# user name

# /////////////
# 
# 
# ترتیب استفاده از تابعی که در  یک اینستنس فراخووانی میشه 

# method resolution order

# __mro__
# mro()
# help(cls)


class A:
    def say_hello(self):
        print("hello python in A")


class B(A):
    pass
    # def say_hello(self):
    #     print("hello python in B")


class C(A):
    pass
    # def say_hello(self):
    #     print("hello python in C")


class D(C, B):
    pass
    # def say_hello(self):
    #     print("hello python in D")


item = D()

# item.say_hello()

print(help(D))



# ///////////
# polymorphism
# چند شکلی یا چند ریختی

# متد یکسان داشتن چند کلاس میشه چند ریختی ۱- 
# مثلا
#در همه اینا کپی و لن  اجرا میشه این متد پلی مورفیسم است
# numbers = [1, 2, 3, 4, 5, 6]
#
# myNums = {1, 2, 3, 4, 5, 6}
#
# person = {
#     'name': 'sara',
#     'family': 'miladi'
# }
#
# numbers.copy()
# myNums.copy()
# person.copy()
#
# print(len(numbers))
# print(len(myNums))


# ساخت پلی مورفیسم
class Animal:

    def makeSound(self):
        raise NotImplementedError


class Dog(Animal):
    def makeSound(self):
        return "cat is making sound"


class Cat(Animal):
    def makeSound(self):
        return "cat is making sound"


class Worm(Animal):
    def makeSound(self):
        return "worm does not make any sound"


dog = Dog()
cat = Cat()
worm = Worm()

print(cat.makeSound())

print(dog.makeSound())

print(worm.makeSound())

# اینجا ساختیم خودمون 

# حالا اگر 
# 
# مقید کنیم که حتما یک کلاس که تعریف میکنیم باید پلی مورفیسم باشه و از یک متد استفاده کنه
# در کلاس مادر خطا میاریم  که اگر دختر ها ارث بری کردند خطا را نشون بده
class Car:
    def move(self):
        raise NotImplementedError
# و بعد که کلاس دختر نداشت
class Benz(Car):
    def __init__(self, model):
        self.model = model

    # def move(self):
    #     print(f"{self.model} is moving")
    
    
# حالا اون متد را که فراخوانی کنیم اگر بود که خروجی میده اگر نبود خطا میده
sls = Benz('sls')
sls.move()
# sls is moving

    # اینجا خطا میده که هی تعریف نکردی
        # raise NotImplementedError
# NotImplementedErro

# برای اون شیوه درست اینه باید تعریف کنی واسش


# حالا اون متد را که فراخوانی کنیم اگر بود که خروجی میده اگر نبود خطا میده
sls = Benz('sls')
sls.move()
# sls is moving

# در موقع تعریف تابع دکمه 
crtl + space


# ۲- روش استفاده از پلی مورفیسم ها
# هر کلاس از ابجکت ارث بری میکنه 
# بخاطر همین برخی از کلاس ها که تعریف میکنیم اتومات خودشون  
__repr__
# و لن و... را دارند
# که خودمون اوررایت میکنیمشون 
# 
class Person:
    def __init__(self, name, family, age, money):
        self.name = name
        self.family = family
        self.age = age
        self.money = money

    def __repr__(self):
        return f"{self.name} {self.family}"
# اگر با اف استرینگ نزنی اینو میده
# __repr__ returned non-string (type tuple)

    def __len__(self):
        return self.age
# مثلا اینجا متد لن را واسش اوردیم روی ایج که اون برگردونه

person_1 = Person('mohammad', 'ordookhani', 24, 1000)
person_2 = Person('sara', 'moradi', 18, 2000)

print(person_1)
print(len(person_1))
# 24

# حالا یه سری چیز ها دیگه هم هستند 
# جمع و ضرب و تقسیم 

    def __add__(self, other):
        return self.money + other.money

    def __mul__(self, other):
        return self.money * other.money

    def __truediv__(self, other):
        return self.money / other.money

# حالا از این به بعد  برای اون کلاس میشه چیزی که میدیم را جمع کنه 
print(person_1 + person_2)
# 3000
print(person_1 * person_2)
# 2000000
print(person_1 / person_2)
# 0.5
# تا پیش از اون خطا میداد


# //////
# کار دیگه چند ریختی اینه که رفتار متفاوت را در قبال کلاس های متفاوت نشون میده
# همریختی 
# پلی مورفیسم
# دو تا کلاس تعریف میکنیم که یه متد اما دو تا رفتار جدا داشته باشه

class dog:
    def talk (self):
        print('bark')

class cat :
    def talk(self):
        print('meow')

# حالا جدا در تایع دیگر
# یعنی برای فراخوانی میایم یه تابع تعریف میکنیم
# تا روی اینستنس ما  اون متد اجرا بشه
# یعنی روی تابعی درون کلاس یه تابع بیاریم
def speak(animal):
    animal.talk()
    # اینجا متد درون کلاس را روی یه ورودی 
    # درون تابع دیگر میاریم
#  استفاده کلاس و تابع


# حالا اینستنس ایجاد میکنیم از کلاس ها
mydog= dog()
mycat=cat()

# حالا میشه یه تابع را فراخوانی کرد و درون اون تابع را اینستنس و شی داد که از یک کلاس شروع شده باشه
speak(mydog)
# bark
speak(mycat)
# meow


# مثال دیگرش اینه که یه بسکتبالیست میتونه فوروارد باشه و یهفوتبالیست هم فوروارد باشه




# ///////////
#  متد
isinstance 
# در کلاس
# دو تا متغیر میگیره اون چیزی که بررسی بشه
# با معیار

 def name(self,myvalue):
        if not isinstance (myvalue,str):


# //////////
# تفاوت 
del 
# , 
deleter

در 
del
# وقتی حذف کرد ارور میده 
# ولی اگر  در کلاس داندر 
# دیلیتر را بیاریم 
# مقدار 
None
# را بر میگردونه و نه ارور 


مثال del

class Persson:
    def __init__(self,name):
        self.ـname=name

    @property   
    def name (self):
        return self.ـname
    @name.setter
    def name(self,myvalue):
        if  isinstance (myvalue,int):
            raise ValueError ('adad manfi hastesh')
        else:
            self._name=myvalue
        
p=Persson('mamad')
print(p.name)

p.name='ali'
del p.name
print(p.name)
# AttributeError: can't delete attribute 'name'


حالا 
deleter

class Persson:
    def __init__(self,name):
        self._name=name
    @property   
    def name (self):
        return self._name


    @name.setter
    def name(self,myvalue):
        if  isinstance (myvalue,int):
            raise ValueError ('adad manfi hastesh')
        else:
            self._name=myvalue
        
    @name.deleter
    def name(self):
        self._name =None
p=Persson('mamad')
print(p.name)

p.name='ali'
del p.name

print(p.name)
# None

# ///////
# مساله 
property
# getter
# ایا برای هر اتربیوت یه بار ستر و گتر تعریف کنیم ؟
# اینجا ما برای 
# name
# تعریف کردیم
    def __init__(self,name,cpu):
        self.ـname=name
    @property
    def name (self):
        return self.ـname


    @name.setter
    def name(self,myvalue):
        if  isinstance (myvalue,int):
            raise ValueError ('adad manfi hastesh')

# و نه برای 
# cpu

# که انگار یه راه اینه که بیایم تک تک تعریف کنیم دوباره برای هر متغیر 

# راه ۲ 
# descriptor 










# /////////
# کدی که میاد  از کلاس مادر اتربیوتی را میگیره 
# بعد توی کلاس بعدی مقدارشو عوض میکنه 
# یعنی میشه چیزی را اورد ولی در کلاس دیگر بهش دسترسی داشت و
# میشه خود کلاس بالایی را فقط به عنوان کلاس محاسب اورد
class Parent:
    def use_it(self, x):
        return self.multiplier * x

class Boy(Parent):
    multiplier = 2


class Girl(Parent):
    multiplier = 3


#  
boy = Boy()
print(boy.use_it(10))
# 20
# 

girl = Girl()
print(girl.use_it(10))
# 30


# ///////////////
کاربرد 
abc
from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):

    @property
    @abstractmethod
    def x(self):
        pass

    def print_me(self):
        print(f'x = {self.x}')

class B(A):

    @property
    def x(self):
        return 1

# A().print_me()
# TypeError: Can't instantiate abstract class A with abstract method x

B().print_me()  # prints x = 1
# x = 1


# //////////
# نکته 
# اگر کتابخانه ای را درون کلاس بزاری در همون کلاس نمیشه ازش استفاده کرد

class A:
    from statistics import mean

    def __init__(self,ghad,vazn,sen):
        self.ghad=ghad
        self.vazn=vazn
        self.sen=sen
# کدی که بیاد به اندازه تعداد اعضا را درون لیست کنه
    @staticmethod
    def miangin():
        # mynumber=int(input('give me the number:'))
        # for i in range(3):
        ghad=mean([int(i) for  i in input('give me the ghad numbers: ').split()])
        vazn=mean([int(i) for i in input('give me the vazn: ').split()])
        sen=mean([int(i) for i in input('give me the sen: ').split()])
        print ('',ghad,'\n',vazn,'\n',sen )  
    # miangin()
    
A. miangin()

# NameError: name 'mean' is not defined




# بلکه باید بیرون از کلاس بزاری
from statistics import mean

class A:

    def __init__(self,ghad,vazn,sen):
        self.ghad=ghad
        self.vazn=vazn
        self.sen=sen
# کدی که بیاد به اندازه تعداد اعضا را درون لیست کنه
    @staticmethod
    def miangin():
        # mynumber=int(input('give me the number:'))
        # for i in range(3):

        ghad=mean([int(i) for  i in input('give me the ghad numbers: ').split()])
        vazn=mean([int(i) for i in input('give me the vazn: ').split()])
        sen=mean([int(i) for i in input('give me the sen: ').split()])
        print ('',ghad,'\n',vazn,'\n',sen )  
    # miangin()
    
A. miangin()




# یا اینکه کتابخانه را درون هر تابع بندازی
class A:

    def __init__(self,ghad,vazn,sen):
        self.ghad=ghad
        self.vazn=vazn
        self.sen=sen
# کدی که بیاد به اندازه تعداد اعضا را درون لیست کنه
    @staticmethod
    def miangin():
        # mynumber=int(input('give me the number:'))
        # for i in range(3):
        from statistics import mean

        ghad=mean([int(i) for  i in input('give me the ghad numbers: ').split()])
        vazn=mean([int(i) for i in input('give me the vazn: ').split()])
        sen=mean([int(i) for i in input('give me the sen: ').split()])
        print ('',ghad,'\n',vazn,'\n',sen )  
    # miangin()
    
A. miangin()



# //////////
# این چجوری حل بشه؟
# قاطی کردن تابع با کلاس سلف
from statistics import mean
class A:
    def __init__(self,ghad,vazn,sen):
        self.ghad=ghad
        self.vazn=vazn
        self.sen=sen
    # @staticmethod
    def miangin(self):
        # mynumber=int(input('give me the number:'))
        # for i in range(3):
        self.ghad=mean([int(i) for  i in input('give me the ghad numbers: ').split()])
        self.vazn=mean([int(i) for i in input('give me the vazn: ').split()])
        self.sen=mean([int(i) for i in input('give me the sen: ').split()])
        return ('',self.ghad,'\n',self.vazn,'\n',self.sen )  
    # miangin()
# مشکلش اینه که اینجا یه سلف میگیره اگر ندی خطا میده
myAclass=A. miangin()
# A.miangin() missing 1 required positional argument: 'self'

# اگر هم اینجوری بنویسیم سه تا میخواد
myAclass=A()
myAclass.miangin()
# TypeError: A.__init__() missing 3 required positional arguments: 'ghad', 'vazn', and 'sen'

# اینو امتحان کن
# https://stackoverflow.com/questions/52831534/why-is-a-method-of-a-python-class-declared-without-self-and-without-decorators
# /////

# کار با استاتیک متد
class MyClass:
    def __init__(self):
        pass

    def myStaticMethod():
        print("a static method")

    @staticmethod
    def myStaticMethodWithArg(my_arg):
        print(my_arg)
        print("a static method")


MyClass.myStaticMethod()
# a static method
MyClass.myStaticMethodWithArg("skhsdkj")
# skhsdkj
# a static method
abc = MyClass()
abc.myStaticMethodWithArg("avc")
# avc
# a static method


# //////
# نوشتن کلاس بدون استفاده از اینیت
# اینجا هیچ کاری با اینیت و سلف نداشتم 
# از کلاس هم استفاده کردم ارث بری هم کردم ام عملا هیچ  نمونه ای ازش درست نکردم
from statistics import mean
class A:
    # def __init__(self,ghad,vazn,sen):
    #     self.ghad=ghad
    #     self.vazn=vazn
    #     self.sen=sen
    @staticmethod
    def miangin():
        mynumber=int(input('give me the number of whole:'))
        sen=mean([float(i) for i in input('give me the sen: ').split()])
        ghad=mean([float(i) for  i in input('give me the ghad numbers: ').split()])
        vazn=mean([float(i) for i in input('give me the vazn: ').split()])
        return (sen,ghad,vazn)  
class B(A):
    pass
my_A=A

my_aa=(my_A.miangin())
my_Aa=dict(enumerate(my_aa))
# print(my_Aa)
my_B=B
myBb=(my_B.miangin())
mybb=dict(enumerate(myBb))
# print(mybb)
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
comparable()

# ////////
# اجرای یک کتابخانه به کلاس ها
        self.heightAve = float(mean(self.heightList))
        
# ////////

# فراخوانی اینپوت در موقع ساخت اینستنس
class birth_calculator:
    def __init__(self,birthday):
        self.berth=birthday

    def birth_splitter(self):
        
 
# اینجا اینپوت را در ساخت اینستنس میزاریم

golmleh=birth_calculator(input('give me the date in like 1995/02/03 format: '))
print(golmleh.birth_splitter())

# /////
# گذاشتن اینپوت در کلاس هم میشه؟


# //////
# مساله
# چرا این وقتی که در حلقه میوفته و قعدتا باید پرینت رانگ بده نمیده  بجای ارور میده؟
from datetime import datetime
class mohasebe_sen:
    def __init__(self,history):
        self._history=history
        # print(self._history) #1995/02/03
        self.ـhistory =datetime.strptime((''.join(self._history.split('/')) )[:8],'%Y%m%d').date() #1995-02-03
        # print(self._history) #1995-02-03
        if self.ـhistory.day >31 or self._history.month > 12:
            print ('WRONG')
        else: 
            print (datetime.today().date().year - self._history.year)
my_instance=mohasebe_sen('1995/02/03')
# 28 را میده

my_instance=mohasebe_sen('1995/23/43')
# این را  ولی این خطا را میده
# raise ValueError("unconverted data remains: %s" %
# ValueError: unconverted data remains: 3

# و جالبه که اینم میده و نه خطا میده نه  پرینت رانگ منو میده
my_instance=mohasebe_sen('1995/02/232')
# 28
# ////
# ؟؟؟؟؟؟؟؟/
# پرسش دوم در باره 
# گتر و ستر
# پراپرتی ها
# در ادامه کد بالا اگر اینرا بدیم 
    @property
    def regular(self):
        return self._history
    @regular.setter
    def regular(self,myvalue):
        myvalue=datetime.strptime((''.join(myvalue.split('/')))[:8],'%Y%m%d').date()
        # این از اول تناقض داره 
        # چون از اول وارد نمیشه کرد تاریخ  غلط تعریف نشده را اگر به فرمت تاریخ برده باشیم
        if myvalue.day >31 or myvalue.month >12:
            return ('WRONG')
        else:
            self._history=myvalue

my_instance=mohasebe_sen('1995/02/03')

my_instance._history ='1995/02/53'
# این خودشو پرینت میکنه یعنی اینو بجای اینکه رانگ بده در ستر
# '1995/02/53'
# اگر  اینو فراخوانی کنیم  هم میگه نه 
# منظورت 
# _history
# هست ایا؟
my_instance.history



# انگار که کل پراپرتی و گتر و ستر خاموش هستند و هشتک دارن
# اونم همونو میده

# مشکل اینه که ما 
regular
# را صدا نکردیم



# مشکلی که این خطا را میده
the_date= current_age('1995/73/53')
# ValueError: unconverted data remains: 3
# raise ValueError("unconverted data remains: %s" %
# ValueError: unconverted data remains: 3
# اینه که تاریخ نادرست را از اول وارد نمیکنه که بعدش ما بخوایم واسش بجاش پرینت کنیم رانگ یا هرچی

# پس اگر ارور میخوایم 
# یک راه اینه که قبلش ارور را بدیم و ببندیم

# یه راه اینه که ارور ای که میده را به چیزی که خودمون میخوایم تبدیل کنیم
# /////////
# ?????////////
# وقتی پرینت میکنی یک تاریخ را درست میده

# ولی وقتی ریترنش میکنی نه
        #   self._history= history
        #     return(datetime.strptime((self._history)[:8],('%Y%m%d')).date())
# TypeError: __init__() should return None, not 'datetime.date'
# بخاط اینه که این متد اغاز گر ساخت ابجت است و چیزی را نباید باهاش برگردونی
# ///
# /////////
# نکته 
# وقتی نریزیم توی یه متغیر هنزو اینو میشناسه
class current_age :
    def __init__(self,history):
        history=(''.join(history.split('/')))
        print(history)
        if int(history[4:6]) > 12 or int(history [6:8]) >31 :
            return ('WRONG')
        else:
            self._history= history
            diffrence= datetime.today().date().year - datetime.strptime(self._history [:8],('%Y%m%d')).date().year
            print(diffrence)
# {'_history': '19950228'}

# ولی وقتی بریزیم تو یه سلف 
else:
            self._history= history
            self._history= datetime.today().date().year - datetime.strptime(self._history [:8],('%Y%m%d')).date().year
            print(self._history)
# {'_history': 28}

# //////////
# پرسش
# property
# چرا این خطا را میده؟
# گتر و ستر

from datetime import datetime
class current_age :
    def __init__(self,history):
        history=(''.join(history.split('/')))
        # print(history)
        self._history=history
        if int(history[4:6]) > 12 or int(history [6:8]) >31 :
            return ('WRONG')
        else:
            self._history= history
            diffrence= datetime.today().date().year - datetime.strptime(self._history [:8],('%Y%m%d')).date().year
            print(diffrence)

        @property
        def get_history (self):
            return self._history
        @history.setter
        def get_history(self,new_history):
            new_history= ''.join(new_history.split('/'))
            if int(new_history[4:6]) > 12 or int(new_history[6:8])>31:
                return('WRONG')
            else:
                self._history=datetime.strptime(new_history[:8],('%Y%m%d')).date()
                self._history=(datetime.today().date().year - self._history.year)
    
the_date= current_age('1995/02/28')

print(the_date.get_history)
# چرا اینو میده
# AttributeError: 'str' object has no attribute 'setter'. Did you mean: 'center'?

# ////



# /////////////
# ست اتربیوت
# setattr
# کار با دیکشنری و کلاس
# ست اتربیوت  میاد دو مقدار را میگیره 
# ریختن دیکشنری در کلاس
# کل دیکشنری را یک  اینستنس یا شی میکنه
class AllMyFields:
    def __init__(self, dictionary):
        # میتونیم درون  کلاس  حلقه ای را بنویسیم که دیکشنری را بکار میندازه و خروجی میده
        for k, v in dictionary.items():
            setattr(self, k, v)
        # سلف که ابجکتشه و کا و وی هم به ترتیب اتربیوت هستند و مقدار اون اتربیوت
o = AllMyFields({'a': 1, 'b': 2})
print(o.a)
# 1
# اینستنسی به اسم 
# o
# اتربیوتی به اسم 
# a
# داره که مقدارش 1 است


# راه دیگر 
# دیکشنری ای که 
# https://stackoverflow.com/questions/30113723/creating-class-instance-from-dictionary

class MyClass(object):
       def __init__(self, **entries):
        self.__dict__.update(entries)

dict = {'key1': 'value1', 'key2': 'value2', 'redundant_key': 'redundant_value'}

ob = MyClass(**dict)
print(ob.key1)
# value1
# فقط این روی دیکشنری تودرتو کار نمیکنه


# //////
# اینم کار میکنه
# فقط نوشته بود ایتر تایمز بجای ایتمز
class MyClass(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

dict = {'key1': 'value1', 'key2': 'value2', 'redundant_key': 'redundant_value'}
ob = MyClass(**dict)
print(ob.key1)
# https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields
# 
# 
# ////

# مساله ۱ چگونه در کلاس های ارث بری اینها را قرار ببدیم؟

# مثال دیگر 

# //////////

# چگونه  کلید دیکشنری را یک اینستنس کنه
# اتربیوت را با توجه به جایگاه بشناسه 
# مقدار را ما بهش بدیم؟

# یعنی
# اسم دیکشنری بشه همون اینستنس
# کلید  به ترتیب بشه اتربیوت در اون کلاس 
# مقدار هم بشه ولیو اون اتربیوت
instanse={attribute:'value1' ,attribute2:'value2',attribute3:'value3',attribute4:'value4',attribute5:'value5',attribute6:'value6'}


class Footballer :
    def __init__(self,**atribute):
        # اما اینجا چی باشه؟
hamid={name:'hamid' ,age:21,height:185,nationality:'iran',post:'deffence',price:12000000}

hamid=Footballer('hamid',21,185,'iran','deffence',12000000)
# اینجا حمید اینستنس باشه 
# چند تا هم اتربیوت داره
# name,age,height,nationality,post,price
# مقدار هر کدوم هم این باشه
# 'hamid',21,185,'iran','deffence',12000000

# ???????????????????


# ////////
# تبدیل کلاس به دیکشنری

# فقط نفهمیدم تابع دوناتینگ چیه؟

class A(object):
    def __init__(self):
        self.b = 1
        self.c = 2
    def do_nothing(self):
        pass

a = A()
a.__dict__
# {'c': 2, 'b': 1}


# /////
# روش دیگر
# تبدیل کلاس به دیکشنری
class A(object):
    def __init__(self):
        self.b = 1
        self.c = 2
    # def do_nothing(self):
    #     pass

a = A()
print(vars(a))
# {'b': 1, 'c': 2}

# ///////

# گرفتن ورودی ها برای ساخت اینستنس از کاربر
# گرفتن اینستنس ها از کاربر  به عنوان دیکشنری
# https://stackoverflow.com/questions/46028544/create-object-of-class-from-string-user-input-python
# اگر کلاسی بداریم که
class Human:
     def __init__(self,age,height):
          self.age=age
          self.height=height

mydict={}
mydict[input (' give me the key: ')]= Human(input('give me the age: '),input('give me the height: '))
print(mydict)

# give me the age: 31
# give me the height: 165
#  give me the key: mamad
# {'mamad': <__main__.Human object at 0x0000021F5D540370>}
# متغیر  را نمیده 
# چرا


# ساخت اینتسنس از دیکشنری
# دریافت گام به گام
# این مثل این میمونه
class Human:
     def __init__(self,age,height):
          self.age=age
          self.height=height

mydict={}
mydict['mamad']= Human(24,48)
print(mydict)

print(mydict.items())
# dict_keys(['mamad'])
# dict_items([('mamad', <__main__.Human object at 0x000001B0FE100370>)])

# پاسخ ۱ 
# متد ریپر
class Human:
     def __init__(self,age,height):
          self.age=age
          self.height=height
     def __repr__(self):
          return f'{self.age }, {self.height}'
    # حتما با متد فرمت بدی بهش
    # یا استرینگ فرمت
    # وگرنه خطا میده
mydict={}
mydict['mamad']= Human(24,48)
print(mydict)
# {'mamad': 24, 48}

print(mydict.items())
# dict_items([('mamad', 24, 48)])

# ///
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

# ////////

# ساخت لیستی از اینستنس ها 
# دسترسی به اینستنس های لیست

class Human:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def __repr__(self):
        return f'{self.name}{self.height}'
mylist=[]
mylist.append(Human('mamad',165))
print(mylist)
# [<__main__.Human object at 0x000002C6941F0370>]
# با متد رپر این میاد
# [mamad165]
# دسترسی
print(mylist[0].name)
# mamad
# ////////

# ساخت لیستی از اینستنس ها 
# ساخت اینستنس در حلقه  تک خطی
class Human:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def __repr__(self):
        return f'{self.name},{self.height}'
    
    
# ساخت اینستنس به وسیله حلقه
mylist=[]
mylist+=[Human(name,height) for name,height in [('mamad',168),('reza',175),('javid',181)]]

print(mylist)
# [mamad,168, reza,175, javid,181]

# حالا دسترسی به اون
for ins in mylist:
    print(ins.name)
    print(ins.height)
# mamad
# 168
# reza
# 175
# javid
# 181
# //////
# ساخت اینستنس به ترتیب
# ساخت اینستنس 
# ساخت شی
# ساخت اینستنس ها در حلقه
# میتونیم یه حلقه بزنیم و یه سری شی بسازیم به ترتیب 
for char in range(1,4):
    name='player'
    print((Human('%s%i'%(name,char))))
# player1
# player2
# player3

# نوع همشون هم کلاس باشه
for char in range(1,4):
    name='player'
    print(type(Human('%s%i'%(name,char))))
# <class '__main__.Human'>
# <class '__main__.Human'>
# <class '__main__.Human'>




# ///////
# حتی میتونی بریزیشون توی یه لیست
m_players=[]
for char in range(1,4):
    name='player'
    m_players.append((Human('%s%i'%(name,char))))
print(m_players)
# [player1, player2, player3]

# که  همشون اینستنس کلاس باشند بازهم
for member in m_players:
    print(type(member))
# <class '__main__.Human'>
# <class '__main__.Human'>
# <class '__main__.Human'>

# بعد میتونی بهشون دسترسی داشته باشی
# مثلا اگر کلاس ما یه اتربیوت به اسم نیم داشته باشه میشه بهشون دسترسی داشت
for member in  m_players:
    print(member.name)
# player1
# player2
# player3


# ///////
# میشه اینستنس یک کلاس کلید باشه و اینتنس ولیو اش یک کلاس دیگه باشه
# کلیدش اسم اون کلاس بالایی باشه و ولیو اش کلاس پایینی؟؟؟؟؟؟؟؟؟؟
# بله
class Human:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f'{self.name}'    

class Footballer(Human):
    def __init__(self,name,age,post):
        super().__init__(name)
        self.post=post
        self.age=age
    def __repr__(self):
        return f'{self.name}, {self.age},{self.post}'

m_players=[]
for char in range(1,4):
    name='player'
    m_players.append((Human('%s%i'%(name,char))))
print(m_players)


# زدن دیکشنری و اینپوت گرفتن اونها و اینستنس یک کلاس کردن
mydict={}
for member in  m_players:
    mydict [member.name]=Footballer(input('give me the name of player: '),int(input('give me the age of player: ')),input('give me the post of the player:'))
print(mydict)
# {'player1': mamad, 25,deffence, 'player2': ali, 53,attack, 'player3': ayda, 45,halfback}


# اما چطور مطمئن بشم همونه؟ یعنی کلید یه کلاس دیگه است و ولیو یکی دیگه؟
# این چه فایده ای داره؟ 
# یعنی اگر کلید یه استرینگ هم بود فرق نداشت



# ####
# اشاره به ویژگی های یک ابجکت  به عنوان ولیو دیکشنری در حلقه

# ساخت ابجکت  از طریق حلقه
# ساخت ابجکت به عنوان ولیو 
# دسترسی به ویژگی های یک ابجکت با اسم ولیو ای که در حلقه افتاده
# اگر  یک کلاس اینجوری بود که ولیو هاش فقط یه کلاس بودند برای دسترسی به یک ولیو کافیه اتربویت را بدی
for chara  in A.items():
    print(f'{list(chara)[1].name} is player of A')
# این  اشاره داره میکنه به ولیوی اون دیکشنری که چون اون ولیو خودش یک شی  ای از کلاس است میتونیم 
# بجای اشاره به تاپل ای که در ولیو است 
(chara)[1][2]
# بزنیم 
(chara)[1].name
# که اصلا باید  بزنیم 
{list(chara)[1].name} 

# ////

# ////////
# میشه اینجوری تعریف کرد سلف را
# یعنی بعدش بهش بده
# به کلاس هم ابجکت بدیم
class RandomChoiceDict(object):
    def __init__(self):
        self.mapping = {}
# /////
# مقایسه کلاس ها با هم
# https://www.geeksforgeeks.org/python-__lt__-magic-method/


# /////


# /////////
