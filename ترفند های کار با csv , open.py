import csv

print("/////////////")
# تایپ هر کردام از اینا به ترتیب اینه :

#<class 'list'>
# <class 'str'>
# <class 'str'>

mak= open('mak.txt')
print(type(mak.readlines()))
print(type(mak.read()))
print(type(mak.readline()))
print("/////////////")
#پرینت کردن از خود فایل . اوردن به عنوان یک فایل پایتون که عملیات را روی آون بعدا انجام بدیم
# ['mandana', '5', '7', '3', '15']
# ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1']
# ['sina', '19', '10', '19', '6', '8', '14', '3']
# ['sara', '0', '5', '20', '14']
# ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7']
# ['ali', '1', '9']
# ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8']
import csv
with open ("np.csv") as esm:
    csv_reader= csv.reader(esm)
    for line in csv_reader:
        print(line)

print("/////////////")
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>



import csv
with open('np2 .csv') as f:
    reader = csv.reader(f)
    for i in reader:
        print(type(i))
print("/////////////")
#دستور nex میاد خط اول را حذف میکنه . مثلا اگر خود header بود اونرا حذف میکنه . عنوان را حذف میکنه
# ['hamid', '3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1']
# ['sina', '19', '10', '19', '6', '8', '14', '3']
# ['sara', '0', '5', '20', '14']
# ['soheila', '13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7']
# ['ali', '1', '9']
# ['sarvin', '0', '16', '16', '13', '19', '2', '17', '8']
import csv
with open ("np.csv") as esm:
    csv_reader= csv.reader(esm)
    next(csv_reader)
    for line in csv_reader:
        print(line)

print("/////////////")
#فقط عنصر n ام هر خط را چاپ هم میشه کرد. مثلا فقط عنصر اول را میشه چاپ کرد.
# hamid
# sina
# sara
# soheila
# ali
# sarvin

import csv
with open ("np.csv") as esm:
    csv_reader= csv.reader(esm)
    next(csv_reader)
    for line in csv_reader:
        print(line[0])


print("/////////////")
# فقط میخونه و یه فایل خالی میسازه
import csv
with open("np.csv") as khundan_file:
    reader_csv = csv.reader(khundan_file)
    with open("xn.csv", "w") as neveshtan_file:
        writer_csv = csv.writer(neveshtan_file)

print("/////////////")
# نوشتن از یک لیست  پایتون درون یک فایل
import csv

# نخست سازخت یه  لیستی از تاپل ها بصورت رندوم

import random
mylist=[]
for i in range(20):
    height=random.randint(155,180)
    weight=random.randint(50,98)
    gender=random.choice(['زن' , 'مرد'] )
    mylist.append((height,weight,gender))
# for char in mylist:
#     print(char)
# print(mylist)
# یو تی اف ۸ را میاریم که بره اونجا بنویسه
with open ('the_csv.csv','w',encoding='utf8',newline='' ) as the_csv:
    # نخست رایتر میسازیم
    neweshte=csv.writer(the_csv)
    for char in mylist:
        # print(char)
        # سپس رایترو میکنیم هر تیکه را  میسازیم
        neweshte.writerow(char)

#
# 161,78,مرد
# 178,80,مرد
# 178,86,زن
# 167,59,زن
# 165,86,مرد
# 170,72,مرد
# 170,91,زن
# 167,94,مرد


print("/////////////")

نوشتن درون یک فایل ار chatgpt
import csv

# define the data to be written
data = [
    ['Name', 'Age', 'Gender'],
    ['John', 25, 'Male'],
    ['Jane', 30, 'Female'],
    ['Bob', 35, 'Male']
]

# specify the file name and mode
filename = 'data.csv'
mode = 'w'

# open the file for writing
with open(filename, mode) as csv_file:
    # create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # write the data to the file
    for row in data:
        csv_writer.writerow(row)

print('Data written to CSV file.')

In this example, we use the csv module to create a CSV writer object and write the data to the file. The writerow() method is used to write each row of data to the file. Finally, we print a message to confirm that the data has been written to the CSV file.

print("/////////////")

