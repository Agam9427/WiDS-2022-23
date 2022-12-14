#   /**PYTHON QUICK NOTES FROM BASICS BITCHES**\

# Uncomment the part you want to run and then run the code for that specific part

# You'll waste your time if you try to study all the functions..Just google them when you need em.
# Understand the basic concepts instead and some imp functions


# # 1.First Code
# name=input("Hey!What's your name buddy\n")
# print("Hey " + name )

# #2.Fundamental Data Types
# int
# float
# bool
# str
# set
# list
# tuple
# dict
# None
# complex

# # you can also make custom data types using classes .Also you can download specialised data types from modules

# #3.int
# #integer number hota hai
# print(2+4)
# print(2/4)
# print(2*4)
# print(2**3)
# print(2-4)
# print(type(2))
# print(type(2+4))
# print(type(4/2))#This isn't int..Why?because the result of division is of float type

# #4.float(floating point number)
# print(type(2/4))
# print(type(8/2))
# print(4/2)
# #int+float=float ex-
# print(type(1))
# print(type(2.0))
# print(type(1+2.0))
# #But....
# print(8//2)
# print(type(8//2))#// makes output of division int

# #5.Algebra and math functions

# #math algebra
# print(2+4)#add
# print(2/4)#divide..ans is floating type
# print(2*4)#multiply
# print(2**3)#raised to the power
# print(5%2)#remainder
# print(2-4)#subtract

# #round(number,ndigits)
# print(round(5.355,2))
# print(round(11.56))#in case of no arguments,rounds off to int

# #abs()#absolute value
# print(abs(-3))

# #6.Operator Precedence
# #() > ** > *,/ > +,-
# print(50+4*3)

# #7.bin()
# #returns the binary representation of an integer as a string
# print(bin(69))
# print(int(bin(69),2))


# #8.Variables
# #its like a place to store your data..data as in int ya bool ya float ya string... any data type ...
# a=35
# b=35.05
# Name='Agam'
# print(Name)
# print(a+b)
# #variable names dont have spaces...no variable can start with a number..
# # variables cant be named similar to a few keywords.
# #Use _ instead of spaces
# a,b,c=3,4,5
# print(a)
# print(b,c)

# #9.Augmented assignment operator
# chutiya=10
# chutiya+=2 #(is equivalent to doing chutiya=chutiya+2)
# print(chutiya)
# chutiya-=2
# print(chutiya)
# chutiya*=2
# print(chutiya)
# chutiya**=2
# print(chutiya)

# #10.str
# # '' or " " or ''' ''' cn be used to denote string according to need
# #if u want to use ' in your sentence use "..ex-
# string1="Schrodinger's Douchebag"
# print(string1)
# #otherwise if you use ' to enclose your string, the compiler will get confused and will throw an error
# #''' is also used for long strings and multi lined strings
# string2='''Hi!
# My Name Is Agam!
# These are notes for quickly learning python '''
# print(string2)
# #Use \n for next line..\t for tab..
# string3='Hi\nMy Name Is Agam\n\tThanks'
# print(string3)
#     #String Addition(yss you can add them)
# first_name='bhenchod '
# last_name='sutta'
# print(first_name+last_name)#This is our department track btw lmao

# #11.Type Conversion
# a=100
# print(5+a)
# print(type(a))
# a=str(a)
# print(type(a))
# print('Hello ' + a)
# a=int(str(int(a)))
# print(type(a))

# 12.Escape Sequences
# I've already adressed this issue..Let's give it a look again..
# The string "OOf that "booty" is good" will throw an error ..How to overcome this?
# a="OOf That \"Booty\" Is Good"
# print(a)
# \t gives tab..note if you really want to print \t instead of using it, use \\t ...\n changes line..

# #13.Formatted Strings
# #in python3-
# name='Saksham'
# age=69
# print(f'Hi Guys, {name} Chutiya Hai aur {age} saal ka buddha hai')
# #in python2-
# print('Hi Guys, {} Chutiya Hai aur {} saal ka buddha hai'.format(name,str(age)))
# print('Hi Guys, {1} Chutiya Hai aur {0} saal ka buddha hai'.format(name,str(age)))
# print('Hi Guys, {new_name} Chutiya Hai aur {umr} saal ka buddha hai'.format(new_name='Prithvi',umr=70))
# #Complicated way..second wala..second method works in python3 too

# # 14.String as an array
# #name[start:stop:stepover]
# dank='Pancho Friday Aaaa!!!'
# print(dank[0])
# print(dank[2:5])
# print(dank[:])
# print(dank[3:])
# print(dank[:10])
# print(dank[-1])#negative indices..ulta chalta hai
# print(dank[-5:-1])
# print(dank[2:10:2])#leaves every second letter
# print(dank[::-1])#reverses the order

