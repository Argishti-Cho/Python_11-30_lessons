# task 1
# ilegal = b, g 

# task 2 
# b => %

# task 3 
# g => from random import randint

# task 4 
# x = input("Enter name: ")
# y = input("Enter age: ")
# if 'Argi' in x and '33' in y:
#     print('You are in the list')
# else:
#     print("you're not in the list")

# task 5
# import math as m
# # 6x2 + 10x – 1 = 0
# # x = (10-m.sqrt(124))/12
# # x = (5+m.sqrt(31))/6
# a = 6
# b = 10 
# c = -1
# d = (b**2)-(4*a*c)
# if d > 0:
#     print(f'2 real roots discriminant = {d}')
# elif d == 0:
#     print(f'1 real root discriminant = {d}')
# else:
#     print(f'2 complex or negative roots discriminant = {d}')


# task 6 
# import math as m
# a = 15
# b = 18
# c = 20
# s = (a+b+c) /2
# area = m.sqrt(s * ((s-a) * (s-b) * (s-c)))
# print(round(area, 3))

# task 7
# import random as r

# options = ['rock', 'scissor', 'paper']
# pc = r.choice(options)
# user = input('Enter your choice rock, scissor or paper:  ').lower()
# if user == 'rock' and pc == 'scissor' or user == 'scissor' and pc == 'paper' or user == 'paper' and pc == 'rock':
#     print(f'You chose {user} and PC chose {pc} ')
#     print('Congrats, you Win !!! ')
# elif pc == 'rock' and user == 'scissor' or pc == 'scissor' and user == 'paper' or pc == 'paper' and user == 'rock':
#     print(f'PC chose {pc} you chose {user} ')
#     print('PC Win')
# elif pc == user:
#     print(f'drow try again')
# else:
#     print('Invalid Input ')

# task 8
# answer a and g

# task 9
# [1, 2, 3, 4]

# task 10
#  answer g

# task 11
#  answer b

# task 12
#  answer b

# task 13 (didn't get the question)
# answer b

# task 14
# for i in mylist.keys()
    # if i == 'name':
        # do soething
# task 15
# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# s = sorted(mydict, key=mydict.get,) [3:]
# print(s)

# task 16
# set.add('element')

# task 17
# set.discard(element)

# task 18
# set.isdisjoint() returns True if two sets don't have common or same items 

# task 19
# set1.issubset(set2) returns True if set1 items exists in set2 ex. set1 = {1, 2, 3} set2 = {4, 5, 7, 1, 9, 2, 3} = True

# task 20
# anser => git checkout name

# task 21
# lambda-ն անանուն ֆունկցիա է, կարողէ վերցնել բազմաթիվ արգումենտներ, բայց ունի միայն մեկ գործողություն

# task 22
# ֆունկցիան կոդի բլոկ է, որին տրվում է անուն և ակտիվամում է միայն անունը կանչելուց հետո, ընդունում է բազմաթիվ  / 
# արգումենտներ և գործողություններ։ Ֆունկցիյան կարող ենք օգտագործել մի բազմակի անգամներ և իմպորտ անել այլ ֆայլի /
# բայց տվյալ ռեպօզիտորիում։ 

# task 23
# ռեկուրսիան օգտագործվում է երբ ֆունկցիայի մեջ կանչում ենք տվյալ ֆունկցիան, լավագույն օրինակն է ֆիբոնաչիի թվերի ֆունկցիան

# task 24
# def product(mylist):
#     pr = 1
#     for i in mylist:
#         pr *= i
#     return pr

# print(product([1, 2, 3, 4, 5]))

# task 25
# def fact(n):
#     factorial_ = 1
#     for i in range(1, n+1):
#         factorial_ *= i
#     return factorial_
# print(fact(5))

# def fact_(n):
#     if n == 0 or n == 1:
#         return n
#     elif n < 0:
#         return f'can\'t be a negative number'
#     else:
#         return n * fact_(n-1)

# print(fact_(6))
