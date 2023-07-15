


# برای مقایسه کردن دو تا چیز 
# اول یه متغیر را خالی تعریف میکنی بالا میزاری
# بعد شرط میاری که اگر اون بزرگتر بود بیاد جاش بشینه در غیر این صورت که هیچی 
# این برای مقایسه دو تا لیست چند تا متغیر هم بدرد میخوره که فقط باید معلوم کنی کدوم ایندکس را با هم مقایسه کنه


# /////////////////
# مثال نقض پیدا کردن چطور میشه؟

# نیافتن اون چی؟

# کدش چطوره؟

# ///////////
# حالت های حلقه ها

# حلقه های تودرتو
# حلقه های تودرتو اینطوره
for x in y:
    for z in y:
        .......

# حلقه های موازی- مادر مشترک - نامربوط
for x in y:
for j in y:

# حلقه های موازی - مادرمشترک- مربوط
for y in g:
    for x in y:
        ...
    for z in y:




# //////////
# کدی که به تعاد معینی که بهش می دیم ازمون دونه دونه میپرسه اینبار چند شد امتیازش؟


games=[]
for score in range(4):
    game=int(input(' emtiazesh chand shod? : '))
    games.append(game)
    print(games)

# ///////
# برای اینکه چند بار یه پرسش را بپرسه مثلا ۴ بار باید در رنج گذاشت و نه صررفا تعداد
enter1= int(input('give me numbers of laptob: '))        # this gets numbers of laptob. example 3 laptob for compare
for char in range(enter1):

# /////
# کار با دندانه ها  در حلقه ها
# give me the age of the senathor: 44
# the big age is  0       در اینجا خودش خودکار صفر میزاره عدد ندی  . بعدشم بعدش نمیزاعره بجای اون   
# give me the age of the senathor: 65
# 44     در انجا ضعفی که این کد داره اینه که عدد قبلی را نشون میده بجای بزرگترین عدد . من میخوام بجای اون بزاره 
# give me the age of the senathor: 76
# 65
# give me the age of the senathor:

age= int(input('give me the age of the senathor: '))
big=int()
print('the big age is ',big)

while age!= -1:
    if age>big:
        big=age
        age= int(input('give me the age of the senathor: '))
        print(big)
print('the big age is ',big)


#  راه حل این بود که بزاریم جای پرینت و سن را عوض کنیم
# اما باز مشکلی که داره اینه که اگر یه عدد بدیم که اون یکی کوچکتره از قبلی اصلا وارد شرط نمیشه که بزاره بجاش و بعد پرینت کنه 
age= int(input('give me the age of the senathor: '))
big=int(0)
print('the big age is ',big)

while age!= -1:
    if age>big:
        big=age
        print(big)
    age= int(input('give me the age of the senathor: '))

print('the big age is ',big)

# راه حل اینه که پرینت را هم بزاریم خارج از شرط 
age= int(input('give me the age of the senathor: '))
big=int(0)
print('the big age is ',big)

while age!= -1:
    if age>big:
        big=age
    print(big)
    age= int(input('give me the age of the senathor: '))

print('the big age is ',big)

# ////
# # برنامه ای که دقیقا به تعدادی که عدد میدی ازت ورودی میگیره
# میریزه تو لیست

chand=int(input(''))
games=[]
for score in range(chand+1):
    game=int(input(' emtiazesh chand shod? : '))
    games.append(game)
    print(games)

# //////////
# این کد کاری به عدد ورودی نداره و صرف اعداد را میشماره و میریزه  و 3 اینجا الکیه
# 3
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


game=int(input(' emtiazesh chand shod? : '))
games=[]
print(game)
for score in list(range(11)):
    games.append(score)
    print(games)

# ////////
# این کد به تعداد رنج یه عدد که میدیم را میریزه تو یه لیست
# 3
# [3]
# [3, 3]
# [3, 3, 3]
# [3, 3, 3, 3]
# [3, 3, 3, 3, 3]
# [3, 3, 3, 3, 3, 3]
# [3, 3, 3, 3, 3, 3, 3]

game=int(input(' emtiazesh chand shod? : '))
games=[]
print(game)
for score in list(range(7)):
    games.append(game)
    print(games)



# ////
for i in range(2, num): 
# خود num را نمیزنه و اگر میخوای بزنه باید به علاوه 1 کنی تا خودشو بگیره 


# ////

#   و  میشه  اون حلقه داخل شرط بشه .میشه شرط داخل حلقه بشه 

num = int(input(""))
if num > 1: # این شرط زده بزرگتر از 1 که اعداد منفی و صفر نباشه 
    # اینجا نیاز داره بگرده همه اعداد را 
    for i in range(2, num):   # همه اعداد به خودش و یک که تقسیم میشن حتی نات پرایم ها ... پس باید از بعد از 1 اغاز کرد و تا خود قبل اون عدد که عملا رنج این کار ا انجام میده
        if (num % i) == 0:   # خود عدد را مثلا 45 را عدد نام قرار میده و بعد دونه دونه میره رنج  را از اول تا اخر آی را میخونه و بعد
            # و بعد بررسی میکنه که ایا باقیمونده عدد نام با آی صفر میشه که اگر شد بنویسه نات پرایم و اگر شد بنویسه پرایم
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")
# //////////////////


# میشه حلقه را به ازای هر ایندکس یا کاراکتر هیچ رخ دهی در حلقه نباشد
# یعنی num اصلا بکار نره
mylist=[1,2,3,4]
shart=[]
for num in range(mylist):
    a=(int(input('give me times tha player:')))
    if a<=2:
        shart.append(a)

# ////////
# عددبگیره تا رسید به چیزی مثلا (منفی یک) ول کنه .هی 
# داخل حلقه فور هم گرفتن اینپوت باحاله
numbers= int(input())
my_list=[]
print(my_list)
count =(0)
numerical=(0)
while (numbers != (-1)) :
    for num in [numbers]:
        my_list.append(num)
        count += 1
        numbers= int(input())
        print(my_list)
        
print(my_list)

# ////
#اینور اونور دنده ها 
# 10
# []
# 20
# [10]
# 20
# 20.0
# 30
# [10, 20]
# 40
# 20.0
# -1
# [10, 20, 30]
# 60
# 20.0
numbers= int(input())
my_list=[]
print(my_list)
count =(0)
numerical=(0)
while (numbers != (-1)) :
    for num in [numbers]:
        my_list.append(num)
        count += 1
        numbers= int(input())
        print(my_list)
    nuum=num+num
    print(nuum)
    aver=nuum/count
    print(aver)

# ////////
#ترکیب فور و ماژول ها . یعنی به ازای هر کدم میریزه تو ماژول
# به ازای اعدادی که داری می دی اونقدر ورودی بگیره میاد یه عملیات را روی تک تک داده های لیست انجام میده
# chandta adad mikhai: 3
# adad chie: 12
# adad chie: 14
# adad chie: 16
# [12, 14, 16]   این لیست میشه
# 3.4641016151377544
# 3.7416573867739413
# 4.0
chandta= int(input("chandta adad mikhai: "))
adadbede=[ 
    x 
for x in list(int(input("adad chie: "))  
for i in range (chandta))  ]
print(adadbede)

# یه عملیات رو روی یه ورودی ای که قبلا داشتیم و بهش دادیم انجام میده
import math
for i in adadbede:
    adad=math.sqrt(i)
    print(adad)

# ////////
# میشه ترکیب کرد یک شرط حلقه را با شرط

long_names = []
for name in titles:
    if len(name) > 30:
        long_names.append(name[:27] + "...")


# ///////
# اغاز حلقه از ۱
# افزودن یه عدد که تغیر کنه به یه اسم

#  اگر میخوایم حلقه را از ۱ اغاز کنه

