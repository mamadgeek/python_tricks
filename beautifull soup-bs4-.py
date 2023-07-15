

# ///////////




# وقتی request زدی یا از  selenium اومدی میاد یه صفحه
# htm  را میده
# ک برای تفسیر اون نیاز به beautifull soup  داریم

# /////////
# نکته 
# . در دسترسی به 
# یه نوشته درون یه سایت ما
# به آخرین تگ باید برسیم (تگ اون ها است که فلش دارن کنارشون در inspect)
# پس ما به آخرین تگ میرسونیم خودمون را که در اینجا th است پس از اون دیگه اتربیوت ها هستند
# و از طریق اتربیوت ها به اون محتوا برسیم . حالا اغلب از هرکدوم از اتربیوت ها میشه رسید
# اتربیوت هم اون ها هستند که  نوشته هستند بعد سمت راستشون = است
# کنار اون مساوی اون ولیو که ما برای دسترسی از اونها استفاده میکنیم و از عنوان اتربیوت
# این tag است
<Head>
    <thead>
        class="standing-table__row"

    # در اینجا کلاس اتربیوت است و standing-table__row مابقی ولیو است
    # برای دسترسی ما به مادر مستقیم اون اشاره میکنیم نه مادربزرگها و نه نیکان
    # یعنی اونها را با حلقه و روش هایی میریم تا برسی
    # به آخرین مادر برس که اتربیوت شو نیاز داری

# ////////
# داده گرفته شده از: selenium
# تا اینجا از

# /////////////////////////
# پس یه جستجوی ساده در گوگل فعلا اینه
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# اول میایم مسیر اون chromedriver را بهش معرفی میکنیم که توسط اون بره گوگل را بگرده یا کاری کنه
# موتور واسطه
driver=Chrome(executable_path='chromedriver.exe')
driver.get('https://Google.com')
# driver.find_element_by_name('q')
search_bar=driver.find_element(By.NAME, "q")
search_bar.send_keys('hello')
search_bar.send_keys(Keys.ENTER)

input()


# از این به بعد BeautifulSoup

# چیزی که توی اون صفحه هستیم را میاد فایل html اش را بهمون دسترسی میده
from bs4 import  BeautifulSoup
# این میاد page source را بهمون میده  که با راست کلیک در کروم هم میشه بهش دسترسی داشت
soup=BeautifulSoup(driver.page_source)

# اینم میاد بهش tag که دادیم را واسمون همه متغیر هاشو میده و محتواشو
print(soup.find_all('h3'))
input()
# [<h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">صادق خلخالی - ویکی‌پدیا، دانشنامهٔ آزاد</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">تاریخ تولد مادرجنده - ❤️ تکست ناب</span></h3>,
# <h3 class="LC20lb MBeuO xvfwl"><span dir="rtl">سال تولد مادرجنده - ❤️ تکست ناب</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">روزی که صادق خلخالی رقصید و امام خندید! - ایسنا</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">مدیر خارکسده مادرجنده خارجنده آپارات</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">معنی مادر جنده - واژه‌نامه آزاد - لام تا کام</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">زندگی نامه آیت الله خامنه ای (بخش نخست)- تولد و والدین - رادیو فردا</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">با سپاس از همۀ عزیزانی که محبت کرده و سالروز تولد اینجانب را ...</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">روز #پادشاه، روز ملی هلند بر شما همراهان گرامی شاد و پیروز باد ...</span></h3>,
# <h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">madar jende i told you مادر جنده ای تولد یو - YouTube</span></h3>]

# میاد لیستی از دونه دونه موارد که tag 'h3 ' داشت را بهمون میده
# ولی در یک خط
# حالا می تونیم کار های دیگر پایتونی باهاش کنیم

# ////////////

# این دونه دونه موارد را میده در لیست را
my_soup=(soup.find_all('h3'))
for name in my_soup:
    print(name)
input()


# حالا اگر همه ی نوشته های جلوی tag هاشو بده
my_soup=(soup.find_all('h3'))
for name in my_soup:
    print(name.text)