# # 15.Immutability
# ghoda='012345678'
# #ghoda[3]=9 will throw an error..you cannot change values of string by accessing each value..
# # you can re assign the value of the entire variable though
# #strings are immutable

# #16.len()
# print(len('Hi kaise ho'))
# sutta='loveYouGuys'
# print(sutta[0:len(sutta)])
# #more
# print(sutta.capitalize())
# print(sutta.find('Y'))
# print(sutta.replace('Guys','Bitches'))
# sutta=sutta.replace('Guys','Bitches')
# print(sutta)#This will print guys and not bitches..and trust me its not because the compiler was offended..remember a string is immutable
# sutta=sutta.replace('Guys','Bitches')
# print(sutta)#reassignment will print bitches

# #17. Booleans
# #True or False
# Econ_Best_Hai=True
# #1 denotes true and 0 denotes false
# a=1
# print(bool(a))
# a=5>2 #Boolean Statement
# print(a)
# a=3<1
# print(a)

# #18.List(like arrays)
# list1=[1,2,3,"Hello Bhai",True]
# print(list1)
# print(list1[3])
# #same as string..also can use :
# #can be changed
# list1[0]="Chutiya"
# print(list1[0:5])
# #IMPORTANT
# list2=['Delhi','Se','Hu',"BC"]
# list3=list2[0:4]
# print(list3)
# list3=list2#passes by reference...to pass by value, list3=list2[:]
# list3[0]="Kat Gaya Chumtiya?"
# print(list2)

# #19.Matrix(Multi Dimensional Arrays)
# matrix=[
#     [1,2,3],
#     [2,4,6],
#     [5,8,9],
#     [
#         ['First','Sub','Array'],
#         ['Second','Sub','Array']
#     ]
# ]
# print(type(matrix))#List type

# print(matrix[3][1][0][3])#prints o of 'Second'
# matrix[3][1][0]='Third'
# print(matrix[3][1][0][3])

# #20.List Methods(A BIG ONE!!!!!)

# sl=['Grocery','Condoms','Toilet papers','Daaru']
# #add to the end
# sl.append('Sutta')
# print(sl)


# #NOTE
# #nl=sl.append('Sutta') will add nothing to nl..
# # append is a void type function..
# # it returns no value just changes the list..

# #add anywhere(.insert(index,object))(NOTE-This has a return type of void..So it returns a list..)
# sl=['Grocery','Condoms','Toilet papers','Daaru','Sutta']
# sl.insert(3,'Ganja')
# print(sl)

# #add a list
# sl=['Grocery','Condoms','Toilet papers','Ganja',Daaru','Sutta']
# sl.extend(['ab bol','bsdk'])
# print(sl)

# #removing
#     #1.pop
# sl=['Grocery','Condoms','Toilet papers','Ganja',Daaru','Sutta','ab bol','bsdk']
# sl.pop()#deletes the last element
# print(sl)
# sl.pop(0)#removes 0th item
# print(sl)
# #NOTE-pop function returns whatever you just removed

# #.remove(i) removes element with entry as i once..ie the first occurence(void return)
# sl.remove('Condoms')
# print(sl)
# #clear(void return type)removes everything
# sl.clear()
# print(sl)


# sl=['Grocery','Condoms','Toilet papers','Daaru',1,1,2,3,4]

# #(.index(Kya dhundhna hai vo daalo idhar,start looking from this index,stop looking before this index)
# print(sl.index('Daaru'))
# # print(sl.index('Daaru',0,3)) #Throws error..mtlb 3 se pehle to nahi hai daaru
# print(sl.index('Daaru',0,4))

#     #EASY AND IMP
#     #{value} in {list}
#     #returns bool
# sl=['Grocery','Condoms','Toilet papers','Daaru',1,1,2,3,4]
# print('Daaru' in sl)
# print('x' in 'Chhoti Bachhi Ho Kya')

# #count(gives number of times an item repeats)
# print(sl.count(1))

# #sort(void return type....)(sorts the list yaayyyy)
# #in case of strings-alphabetically
# #in case of numbers, increasing order me
# #make the list either all numbers or all strings
# sl=['Grocery','Condoms','Toilet papers','Daaru']
# sl.sort()
# print(sl)

# #sorted(return type list)(sorted takes input by value not by reference..)
# # in simple bhasha...ye list ki nayi copy bnake usme pange krega
# sl=['Grocery','Condoms','Toilet papers','Daaru']
# print(sorted(sl))
# print(sl)

# # #copying..one way is to do nl=sl[:]
# sl=['Grocery','Condoms','Toilet papers','Daaru']
# nl=sl.copy()#passes by value
# nl.clear()
# print(nl)
# print(sl)

