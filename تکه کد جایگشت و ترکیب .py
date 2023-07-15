


# /////////////////////////////

# این قطعه کد میاد به ازای هر کدوم از اعضای پارت اول یک عضو پارت دوم را میاره . میریزه تو خودش
# از اون به بعدش عضو بعدی پارت دو را میریزه توی اون لیست 
# تا اینکه همه عضو های پارت دوم با عضو اول ترکیب برداشتنبعد میره سراغ عضو بعدی پارت اول که بی باشه
#  . دوباره میاد عضو های پارت اپدوم را میریزه 

player1=[['a'],['b'], ['c'] ,['d']]
player2=['A','B','C' ,'D']

new=[]
for part in player1:
    for parts in player2:
        part.append(parts)
        print('part mishe ',part)

# دوتا نکته هستش. اول اینکه باید داخل لیست باشه پارت1 وگرنه ارور میده
# دومی ولی باید استرینگ خالی باشه وگرنه دومی را تو لیست میکنه

# part mishe  ['a', 'A']
# part mishe  ['a', 'A', 'B']
# part mishe  ['a', 'A', 'B', 'C']
# part mishe  ['a', 'A', 'B', 'C', 'D']
# part mishe  ['b', 'A']
# part mishe  ['b', 'A', 'B']
# part mishe  ['b', 'A', 'B', 'C']
# part mishe  ['b', 'A', 'B', 'C', 'D']
# part mishe  ['c', 'A']
# part mishe  ['c', 'A', 'B']
# part mishe  ['c', 'A', 'B', 'C']
# part mishe  ['c', 'A', 'B', 'C', 'D']
# part mishe  ['d', 'A']
# part mishe  ['d', 'A', 'B']
# part mishe  ['d', 'A', 'B', 'C']
# part mishe  ['d', 'A', 'B', 'C', 'D'] 



# /////////////////////////
# الان کدی میخوام که کد بالا هم: . 
# اولین خروجی فقط باشه  بطور تنها
# بعد بقیه عنصر ها بطور تنها 

# این کد این کار را انجام میده . میاد اولین عنصر پارت یک را دو به دو بطور تنها میزاره توی اون 

player1=[['a'],['b'], ['c'] ,['d']]
player2=['A','B','C' ,'D']

new=[]
for part in player1:
    for parts in player2:
        part.append(parts)
        print('part mishe ',part)
        new.append(part[:])
        print('new mishe' ,new)
        part.pop(-1)
        print('pop mishe')



# part mishe  ['a', 'A']
# new mishe [['a', 'A']]
# pop mishe
# part mishe  ['a', 'B']
# new mishe [['a', 'A'], ['a', 'B']]
# pop mishe
# part mishe  ['a', 'C']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C']]
# pop mishe
# part mishe  ['a', 'D']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D']]
# pop mishe
# part mishe  ['b', 'A']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A']]
# pop mishe
# part mishe  ['b', 'B']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B']]
# pop mishe
# part mishe  ['b', 'C']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C']]
# pop mishe
# part mishe  ['b', 'D']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D']]
# pop mishe
# part mishe  ['c', 'A']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A']]
# pop mishe
# part mishe  ['c', 'B']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B']]
# pop mishe
# part mishe  ['c', 'C']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B'], ['c', 'C']]
# pop mishe
# part mishe  ['c', 'D']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B'], ['c', 'C'], ['c', 'D']]
# pop mishe
# part mishe  ['d', 'A']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B'], ['c', 'C'], ['c', 'D'], ['d', 'A']]
# pop mishe
# part mishe  ['d', 'B']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B'], ['c', 'C'], ['c', 'D'], ['d', 'A'], ['d', 'B']]
# pop mishe
# part mishe  ['d', 'C']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B'], ['c', 'C'], ['c', 'D'], ['d', 'A'], ['d', 'B'], ['d', 'C']]
# pop mishe
# part mishe  ['d', 'D']
# new mishe [['a', 'A'], ['a', 'B'], ['a', 'C'], ['a', 'D'], ['b', 'A'], ['b', 'B'], ['b', 'C'], ['b', 'D'], ['c', 'A'], ['c', 'B'], ['c', 'C'], ['c', 'D'], ['d', 'A'], ['d', 'B'], ['d', 'C'], ['d', 'D']]
# pop mishe


# /////////////

# اگر فقط همین یک تکه را برششو نزاری . اونجوری بهم میریزه . یعنی میاد کل پارت را میزاره 

player1=[['a'],['b'], ['c'] ,['d']]
player2=['A','B','C' ,'D']

new=[]
for part in player1:
    for parts in player2:
        part.append(parts)
        print('part mishe ',part)
        new.append(part)
        print('new mishe' ,new)
        part.pop(-1)
        print('pop mishe')