print("/////////////")
#خواندن یک فایل csv و خروجی دادن یک فایل csv دیگر . کار با تابع .
import csv
from collections import OrderedDict
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
    #input_file_name = input("adres ra bede: ")
    with open(input_file_name) as fi:
        khandan = csv.reader(fi)
        with open(output_file_name, 'w', newline='') as nomre:
            neveshte = csv.writer(nomre)
            cor = (OrderedDict())
            for khat in khandan:
                value = (khat[1:])
                key = (khat[0])
                cor[key] = value
                cor = {k: list(map(float, v)) for k, v in cor.items()}
            for k, v in cor.items():
                v = mean(v)
                neveshte.writerow([k,v])

input_file_name= input('adresi ke mikhai bekhunam ra bede: ')
output_file_name= input('adresi ke mikhai berizam ra bede: ')
calculate_averages(input_file_name, output_file_name)

print("/////////////")
# میشه خروجی هر حلقه را هم پرینت کنه در فایل .


cor = {k: (mean(v)) for k, v in cor.items()}
            #print(cor)
            neveshte.writerow([cor])
            for (key, value) in sorted(cor.items()):
                neveshte.writerow([key,value])
print("/////////////")
# دستور اجرای در پرینت . یعنی از دیکشنری اینجوری میاریم بیرون
for (key, value) in (cor.items()):
    neveshte.writerow([key, value])
print("/////////////")


print("/////////////")



print("/////////////")



print("/////////////")

print("/////////////")











#{'mandana': ['5', '7', '3', '15'], 'hamid': ['3', '9', '4', '20', '9', '1', '8', '16', '0', '5', '2', '4', '7', '2', '1'], 'sina': ['19', '10', '19', '6', '8', '14', '3'], 'sara': ['0', '5', '20', '14'], 'soheila': ['13', '2', '5', '1', '3', '10', '12', '4', '13', '17', '7', '7'], 'ali': ['1', '9'], 'sarvin': ['0', '16', '16', '13', '19', '2', '17', '8']}
import csv
from collections import OrderedDict
a=input('give me a cvs adress (np.csv): ')
with open (a) as fi:
    khandan= csv.reader(fi)
    cor = (dict())
    for khat in khandan :
        value=(khat[1:])
        key=(khat[0])
        cor[key]= value
print(cor)


print("/////////")
# appand


# //////////////////////////////

# فرض کن از یه صفحه بار گذاری می کنی و اطلاعاتی
# را میگیری و میخوای بخشیشو بریزی توی یه فالی text
my_soup=(soup.find_all('h3'))
# تا اینجا از فایل میگیریم . حالا بجای پرینت میگیم بریز توی یه فایل . ولی یک تیکه خاصشو
with open ('my_example','a',encoding='utf8') as f:
    # چون در فایل دریافتی soup همه ی اون موارد را درون لیست میده پس در حلقه میزنیم و دونه دونه میریزیم توی فایلمون
    for name in my_soup:
        f.write(name.text)
        # این text  فرمت اون tag html است که میگیم نوشته هاشو بده و رایت کن .
        f.write('\n')
        # این هم برای اینه که دونه دونه موارد برن سر خط در فایلی که میسازیم
# توضیح
# اگر نزنی یه فایل را که قبلا وجود نداشته باشه از نوع appand یعنی 'a' ین خطا را میده
# with open ('my_example') as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'my_example'

# توضیح
# اگر نزنی utf8 میگه : و این خطا را میده:
# UnicodeEncodeError: 'charmap' codec can't encode character '\u06cc' in position 10: character maps to <undefined>


# ///////////
# دانلود محتوا . یعنی عکس و فیلم و... از درون یک فایل
# دانلود کردن یه عکس درون یک سایت

import  requests
url='https://www.python.org/static/img/python-logo@2x.png'
my_response=requests.get(url)
print(my_response.text)
with open('ax.jpg','wb') as r:
    r.write(my_response.content)

# میره ذخیره میکنه عکس ها را
# از 'wb' یعنی باینری رارایت کن
# content هم برای محتواهای عکس و... است


# ///////