# #reverse
# sl.reverse()
# print(sl)


# #21.Useful List tricks
# sl=[1,2,3,6,4,7,3,3,5,5,4,8,9,1,2,44,65,34,23,12,89]

#     #1.len command
# print(len(sl))
#     #2.get dec order without changing the actual list
# print(sorted(sl)[::-1])
# print(sl)
#     #3.range
# print(list(range(0,100)))
# print(list(range(100)))
#     #4.join(its actually a string method)(return type void again)
# new=' chutiyo '.join(['Hi','I\'m','Agam','Hahaha'])
# print(new)


# #22.List Unpacking
# a,b,c, *other,d=[1,2,3,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# #23. None
# #absence of value
# weapons=None
# print(weapons)

# #24.Dict(Dictionary) & Dictionary methods
# #key:value
# #lists can have dictionaries too
# #dictionaries have no order..lists have..order here refers to how lists have indexes
# dictionary={
#     'Econ':{
#         'Saksham':'Amrican Hardworker',
#         'Primthvi':'Typical Jee Wala Bachha',
#         'Aastha':'CR',
#         'Anisha':'Chhoti Bachhi Ho Kya',
#         'Agam':'Mai To Nalayak Hu'
#     },
#     'Mech':{
#         'People':''' Sab Chumtiye Screw Bnaenge'''
#     },
#     'Elec':{
#         'People':'Sab Saanp Hain'
#     },
#     'Hi':'Beta'
# }
# #keys should be immutable..so lists can not be keys..tuples can be keys though
# #adding same key will overrite the previous one
# print(dictionary)
# print(dictionary['Hi'])
# print(dictionary['Econ']['Aastha'])
# print(dictionary.keys())
# print(dictionary['Econ'].keys())
# print(dictionary.values())
# print(dictionary['Econ'].values())
# print(dictionary.get('CSE'))#returns none..unlike the above way of accessing values which throws an error
# print(dictionary.get('CSE','Nerds'))#if cse exists it'll get it..otherwise will return the defaukt value we've set..in this case it's 'Nerds'..wont change the dict
# #another way to create a dictionary
# #var_name=dict(key='value')(key is not an expression here)
# bb101=dict(ChutiyaLevel='Boht Zyada')
# print(bb101)

#25.More Methods for dict
sample={
    'basket':[1,2,3],
    'greet':'hello',
    'age':{
        'Hey':'Siri'
    }
}
# print('basket' in sample)#looks at keys
# print('hello' in sample.values())#looks at values only
# print('Hey' in sample.items())#searches the first keys and values only
# print(1 in sample.items())#searches the first keys and values only
# print(1 in sample['basket'])
# #print(sample.clear())  Clears the dictionary
# new_sample=sample.copy()
# new_sample.clear()
# print(new_sample)
# print(sample)
# #pop command(returns value of what you removed)
# print(sample.pop('age'))
# print(sample)
# print(sample.popitem())#pops anything randomly
# print(sample)

# #update(return type none)(add or edit)
# sample={
#     'basket':[1,2,3],
#     'greet':'hello',
#     'age':{
#         'Hey':'Siri'
#     }
# }
# print(sample.update({'age':55}))#returns none
# print(sample.items())#returns key and value pair as a tuple
# print(sample)
# sample.update({'Newage':{'Hey':'Siri'}})
# print(sample)

# #26.Tuples(Immutable Lists)
# tuple1=('Sup','Bitches',420)
# print(tuple1[1])
# #tuple[1]='Hi'(this cant be done)
# print('Bitches' in tuple1)
# #cant be sorted or reversed..cant be changed in any way..However a tuple can be copied onto list and then the list can be changed
# example=list(tuple1)
# example[1]='Lads'
# print(example)

# print(tuple1[0:2])#all this can be done though


# #27.More on tuples
# base=(1,2,3,4,5,6,7,7,7)
# x,y,z,*other,a=base
# print(x)
# print(y)
# print(z)
# print(a)
# print(other)
# print(type(other))#returns as a list
# print(base.count(7))#How many 7's?
# print(base.index(5))#index of first ocuurence of 5?
# print(len(base))

# #28.Sets
# #unique objects..unordered like dict..i.e. no indexes
# set1={1,2,3,4,5,5,5,5,5,0,6,4,3}
# print(set1)#while printing it automatically makes it unique..3 and 3.0 are same in set
# #print(set1[0]) will throw an error
# #adding elements
# set1.add(3.5)
# print(set1)
# set1.add('Hi')
# print(set1)
# #more methods
# print(len(set1))#counts just one 5.
# print(1.0 in set1)#remember 1 and 1.0 are same
# #sets can be copied using copy command unlike tuples
# new=set1.copy()
# new.clear()
# print(new)
# print(set1)

