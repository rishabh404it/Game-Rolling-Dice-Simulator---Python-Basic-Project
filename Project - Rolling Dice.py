from time import *
import random

print('""Welcome to Rolling Dice Stimulator""')
sleep(2)
print('Are you ready ? Lets Play !')
sleep(2)
print('GAME RULES : YOU WILL BE PROVIDED WITH 2 DICE & YOU HAVE TO ROLL THEM TO GET THE TARGET NUMBER')
sleep(3)
print('IF YOU GET THE TARGET NUMBER , YOU  WILL WIN')
sleep(3)
print('IF YOU DONT GET THE TARGET NUMBER, YOU WILL LOSE')
sleep(3)
print('REMEMBER THAT YOU WILL BE GIVEN 3 ATTEMPTS TO WIN THE GAME')
sleep(3)
print('WISH YOU GOOD LUCK !')
sleep(4)
z=random.randint(2,12)
print('YOU HAVE TO GET',z,'To WIN THE GAME')
sleep(0.5)
input('Press the Enter button to start Rolling the Dice : ')
print('Rolling the first Dice')
sleep(2)
x=random.randint(1,6)
print('You got value of 1st die : ',x)
sleep(1)
print('Now Rolling the second Dice')
y=random.randint(1,6)
print('You got value of 2nd die : ',y)
c=x+y
if x+y==z:
    print('Congo You Got : ',z)
    print('YOU WON')
else:print('Oh No You Got : ',c)
print('YOU LOST')
sleep(2)
print('You have 2 more attempts left')
sleep(2)
print(input('Lets start again Press the Enter key to roll the dice again : '))
print('Rolling the first Dice')
sleep(2)
a=random.randint(1,6)
print('You got value of 1st die : ',a)
sleep(2)
print('Now Rolling the second Dice')
sleep(2)
b=random.randint(1,6)
print('You got value of 2nd die : ',b)
sleep(2)
d=a+b
if a+b==z:
    print('Congo You Got',z)
    sleep(2)
    print('YOU WIN !')
else:print('Oh no You Got',d)
sleep(2)
print('YOU LOST')
print('You have 1 more attempt left. This is your last attempt. Good Luck !')
sleep(2)
print(input('Lets start again Press the Enter key to roll the dice again : '))
print('Rolling the first Dice')
sleep(2)
e=random.randint(1,6)
print('You got value of 1st die : ',e)
sleep(2)
print('Now Rolling the second Dice')
sleep(2)
f=random.randint(1,6)
print('You got value of 2nd die : ',f)
sleep(2)
g=e+f
if e+f==z:
    print('Congo You Got',z)
    sleep(2)
    print('YOU WIN !')
else:print('Oh no You Got',g)
sleep(2)
print('SADLY YOU LOST THE GAME BUDDY')
sleep(2)
while True :
   i = input('Do you wish play again ? y/n')
   if i == 'y':
       z = random.randint(2, 12)
       print('YOU HAVE TO GET',z,'To WIN THE GAME')
       sleep(0.5)
       input('Press the Enter button to start Rolling the Dice : ')
       print('Rolling the first Dice')
       sleep(2)
       x = random.randint(1, 6)
       print('You got value of 1st die : ', x)
       sleep(1)
       print('Now Rolling the second Dice')
       y = random.randint(1, 6)
       sleep(1)
       print('You got value of 2nd die : ', y)
       sleep(1)
       c = x + y
       if x + y == z:
           print('Congo You Got : ', z)
           sleep(1)
           print('YOU WON')
       else:
           print('Oh No You Got : ', c)
           sleep(1)
       print('YOU LOST')
       sleep(1)
       print('You have 2 more attempts left')
       sleep(2)
       print(input('Lets start again Press the Enter key to roll the dice again : '))
       print('Rolling the first Dice')
       sleep(2)
       a = random.randint(1, 6)
       print('You got value of 1st die : ', a)
       sleep(1)
       print('Now Rolling the second Dice')
       sleep(2)
       b = random.randint(1, 6)
       print('You got value of 2nd die : ', b)
       sleep(1)
       d = a + b
       if a + b == z:
           print('Congo You Got', z)
           sleep(1)
           print('YOU WIN !')
       else:
           print('Oh no You Got', d)
       sleep(1)
       print('YOU LOST')
       print('You have 1 more attempt left. This is your last attempt. Good Luck')
       sleep(2)
       print(input('Lets start again Press the Enter key to roll the dice again : '))
       print('Rolling the first Dice')
       sleep(2)
       e = random.randint(1, 6)
       print('You got value of 1st die : ', e)
       sleep(2)
       print('Now Rolling the second Dice')
       sleep(2)
       f = random.randint(1, 6)
       print('You got value of 2nd die : ', f)
       sleep(1)
       g = e + f
       if e + f == z:
           print('Congo You Got', z)
           sleep(1)
           print('YOU WIN !')
       else:
           print('Oh no You Got', g)
       sleep(1)
       print('SADLY YOU LOST THE GAME BUDDY')
       sleep(2)


   elif i == 'n':
        y=input('Do you really wanna quit ? y/n')
        if y=='n':
            z=input('Do you want to play again ? y/n')
            if z=='y':
                z = random.randint(2, 12)
                print('YOU HAVE TO GET',z,'To WIN THE GAME')
                sleep(2)
                input('Press the Enter button to start Rolling the Dice : ')
                print('Rolling the first Dice')
                sleep(2)
                x = random.randint(1, 6)
                print('You got value of 1st die : ', x)
                sleep(2)
                print('Now Rolling the second Dice')
                y = random.randint(1, 6)
                print('You got value of 2nd die : ', y)
                c = x + y
                if x + y == z:
                    print('Congo You Got : ', z)
                    sleep(1)
                    print('YOU WON')
                else:
                    print('Oh No You Got : ', c)
                    sleep(1)
                print('YOU LOST')
                sleep(1)
                print('You have 2 more attempts left')
                sleep(2)
                print(input('Lets start again Press the Enter key to roll the dice again : '))
                print('Rolling the first Dice')
                sleep(2)
                a = random.randint(1, 6)
                print('You got value of 1st die : ', a)
                sleep(1)
                print('Now Rolling the second Dice')
                sleep(2)
                b = random.randint(1, 6)
                print('You got value of 2nd die : ', b)
                sleep(1)
                d = a + b
                if a + b == z:
                    print('Congo You Got', z)
                    sleep(1)
                    print('YOU WIN !')
                else:
                    print('Oh no You Got', d)
                sleep(1)
                print('YOU LOST')
                print('You have 1 more attempt left. This is your last attempt. Good Luck')
                sleep(2)
                print(input('Lets start again Press the Enter key to roll the dice again : '))
                print('Rolling the first Dice')
                sleep(2)
                e = random.randint(1, 6)
                print('You got value of 1st die : ', e)
                sleep(2)
                print('Now Rolling the second Dice')
                sleep(2)
                f = random.randint(1, 6)
                print('You got value of 2nd die : ', f)
                sleep(1)
                g = e + f
                if e + f == z:
                    print('Congo You Got', z)
                    sleep(1)
                    print('YOU WIN !')
                else:
                    print('Oh no You Got', g)
                sleep(1)
                print('SADLY YOU LOST THE GAME BUDDY')
                sleep(2)


            elif z=='n':
               break
        elif y=='y':
           break
sleep(1)
print('Thanks for playing the game')
sleep(1)
print('Come back again later !')
