input()


# صادق خلخالی - ویکی‌پدیا، دانشنامهٔ آزاد
# تاریخ تولد مادرجنده - ❤️ تکست ناب
# سال تولد مادرجنده - ❤️ تکست ناب
# روزی که صادق خلخالی رقصید و امام خندید! - ایسنا
# تاریخ تولد مادرجنده | ❤️یک نت
# اشموغAshmogh on Twitter: "تولد یگانه پیامبر مادرجنده را به تمام ...
# مدیر خارکسده مادرجنده خارجنده آپارات
# با سپاس از همۀ عزیزانی که محبت کرده و سالروز تولد اینجانب را ...
# معنی مادر جنده - واژه‌نامه آزاد - لام تا کام
# زندگی نامه آیت الله خامنه ای (بخش نخست)- تولد و والدین - رادیو فردا

# حالا اگر بریزیم توی یه فایل text

# چیزی که توی اون صفحه هستیم را میاد فایل html اش را بهمون دسترسی میده
from bs4 import  BeautifulSoup
# این میاد page source را بهمون میده  که با راست کلیک در کروم هم میشه بهش دسترسی داشت
soup=BeautifulSoup(driver.page_source)
# این تیکه هم بیشتر مربوط به کار با فایل ها است چون که میخوایم بریزیم توی فایل
my_soup=(soup.find_all('h3'))
with open ('my_example2','a',encoding='utf8') as f:
    for name in my_soup:
        f.write(name.text)
        f.write('\n')

# که اخرش فایلی text درست میکنه که اینو میده
# گرفتن فایل از اینترنت و ریختن رد یک فایل
# صادق خلخالی - ویکی‌پدیا، دانشنامهٔ آزاد
# تاریخ تولد مادرجنده - ❤️ تکست ناب
# سال تولد مادرجنده - ❤️ تکست ناب
# روزی که صادق خلخالی رقصید و امام خندید! - ایسنا
# مدیر خارکسده مادرجنده خارجنده آپارات
# معنی مادر جنده - واژه‌نامه آزاد - لام تا کام
# زندگی نامه آیت الله خامنه ای (بخش نخست)- تولد و والدین - رادیو فردا
# با سپاس از همۀ عزیزانی که محبت کرده و سالروز تولد اینجانب را ...
# آیت الله خلخالی که بود و چه کرد؟ | رویداد24
# madar jende i told you مادر جنده ای تولد یو - YouTube

# البته میشد تیکه اولشو گرفت

my_soup=(soup.find_all('h3'))
print(my_soup[1])
# که اینو میداد
# [<h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">صادق خلخالی - ویکی‌پدیا، دانشنامهٔ آزاد</span></h3>,

# البته find هم اولیو پیشفرض میگیره میده
my_soup=soup.find('h3')
print(my_soup)
# [<h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">صادق خلخالی - ویکی‌پدیا، دانشنامهٔ آزاد</span></h3>,






# ////////
# request - bs4 - html


# وقتی میخوایم از requests استفاده کنیم
r=requests.get('html:\\divar.ir')
# و پس از اون ببرم توی bs4:

# text صفحه را میریزیم توی متغیر request
soup=BeautifulSoup(r.text,'html.parser')
# که فرمت اش را با تکست بهمون میده
# که باید حالیش کنیم اون text چیه فرمتش


# بعد اگر چجوری ای که ما میخوایم را
# یعنی از صفحه body یا h2 یا h3  و... را بگیریم
find
# اولین  را میده که پیدا کرده
soup.find('h2')

# میره از فایل html اولین h2 را میده بهمون
# [<h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">صادق خلخالی - ویکی‌پدیا، دانشنامهٔ آزاد</span></h3>,

# توجه شود که اینها ابجکست هست و میشه دیتای دیگر هم از درون اون گرفت

# ////////

# بطور کلی دستور اینه
import requests
my=requests.get('https://divar.ir/s/tehran')
print((my))
print(my.text)
# که یه تکست میاره
# حالا بقیش میشه
# bs4