#29.Imp methods on set
set_a={1,2,3,4,5,6,7}
set_b={4,5,6,7,8,9,10}
set_c={1,6}

    #.difference(firstset.difference(secondset))
print(set_a.difference(set_b))

    #.discard
set_a.discard(7)
print(set_a)

    #difference.update()
set_a.difference_update(set_b)#removes all setb elements from seta
print(set_a)

    #.intersection()
set_a={1,2,3,4,5,6,7}
print(set_a.intersection(set_b))
print(set_a.intersection(set_b,set_c))

    # .isdisjoint()
print(set_a.isdisjoint(set_b))#If intersection>0...this gives false..

    # .issubset()
print(set_a.issubset(set_b))#are all elements of a in b.
print(set_c.issubset(set_a))

    # .issuperset()
print(set_a.issuperset(set_c))#all elements of c in a?

    # .union()
print(set_a.union(set_b))
print(set_a)
print(set_b)


####   NOTE- NO NEED TO MEMORIZE EVERYTHING>>JUST UNDERSTAND>>>BAAD ME GOOGLE KRLENA   ###

#######      BORING PART ENDS HERE!!!!AB EVERYTHING WILL BE INTERESTING      #######

####      PYTHON ME INDENTATION MATTERS ...Indentations is imp to show heirarchy..     ####

# #30.Conditional Logic
# attendance=True
# passed=True
# cheating=False
#     #if
# if attendance:#if attendance is true to aage ka loop chalega..indentation ka dhyan rakho..
#     print("Tu Lecure Bhi Attend Karta Hai??")
# if passed:
#     print('Tomper Saala')
# if passed and attendance:
#     print('Maaro Saale Ko')

#     #else
# if cheating:
#     print('Chad')
# else:
#     print('Chutiya')

#     #elif(if galat ho to elif..)
# attendance=False
# if attendance:
#     print('Waah')
# elif passed:
#     print('Jug Jug Jio')
# else:
#     'Bhakk'

# #31.Truthy and Falsy
#     #Truthy values
# print(bool('Hi'))
# print(bool(5))
#     #Falsy
# print(bool(''))
# print(bool(0))
# print(bool(None))#Used often..
# #CHECK FALSY VALUES ON WEB AGAR DEKHNI HAI TO

# #32.Ternary Operator
# # condition_if_true if condition else condition_if_else
# #example-
# is_chutiya=True
# can_do_chutiyapa='chutiyapa Kar sakte ho' if is_chutiya else "nahi kar sakte "
# print(can_do_chutiyapa)
# is_chutiya=False
# can_do_chutiyapa='chutiyapa Kar sakte ho' if is_chutiya else "nahi kar sakte chutiyapa"
# print(can_do_chutiyapa)

# #33.Short Circuiting
# is_chutiya=True
# is_friend=True
# if is_chutiya or is_friend:
#     print('bsdk')
# #if statement gets short circuited after is_chutiya as its true..so or here is more efficient than and....

# #34.Logical Operators
#     #and
#     # or
#     # >
#     # <
#     # ==   #(remember =is used to assign..so we use double =)
#     # !=   #(not equal to)
#     # not
# print(not True)
# print('a'>'b')#gives false
# print('a'>'A')#gives true
# #WHY?look at ascii values


# #35.is vs ==
# print(True==1)
# print(bool('')==0)
# print(bool([])==0)
# print(10==10.0)
# print([]==[])

# print(True is 1)
# print(bool('') is 0)
# print(bool([]) is 0)
# print(10 is 10.0)
# print([]is[])
# #data structures are stored in new places evrytime...is checks if python stores a at the same place as b by default..
# #if a=5 and b=5..a is b will give true..a and ba re stored in different spaces but the valye that python picks up..ie 5..is picked from a common space
# a=100
# b=50*2
# print(a is b)
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)#gives false

# #36.For Loops
# for i in [1,2,3,4,5,6]:
#     print(i)
# print(i)#i has value 6 after the loop
# #prints every element
#     #nesting
# for i in ['Hi','Madam']:
#     for j in[1,2,3]:
#         for k in{2,3,4}:
#             print(i,j,k)
# dictionary={
#     'Econ':{
#         'Saksham':'Amrican Hardworker',
#         'Primthvi':'Typical Jee Wala Bachha',
#         'Aastha':'CR',
#         'Anisha':'Chhoti Bachhi Ho Kya',
#         'Agam':'Mai To Nalayak Hu'
#     },
#     'Mech':{
#         'People':''' Sab Chumtiye Screw Bnaenge'''
#     },
#     'Elec':{
#         'People':'Sab Saanp Hain'
#     },
#     'Hi':'Beta'
# }
# for i in dictionary:
#     print(i)
#     #prints just the keys


