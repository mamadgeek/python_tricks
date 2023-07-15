


# /////
# وقتی میخوایم دو تا شرط را با هم بررسی کنیم یا میشه از اند استفاده کرد و یا شرط های تو در تو 
# در اینجا اگر بزرگتر باشه را بررسی کردیم  . و در اون صورتی که بزرگتر باشه دو حالت داره یا بزرگتر یا کوچکتره 
# اگر کوچکتر باشه و اگر بزرگتر باشه 
# هرچند شاید بشه همین برنامه را با و منطقی و یا هم بشه نوشت
age= int(input('give me the age of the senathor: '))
big=int(0)
age2=int()
while age!= -1:
        if age>age2:
            if age<big:
                age2=age
                print(f'in ifif  age 2 is  {age2 }')
            elif age>big:
                age2=big
                big=age
                print(f'in ifelif  age 2 is  {age2 } and big is {big}')
        print(f'in else  age 2 is  {age2 } and big is {big} and age is {age} ')
        age= int(input('give me the age of the senathor: '))
print('the big age is ',big)
print('the age 2 is ', age2)

# //////////
# وقتی شرط الس همون = باشه دیگه نیاز نیست حتی بنویسیم الس را . 
number= (int(input('give me the number: ')))
    count = prime_count(number)
    if count>bigest:
        bigest=count
        bigestnumber=number
    elif count==bigest:
        if number>bigestnumber:
            bigest=count
            bigestnumber=number
        # else:
        #     bigest=bigest
        #     bigestnumber=bigestnumber
           
            # ایا اگر بریک کنیم در الس کار میکنه همون نتیجه ؟  یا اگر الس را هم نزاریم باز همون میشه؟ یعنی دستور ندیم همون میمونه؟
           # بله مساوی همون میمونه حتی نیاز نیست بنویسیم
            # (یه راه پیدا کردن مبتدی اینه که برای احتیاط کارهای مطمن را انجام میده ولی حرفه ای کار کمتر و راحت تر و سریعتر را ) 
print(bigestnumber, bigest)



# //////////////

# میشه ایف را درون فور قرار داد که تا 
# رسید به اون قطع کنه و گرنه ادامه بده
string = input("")
kol=[]
for i in range (1,11):
    string = string .lower()
    string = string .capitalize()
    kol.append(string)
    if i==10:
        break
    else:
        string = input("")
#print(kol)
for i in kol:
    print(i)
    
# //////////

# در این برنامه شمارنده را فقط برابر ی میکنه و اگر میخوای 
# شمارنده بیاد ل را بشماره بزارش روی حلقه فور
for i in sentence:

    count_big= 0
    count_small=0  
    # یه چیزی میخوام که بررسی کنه که اونی که میبینه بزرگه یا کوچیکه
    
    if i.isupper():
        print(i)
        count_big +=1
        print(f'count_big is {count_big} ')
    else:
        print(i)
        count_small+=1
        print(f'count_small is {count_small} ')


# //////////

number = int(input('give me:') ) 
if number >1:
    for i in range(2,number):
        if number % i ==0:
            print('not prime', i , number/i)
            break
# اگر در این خط بزنیم میره رد میکنه ولی اگر
# الس را یه خط جلوتر بزنیم مشکل ایجاد میکنه و یه بار هم مینویسه پرایم
    else:
        print('prime')
            
else:
    print('not prime')

# give me:478965
# not prime 3 159655.0

# اما در این کد:
num = int(input(""))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("not prime")
            break
        else:
            print("prime")
else:
    print("not prime")
# خروجی این میشه
# give me:478965
# prime
# not prime 3 159655.0


# ////////////
# میشه در شرط هم متد گذاشت
for char in criterion :
    print(char)
    if right_test.find(char):
        print(char)

/////////////
# اگر مشکلی اومد  که مثلا چیزی که میخواستی را باز مینوشت یا بیشتر از بازه میاره چند تا علت داره
# یکی اینکه جای اینپوت درست نیست . عمدتا باید پس از شرط ها نوشته بشه
# اگر چیزی اضافه نوشته میشه یا کم نوشته میشه کافیه جاشو درست بزاری یا دندونشو
import random
#the function that take two numbers and return one number(we have already this function: randint)
# then cpu adjust the guesses to a user
def random_adjuster (startnumber,finalnumber):
    cpu_number= random.randint(startnumber,finalnumber)
    # print(cpu_number)
    user_number=int(input('give me your guess: '))
    while user_number != cpu_number:
        if user_number<startnumber or user_number>finalnumber:
            print(f'your guess is out of range please select a number between {startnumber}and {finalnumber}')
        print('you have to take me guesses')
        if user_number>cpu_number:
            print('your guess is big ')
        elif user_number<cpu_number:
            print('your guss is small') 
            
        user_number=int(input('give me your guess: '))
        # این یوزر نامبر جاشو اگر بالا مینوشتیم دیگه در اولین حدس نمینوشت کوچیکه یا بزرگه . پس جاشو اینجا اوردم درست شد

    return('you did it')

print(random_adjuster(1,10))
# //////////////////////////////////

# ترکیب شرطی تک خطی با لامبدا
# شرطی تکخطی
# بجای اینکه بزنی تو یه متغیر و یا پرینت کنی  
# یه ضرب بدون نوشتن پرینت میزنی
# نوع نوشتن اش هم
# زیر شرط را پشت شرط می نویسی الس را جلوی شرط
# map
# یا  اون تابع میشه با لامیدا تعریف بشه
mylist=[1,2,3,4,5,6]
my2= list(map(lambda x:'big' if x>3 else 'small' , mylist))
print(my2)
# ['small', 'small', 'small', 'big', 'big', 'big']



# /////
#  شرطی تک خطی تو در تو

if expression1:
       statement1
elif expression2:
   statement2
else:
   statement3

# هم ارز هستند

statement1 if expression1 else (statement2 if expression2 else statement3)
# 


# //////
# شرطی تک خطی
# ساختار اینه :
# ولی گفت این درباره اکسپرشن کار میکنه نه استیتمنت
# فرقشون چیه؟؟؟؟؟؟؟؟؟؟؟؟؟؟
# بالا نوشته اونی که جزو شرطه اکسپرشنه . یعنی مقدم
# اونی که تالی است استیتمنت است 
b=42
# expr1 if condition1 else expr2 if condition2 else expr
a = "neg" if b<0 else "pos" if b>0 else "zero"
# اول سمت چپ را میاره 
# اگر بی کوچکتر از صفر بود  بیار پشت شرط یعنی نگ 
# در غیر این صورت ؟؟؟؟؟

print(a)
# pos
# ////////////////
# مثال  ۲ 
x=5
x if x>0 else ("zero" if x==0 else "invalid value")
5
x = 0
x if x>0 else ("zero" if x==0 else "invalid value")
'zero'
x = -1
x if x>0 else ("zero" if x==0 else "invalid value")
'invalid value'


# ///////////