m_players=[]
for char in range(1,4):
    name='player'
    m_players.append (('%s%i'%(name,char)))
print(m_players)
# ['player1', 'player2', 'player3'] 

# ///////////
# چرا میزنه خارج از رنج؟
true_word='abbas agha'

i = len(true_word)
while i >= 0:
    print(true_word[i])


# //////

# ترفند 

true_word='abbas agha'
i = len(true_word)-1
while i >= 0:
    print(true_word[i])
    
    
# //////////////
# برعکس میکنه در فور:

string = input ('gomle bede : ')
string = string . lower()
print (string)
gomlebarax=''
for i in string :
    
    print (i)
    gomlebarax= i+gomlebarax    
    # اینجا هر چی توی جمله برعکس بود را بعد از ای قرار میده  . این عملا یعنی برعکس کردن رشتهه 
    print('badi mishe',gomlebarax)
    
# ///////////
# ترکیب دو حلقه با هم
# به ازای هر ایتمی که در اولی است هر کدوم از اعضای دومی را......باهاش این کار را کن
 
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
        # بعد از ایتم میاد یکی کم میکنه . چون لیست بهم نریزه و 
        # لیست مون دست نخورده بمونه که دفعه بعد کار کنه . 
        print('item hazf karde mishe: ',item)
print(possible)
# جواب آخر:
# [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'],
#  ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat'],
#  ['Mango', 'Fruit', 'Juice'], ['Mango', 'Fruit', 'Eat']]

# ////////////////
# میشه یه ضرب در خود حلقه و نه
# متفیر را ورودی اورد و بعد حتی یه متد روی اونجاش اجرا کرد

for i in input(' give me the 3 point: ').split():
    print(list(i))

#  give me the 3 point: 4 5 6
# ['4']
# ['5']
# ['6']



# /////////

# همین کد بالا اگر استرینگ بدیم هر کدوم را جدا می کنه 

for i in input(' give me the 3 point: ').split():
    print(list(i))

# give me the 3 point: mamad namjoo shomali
# ['m', 'a', 'm', 'a', 'd']
# ['n', 'a', 'm', 'j', 'o', 'o']
# ['s', 'h', 'o', 'm', 'a', 'l', 'i']




# //////////
# میشه حلقه سه تا عضو بداره
# ایتم ۱ و ۲ و ۳ را با هم میشه نوشت
list1=[1,2,3,4,5,6,7,8,9]
list2=[4,6,8,2,3,7]
list3=[7,3,9,1,4,6,8,2]
for item1,item2,item3 in zip(list1,list2,list3):
    print(str(item1)+','+str(item2)+','+str(item3))




# ///////////
# کاربرد حلقه در تابع 
# کاربر گرفتن یک  لیست درون ابع
numbers = []
def loop_function(numbers):
    # در این قسمت میاد از درون لیست تابع میگیره . برای تعریف
    x = 6
    i = 0
    while i < x:
        print ("At the top i is %d" % i)
        # اینجا به نامبرز ای را میافزاییم
        numbers.append(i)
        # اینجا برای اینکه عدد شمار بینهایت نشه یه به علاوه میزنیم
        i = i + 1
        print ("Numbers now: ", numbers)
        print ("At the bottom i is %d\n" % i)
    # هم ارز وایل ریترن را میزنن
    return numbers
loop_function(numbers)
print ("The numbers: " )
# اینجا هم برای اینکه اون لیست بوجود امده را خارج کنیم اعدادش را میزنیم
for num in numbers:
    print (num)


# /////////
# نکته اگر داده ها زیر حلقه while 
# باشند اون موقع درست عمل نمیکنه چون داخل حلقه افتاده
def find_biggest ():
    what= int(input('give me the number: '))
    biggest=0
    the_second= 0
    while what != -1:
        if what > biggest :
            the_second=biggest
            biggest= what
            print ('the second is ',the_second ,'the biggest is', biggest)
        elif what< biggest and what > the_second:
            the_second=what
            print ('the second of elif ',the_second ,'the biggest of elif  is', biggest)

        what= int(input('give me the number2: '))
    return ('the big number is ', biggest , 'and sec number is : ',the_second)

print (find_biggest())

# یعنی این کد :
#     while
#     biggest=0
#     the_second= 0
# فرق داره با 
# و چون داخل حلقه میوفته اعداد را اول عوض نمیکنه
#     biggest=0
#     the_second= 0
#     while
# //////////////////////////

# نکته . اگر بجای 
# if
# حلقه وایل 
# بزاریم اون خود عدد اخر هم حساب میکنه
# اما چرا؟
def counter_prime():
    num= int(input('give me the num:'))
    counter_num=0
    list_of_primes= []
    for i in range(2, num+1):
        # print(i)
        while num%i ==0:
            print(i,'is prime')
            print('num is ',num,'and i is ',i,)
            list_of_primes.append(i)
            counter_num +=1
            print('counter name is ', counter_num ,'list is', list_of_primes)
            num = num/i
            print('now num would be',num)
            # باگ این برنامه اینه که اگر به عدد اول رسید نمیاد اضافه کنه 
            # خوب چطور اضافش کنم ؟
        # elif num%i != 0:
    return "counter_num"  , counter_num , list_of_primes

print (counter_prime())            
    
# /////////////////////////////////


# جدا کردن یه  کاراکتر در یک حلقه به دو صورت انجام میشه
# یا میشه بگی اونایی که در اون کاراکتر معیار نیستن را  بریز توی یه متغیر تازه
# مانند این

empty=''
test_item = 'edaoif'
criterion = ['a','e','o','i','u']
for char in test_item:
    # name=''.join(lowerer)
    if char not in criterion:
        empty += char
print (empty)
# df


# یا میتونی بگی اونایی که هستن را جایگزین کن با هیچی 
# یا متد دیگری را
vowl= 'o' , 'a' , 'e'
small = 'rtyuifdoevbhnj'
for char in small:
    # for char2 in vowl:
    #print(char, char2)
        if char in vowl:
            small= small.replace(char,'')
            # print('ent alan shod',small)
        #  entereance= entereance[entereance.replace(char,'?'):]
        #  print('ent alan shod',entereance)
print (small)
# df


# ولی مساله اینه که اگر بجای
# in
# بزنی
# ==
# منطبق نمیکنش
for char in small:
    # for char2 in vowl:
    #print(char, char2)
        if char == vowl:
            small= small.replace(char,'')
            # print('ent alan shod',small)
        #  entereance= entereance[entereance.replace(char,'?'):]
        #  print('ent alan shod',entereance)
print (small)



# //////////
# زدن حلقه و اجرای متد استرینگ و لیست کردنش
# میاد لیست میکنه یه کاراکتر را و بعد متد استرینگ را روش اجرا میکنه
a='sdfghjklrtyrty'
for char3 in [a] :
    a=('.').join(char3)
print(a)
# s.d.f.g.h.j.k.l.r.t.y.r.t.y

# اگر بجای  
# [a]
# بزایم 
# a
# خالی . اون موقع فقط کاراکتر اخر را نشون میده
# ////////////////////////////

# کار با حلقه فور و کامپرهنشن در فور  و لن
string = #dfghj frtghj
# باید آی را در لیست بزاره
lst = [string[i] for i in range(0,len(string))]
print(lst)
# میاد دونه دونه میریزه توی لیست
# ['d', 'f', 'g', 'h', 'j', ' ', 'f', 'r', 't', 'g', 'h', 'j']
lst.sort()
print(lst)
# سورت میکنه
# [' ', 'd', 'f', 'f', 'g', 'g', 'h', 'h', 'j', 'j', 'r', 't']
for i in lst:
    print(i, end = "")