# for i in dictionary.items():
#     print(i)
#     #yay prints everything

# for i in dictionary.values():
#     print(i)
#     #prints values

# #IMP TRICK
# for i in dictionary.items():
#     keys,values,*others=i
#     print(keys,values,*others)
#     #yay prints everything but doesnt return key value pair as a tuple..good stuff

# #ORRR DO THIS

# for keys,values,*subdict in dictionary.items():
#     print(keys,values,subdict)

# 37.Iterable
# can be list set string tuple dictionary,.....any collection of items..so we cant iterate over integers
# iterating- ekek krke har item check kro
# set1={1,1,2,2,3,3,4,4}
# for i in set1:
#     print(i)

# #38.range()
# for i in range(0,5):
#     print(i)

# for i in range(0,5,2):#every second number is printed
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range (2):
#     print(list(range(2,16,2)))

# #39.enumerate()
# for i in enumerate('Helloooo'):
#     print(i)
# for i,j in enumerate('Helloooo'):
#     print(i,j)


# #40.while
# #while condition_is_true:
#     #do this
# i=0
# while i<5:
#     print(i)
#     i+=1
# else:
#     print('Done Vro')

# i=0

# while i<5:
#     print(i)
#     i+=1
#     break
# else:
#     print('Done Vro')#this else won't be printed

# 41.break ,continue,pass
# used in for and while both
# continue=starts the loop again
# break=breaks the loop
# pass-does nothing lol

# #42.Functions
# def namaste_bolo():
#     print('Namaste')

# def tree_banao():
#     #Exercise!
#     picture=[
#         [0,0,0,1,0,0,0],
#         [0,0,1,1,1,0,0],
#         [0,1,1,1,1,1,0],
#         [1,1,1,1,1,1,1],
#         [0,0,0,1,0,0,0],
#         [0,0,0,1,0,0,0]
#     ]
#     for i in picture:
#         for j in i:
#             if j==0:
#                 print(' ',end='')
#             else:
#                 print('*',end='')
#         print('\n')


# namaste_bolo()
# tree_banao()

# #43.parameters and arguments

# def say_hello(name,emoji):#these two are parameters
#     print(f'helloooooo {name}{emoji} ')

# #positional arguments
# say_hello('Agam',':)')

# #keyword arguments
# say_hello(emoji=':)',name='Beta')

# #default parameters-when no argument given..uses default value
# def say_hello(name='Agam',emoji=":P"):#these two are parameters
#     print(f'helloooooo {name}{emoji} ')

# say_hello()


# #44.return
# def sum(n1,n2):
#     return n1+n2


# print(sum(4,5))
# print(sum('Agam',str(5)))
# print(sum('Lauda ',sum('Ka ','Sarkar ')))

# #return types can be of an datat type..or even None(void )..return exits the functionwe're in.
# # .uske baadkuchh likhoge us fn me to nhi chlega

# def mult(n1,n2):
#     def mult2(n1,n2):
#         return n1*n2
#     return mult2


# multiply=mult(10,5)#multiply stores mult2 function
# print(type(multiply))
# print(multiply)
# print(multiply(10,20))


# 45.Methods vs functions
# methods are owned by a data type..functions work independently...


# #46.Docstrings#while using the function you'll see info about it
# from cgi import test


# def hi(a):
#     '''
#     This fn prints a
#     '''
#     print(a)
#     return


# hi('Vro')
# # help(hi)
# print(hi.__doc__)


# #47.*args **kwargs
# #args exists as tuple, kwargs as dictionary
# def summmm(*args,**kwargs):
#     print(args)#args is a tuple inside this fn
#     print(*args)#we convert it into elements
#     print(kwargs.values())
#     return sum(args)

# print(summmm(1,2,3,4,5,6,7,8,9,beta="sweater pehno",a=5))
# #rule- params,args,default params,**kwargs


# #48.Scope and Scope Rules
# #scope- what variables can I access
# a=1
# def confusion():
#     a=5#this is different from the a above...The function creates a new variable a and destroys it after returning a value
#     return a

# print(a)
# print(confusion())
# print(a)

# #if we didn't define a in the function,the function would have printed 1..we can return the global variable but canniot change it simply.

# # General Rule-
# # a) Start withlocal variable
# # b)Then check Parent Local
# # c)Check for a Global variable
# # d)Built in python

# #Paramters are local variables..What if you want to acces a global one which has the same name?

# total=0

# #def count():
# #    total+=1
# #    return total
# #print(count())
# #this throws an error

# total=0
# def count():
#     global total
#     total+=1
#     return total

