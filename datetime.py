import datetime 

import jdatetime

print((jdatetime.datetime.now()))
# 1401-10-20 14:37:56.708408


# ///////
# datetime
my_history=datetime.datetime.now()
print(my_history)
# 2023-01-29 15:56:50.388594




# /////
# اینم همونه  نشون دادن تاریخ 
from datetime import datetime
print(datetime.today())
# 2023-02-01 14:55:26.134563


# //////
# حالا سال را نشون بده

my_history2=datetime.datetime.now().year
print(my_history2)
# 2023
# //////////
my_history3=datetime.datetime.now().day
print(my_history3)
# 29


# //////
# حالا میتونیم محاسات را انجام بدیم
my_history4=datetime.datetime.now().year-100
print(my_history4)
# 1923

# ///////
my_history5= (datetime.datetime.now()) - jdatetime.datetime.now()
print(my_history5)
# 0:00:00

# ///////
# تفاوت سال میلادی و جلالی
my_history5= (datetime.datetime.now().year) - jdatetime.datetime.now().year
print(my_history5)
# 622

# ///////
my_history5= (datetime.datetime.now().year) - jdatetime.datetime.now().year
print(my_history5)
# 622
# ////


# تبدیل استرینگ به فرمت تاریخ 
# و تیدیل فرمت تاریخ به استرینگ
# تبدیل اینتیجر به فرمت تاریخ 
# تبدیل فرمت تاریخ به اینتیجر
# این تاریخ را کامل میده در لیست تبدیل تاریخ به استرینگ



# تبدیل تاریخ به استرینگ  و دو بخش مجزا کردن
print(str(datetime.today()).split())
# ['2023-02-01', '15:03:09.707183']

# حالا اشاره به   تاریخ سال و ماه و روز
print(str(datetime.today()).split()[0])
# 2023-02-01

# یا اینکه یه ضرب بنویسه
print(str(datetime.today().date()).split())
# ['2023-02-01']

# اینم همونه با متد 
# strftime
print(datetime.today().strftime('%Y-%m-%d'))
# 2023-02-01




# حالا نمایش با فرمت ساعت و ثانیه
print(datetime.today().strftime('%Y-%m-%d  %H:%M:%S'))
# 2023-02-01 15:12:19

# نمایش امروز با متد
date
# در استرینگ
from datetime import date
print(str(date.today()))
# 2023-02-01


print(type(date.today()))
# <class 'datetime.date'>


# /////
# نمایش تاریخ  فقط با فرمت سال و روز
print(datetime.datetime.today().date())
# 2023-02-01

# /////////

# تبدیل فرم تاریخ گرگوریان به میلادی
# این عدد معنای مشخصی داره لابد در تقویم
d=datetime.fromordinal(733828)
print(d)
# 2010-02-25 00:00:00


# ////
# تبدیل استرینگ به تاریخ
# هشت تا کاراکتر میشماره اگر بیرون بیوفته خطا میده
# وگر درون بیوفته میشماره اخری میشه عنصر روز اخر 

from datetime import datetime
mynumber='20101103'
my=(datetime.strptime(mynumber[:8],'%Y%m%d'))
print(my)
# 2010-11-03 00:00:00
print(type(my))
# <class 'datetime.datetime'>

# حالا اگر برش زدن را دستکاری کنی یا روز را وارد نکنی تغیر میکنه
# مثلا
# اینجا چون شیش بود شیش تا میره جلو و بعد اون دو تا را صفر میزاره
from datetime import datetime
mynumber='20101103'
my=(datetime.strptime(mynumber[:6],'%Y%m%d'))
print(my)
# 2010-01-01 00:00:00
# به گمونم میاد میشماره 
# چون سال ۴ تا میگیره 
# ماه دو تا 
# روز دو تا 
# میاد برش میزنه ۶ تا ۴ تای اولیشو برای سال میزاره
# بعدی یک هستش میاد صفر یک میخونه 
# بعدی هم یک هست که صفر یک میخونه

# ///
# توجه شود که حتما فرمت  این باشه
# یعنی درون استرینگ بزنی 
%Y%m%d
self._history=datetime.strptime(self._history[:8],('%Y%m%d')).date()

# ///////