# بعد اون لیست را خارج میکنیم و میریزیم بیرون از لیست
# dffgghhjjrt

# ////////
# جاانداختن
# اگر اون شد رد کن و جدا بنداز بقیه را بیار ادامه بده
# اینجا ۵ را جا انداخت
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if i == 5:
        continue
    print(i)
    
# //////////
# شکستن حلقه
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if i == 5:
        break
    print(i)




# //////////////
# دو تا حلقه اوردن
# میگی هر کدوم از اونا در هر کدوم از اون هر کدوما
# اونا را یه کاری کن. مثلا با هم جمع بزن
mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 0
for i in mtrx:
    for j in i:
        x += j

print(x) 
#45



# /////////
# اگر متغیر تازه وارد کنی آخریشو میزنه
# فقط
for i in range(3):
    a =input().capitalize()
print(a)
# tfgyj  input
# tfgvbhjmk  input
# XDCFVGBHN    input

# Xdcfvgbhn   
# //////////
# ولی اگر میخوای داشته باشیشون میتونی توی یه لیست بریزونی

p=[]
for i in range(3):
    a =input().capitalize()
    p.append(a)
print(a)
print(p)

# fvgbhnj
# vgbhnm
# rtyui
# Rtyui
# ['Fvgbhnj', 'Vgbhnm', 'Rtyui']


# /////////////
# حلقه تودرتو
# اگر به ترتیب میخواد چاپ کنه باید بریزه توی یه لیست و بعد 
# اون لیست را در حلقه دیگری بریزه
names= [input().capitalize() for name in range(3)]
for i in names:
    print(i)

# retyuikl    input
# ASDFGHJKL     input
# dfghjk          input
# تا اینجا توی یه لیست میریزه
# از این جا به پس از اون توی حلقه انداخته که چاپ کنه اون لیست را
# Dfghjk
# Retyuikl
# Asdfghjkl
# ////////////////////
# اگر هم همون لحظه میخواد خروجی را ببینه اینجوری باید بنویسه
for i in range(3):
    a =input().capitalize()
    print(a)
# trghjkl   input
# Trghjkl
# fghjk        input
# Fghjk
# ghjkl      input
# Ghjkl

# ....................
# اگر درون حلقه دوم یه شرط بزاری که فالس باشه 
# اون موقع برمیگردونه حلقه دومی و از اون آغاز میکنه نه حلقه بالایی.
# یعنی از  
# char2
# آغاز میکنه 
for char in positive_Gained:
    print('char is ',char)
    for char2 in criterion:
        print('char2 is ',char2)
        if char2 == char:
            print('char==char2' is char2 ==char)
            positive_Gained= positive_Gained.replace (char2,'',positive_Gained.find(char2))


print (positive_Gained)


# ////////
# چجوری در حلقه ویژگی ای را تا یافت بیاد بیرون بگه یافتم
# روش اینکه بیاد مقایسه کنه به محض اینکه بین اون دو ویژگی را دید بیاد بگه بله یافتم
# و بزنه بیرون چیزی را پرینت کنه یا کاری را انجام بده
# این مشکلی دارم . هپی ایرسا نمیزنه پور ایرسا میزنه

enter1= int(input('give me numbers of laptob: '))        # this gets numbers of laptob. example 3 laptob for compare
print('irsa at first is poor')
poor_irsa=True
# در اینجا تا بی نهایت می پرسه و کاری هم نداره که چندتا داده باشی در حلقه فور
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



# اینم مشکل را حل نکرد 

enter1= int(input('give me numbers of laptob: '))        # this gets numbers of laptob. example 3 laptob for compare
last_laptop=[0,0]
print('irsa at first is poor')
poor_irsa=True

# در اینجا تا بی نهایت می پرسه و کاری هم نداره که چندتا داده باشی در حلقه فور
while poor_irsa ==True:
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

# //////////
# دو حلقه زدن
# چگونه دو حلقه را  بزنم در دیکشنری که عنصر اخر را بیاره
mylist=[[1,10],[7,3]]
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
# چگونه ذخیره کنه
# {1: 3, 10: 3}
# ////////////////////////////////////////
# give me numbers of laptob: 2
# irsa at first is poor
# price and quality:1 10
# ['1', '10']
# [1, 10]
# irsa is steel poor
# the last laptob would be: [1, 10]
# price and quality:7 3
# ['7', '3']
# [7, 3]
# irsa is steel poor
# the last laptob would be: [7, 3]
# price and quality:1 5
# ['1', '5']
# [1, 5]
# irsa is steel poor
# the last laptob would be: [1, 5]
# price and quality:58 8
# ['58', '8']
# [58, 8]
# irsa is steel poor
# the last laptob would be: [58, 8]
# price and quality:9 4
# ['9', '4']
# [9, 4]
# irsa is steel poor
# the last laptob would be: [9, 4]
# price and quality:

# ///////////////////////////////////////////
# جایگشت سازی
# مقایسه یه لیست تودرتو با یک تک لیست در لیست دیگر
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

# به تعداد لیست تو در تو برای دسترسی باید حلق درست کرد. 
# یک لیست یک حلقه میشه  یه لیست و یه لیست درونش دو حلقه میشه
# یه لیست که خودش لیست هایی داره که هر کدوم هم درونشون لیست هایی دارن سه حلقه میشه
# یا اینکه به صورت
# i[0][0][0]
# بشه

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

    
        
# /////////
# باز کردن همه اعضای درون نستد لیست ها
biglist=[[1, 10], [7, 3],[4,5]]
for i in range(len(biglist)):
    # print(biglist[i])
# [1, 10]
# [7, 3]
# [4, 5]
    for j in biglist[i]:
        print(j)
# 1
# 10
# 7
# 3
# 4
# 5
# .
# فرق نمیکنه که ای باشه یا جی

biglist=[[1, 10], [7, 3],[4,5]]
for i in range(len(biglist)):
    # print(biglist[i])
# [1, 10]
# [7, 3]
# [4, 5]
    for i in biglist[i]:
        print(i)
# 1
# 10
# 7
# 3
# 4
# 5
# /////////////
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

# اما چطور میشه خودشونو با خودشون دیگه مقایسه نکنن؟

# /////
# توجه شود که تغیر پذیری در حلقه باید باشد و باید رنج بزنی و یا لن بزنی 
# وگرنه خطای ایتربل میده
enter= int(input('give me whole votes: '))

for each_numbers in enter:
    each_numbers.input('give me the name of country: ')
# این درسته
for each_numbers in range(enter):

# ////////
# اینجا ورودی میاره به ازای هر کدام. ولی ورودی را چکار میکنه... یعنی ایچ نامبرز را یه بار عنصر 
# یکم یه بار دوم یه بار سوم و... میاره و میپرسه ولی بعدش چی؟
# یعنی سینتکسی درسته ولی کاربردی نیست
enter= int(input('give me whole votes: '))

for each_numbers in range(enter):
    input('give me the name of country: ')

# give me whole votes: 3
# give me the name of country: hghg
# give me the name of country: hg
# give me the name of country: gvg 
# //////////////
first=0
final=100
hads= random.randint(first,final)
print(hads)
mynumber=40
# در اینجا کافیه یه بار بیوفته توی حلقه و تا بینهایت میره
while hads != mynumber:
    if mynumber<hads:
        final=hads
    elif mynumber>hads:
        first=hads
    hads= random.randint(first,final)

print('you did it cpu')

# باید یه بار پایین بیاره دوباره

while hads != mynumber:
    if mynumber<hads:
        final=hads
    elif mynumber>hads:
        first=hads
    hads= random.randint(first,final)
# الان کار میکنه

# /////////