# count()
# count()
# print(count())


# #49.nonlocal
# #accesses parent local

# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner:",x)

#     inner()
#     print("outer:",x)

# outer()

# #50.map()
# #makes a new mapping
# #lets say you have to do operation on a vector..say multiply it by 2.

# from cmath import sqrt


# vT=[1,2,3]#transpose of your column vector

# def multiply_by2(item):
#     return item*2

# print(type(map(multiply_by2,vT)))#no need to write multiply_by2()..remember we're not calling the function..we're just supplying it.
# print(list(map(multiply_by2,vT)))
# print(vT)#vT hasn't changed


# #51.filter()
# #filters the collection

# vT=[1,2,3]
# def only_odd(item):
#     return item%2!=0

# print(list(filter(only_odd,vT)))

# #52.zip
# #makes  tuples joining ith entries..
# vector1=[1,2,4]
# vector2=[2,3,8]
# print(list(zip(vector1,vector2)))

# def magnitude(v1,v2):
#     return sqrt(sum([(x1-x2)**2 for x1,x2 in zip(v1,v2)]))

# print(magnitude(vector1,vector2))

# #53.reduce(function,data,initial)
# #gives a list
# #rolling computations..

# from functools import reduce
# vT=[1,2,3]
# def accumulator(acc,item):
#     print(acc,item)
#     print(f"Setting acc to {acc+item}")
#     return acc+item

# print(reduce(accumulator,vT,2))#setting the initial value to 2

# #54.List Comprehensions
# list1=[char for char in 'Hello']
# list2=[number for number in range(0,10)]
# list3=[number*2 for number in range(0,10)]
# list4=[number*2 for number in range(0,10) if number%2==0]
# print(list1)
# print(list2)
# print(list3)
# print(list4)

# #55.set and dict comprehensions
# set1={char for char in 'Hello'}
# set2={number for number in range(0,10)}
# set3={number*2 for number in range(0,10)}
# set4={number*2 for number in range(0,10) if number%2==0}
# print(set1)
# print(set2)
# print(set3)
# print(set4)

# username=['Agam','Anushka','Aastha','Arpit','Aashish']
# password=[50,12,23,34,56]
# my_dict={key:value**2 for key,value in zip(username,password) if value!=12}

# print(my_dict)

# #Q.Make a list of duplicating elements
# some_list=['a','b','c','b','f','c']
# duplicates=list({char for char in some_list if some_list.count(char)>1})
# print(duplicates)

# #56.Modules..
# #attaching another .py file..
# import pattern
# print(pattern)
# pattern.make_tree()

# 57.Packages
# modules are files..packaages are a bundle of modules...simply put,folder hai bc.
# How to import?
#import package.module

# #58.Random Module
# import random
# randomno=random.randint(1,200)
# print(randomno)

# #59.File I/O
# #make any .txt file name agam
# file=open('agam.txt','r')#.r specifies read only mode..no argument also makes read only..
# data=file.read()#supplying int arguments will read that many characters
# print(data)
# file.close()
# file=open('agam.txt','r')
# line=file.readline()#reads first line
# print(line)
# line=file.readline()#reads second line
# print(line)
# file.close()

# #60.Writing Files
# f=open('another.txt','w')
# f.write('OOOOf')
# f.close()
# #'a' to append material and use command .append()

# #61.using with
# with open('agam.txt','r') as f:
#     data=f.read()#the file closes on its own after this
# print(data)

# BASICS END HERE
# New way of prgramming
# OBJECT ORIENTED PROGRAMMING

# #62.Class(It's basically a template)
# class RailwayForm:
#     formType="Railway Form"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# agamsapplication=RailwayForm()
# agamsapplication.name = "Agam"
# agamsapplication.train = "Rajdhani"
# agamsapplication.printData()

# #can't explain it enough..It becomes natural with practice..

# ##  Nouns        ----->   Class             ----->      Employee
# ##  Adjectives   ----->   Attributes        ----->      Name,Age,Salary
# ##  Verbs        ----->   Methods           ----->      getSalary(),increment()

# #63.Class Attribute
# class Employee:
#     Company="Google"
#     Salary=20,000

# Agam=Employee()
# Aryan=Employee()
# print(Agam.Company)
# print(Aryan.Company)
# Aryan.Company="Bittu Tikki Wala"
# print(Aryan.Company)
# Agam.leaves_per_month=32
# Aryan.leaves_per_month=7

# #64.self parameter
# class Employee:
#     company="Google"
#     def getSalary(self):
#         print(f"Salary for {self.name} working in {self.company} is {self.salary}")

# agam=Employee()
# agam.name="Agam"
# agam.salary=20000
# agam.getSalary()
# #This line are actually equivalent to Employee.getSalary(agam)..so we're giving an argument self....self refers to agam..