mypage=BeautifulSoup(my.text,'html.parser')
my_objects= (mypage.find_all('h2'))
print(my_objects[20])
# <h2 class="kt-visually-hidden">فیلترها</h2>
# فقط یه تیکه از اونو جدا میکنه

# حالا میتونیم اون تیکشو که میخوایم را بگیریم

# اتربیوت هاشو میده یا اون متد های دیگر مثل text
# {'class': ['kt-visually-hidden']}

# یا میتونیم همشونو مواردی که میخوایم را بگیریم اسم و.... شونو
for ob in my_objects:
    print(ob.attrs , ob.text)
# {'class': ['kt-visually-hidden']}
# {'class': ['kt-accordion-title', 'kt-caption']} دسته‌ها
# {'class': ['kt-visually-hidden']} فیلترها
# {'class': ['kt-visually-hidden']}  دربارهٔ دیوار
# {'class': ['kt-visually-hidden']} دیوار در شبکه‌های اجتماعی

# /////////
# کارهای مختلف با html
# گرفتن body
print(mypage.find('body'))


# یا
print(mypage.find('article'))


# یا

print(mypage.find('h2',attrs='kt-post-card__title'))
# <h2 class="kt-post-card__title">کیسه بوکس و کش ورزشی</h2>



# //////
# اما مشکل
# من بخوام زیر مجموعه ای از چیزی را انتخاب کنم مشکله واسم
a=(mypage.findall('article'))
for i in a:
    print(i)
# این خطا را میده
# TypeError: 'NoneType' object is not callable

# //////////

# ????????//////////
# اما چجوری بفهمم که کلید اون تیکه ای که میخوام چیه؟
# یعنی مثلا  ها و اسم خودرو را
# میخوام بدم بهش که بعد قیمت هارا بده بهم
# چجوری باید این کار را کنم؟



# ////////
# پس از ریکوئست
import  requests
from bs4 import BeautifulSoup
url='https://www.python.org/'
my_response=requests.get(url)
# print(my_response.text)
# دو قسمت داره این کتابخونه
# پارسر که تجزیه کننده است که میشه xml هم باشه
# و اون فرمت text ای که از get گرفتیم
soup=BeautifulSoup(my_response.text,'html.parser')
# این میاد در وهله نخست به زبان خود بیوتیفول سوپ میاره که مرتب تر میکنه

# ////////////
# نشون دادن tag name ها
# یه دونه اولی
soup=BeautifulSoup(my_response.text,'html.parser')
show=soup.find('a')
print(show)
# <a href="#content" title="Skip to content">Skip to content</a>


# ////
# نشون دادن همه tag name هایی که با اسم خاصی بوجود اومدن
soup=BeautifulSoup(my_response.text,'html.parser')
show=soup.findAll('a')
print(show)
# <a href="#content" title="Skip to content">Skip to content</a>
# ///////
# جالبه که اگر اخریشو اینجوری بزنی هم میده
# یعنی findall را حتی نزنی
show=soup.find_all('div',{'class':'detail-container'})
# print(show)
for detail_container in show:
    for title_price_location in detail_container.find_all('div',{'class':'title-price-location'}):
        # print(title_price_location)
        for location in title_price_location('div',{'class':'location'}):
            print(location.text)   # جنت اباد جنوبی

# /////////////
# اتربیوت های درون هر تگ
# توجه شود که با این مقدارها-المنت ها
# نشان داده نمیشن بلکه اتربیوت ها هستند
# برای نمایش اتربیوت href که درون a است این کار را میکنیم
# میریزم درون براکت
soup=BeautifulSoup(my_response.text,'html.parser')
show=soup.findAll('a')
# print(show)
for char in show:
    print(char['href'])

# //////////////
# سوال
# اینرا اگه هم بنویسیم میاره چیزهایی را
for char in show:
    print(char['title']['href'])
