
# کار با jupyter
# برای کارهای دیتا ساینس 

# /////
pip install jupyter
# اسم قدیمیش نوت بوک هستش
# یا اناکوندا همه ی دیتاساینس را داره همراه 
# نام پای . پانداس . مت پلات لایب . ...
pip install anaconda

# ///
# بالا اومدن برای پایتون
# در مسیری که میخوای مثلا
PS E:\.python and every thing\codes and projects\exer\Jupyter_exer\.ipynb_checkpoints>
# که اینو باید بزنی در ترمینالی که فرض کن تا فا
# یل code and project هستی
cd exer\Jupyter_exer\.ipynb_checkpoints


# اینو بزن

python -m notebook

# این لینکو بهت میده در ترمنیال شبیه
http://127.0.0.1:8888/?token=c2db88d27c92b816d432643498cfc589270afc29fe739a78
# که باید بری تا ترمینال را بیاره بالا

# اگر خواستی یه فایل را دوباره باز کنی . باید بری توی مسیرش در ترمینال پس از اون
python -m notebook
# را بزنی همون مسیر را میاره


# اگر میخوای  تازه بنویسی باید 
new 
# بزنی

# ////
# توجه باید اینتر را بزنی در برنامه و صرفا نوشتن نیست باید کنترل اینتر بزنی که به حالت عدد در بیاد شمارنده سلول
# وگرنه عمل نمیکنه

# /////////
# توجه اگر در یک فایل پر بزنی میاره در همونجا فایل ژوپیترتو ایجاد میکنه و با باز کردن لینک هم از همونجا اغاز میکنه
# ولی اگر میخوای در یه جا دیگه باشه به وسیله vscode از جای دیگر باز کن

# در ضمنن پس از ایجاد خودش در همین مسیر فایلی میسازه
# با pychrm  هم میشه باهاش کار کرد

# /////
# نصب یک کتابخانه برای ژوپیتر

# یا باید دقیقا بری توی همون مسیر دایرکتوری ای که داره باز میشهو بعد بزنی
PS E:\.python and every thing\codes and projects\exer\Jupyter_exer\.ipynb_checkpoints>


pip install more_itertools

# یا این

import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)


# /////////////////
# هر قطعه یک cell  است
# in[]: کد مینویسیم
# با اینتر خط عوض میشه در همون قططع


# با run کردن میره جلو
#
# پرینت کردن و اجرا
# crtl+enter


# ///////

با insert 
یه سلول میسازه بالا یا پایین

A بالا میسازه یه سلول
B پایین میسازه

# //////
# کار دیتا ساینتیست ها

# در یک سلول اول 
# imprort


# در سلول دوم
# دیتا هارا میخونن


# در سلول سوم 
# تغیر دیتا

# سلول چهارم
# خروجی

# فقط کافیه اون سلول را اجرا کنه

# ///////////
# یادداشت گذاری

اگر 
M
یا 
cell- cell type -Mark down
میشه یاد داشت گذاری کرد

# تیتیر بزرگ
## تیتر کوچک
### تیتر خیلی کوچیکتر

پایینشم میشه نوشت

-point1
-point2

# //////////



# اگر در متغیری نوشتی در همون سلول یا سلول دیگر کافیه  فقط همون متغیر را بنویسی

a=np.array(5)
a

بهت میده
array(5)
# /////


# توجه اگر در یک سلول چیزی را زدی که در سلول دوم اورد
# بعد که سلول اول را تغیر میدی باید دوباره از بالا اینتر کنترل بزنی و بیای پایین اینتر بزنی 
# تا اون یکی هم تغیر کنه


# ///////
Y تبدیل سلول به کد
M تبدیل سلول به کامنت گذاری
B ایجاد خط در پایین
A ایجاد خط در بالا