# 65.Static Method
# used of you want to create a fn not specific to object
# class Employee:
#     company="Google"
#     def getSalary(self):
#         print(f"Salary for {self.name} working in {self.company} is {self.salary}")

#     @staticmethod#This is a decorator
#     def greet():
#         print(f"Good Morning")

# agam=Employee()
# agam.name="Agam"
# agam.salary=20000
# agam.greet()

# #66.Constructor
# #__init__()
# #takes self argument and can take more
# class Employee:
#     company="Google"

#     def __init__(self):
#         print("Constructor prints This")

#     def getSalary(self):
#         print(f"Salary for {self.name} working in {self.company} is {self.salary}")

#     @staticmethod#This is a decorator
#     def greet():
#         print(f"Good Morning")

# agam=Employee()
# #init constructor prints ..this means on creating any object,constructor is called

# #67.Inheritance
# #Creating child classes from parent classes
# #Single Inheritance-
# class Employee:
#     company ="Google"

#     def showDetails(self):
#         print("This is an employee")


# class Programmer(Employee):
#     language="Python"

#     def getanguage(self):
#         print(f"The language is {self.language}")

# agam=Employee()
# aman=Programmer()
# agam.showDetails()
# aman.showDetails()


# #We can use methods and attributes of Employee in Programmer object ...and also overrite it if we want..
# #Multiple Inheritance-
# class Employee:
#     company ="Google"

#     def showDetails(self):
#         print("This is an employee")

# class Freelancer:
#     company="Fiverr"


# class Programmer(Employee,Freelancer):#Employee as written first is more trusted parent
#     language="Python"

#     def getanguage(self):
#         print(f"The language is {self.language}")

# agam=Employee()
# aman=Programmer()
# agam.showDetails()
# print(aman.company)

# #Multilevel Inheritance
# class Person:
#     sex="Male"
#     living="True"


# class Employee(Person):
#     company ="Google"
#     living="Truth"

#     def showDetails(self):
#         print("This is an employee")


# class Programmer(Employee):
#     language="Python"

#     def getLanguage(self):
#         print(f"The language is {self.language}")


# p=Person()
# e=Employee()
# pr=Programmer()
# print(pr.living)#prints living of itself..if it does not exist then just upar wala parent jiska exist kre..


# #68.Super() method

# class Person:
#     sex="Male"
#     living="True"
#     def showDetails(self):
#         print("In Person Class")
#         print("This is a person")
#         print("Going to Employee Class")


# class Employee(Person):
#     company ="Google"
#     living="Truth"

#     def showDetails(self):
#         print("In Employee Class")
#         print("Going to Person Class")
#         super().showDetails()

#         print("In Employee Class")
#         print("Printing Employee details")
#         print("Going to Programmer class now")


# class Programmer(Employee):
#     language="Python"

#     def getLanguage(self):
#         print("Going to Employee class now")
#         super().showDetails()
#         print("In Programmer Class now")
#         print(f"The language is {self.language}")


# agam=Programmer()
# agam.getLanguage()

# #69.Class Methods
# class Employee:
#     company = "Camel"
#     salary = 100
#     location = "Delhi"

#     # def changeSalary(self, sal):
#     #     self.__class__.salary = sal

#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal

# e = Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employee.salary)

# #70.Property Decorator(getter)
# class Employee:
#     company="Sippline"
#     salary=50
#     bonus=10

#     @property
#     def totalSalary(self):
#         return self.salary +self.bonus


# e= Employee()
# print(e.totalSalary)#This is not a function .we are not using ()..
# #What if you want to change the total salary?

# #71.@.getters and @.setters
# class Employee:
#     company="Sippline"
#     salary=50
#     bonus=10

#     @property
#     def totalSalary(self):
#         return self.salary +self.bonus

#     @totalSalary.setter
#     def totalSalary(self,val):#val total salary ka argument hai..apne aap fill ho jaega
#         self.bonus=val - self.salary

# e= Employee()
# print(e.totalSalary)
# e.totalSalary=80
# print(e.salary)
# print(e.bonus)


# #72.Operator Overloading
# class Number:
#     def __init__(self,num):
#         self.num=num

#     def __add__(self,num2):
#         print("Let's add")
#         return self.num*num2.num

# n1=Number(4)
# n2=Number(2)
# print(n1+n2)

# class Vector:
#     def __init__(self,x,y,z):
#         self.vec=[x,y,z]

#     def __add__(self,v2):
#         return [(x1+x2) for x1,x2 in zip(self.vec,v2.vec)]

# v1=Vector(1,2,3)
# v2=Vector(2,3,4)
# print(v1+v2)