first=0
final=100
hads= random.randint(first,final)
print(hads)
# 19
mynumber=40
while hads != mynumber:
    if mynumber<hads:
        final=hads
    elif mynumber>hads:
        first=hads
    hads= random.randint(first,final)
    
    print (hads)
print('you did it cpu')
# این برنامه خودش هی نمیپرسه پس خودش انقدر میره تا برسه به اون که خودش میخواد
# 80
# 9
# 26
# 69
# 47
# 47
# 29
# 44
# 33
# 35
# 37
# 43
# 37
# 37
# 37
# 41
# 39
# 41
# 39
# 39
# 41
# 40
# you did it cpu
        
# برای اینکه پرسش و پاسخی باشد دوباره درون حلقه باید پرسید 

# انگار وایل یه شرط بزرگ است. 


# ///////////
# در دادن متغیر به حلقه بسیار دقت کن . گاه حلقه کار میکنه ولی  جواب مدنظرتو نمیده
# آزمون کن اولا همه برنامه هاتو چندتا تسک بیار که سخت باشه و رد بشه از اونا

while mynumber != 'm':
# این برنامه کار میکنه ولی  چی اگر کا باشه؟  صرفا اگر کا را دیدی؟ مسخره است

    if 'k':  #my number< in hadse
        final=hads
    elif 'b':  #my number>in hadse
        first=hads
    hads= random.randint(first,final)
    print (hads)
    mynumber=input('aia hadse man az in bozorgtare ia koochektare ia mosavie?? m/b/k) ')

بجاش باید اینو بنویسی 
while mynumber != 'm':
    # این برنامه کار میکنه ولی  چی اگر کا باشه؟  صرفا اگر کا را دیدی؟ مسخره است

    if mynumber== 'k':  #my number< in hadse
        final=hads
    elif mynumber=='b':  #my number>in hadse
        first=hads
    hads= random.randint(first,final)
    print (hads)
    mynumber=input('aia hadse man az in bozorgtare ia koochektare ia mosavie?? m/b/k) ')
# ////////

# حلقه بینهایت 
# اما چرا تا اخر میره ؟
harrasment=int(input())
while harrasment != -1:
    print('right')
# ht
# right
# right
# right
# rig
# چون یه بار افتاده و دیگه فرصت نداری منفی یک بدی 
# باید بشه برگرده و این لوپ برگرده
harrasment=int(input())

# ////////
# میشه در خود حلقه از اول اشاره کرد و محدودش کرد.
# در سی ای که اخری نباشه ( چون قانون داشتیم تا سر اخری)
c=bcmnvx
for i in c[0:-1]:
    print(i)
    
    
# /////////
# اگر میخوای len  در حلقه 
# for
# بزنی سینتکس درستش اینه 
my=[6,9,10]
for arr in range (len(my)):
    print(my[arr],arr)
# 6 0
# 9 1
# 10 2
# ////////////
ar=[1, -34, 23, 2342, 52, -3, -12, -123, -23]
def abs1(array):
    for i in range(len(array)):
        # میگه اگر اون ارای منفی بود
        if array[i] < 0:
            # بیا ضربدر منفی یکش کن بریز توش 
            # منفی در منفی میشه مثبت
            array[i] = array[i] * (-1)
            print(array[i] , (array[i] * (-1)))
    print(array)
abs1(ar)
# [1, 34, 23, 2342, 52, 3, 12, 123, 23]

# ///////
# حالا اگر بخوایم همه ی اعضای درون لیست را با هم قدر مطلق بگیریم
a=[6,9,10]
print(list(map(abs,a)))
# [6, 9, 10]

# /////////
# توضیحات  را جدا  جدا نوشتم در سه قسمت که قاطی نشه
# اگر اعضای درونی یک حلقه را بخوایم با هم مقایسه کنیم
# که بعدش اختلافشونو بگیریم و یا قدر مطلقشونو یا جمعشونو
# مقایسه اعضای درونی یه لیست باهم در حلقه 
def sumPairs(lst):
    diffs = []
    print(list(enumerate(lst)))    #[(0, 6), (1, 9), (2, 10)] این میشه خروجی انومریت ها ولی نه در لیست 
    for x in enumerate(lst):
        # در enumerate
        # اگر فقط ایکس را وارد کنی فقط تاپل هاشو میده  بهمون یعنی بسته را
# (0, 6)
# (1, 9)
# (2, 10)
        print(x)

  
lst = [6, 9, 10]
print(sumPairs(lst))
# None

# ///////////
# توضیحات  را جدا  جدا نوشتم در سه قسمت که قاطی نشه

def sumPairs(lst):
    diffs = []
    # چرا انومریت کرد؟ برای اینکه موقع مقایسه کردن 
    # اگر ۲  اولی  ۲ سومی مثلا بود بتونه مقایسه کنه یعنی
    # به ایندکس اشاره کنه  نه به عدد  که ممکنه تکراری بوجود بیاد
    print(list(enumerate(lst)))    #[(0, 6), (1, 9), (2, 10)]  . 
    # 
    # این میشه خروجی انومریت ها ولی نه در لیست 
    # چون در خودش تاپل تاپل میده و خروجی را اگر بگیریم یه همچین چیزی میده  که اشاره به جای در حافظه میکنه
    # <enumerate object at 0x0000017DB5A3F100>
    for i, x in enumerate(lst):
        print(i,x)
                # بهمون میده
                #     0 6
                    # 1 9
                    # 2 10       
                    # ما اندیس را نمیخوایم ما محتوا
                    # را و خود عدده را میخوایم یعنی دومی         
        for j, y in enumerate(lst):
            # دوباره به همون لیست اشاره میکنه
            # . یعنی اعضای یه لیست را با هم جایگشت میکنه
            if i != j:
                # اینجا برای مقایسه کردن باید ایندکس را در نظر بگیری
                # چون ممکنه ایکس ۲ باشه اونور در وای هم ۲ باشه
                diffs.append(abs(x-y))
    return int(sum(diffs)/2)
# Driver program
lst = [6, 9, 10]
print(sumPairs(lst))
# 8

# ////////////
# توضیحات  را جدا  جدا نوشتم در سه قسمت که قاطی نشه
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


# x is:  6
# y is:  9
# x , y is 6 9
# diffs is now:  [3]
# y is:  10
# x , y is 6 10
# diffs is now:  [3, 4]
# x is:  9
# y is:  6
# x , y is 9 6
# diffs is now:  [3, 4, 3]
# y is:  10
# x , y is 9 10
# diffs is now:  [3, 4, 3, 1]
# x is:  10
# y is:  6
# x , y is 10 6
# diffs is now:  [3, 4, 3, 1, 4]
# y is:  9
# x , y is 10 9
# diffs is now:  [3, 4, 3, 1, 4, 1]
# [3, 4, 3, 1, 4, 1]
# 8




# ////////////

def sumPairs(lst):
    # اول یه لیست خالی تعریف میکنه
    diffs = []
    # برای جایگشت باید دو تا حلقه فور نوشت که مقایسه کنه
    for i, x in enumerate(lst):
        for j, y in enumerate(lst):
            # چون چیزی با خودش مقایسه نمیشه پس باید  این شرط را بیاری  که مقایسه نکنه
            if i != j:
                # هر ایکس و وای که داره مقایسه میکنه را قدر مطلق بگیر بریز توی اون لیست ما
                diffs.append(abs(x-y))
                # جمع کن اعداد درون اون لیست را 
                # اما چرا تقسیم بر ۲؟ 
    return int(sum(diffs)/2)
# Driver program
lst = [1, 2, 3, 4]