# اگه اینرا هم بیاریم میاره
for char in show:
    print(char['title']

# چه فرقی دارن؟


# ////////////////////////
# جایگاه و کار اتربیوت ها در html
# درون صفه اونی که اول نوشته شده تگ هست
# اونی که مقدار داره اتربیوت است که جلوش مساوی است


# لینک ها درون اتربیوت href هستند









# ///////////

# دریافت المنت ها درون اتربیوت ها
# با استفاده از اتربیوت ها
#     فکر کنم
    # اولین عنصر tag است
    # عناصر بعدی اتربیوت

# اگر بخوایم از صفحه www.python.org
    # از دکمه go
    # اون نوشته go را بهش دسترسی داشته باشیم


# روش ۱
select_one
    یه نمونه را میده
select همه
    را میده

# دسترسی با علامت ها . بعد از نوشتن تگ از
# با استفاده از هرکدوم از اتربیوت ها میشه بهش دستترسی داشت
# علامت . برای class
# علامت شارپ یا # برای id است

import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
my_response = requests.get(url)

soup = BeautifulSoup(my_response.text, 'html.parser')
# در اینجا مقدار اون کلید اتربیوت را باید بدی نه خود اتربیوت را
# یعنی اول تگ مادر سپس مقدار
show = soup.select_one('button.search-button')
# ما text را میخواستیم و یه نامنظم میده
print(show.text)
    #
    # GO
    #
# حالا برای مرتب کردن اون داده میتونیم از رجکس یا strip  استفاده کنیم
print(show.text.strip())
# GO
#     مرتب میده
# //////////
#     متد شارپ که از id میده
soup = BeautifulSoup(my_response.text, 'html.parser')
show = soup.select_one('button#submit')
print(show.text.strip())
#
# GO
#
# ////////////////

# حالا روش find
    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.python.org/'
    my_response = requests.get(url)
    # حالا اگر از روش find بریم
    soup = BeautifulSoup(my_response.text, 'html.parser')
    # باید اون تگ را اول بگیم . پس از اون
    # یه اکولاد
    # اسم هر اتربیوت به غیر از کلاس
    # را درون  میزاریم که کلید میشه و ولیو میشه درون استرینگ
    # این شکلی
    # show=soup.find('tag',{'attrebute':'value'})

    show = soup.find('button', {'id': 'submit'})
    print(show.text.strip())
    # GO

# //////////////
# برای دسترسی معمولا div  نیست بلکه پایینه اونه
    # یه راه دیگه اون اخرین چیزیه که نوشته شده
    # ////////////
# حالا اگر بخوایم از یه
# صفحه یه تگ که چند تا تگ داره و هرکدام اتربیوت های مختلف دارن
# تگ های تتودرتو

    # مثال . لیگ انگلیس
    # یه تگ مادربزرگ داریم - به اسم table
    # - خود تیبل دو تا تگ داره thead- tbody  -
    # هر کدوم از تیهد و تیبادی خود تگ tr دارن
    # خود تگ tr  خودش تگ های th مختلفی داره


from bs4 import BeautifulSoup
url='https://www.skysports.com/premier-league-table'
my_response=requests.get(url)

soup=BeautifulSoup(my_response.text,'html.parser')
Table=soup.find('table')
print(Table)
# اینجا فقط اون تگ کلید را پیدا میکنه و میاره بالا

# تگ های تودرتو را درونش اورده
# اینجا جدولمون دو قسمت داره یعنی دوتا tag داره
thead - tbody
# که در تی هد نوشته که تیم و امتیاز و....
#
    # اینم روش دسترسی به تگ تودرتو

# جدول اصلی و اولی فقط یه دونه است
Table = soup.find('table')
# چون ما همه اطلاعاتمون درون متغیر Table  است
rows=Table.find_all('thead')
# rows=Table.find_all('tbody') #یا ## حالا بطور موازی
print(rows)
# چون تگ بقیه هی سطر های مختلف داره از findall  استفاده میکنیم
print(rows)
# اینو میاره : لیستی از اشیا یعنی ابجکت ها
# و به گمونم هم دختر هارا میده هم دختر دختر ها را
    # یعنی خودش باز میکنه هرکدوم هم را
# [<thead>
# <tr class="standing-table__row">
# <th class="standing-table__cell standing-table__header-cell" data-index="0" data-label="pos" title="Position">#</th>
# <th class="standing-table__cell standing-table__header-cell standing-table__cell--name" data-index="1" title="Team">Team</th>
# <th class="standing-table__cell standing-table__header-cell" data-index="2" data-label="pld" title="Played">Pl</th>
# <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="3" data-label="w" title="Won">W</th>
# <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="4" data-label="d">D</th>
# <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="5" data-label="l">L</th>
# <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="6" data-label="f">F</th>
# <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="7" data-label="a">A</th>
# <th class="standing-table__cell standing-table__header-cell" data-index="8" data-label="gd">GD</th>
# <th class="standing-table__cell standing-table__header-cell" data-index="9" data-label="pts" data-sort-value="use-attribute">Pts</th>
# <th class="standing-table__cell standing-table__header-cell is-hidden--bp15 is-hidden--bp35" data-index="10" data-sort-value="use-attribute">Last 6</th>
# </tr>
# </thead>]



#  چون درون لیست بهمون میده ما میایم موارد را میکشیم بیرون با یه حلقه
#     که موارد درون لیست را دونه دونه بهمون بده
    for row in rows:
        print(row)
# این شکلی میده دونه دونه
#     این یه row است
# < thead >
    #     این یه row است
    # < tr class ="standing-table__row" >
# <th class="standing-table__cell standing-table__header-cell" data-index="0" data-label="pos" title="Position">#</th>
# </tr>
# </thead>

#         حالا اگر اون حلقه را دوباره باز کنیم با حلقه

    for row in rows:
        # print(row)
        for  head in row:
            print(head)

# <tr class="standing-table__row">
# < th class ="standing-table__cell standing-table__header-cell" data-index="0" data-label="pos" title="Position" >  # </th>
# < / tr >

# حالا  اگر  از اول اینو مینوشتیم
    for row in rows:
        print(row.findAll('th'))
        # for  head in row:
        #     print(head)
        # [<th class="standing-table__cell standing-table__header-cell" data-index="0" data-label="pos" title="Position">#</th>, <th class="standing-table__cell standing-table__header-cell standing-table__cell--name" data-index="1" title="Team">Team</th>, <th class="standing-table__cell standing-table__header-cell" data-index="2" data-label="pld" title="Played">Pl</th>, <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="3" data-label="w" title="Won">W</th>, <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="4" data-label="d">D</th>, <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="5" data-label="l">L</th>, <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="6" data-label="f">F</th>, <th class="standing-table__cell standing-table__header-cell is-hidden--bp35" data-index="7" data-label="a">A</th>, <th class="standing-table__cell standing-table__header-cell" data-index="8" data-label="gd">GD</th>, <th class="standing-table__cell standing-table__header-cell" data-index="9" data-label="pts" data-sort-value="use-attribute">Pts</th>, <th class="standing-table__cell standing-table__header-cell is-hidden--bp15 is-hidden--bp35" data-index="10" data-sort-value="use-attribute">Last 6</th>]

# پس یعنی اگر بازش کنیم اونو اضافه میکنه?
#         نه .
        #         ما تگ th را برگزیدیمfindAll   و بخاطر همین اینو نیاورد واسمون
        # <tr class="standing-table__row">
# در صورتی که داخل لیست نبود


# حالا هرکدوم از th ها یه دونه از این هستند

    # Team
    # Pl
    # W
    # D
    # L
    # F
    # A
    # GD
    # Pts
    # Last 6

# پس ما به آخرین تگ میرسونیم خودمون را که در اینجا th است پس از اون دیگه اتربیوت ها هستند
# ///////////////
#         حالا چون ما داده های هر کدوم را جدا جدا میخوایم که اخرین مادر هستش این را میاریم:
    for row in rows:
        for head in row.findAll('th'):
            print(head)
    # <th class="standing-table__cell standing-table__header-cell" data-index="0" data-label="pos" title="Position">#</th>

# ولی چون text را میخوایم و بادی را نمیخوایم
# میام:
    for row in rows:
        for head in row.findAll('th'):
            print(head.text)
    # #
    # Team
    # Pl
    # W
    # D
    # L
    # F
    # A
    # GD
    # Pts
    # Last 6

# //////////////////
# نکته در thead ما از طریق رفته بودیم
soup = BeautifulSoup(my_response.text, 'html.parser')
Table = soup.find('table')
rows = Table.find_all('thead')
for row in rows:
    for head in row.findAll('th'):
        print(head.text)

# که بهمون همونو داد
#     ولی میشد tr داد
soup = BeautifulSoup(my_response.text, 'html.parser')
Table = soup.find('table')
rows = Table.find_all('tr')
for row in rows:
    for head in row.findAll('th'):
    print(head.text)

# حالا چرا کار میکنه؟
# شاید چون همون یه دونه را عضو داره
#     از طرف دیگه مادربزرگ هر دو یکی است tr و نه thead
    # اینجوری میشه با یه حلقه ادامه کار را داد
for row in rows:
    for head in row.findAll('th'):
        print(head.text)
    for body in row.findAll('td'):
        print(body.text)

# حالا بقیش کار پایتونی است و مرتب کردن با هم که یا با پانداس (یا...)

# این میاد به ازای هر سرتیتر در همونجا بقیه را میزاره

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

    # یا اینکه بیایم فقط تا یه سریشو بده  از اول و اضافه هاشو نگیره اصلا
    for head in row.findAll('th')[:9]:
        heads = (head.text)
    my_data.append(heads)

    for body in row.findAll('td')[:9]:
        bodies = (body.text.replace('\n', ''))
    my_data.append(bodies)
    print(my_data)
    # ///////////////////////////////////
# نمونه کد
# پس خلاصه کار با bs4
import  requests
from bs4 import BeautifulSoup
url='https://www.skysports.com/premier-league-table'
my_response=requests.get(url)

soup=BeautifulSoup(my_response.text,'html.parser')
Table=soup.find('table')
rows=Table.find_all('tr')
# print(rows)

for row in rows:
    my_data=[]
    for head in row.findAll('th')[:9]:
        heads= (head.text)
        my_data.append(heads)

    for body in row.findAll('td')[:9]:
        bodies= (body.text.replace('\n',''))
        my_data.append(bodies)
    print(my_data)


# ایا میشه همین  خروجی را برد توی دیتا بیس؟ یعنی ببرم اونجا و به زبان دیگری ترجمش کنم ؟
# یه سایت اصلا درست کنم واسش؟
# که اون اتربیوت ها بشه لیست نخست و مابقی بشه موارد اونها
#     حتی میتونم احتمال قهرمانی یه تیم را پس از هر بازی بیارم
#     یا جایگشت های بازی ها را بیارم
#     حتی از زبان طبیعی استفاده کنه . وویس بگیره و واسه ما بیاره بخونه
#     یا موارد را نشون بده در یک تصویر

# ///////////////////////
# نکته
# وقتی که متغیر نخست یکی باشه که به چندتا تجزیه میشه اینطور مینویسیم

Table = soup.find('table')
rows = Table.find_all('tr')
# print(rows)

for row in rows:
    my_data = []
for head in row.findAll('th')[:9]:
    heads = (head.text)

# وقتی که متغیر نخست از اول خودش چند تا باشه اینطور مینویسیم
for a in divar_a:
    for article in a.find_all('article'):
        print(article)

# //////////////////////////

# بردن فایل های دریافتی در pandas و excel


# // // // // //


# ////////////////
#  دانلود از اینترنت



# /////////////
# کار با رجکس برای اشاره به یه tag یا اتربیوت




# //////////
# پرسش
# چرا اینجا نمیشه شمرد تعداد را ؟
    for div in article.select('div.kt-post-card__description'):
    # print(div.text)
    # میخوام بشماره
        number = 0
    while (div.text) == 'کارکرده':
        print(f'{div.text} : {a.text.strip()}')
        print(number)
        number += 1
        break
# کارکرده : مبل استیل 8 نفره زرشکیکارکرده۳,۵۰۰,۰۰۰ تومانلحظاتی پیش در امیر بهادر
# 0
# /////////////




# ایا میشه به یه سری متغیر فقط با یه findall یا select  دسترسی داشت؟


# دسترسی به موارد html

# یعنی همه قیمت ها در سایت
# https://www.truecar.com/used-cars-for-sale/listings/bmw/location-saint-bonaventure-ny/
# اگر نه روش دسترسی به لینک زیر مجموعه چیست ؟ ایا اینکه از بالا همه کرکره ها را بریم؟

# مرحله ۱ - ثابته

import requests
from bs4 import BeautifulSoup
brand='bmw'
url = 'https://www.truecar.com/used-cars-for-sale/listings/'+brand+'/location-saint-bonaventure-ny/'
print(url)
myrequest=requests.get(url)
soup=BeautifulSoup(myrequest.text,'html.parser')


# طبقه بندی ها اینه  در صفحه
tag-div:
    tag-ui:
        tag-li:   #اینجا میرسی به یه عالمه ماشین که همشون تا اینجا یکی بودن و از این به بعد مواردشون یکی است
            tag-div:
                tag-div + <body>: # یعنی یه تگ داره یه دی ای وی
                # درون خودش یه سری مشخصات اصلی داره که اگر به موارد اون خواستیم دسترسی پیدا کنیم از این میرسیم
                #     حالا ۳ تا tag داره -
                    # ۱- عکس ۲- قلب ۳- بدنه
                    tag3: # 1- اتربیوت داره ۲- ۵ تا تگ داره ۳- یه بادی داره
                        atrebutes: #
                        5tags:
                            # هرکدوم دوباره یه زیر تگ یا چند زیر تگ داره
                            # ولی همشون اسمشون div است
                            # آخرش به atrebute ها میرسن:



# بهترین راه حل اینه که یه ضرب از کوچکترین کرکره بیایم دسترسی داشته باشیم بهش
# بجای اینکه دونه دونه تگ را از بالا باز کنیم
# ۲- حالا اگر مستقیم دسترسی بخوایم داشته باشیم:
show=soup.select('div.heading-base')
# print(show.text)
for char in show:
    print(char.text)
# Sponsored2017 BMW X1xDrive28i AWD
# Sponsored2018 BMW M2Coupe
# Sponsored2019 BMW 4 Series430i xDrive Gran Coupe
# 2020 BMW 3 Series330i xDrive
# 2019 BMW X1xDrive28i AWD

#
# نکته الف -
# برای پیدا کردن اون مورد باید بری کرکره ها را و روی
# ctrl+shif+c که زدی
# اون چیزی که میخوا را انقدر بری تا پیدا کنه و به شرطی که یه دست باشه و
# نه تیکه تیکه یعنی
show=soup.select('div.vehicleCardYearMakeModel')
# print(show.text)
for char in show:
    print(char.text)
# نمیاره
# چون خودش هد نیست بلکه جدا شده و اگر میخوای به موارد اشاره کنی که برو توی اتربیوت بیار دیگه


# نکته ب :
# در
# select جای  مقدار را بزن نه کلید را
show=soup.select('tag.value')

# نکته ج .
# چیزی که روی صفحه مینویسه را کپی کن یا بنویس نه چیزی که روی اون inspect اورده
# مثلا بجای
show=soup.select('div.flex w-full flex-col')
# بزن
show=soup.select('div.flex.w-full.flex-col')
# چون توی صفحه دومی را نوشته

# نکته پ
# اگر یه متغیر این تیکه ای باشه و نقطه دادی نگرفت
show=soup.select('div.vehicle-card-bottom-pricing-secondary pl-3 lg:pl-2 vehicle-card-bottom-max-50')
# تیکه اولشو فقط بزن
show=soup.select('div.vehicle-card-bottom-pricing-secondary')

# نکته ج
# از طریق کلاس بهشون دسترسی داشته باش نه مواردی مثل data-test و....



# نکته س
# از مادربزرگ هم میتونی دسترسی داشته باشی و چیزی را بیاری ولی راحت تر نیستی پس بهتره بری پایین تا برسی به دختر و دختر دختر که چیزی که میخوا را برسی


# نکته د
# پرسش
# وقتی یه بخشی از چند تا پارامتر تشکیل شده باشه که هر قدر به مادر و دخترش بریم نگیره
show_mile=soup.select('div.mt-2-5')
for char in show_mile:
    print(char.text)
# مثلا یه نمونه
# 53, 155 miles690 mi - Norcross, GA$599 shipping fee to store nearest you(Buffalo, NY) White exterior, Black interior

# یا وقتی اینو میزنی اصلا یه سری موارد دیگه را میاره
show_mile=soup.select('div.truncate.text-xs')
for char in show_mile:
    print(char.text)
# sDriveM40i
# $56 off avg. list price
# 12,947 miles
# Upfront Price Available
# Black exterior, Black interior
# 530i xDrive
# At or near avg. list price
# 25,330 miles

# که یعنی اینو اورده

# راه ۱ - رجکس کردن اون چیزی که میخوایم است
# ما فقط مایل و عددشو میخوایم پس رجکسش را میریم توی سایت
# اینو میاریم
(\d+,\d+ miles)
# یا اینکه اگر بخوایم مایلشو برداریم
(\d+,\d+) miles

# //////
# دسترسی به html ها
# انتخاب نوشته کنه و سپس راست کلیک inspect element
# //////
# اگر صفحات را بخوایم بزنه بره صفحه بعدی
def get_data_site(url,pages=2):
    # url='https://www.technolife.ir/product/list/69_800_801/%D8%AA%D9%85%D8%A7%D9%85%DB%8C-%DA%AF%D9%88%D8%B4%DB%8C%E2%80%8C%D9%87%D8%A7?code=69_800_801&plp=%D8%AA%D9%85%D8%A7%D9%85%DB%8C-%DA%AF%D9%88%D8%B4%DB%8C%E2%80%8C%D9%87%D8%A7&page=2'
    for page in range(1,pages):
        MyRequest=requests.get(url+str(page))
# ////
دسترسی html
نیازی نیست که برای استخراج بیای از بالا مجموعه ترین انتخاب کنی
Grany_data=soup.find_all('li',{'class':'ProductPrlist_product__PdoZm'})
# این li بالا مجموعه a است
# و این اطلاعات اضافی را هم میاره
# مقایسهگوشی موبايل سامسونگ مدل گلکسی A32 4G دو سیم کارت - ظرفیت 128 گیگابایت - رم 6 گیگابایت1286.464500010,495,000تومان


# ولی با انتخاب این یکی ما بهتر میتونیم دسترسی داشته باشیم
# یعنی دقیق تر و مشخص تر میشه

Grany_data = soup.select('a.ProductComp_product_title__bOrf5')

# اینها را میاره
# گوشی موبايل سامسونگ مدل گلکسی A32 4G دو سیم کارت - ظرفیت 128 گیگابایت - رم 6 گیگابایت

# که خوب قیمت نیست توی این

# ////
# برای دسترسی باید ببینی اون اتربیوت در کدوم تگ مادر هست.
# اگر کامل تر میخوای به مادر مادر رجوع کن



# //////
battery=[ x.text for x in soup.findAll('span')]
        print(battery)


# /////////
# چطور وقتی یک اسپن بین دوتا باشه را پیدا کنیم؟
# https://stackoverflow.com/questions/65114027/extracting-text-from-span-tag-with-no-classes-in-beautifulsoup
# https: // stackoverflow.com / questions / 61056040 / beautifulsoup - extract - the - data - in -the - text - after - a - particular - span
# https://stackoverflow.com/questions/26646231/beautiful-soup-parsing-span-element
# وقتی که اسم کلاس نداشته باشه
soup.find('span', attrs={'data-automation': True})

# //////////////
# چطور مواردی که کاراکتر های یکسانی ندارند را در یک دیتا بیس در یک دسته بندی قرار بدیم؟