# #73. More dunder methods
# class Vector:
#     def __init__(self,x,y,z):
#         self.vec=[x,y,z]

#     def __add__(self,v2):
#         return [(x1+x2) for x1,x2 in zip(self.vec,v2.vec)]

#     def __str__(self):
#         return f"The vector is: {self.vec}"

#     def __len__(self):
#         return  len(self.vec)

# v1=Vector(1,2,3)
# v2=Vector(2,3,4)
# print(v1)
# print(v2)
# print(len(v1))

########OOP ENDSS!!!##########


###################################OPTIONAL TOPICS##########################################


# #74.try
#        #try------->executes
#        #except------->deals with error
#        #else--------->executes if no error in try
#        #finally------>executes hamesha..even if program exit kro except me
# while True:
#     print("press q to quit")
#     a=input("enter a number: ")
#     if(a=='q'):
#         break
#     try:
#         a=int(a)
#         if a>6:
#             print("you entered a number greater than 6")
#     except Exception as e:
#         print(e)
#     #agar user kuchh aur input krta hai jaise malo agam input krdiya..to game crash na ho ..btae hame ki kya error kra hai..

# #Handling different errors
# try:
#     a = int(input("Enter a number: "))
#     c = 1/a
#     print(c)

# except ValueError :
#     print("Please Enter a valid value")

# except ZeroDivisionError :
#     print("Make sure you are not dividing by 0")

# print("Thanks for using this code!")

# #Raising Exceptions#khud error bnao

# def increment(num):
#     try:
#         return int(num) + 1
#     except:
#         raise ValueError("This is not good - Beta")

# a = increment('df364')
# print(a)

# #try with else
# #koi error na ae to else bhi execute hoga
# try:
#     i = int(input("Enter a number: "))
#     c = 1/i
# except Exception as e:
#     print(e)
# else:
#     print("We were successful")

# #try except finally

# while (True):
#     try:
#         i = int(input("Enter a number: "))
#         c = 1/i
#     except Exception as e:
#         print(e)
#         exit()

#     else:
#         print("marja")

#     finally:
#         print("We are done")

#     print("Thanks for using the program")

# #75.if __name()=="__main__"
# if __name__=="__main__":
#     print("Hi")
#     #agar ye module kahi import kra to ye run nahi hoga ab
# print(__name__)


# # 76.Virtual Environment
# # installation- pip install virtualenv
# # create a new , parallely running environment- virtualenv agamenv
# # folder create hoga
# # activate(formac)- source agamenv/bin/activate
# # install modules..like ...pip install flask...ye sb virtual env me hoga..
# # to deactivate..- deactivate likho

# pip freeze
#sb modules bta dega..

# #77.lamnda functions
# # def func(a):
# #     return a+5

# func = lambda a: a+5
# square = lambda x: x*x
# sum = lambda a, b, c: a+b+c

# x = 3
# print(func(x)) # Prints 8
# print(square(x)) # Prints 9
# print(sum(x, 1, 2)) # Prints 6


###########************PYTHON HOGAYIIIIII CONGRATSSSSS!!!!!!************#############

# ## Simple Library
# class Library:
#     def __init__(self, listOfBooks):
#         self.books = listOfBooks

#     def displayAvailableBooks(self):
#         print("Books present in this library are: ")
#         for book in self.books: 
#             print(" *" + book)
    
#     def borrowBook(self, bookName):
#         if bookName in self.books:
#             print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
#             self.books.remove(bookName)
#             return True
#         else:
#             print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
#             return False

#     def returnBook(self, bookName):
#         self.books.append(bookName)
#         print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

# class Student: 
#     def requestBook(self):
#         self.book = input("Enter the name of the book you want to borrow: ")
#         return self.book

#     def returnBook(self):
#         self.book = input("Enter the name of the book you want to return: ")
#         return self.book
         

# if __name__ == "__main__":
#     centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
#     student = Student()
#     # centraLibrary.displayAvailableBooks()
#     while(True):
#         welcomeMsg = '''\n ====== Welcome to Central Library ======
#         Please choose an option:
#         1. List all the books
#         2. Request a book
#         3. Add/Return a book
#         4. Exit the Library
#         '''
#         print(welcomeMsg)
#         a = int(input("Enter a choice: "))
#         if a == 1:
#             centraLibrary.displayAvailableBooks()
#         elif a == 2:
#             centraLibrary.borrowBook(student.requestBook())
#         elif a == 3:
#             centraLibrary.returnBook(student.returnBook())
#         elif a == 4:
#             print("Thanks for choosing Central Library. Have a great day ahead!")
#             exit()
#         else:
#             print("Invalid Choice!")

        

a=int(input())
b=int(input())

print(a+b)