# ///////////

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
# /////////////////////////////////
from itertools import permutations , combinations , combinations_with_replacement
# بدون نیاز به حلقه جایگشت زدن
# بدون حلقه
# رنج بدون حلقه
my=list(permutations(range (1,4)))
print(my)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# //////////////////////////////////////////////////////////////////////////
from itertools import combinations, permutations ,combinations_with_replacement ,product
# ترکیب  دو لیست در حلقه
my_list=(1,2,3)
my_list2=(4,5,6)
for i in product(my_list,my_list2):
    print(i)
    
# (1, 4)
# (1, 5)
# (1, 6)
# (2, 4)
# (2, 5)
# (2, 6)
# (3, 4)
# (3, 5)
# (3, 6)
# //////////
# توضیح حلقه تودرتو
# حلقه در دیکشنری از کلید ها میاد
my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}     
sentence=['you','say','to','i','guy','hello']
for char in sentence:              
    for klid in my_vazhenameh:
        print('klid is',klid ,'char is',char)
# اول نخستین کاراکتر خط بالاتر را میخون که در اینجا یو است
# پس از اون به ترتیب دونه دونه هلو را کاراکتر میگیره 
# پس از اون یو و و ای و.... را 
# توجه: در حلقه کلید ها  را جستجو میکنه

# klid is hello char is you
# klid is you char is you
# klid is i char is you
# klid is we char is you
# /////////////////////////////////////////////     
# klid is hello char is say
# klid is you char is say
# klid is i char is say
# klid is we char is say
# ////////////////////////////////////////
# klid is hello char is to
# klid is you char is to
# klid is i char is to
# klid is we char is to
# /////////////////////////////////////////
# klid is hello char is i
# klid is you char is i
# klid is i char is i
# klid is we char is i
# ///////////////////////////////////
# klid is hello char is guy
# klid is you char is guy
# klid is i char is guy
# klid is we char is guy
# ///////////////////////////////////
# klid is hello char is hello
# klid is you char is hello
# klid is i char is hello
# klid is we char is hello
# /////////////////////////////////

for klid in my_vazhenameh:  
        for char in sentence:              
            print('klid is',klid ,'char is',char)
# از خط بالا اغاز میکنه .  اولین کاراکتر را هلو میکنه 
# پس از اون دونه دونه حبقه دوم برای لیسته هست
# klid is hello char is you
# klid is hello char is say
# klid is hello char is to
# klid is hello char is i
# klid is hello char is guy
# klid is hello char is hello
# ///////////////////////////////////////////////
# klid is you char is you
# klid is you char is say
# klid is you char is to
# klid is you char is i
# klid is you char is guy
# klid is you char is hello
# ////////////////////////////////////////////
# klid is i char is you
# klid is i char is say
# klid is i char is to
# klid is i char is i
# klid is i char is guy
# klid is i char is hello
# /////////////////////////////////////////
# klid is we char is you
# klid is we char is say
# klid is we char is to
# klid is we char is i
# klid is we char is guy
# klid is we char is hello
# /////////////////////////////////////////
# بررسی == در شرط 
# مقایسه و بررسی دو حلقه 
my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
# sentence=input('give me the sentence for translating: ').split()
sentence=['you','say','to','i','guy','hello']
for klid in my_vazhenameh:  
        for char in sentence:              
            print('klid is',klid ,'char is',char)
            if klid==char:
                print('klid==char is',klid==char,klid,char)
# دونه دونه به ازای هر کلید در دیکشنری ما میاد یه دونه از لیسته را مقایسه میکنه
# klid is hello char is you
# klid is hello char is say
# klid is hello char is to
# klid is hello char is i
# klid is hello char is guy
# klid is hello char is hello
# klid==char is True hello hello          اینجا مساوی بود هلو با هلو
# //////////////////////////////////////////////////////////////////////
# klid is you char is you
# klid==char is True you you                  اینجا  کلید همون چیزی بود که در اون لیست بود
# klid is you char is say
# klid is you char is to
# klid is you char is i
# klid is you char is guy
# klid is you char is hello
# ////////////////////////////////////////
# klid is i char is you
# klid is i char is say
# klid is i char is to
# klid is i char is i
# klid==char is True i i                کلید همون چیزی است که درون لیست است
# klid is i char is guy
# klid is i char is hello
# ////////////////////////////////
# klid is we char is you
# klid is we char is say
# klid is we char is to
# klid is we char is i
# klid is we char is guy
# klid is we char is hello
# ///////////////////////////////////////
# is هم همون کار ==  را میکنه 
my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
# sentence=input('give me the sentence for translating: ').split()
sentence=['you','say','to','i','guy','hello']
for klid in my_vazhenameh:  
        for char in sentence:              
            print('klid is',klid ,'char is',char)
            if klid is char:
                print('klid==char is',klid==char,klid,char)
# دونه دونه به ازای هر کلید در دیکشنری ما میاد یه دونه از لیسته را مقایسه میکنه
# klid is hello char is you
# klid is hello char is say
# klid is hello char is to
# klid is hello char is i
# klid is hello char is guy
# klid is hello char is hello
# klid==char is True hello hello          اینجا مساوی بود هلو با هلو
# //////////////////////////////////////////////////////////////////////
# klid is you char is you
# klid==char is True you you                  اینجا  کلید همون چیزی بود که در اون لیست بود
# klid is you char is say
# klid is you char is to
# klid is you char is i
# klid is you char is guy
# klid is you char is hello
# ////////////////////////////////////////
# klid is i char is you
# klid is i char is say
# klid is i char is to
# klid is i char is i
# klid==char is True i i                کلید همون چیزی است که درون لیست است
# klid is i char is guy
# klid is i char is hello
# ////////////////////////////////
# klid is we char is you
# klid is we char is say
# klid is we char is to
# klid is we char is i
# klid is we char is guy
# klid is we char is hello
# ///////////////////////////////////////
# اگر مورد بررسی را هم تغیر بدیم باز هم همون خروجی را میده
# یعنی بگیم کاراکتر مساوی مساوی کلید است همون کلید مساوی مساوی کاراکتر
my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
# sentence=input('give me the sentence for translating: ').split()
sentence=['you','say','to','i','guy','hello']
for klid in my_vazhenameh:
        for char in sentence:         
            print('klid is',klid ,'char is',char)
            if char ==  klid:
                print('klid==char is',klid==char,klid,char)
# دونه دونه به ازای هر کلید در دیکشنری ما میاد یه دونه از لیسته را مقایسه میکنه
# klid is hello char is you
# klid is hello char is say
# klid is hello char is to
# klid is hello char is i
# klid is hello char is guy
# klid is hello char is hello
# klid==char is True hello hello          اینجا مساوی بود هلو با هلو
# //////////////////////////////////////////////////////////////////////
# klid is you char is you
# klid==char is True you you                  اینجا  کلید همون چیزی بود که در اون لیست بود
# klid is you char is say
# klid is you char is to
# klid is you char is i
# klid is you char is guy
# klid is you char is hello
# ////////////////////////////////////////
# klid is i char is you
# klid is i char is say
# klid is i char is to
# klid is i char is i
# klid==char is True i i                کلید همون چیزی است که درون لیست است
# klid is i char is guy
# klid is i char is hello
# ////////////////////////////////
# klid is we char is you
# klid is we char is say
# klid is we char is to
# klid is we char is i
# klid is we char is guy
# klid is we char is hello
# ///////////////////////////////////////
# اوردن فالس و ترو در بررسی دو حلقه

my_vazhenameh={'hello':'dorod','you':'tu','i':'man','we':'ma'}
# sentence=input('give me the sentence for translating: ').split()
sentence=['you','say','to','i','guy','hello']
for klid in my_vazhenameh:  
        for char in sentence:
            print('klid is',klid ,'char is',char)
            if char ==  klid:
                print('klid==char is',klid==char,klid,char)
            else:
                print('klid==char is',klid==char,klid,char)