# part mishe  ['a', 'A']
# new mishe [['a', 'A']]
# pop mishe
# part mishe  ['a', 'B']
# new mishe [['a', 'B'], ['a', 'B']]
# pop mishe
# part mishe  ['a', 'C']
# new mishe [['a', 'C'], ['a', 'C'], ['a', 'C']]
# pop mishe
# part mishe  ['a', 'D']
# new mishe [['a', 'D'], ['a', 'D'], ['a', 'D'], ['a', 'D']]
# pop mishe
# part mishe  ['b', 'A']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b', 'A']]
# pop mishe
# part mishe  ['b', 'B']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b', 'B'], ['b', 'B']]
# pop mishe
# part mishe  ['b', 'C']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b', 'C'], ['b', 'C'], ['b', 'C']]
# pop mishe
# part mishe  ['b', 'D']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b', 'D'], ['b', 'D'], ['b', 'D'], ['b', 'D']]
# pop mishe
# part mishe  ['c', 'A']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c', 'A']]
# pop mishe
# part mishe  ['c', 'B']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c', 'B'], ['c', 'B']]
# pop mishe
# part mishe  ['c', 'C']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c', 'C'], ['c', 'C'], ['c', 'C']]
# pop mishe
# part mishe  ['c', 'D']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c', 'D'], ['c', 'D'], ['c', 'D'], ['c', 'D']]
# pop mishe
# part mishe  ['d', 'A']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c'], ['c'], ['c'], ['c'], ['d', 'A']]
# pop mishe
# part mishe  ['d', 'B']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c'], ['c'], ['c'], ['c'], ['d', 'B'], ['d', 'B']]
# pop mishe
# part mishe  ['d', 'C']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c'], ['c'], ['c'], ['c'], ['d', 'C'], ['d', 'C'], ['d', 'C']]
# pop mishe
# part mishe  ['d', 'D']
# new mishe [['a'], ['a'], ['a'], ['a'], ['b'], ['b'], ['b'], ['b'], ['c'], ['c'], ['c'], ['c'], ['d', 'D'], ['d', 'D'], ['d', 'D'], ['d', 'D']]
# pop mishe


# ////////////////

# کدی میخوام که اولین عنصر را اولین عنصر  
# چفت کنه . و بعد بچرخه عوض کنه تا همه جایگشت هاش





# ///////////////////

# /////////////



# //////////


player1=[['a'],['b'], ['c'] ,['d']]
player2=['A','B','C' ,'D']

new=[]
for part in player1:
    for parts in player2:
        zipped= list(zip(part,parts))
        print(zipped)

# [('a', 'A')]
# [('a', 'B')]
# [('a', 'C')]
# [('a', 'D')]
# [('b', 'A')]
# [('b', 'B')]
# [('b', 'C')]
# [('b', 'D')]
# [('c', 'A')]
# [('c', 'B')]
# [('c', 'C')]
# [('c', 'D')]
# [('d', 'A')]
# [('d', 'B')]
# [('d', 'C')]
# [('d', 'D')]


# ///////////////

# //////////

# چهار حالا میخوام یه جور زیپ کنه که عنصر ها طوری بشن که
# اگر  ای کپیتال ای اومد بره روی بی کپیتال بی . .. و 
#  بار که این کار را کردبعد هر کدوم را یه بازی بنامیم  

# یعنی اینو 

# [('a', 'A')]
# [('a', 'B')]
# [('a', 'C')]
# [('a', 'D')]

# [('b', 'A')]
# [('b', 'B')]
# [('b', 'C')]
# [('b', 'D')]

# [('c', 'A')]
# [('c', 'B')]
# [('c', 'C')]
# [('c', 'D')]

# [('d', 'A')]
# [('d', 'B')]
# [('d', 'C')]
# [('d', 'D')]

# چجوری تبدیل کنم به :

# [('a', 'A')] [('b', 'B')] [('c', 'C')] [('d', 'D')]   عنصر اول اولی . دوم دومی سوم سومی وچهارم چهارمی 
# [('a', 'B')] [('b', 'A')]  [('c', 'D')]  [('d', 'C')]
# [('a', 'C')]
# [('a', 'D')]

# راه حل این باشه =  
# 1- همه را بیارم ای ها را به اسم ای بی ها را بی 
# بعد باید از هر کدوم دوباره زیپ کنم ولی اونی که کپیتال ای را داره را نگیره 
# چجوری بهش برنامه بدم وقتی دید بره بعدی . یعنی نه اولین عنصرش تکراری باشه نه دومیش 

# ////////

from itertools import permutations
l = list(permutations(range(1, 4)))
print(l)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 


# //////////////////

# Python function to print permutations of a given list
def permutation(lst):
    
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function
data = list('123')
for p in permutation(data):
    print (p)

# ['1', '2', '3']
# ['1', '3', '2']
# ['2', '1', '3']
# ['2', '3', '1']
# ['3', '1', '2']
# ['3', '2', '1']



# ////////////////

from itertools import permutations
l = list(pefrmutations(['A','B','C' ,'D']))
print(l)
# [('A', 'B', 'C', 'D'), ('A', 'B', 'D', 'C'), ('A', 'C', 'B', 'D'), ('A', 'C', 'D', 'B'), ('A', 'D', 'B', 'C'), ('A', 'D', 'C', 'B'), ('B', 'A', 'C', 'D'), ('B', 'A', 'D', 'C'), ('B', 'C', 'A', 'D'), ('B', 'C', 'D', 'A'), ('B', 'D', 'A', 'C'), ('B', 'D', 'C', 'A'), ('C', 'A', 'B', 'D'), ('C', 'A', 'D', 'B'), ('C', 'B', 'A', 'D'), ('C', 'B', 'D', 'A'), ('C', 'D',
# 'A', 'B'), ('C', 'D', 'B', 'A'), ('D', 'A', 'B', 'C'), ('D', 'A', 'C', 'B'), ('D', 'B', 'A', 'C'), ('D', 'B', 'C', 'A'), ('D', 'C', 'A', 'B'), ('D', 'C', 'B', 'A')]

# /////
# به کتابخانه ایترتولز 