# حالا اگر روز را نزاری در همین
from datetime import datetime
mynumber='20101103'
my=(datetime.strptime(mynumber[:6],'%Y%m'))
print(my)
# 2010-11-01 00:00:00


# ///
# تبدیل یه استرینگ  به تاریخ 
# تغیر استرینگ به تاریخ
# در یک خط
history= '1995/02/03'
history =datetime.strptime((''.join(history.split('/')) )[:8],'%Y%m%d').date()
# اول میای اسپلیت میکنی که هرجا فرمت بک اسشلش دید را بگیره بریزه توی لیست و سپس با هیچی جوین کنه تا استرینگ بشه 
# پس از اون استریپتایم را روش بکار میبریم تا به فرمت تاریخ تغیر کنه و سپس  دیت را اخر میاریم که ساعت و زمان را برداره ازش
#
# ///
# حالا کم کردن اکنون از تاریخ داده شده
# کافیه تاریخ اکنون را از  اون تاریخ تبدیل شده کم کنی

print( datetime.today()-my )
# 4475 days, 15:54:18.134670

# /////


# محاسبه از زمانی که بهش میدیم
# فاصله زمانی را حساب میکنه
# محسابه زمانی کارکرد کارمند
import datetime as dt
from dateutil.relativedelta import relativedelta


employee = '201011003'
date_joined = dt.datetime.strptime(employee[:6], '%Y%m')
result = relativedelta(dt.datetime.today(), date_joined)

print('The employee has been working for {} years, {} months and {} days'.format(
    result.years, result.months, result.days))

# The employee has been working for 9 years, 6 months and 11 days


# ////////


# ///////////
# کاربرد رلتیو دلتا
# اشاره به سال و ماه با لیست 
from datetime import date
from dateutil.relativedelta import relativedelta

birthday = list(map(lambda x: int(x), input().split('/')))
today = list(map(lambda x: int(x), str(date.today()).split('-')))

if birthday[1] > 12:
    print('WRONG')
elif birthday[2] > 31:
    print('WRONG')
else:
    t1 = date(year = birthday[0], month = birthday[1], day = birthday[2])
    t2 = date(year = today[0], month = today[1], day = today[2])
    age = relativedelta(t2, t1)
    print(age.years)
# ////

# نکته 
# تاریخ های انگلیسی ممکنه این خطارا بدهند
# ValueError: day is out of range for month

# مثلا برج ۲ یا همون فبریه ۲۸ روز دارد
# یعنی برای برج ۲ بیشتر از ۲۸ بزنی این خطار ا میده

# ژانویه ۳۱ روز   ۱
# فوریه ۲۸   ۲
# مارچ ۳۱   ۳
# اپریل ۳۰  ۳
# می ۳۱  ۴
# ژون ۳۰    ۵
# ژولای ۳۱   ۶ 
# اگوست ۳۱   ۷
# سپتامبر ۳۰   ۸
# اکتبر ۳۱   ۹
# نووامبر ۳۰   ۱۰
# دسامبر ۳۱   ۱۱

# ژفم آمژ ژاس اند

# ///////

# ولی چرا در متد
strptime 
history= datetime.strptime((''.join(history.split('/')))[0:8],('%Y%m%d')).date()
        print(history)
# وقتی بنویسیم 
the_date= current_age('1995/02/51')

# اینو میده
# ValueError: unconverted data remains: 1


# ///////
# ?????????
# پرسش 
# وقتی اینو بزنیم کامل و خوب میده
self._history= history
            diffrence=datetime.strptime((self._history)[:8],('%Y%m%d')).date()
            print(diffrence)
            now=(datetime.today().date())
            print(now)
# 19950228
# 1995-02-28
# 2023-02-03

# حالا اگر منها کنم به روز میده
  self._history= history
            now= datetime.today().date()
            diffrence=datetime.strptime((self._history)[:8],('%Y%m%d')).date()
            build=now - diffrence
            print(build)
# 10202 days, 0:00:00
# چون باید سال ها را از هم کم کنیم 
# و اخرشو باید بزنی سال
# .year
build=now.year - diffrence.year
            print(build)
# 28

# //////
# https://stackoverflow.com/questions/20327937/valueerror-unconverted-data-remains-0205
# https://stackoverflow.com/questions/65660619/how-to-make-months-not-exceed-12