# حالا دوباره کاراکتر نخست یعنی هلو را با لیست دوم میسنجه 
# اگر اون کاراکتر در لیست دوم بود که ترو میده 
# اگر نبود فالس میده 
# از اونجایی که بیشتر اون لیست دوم هلو نیست پس مادام فالس میده 
# مگر اینکه به هلو برسه
# klid is hello char is you
# klid==char is False hello you
# klid is hello char is say
# klid==char is False hello say
# klid is hello char is to
# klid==char is False hello to
# klid is hello char is i
# klid==char is False hello i
# klid is hello char is guy
# klid==char is False hello guy
# klid is hello char is hello
# klid==char is True hello hello                  اینجا بلاخره پیدا کرد
# klid is you char is you
# klid==char is True you you
# klid is you char is say
# klid==char is False you say
# klid is you char is to
# klid==char is False you to
# klid is you char is i
# klid==char is False you i
# klid is you char is guy
# klid==char is False you guy
# klid is you char is hello
# klid==char is False you hello
# klid is i char is you
# klid==char is False i you
# klid is i char is say
# klid==char is False i say
# klid is i char is to
# klid==char is False i to
# klid is i char is i
# klid==char is True i i
# klid is i char is guy
# klid==char is False i guy
# klid is i char is hello
# klid==char is False i hello
# klid is we char is you
# klid==char is False we you
# klid is we char is say
# klid==char is False we say
# klid is we char is to
# klid==char is False we to
# klid is we char is i
# klid==char is False we i
# klid is we char is guy
# klid==char is False we guy
# klid is we char is hello
# klid==char is False we hello

# //////////////////////////////////////
# برای افزودن استرینگ هم باید یه متغیر خالی تعریف کنی
my=''
for lin in f:
    my= my.strip()
    print(my)

# ///////////////////////////////
# مشکل اخری:
# وقتی که در حلقه یه سری چیز ها را میریزی درون یه متغیر 
# اون اخریشو فقط ذخیره میکنه
# برای این یا باید لیست کنی بریزه با اپند یا 
# += 
# کنی یا 

# ////////////
# هر بار حلقه یک بار باز میکنه 
# مثلا حلقه اول اشاره میکنه به اعضای درونی این
['adddf','dfdfs','dfdff','dfdsas',]
# یعنی میده
# adddf
# dfdfs
# و.... را 
# دفعه وم حلقه میاد اعضای درونی هر کدام از اعضا را میده یعنی 
# a
# d
# d
# و.... را 
# یعنی شما به اندازه تعداد زیر مجموعه ها میتونی حلقه بزنی 
# اگر یه زیر مجموعه باشه یک بار 
# دو زیر مجموعه بداره  دو بار حلقه بزنی 
# تا اینکه به اتم ها برسه که دیگه  زیر مجموعه ای در پایتون نداشته باشه . یعنی اتم ها

# ساختار کلی اینه
for 1 in A:
    for 2 in 1:
        print(2)
# ///////// 
# حلقه زدن در فایل
import csv
# متد رایتروز
def moadel(input_adress,output_adress):
    with open (input_adress ,'r') as vorodi , open (output_adress,'w',newline='') as khorogi:
        my_vorodi=csv.reader(vorodi)
        my_khrogi=csv.writer(khorogi)

        for char in my_vorodi:
            # اما چرا اینجوری فقط میشه بهش اشاره بشه؟
            # یعنی برش بزن از صفر تا ۱ را 
            # خوب راه بهتری برای دسترسی نبود؟
            print(char[0:1]) # پرینت کار میکنه  
            if char[0:1] ==['mandana']:
                print(f'toii?',char[0:1] )

        # my_khrogi.writerows(my_vorodi)
# /////
# ['mandana']
# toii? ['mandana']
# ['hamid']
# ['sina']
# ['sara']
# ['soheila']
# ['ali']
# ['sarvin']
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
print(moadel('E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\csv-mean.csv','E:\.python and every thing\codes and projects\maktab khoneh\introductry\exer\csv_mean7.csv'))


# ///////////
# اینجا تغیرات را صورت میده میاد بیرون و تغیر انجام شده؟
        for char in my_vorodi:
            # print(char[0:1]) # پرینت کار میکنه 
            # if char[0:1] ==['mandana']:
            for c in  (char[0:1]):
                # حالا چطور ماندانا را تغیر بدم به ممد یا....؟
                # یا چیزی را بررسی کنه ؟
                # بعد بریزه توی فایل تازه؟
                if c == 'mandana':
                    char[0]=c.replace(c, 'mamad')
                # print(char[0:1])
            print(char)
# //////////////////
            # /////////
            # دو حلقه درون یک حلقه
            # میشه دوتا حلقه درون یک حلقه باشه 
            # یعنی یک پدر بزرگ و  دو پدر
            # حالا درون هر پدر یک نوه باشه
            # اینجا پس از  کاری که با حلقه پدر نخست انجام شد میره سراغ بعدی 
            
        MY=[]
        for char in my_vorodi:
            # print(char)
            for c in  (char[0:1]):
                # print(c)
                if c == 'mandana':
                    char[0]=c.replace(c, 'mamad')
            for j in char:
                # print(j)
               
                # کار کاراکتری نه استرینگ باشه و نه استرینگ اون موقع اونو با چیزی جایگیزین کن
                # اما این کار نمیکنه
                if type(j) != str and int:
                    # print('this is ',j)
                    char=j.replace('', j)
                    # print('this is my',char)
            MY.append(char)
            
            # این تیکه میاد بجای کاراکتر های خالی اونها را حذف میکنه
            while (''in char):
                print(True)
                char.remove('')

            # اینجا چون همه کارها انجام میشه روی 
            # char
            # پس بیرون که از اون حلقه های پدر میان تغیر میکنه

            # ولی هنوز توی حلقه پدربزرگ هستیم
            # پس اپند میکنه به لیست مد نظر
            MY.append(char)
# //////////
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
# با فیلتر هم میشه
# https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/#:~:text=Method%20%231%3A%20Using%20remove(),string%20is%20found%20in%20list.

# ////////
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


# //////////////////////

# سینتکس حلقه تودرتو
# در لیست تک خطی
flatten_matrix = [val for 1 for 2]
for 1:
    for 2:
        val


flatten_matrix = [val for sublist in matrix for val in sublist]
# //////


# حلقه زدن در یک لیست تو در تو
# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]



# ///////
# زدن حلقه در لیست تودرتو
# حلقه  دو متغیره
# حلقه دوکاراکتری
groups = [['Group1', 'A', 'B'], ['Group2', 'C', 'D']]
    for value,keys in groups:
        
# ////////
# حلقه زدن در لیست تودرتو

