# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:05:26 2018

@author: Binoy
"""

# IF, ELIF, ELSE LOOP

print("Please enter your User Name")
myname=input()
if myname =='Binoy':
    print('Hi ' + myname + ' Welcome Back')
elif myname == 'Admin':
    print('You are logging in as ' + myname)
else:
    print('Invalid User Name, Access Denied')


# WHILE LOOP

count = 0
if count < 5:
    print('Hello, world.')
count = count + 1


count = 1
while (count <= 10):
    print ('The count is:', count)
    count = count + 1

print ("Good bye!")

myname=' '

while myname != 'Binoy':
    print('Please Enter Your Name')
    myname=input()

print('Thank You!')




while True:
    print('Please type your name.')
    name = input()
    if name == 'Binoy':
        break

print('Thank you! ' + name)



test=''
while test != 'Binoy':
    print('Please Enter your Name')
    test=input()

print('Thank you '+test)





while True:
    print('Please Enter your Name')
    test=input()
    if test=='Binoy':
        break

print('Thank you')



#Continue Loop

while True:
    print('Who Are You:')
    mname=input()
    if mname != 'Binoy':
        continue
    
    print('Hello ' + mname + ' Whats your Password? ( Hint: Its a Fish )')
    password=input()
    if password=='Swordfish':
        break
    
print('Access Granted')
