my= [(('2022-01-16', 9), ('2022-01-16', 1)), (('2022-01-23', 14), ('2022-01-23', 1)), (('2022-01-30', 15), ('2022-01-30', 1)), (('2022-02-06', 13), ('2022-02-06', 1)), (('2022-02-13', 11), ('2022-02-13', 1)), (('2022-02-20', 10), ('2022-02-20', 1)), (('2022-02-27', 10), ('2022-02-27', 1)), (('2022-03-06', 9), ('2022-03-06', 1)), (('2022-03-13', 9), ('2022-03-13', 1)), (('2022-03-20', 15), ('2022-03-20', 2)), (('2022-03-27', 13), ('2022-03-27', 1)), (('2022-04-03', 14), ('2022-04-03', 1)), (('2022-04-10', 13), ('2022-04-10', 1)), (('2022-04-17', 18), ('2022-04-17', 1)), (('2022-04-24', 16), ('2022-04-24', 1)), (('2022-05-01', 18), ('2022-05-01', 1)), (('2022-05-08', 14), ('2022-05-08', 1)), (('2022-05-15', 13), ('2022-05-15', 1)), (('2022-05-22', 13), ('2022-05-22', 1)), (('2022-05-29', 18), ('2022-05-29', 6)), (('2022-06-05', 16), ('2022-06-05', 5)), (('2022-06-12', 10), ('2022-06-12', 2)), (('2022-06-19', 10), ('2022-06-19', 2)), (('2022-06-26', 10), ('2022-06-26', 1)), (('2022-07-03', 9), ('2022-07-03', 1)), (('2022-07-10', 11), ('2022-07-10', 1)), (('2022-07-17', 11), ('2022-07-17', 1)), (('2022-07-24', 10), ('2022-07-24',
1)), (('2022-07-31', 13), ('2022-07-31', 1)), (('2022-08-07', 14), ('2022-08-07', 1)), (('2022-08-14', 9), ('2022-08-14', 2)), (('2022-08-21', 11), ('2022-08-21', 1)), (('2022-08-28', 15), ('2022-08-28', 1)), (('2022-09-04', 18), ('2022-09-04', 1)), (('2022-09-11', 100), ('2022-09-11', 1)), (('2022-09-18', 93), ('2022-09-18', 4)), (('2022-09-25', 61), ('2022-09-25', 4)), (('2022-10-02', 85), ('2022-10-02', 4)), (('2022-10-09', 38), ('2022-10-09', 4)), (('2022-10-16', 33), ('2022-10-16', 6)), (('2022-10-23', 29), ('2022-10-23', 4)), (('2022-10-30', 27), ('2022-10-30', 3)), (('2022-11-06', 19), ('2022-11-06', 3)), (('2022-11-13', 25), ('2022-11-13', 3)), (('2022-11-20', 22), ('2022-11-20', 2)), (('2022-11-27', 19), ('2022-11-27', 2)), (('2022-12-04', 30), ('2022-12-04', 2)), (('2022-12-11', 19), ('2022-12-11', 2)), (('2022-12-18', 17), ('2022-12-18', 2)), (('2022-12-25', 17), ('2022-12-25', 2)), (('2023-01-01', 21), ('2023-01-01', 2)), (('2023-01-08', 21), ('2023-01-08', 2))]
    # dictio=collections.defaultdict(list)

# اگر یک کاراکتر بزنیم
    for (madarbozorg) in my:
        print(madarbozorg)

# (('2022-01-16', 9), ('2022-01-16', 1))
# (('2022-01-23', 14), ('2022-01-23', 1))
# (('2022-01-30', 15), ('2022-01-30', 1))

# /////////////////
# این کد  هر تاپل را باز میکنه 
# یعنی تاپل مادربزرگ را به مادرها تقسیم میکنه
    for (madar),(pedar) in my:
        print(madar)
        print(pedar )
# ('2022-01-16', 9)
# ('2022-01-16', 1)

# ('2022-01-23', 14)
# ('2022-01-23', 1)


# //////
# اینجا چون در لیست ما کاراکتراول تاپل ما یکی بوده که همون تاریخ است پس یکی میشه
    for (madar,dokhtar),(pedar,pesar) in my:
        print(madar,dokhtar)
        print(pedar,pesar)

# 2022-01-16 9
# 2022-01-16 1

# 2022-01-23 14
# 2022-01-23 1


# ///////////
    for (madar,dokhtar),(pedar) in my:
        print(madar)
        print(pedar)

# 2022-01-16
# ('2022-01-16', 1)
# 2022-01-23
# ('2022-01-23', 1)
# 2022-01-30
# ('2022-01-30', 1)


# /////////////
    for (madar,dokhtar),(pedar) in my:
        print(madar,dokhtar)
        print(pedar)

# 2022-01-16 9
# ('2022-01-16', 1)
# 2022-01-23 14
# ('2022-01-23', 1)
# 2022-01-30 15
# ('2022-01-30', 1)

# /////////////
# میشه در حلقه چیزی را نوشت ولی اصلا با اون کاری نداشت
    for x in range (number):
        # print  (dict[khamenei].items() , dict[pahlavi].items())
            my=(list(zip(dict[khamenei].items(), dict[pahlavi].items())))
    # print(my)    
# //////////
# این کد کار میکنه و همه را که در لیست وایل اومده و خالی است را حذف میکنه
           for charr in roder:
                while '' in charr:
                charr.remove('')
            
        print(roder)

# حالا اگر اینو برش زدشو مدنظر قرار بدیم
        for charr in roder[1:]:
            while '' in charr:
                charr.remove('')
            
        print(roder)
# کار نمیکنه . از اون به بعدشو

# ///

# زدن دو حلقه درون یک حلقه
# با کردن اعضای یک حلقه

# [['mandana', '5', '7', '3', '15'], ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], ['sina', '19', '10', '19', '6', '8', '14', '3'], ['sara', '0', '5', '20', '14'], ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], ['ali', '1', '9'], ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8'], [], [], [], [], [], [], [], [], []]
        roder=list(my_Reader)
        my=[]
        for charr in (roder):
            while '' in charr:
                charr.remove('')
            for k in (charr[1:]):
                my.append(int(k))            
        print(roder)
        print(my)

# [5, 7, 3, 15, 3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1, 19, 10, 19, 6, 8, 14, 3, 0, 5, 20, 14, 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7, 1, 9, 0, 16, 16, 13, 19, 2, 17, 8]

# ///////////
# sep
# جدا کننده
for obj in list:
    print(obj.name, obj.roll, sep=' ')
    
# در پرینت  متغیر های کنار هم را جدا میکنه
# Akash 2
# Deependra 40
# Reaper 44
# veer 67
    
# //////
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
#
# تغیر ترتیب بندی در حلقه
# یا نیاوردن یک کاراکتر خاص در لیست جدید یا در چاپ
# بجای چاپ یا افزودن این ترتیب
# Mahdi 90 190
# Amin 75 180
# Ahmad 60 175
# Mohammad 75 175

    for char in best:
        print (char[1],char[3],char[2])
biggest_height(mycursor)

# این میشه
# Mahdi 190 90
# Amin 180 75
# Ahmad 175 60
# Mohammad 175 75

# حتی میتونستیم دونه دونه بریزیم در یک لیست دیگر


# /////////////////////
# حلقه های موازی در مقابل حلقه های تودرتو - مادر مشترک
# توجه اگر دوتا ابجکت تودرتوی موازی داشته باشیم  که مادر یکسانی داشته باشند
# که لیست مادر rows باشه
# که بعد یکی head  باشه و یکی body

for row in rows:
    for head in row.findAll('th'):
        print(head.text)
    for body in row.findAll('td'):
        print(body.text)

# اگر اینجوری بنویسیم حلقه دوم را بهمون نمیده چون موازی است و در دل اولی
# نیست که بده . اگر اولی هم تجزیه میشد میداد
for row in rows:
    for head in row.findAll('th'):
        print(head.text)
        for body in row.findAll('td'):
            print(body.text)
# اما
# این اول حلقه اول را کامل میاد دونه دونه اجرا میکنه و پس از اون دومی را اجرا میکنه
# بهش بگیم اجرای مستقل-ترتیبی

# حالا اگر یکی یکی باشه چی؟
# اجرای زیگزاگی . یعنی یه دونه از این که
# مثلا عنصر اول را میده و فورا بره عنصر اول حلقه دوم را بده

# ///////////////////
# اپند کردن درون حلقه . زیر حلقه مادر
# محل appand
# جانمایی appand

    for row in rows:
        my_data = []
    for head in row.findAll('th'):
        heads = (head.text)
    my_data.append(heads)
    for body in row.findAll('td'):
        bodies = (body.text)
    my_data.append(bodies)
    print(my_data)

    # ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6']
    # ['1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n']
    # ['2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n']
    # ['3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n']
    # ['4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n']
    # ['5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n']
    # ['6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n']
    # ['7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n']
    # ['8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n']
    # ['9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n']
    # ['10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n']
    # ['11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n']
    # ['12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n']
    # ['13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n']
    # ['14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n']
    # ['15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n']
    # ['16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n']
    # ['17', '\nLeeds United\n', '24', '5', '7', '12', '29', '39', '-10', '22', '\n\n       \n']
    # ['18', '\nEverton\n', '24', '5', '6', '13', '17', '32', '-15', '21', '\n\n       \n']
    # ['19', '\nBournemouth\n', '24', '5', '6', '13', '22', '48', '-26', '21', '\n\n       \n']
    # ['20', '\nSouthampton\n', '24', '5', '3', '16', '19', '41', '-22', '18', '\n\n       \n']
    #


# حالا اگر این بالا بزنیم
my_data = []

for row in Table.find_all('tr'):
    # for row in rows:
        for head in row.findAll('th'):
            heads= (head.text)
            my_data.append(heads)
        for body in row.findAll('td'):
            bodies= (body.text)
            my_data.append(bodies)
        print(my_data)
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n', '15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n', '15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n', '16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n', '15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n', '16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n', '17', '\nLeeds United\n', '24', '5', '7', '12', '29', '39', '-10', '22', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n', '15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n', '16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n', '17', '\nLeeds United\n', '24', '5', '7', '12', '29', '39', '-10', '22', '\n\n       \n', '18', '\nEverton\n', '24', '5', '6', '13', '17', '32', '-15', '21', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n', '15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n', '16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n', '17', '\nLeeds United\n', '24', '5', '7', '12', '29', '39', '-10', '22', '\n\n       \n', '18', '\nEverton\n', '24', '5', '6', '13', '17', '32', '-15', '21', '\n\n       \n', '19', '\nBournemouth\n', '24', '5', '6', '13', '22', '48', '-26', '21', '\n\n       \n']
# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6', '1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n', '2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n', '3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n', '4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n', '5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n', '6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n', '7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n', '8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n', '9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n', '10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n', '11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n', '12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n', '13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n', '14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n', '15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n', '16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n', '17', '\nLeeds United\n', '24', '5', '7', '12', '29', '39', '-10', '22', '\n\n       \n', '18', '\nEverton\n', '24', '5', '6', '13', '17', '32', '-15', '21', '\n\n       \n', '19', '\nBournemouth\n', '24', '5', '6', '13', '22', '48', '-26', '21', '\n\n       \n', '20', '\nSouthampton\n', '24', '5', '3', '16', '19', '41', '-22', '18', '\n\n       \n']


# حالت سوم
for row in rows:
    my_data=[]
    for head in row.findAll('th'):
        heads= (head.text)
        my_data.append(heads)
    my_data2=[]
    for body in row.findAll('td'):
        bodies= (body.text)
        my_data.append(bodies)
    # print(my_data)
    print(my_data2)

# ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6']
# []
# []
# ['1', '\nArsenal\n', '24', '18', '3', '3', '52', '23', '29', '57', '\n\n       \n']
# []
# ['2', '\nManchester City\n', '25', '17', '4', '4', '64', '25', '39', '55', '\n\n       \n']
# []
# ['3', '\nManchester United\n', '24', '15', '4', '5', '41', '28', '13', '49', '\n\n       \n']
# []
# ['4', '\nTottenham Hotspur\n', '25', '14', '3', '8', '46', '35', '11', '45', '\n\n       \n']
# []
# ['5', '\nNewcastle United\n', '23', '10', '11', '2', '35', '15', '20', '41', '\n\n       \n']
# []
# ['6', '\nFulham\n', '25', '11', '6', '8', '36', '31', '5', '39', '\n\n       \n']
# []
# ['7', '\nLiverpool\n', '23', '10', '6', '7', '38', '28', '10', '36', '\n\n       \n']
# []
# ['8', '\nBrighton and Hove Albion\n', '22', '10', '5', '7', '39', '29', '10', '35', '\n\n       \n']
# []
# ['9', '\nBrentford\n', '23', '8', '11', '4', '37', '30', '7', '35', '\n\n       \n']
# []
# ['10', '\nChelsea\n', '24', '8', '7', '9', '23', '25', '-2', '31', '\n\n       \n']
# []
# ['11', '\nAston Villa\n', '24', '9', '4', '11', '30', '38', '-8', '31', '\n\n       \n']
# []
# ['12', '\nCrystal Palace\n', '24', '6', '9', '9', '21', '31', '-10', '27', '\n\n       \n']
# []
# ['13', '\nNottingham Forest\n', '24', '6', '7', '11', '18', '42', '-24', '25', '\n\n       \n']
# []
# ['14', '\nLeicester City\n', '24', '7', '3', '14', '36', '42', '-6', '24', '\n\n       \n']
# []
# ['15', '\nWolverhampton Wanderers\n', '24', '6', '6', '12', '18', '33', '-15', '24', '\n\n       \n']
# []
# ['16', '\nWest Ham United\n', '24', '6', '5', '13', '23', '29', '-6', '23', '\n\n       \n']
# []
# ['17', '\nLeeds United\n', '24', '5', '7', '12', '29', '39', '-10', '22', '\n\n       \n']
# []
# ['18', '\nEverton\n', '24', '5', '6', '13', '17', '32', '-15', '21', '\n\n       \n']
# []
# ['19', '\nBournemouth\n', '24', '5', '6', '13', '22', '48', '-26', '21', '\n\n       \n']
# []
# ['20', '\nSouthampton\n', '24', '5', '3', '16', '19', '41', '-22', '18', '\n\n       \n']

# ////////////
# حذف کاراکتر هایی که خودمون نمیخوایم از اول بیاد


# حالا کار دیگر هم میشه کرد مثلا حذف \n

    for row in rows:
        my_data = []
    for head in row.findAll('th'):
        heads = (head.text)
    my_data.append(heads)

    for body in row.findAll('td'):
        bodies = (body.text.replace('\n', ''))
    my_data.append(bodies)
    print(my_data)
    # '#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'Last 6']
    # ['1', 'Arsenal', '24', '18', '3', '3', '52', '23', '29', '57', '       ']
    # ['2', 'Manchester City', '25', '17', '4', '4', '64', '25', '39', '55', '       ']

# برش زدن ورودی از اول
# یا اینکه بیایم فقط تا یه سریشو بده  از اول و اضافه هاشو نگیره اصلا
    for head in row.findAll('th')[:9]:
        heads= (head.text)
        my_data.append(heads)

    for body in row.findAll('td')[:9]:
        bodies= (body.text.replace('\n',''))
        my_data.append(bodies)
    print(my_data)
    # ['#', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD']
    # ['1', 'Arsenal', '24', '18', '3', '3', '52', '23', '29']
    # ['2', 'Manchester City', '25', '17', '4', '4', '64', '25', '39']
    # ['3', 'Manchester United', '24', '15', '4', '5', '41', '28', '13']



# /////////////
# کنار هم آوردن دو لیست در با هم
# حلقه زدن دو لیست
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

# ///////////////
# حلقه تودرتو

for s in words.split():
        if not any(c.isdigit() for c in s):
            print(s)
# یعنی حلقشو همینجا میزنی جلوی ایف
' '.join(s for s in words.split() if not any(c.isdigit() for c in s))

# /////////
# نکته جالب اینه میشه در حلقه ها یه ضرب خودشو انجام بده
# یعنی
for s in words.split():
    # اجرای یه متد در خود چنته حلقه و نه در دو مرحله


# //////