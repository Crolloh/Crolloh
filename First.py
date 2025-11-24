#Variables (String, integers, float, booleans)
#String
First_gf = "Claire"
print(First_gf)
#Int
Fav_no = 67
print(f'my fave number is {Fav_no}')
#Float
Not_fav = 1.1
print(f'{Not_fav} is my least fav number')
#Boolean
Love = True
if Love:
    print('love is true')
else:
    print('love is not true')

#Typecasting using str(), int(), float(), bool()
name = "ian"
age = 25
age = str(age)
print(type(age))

#Input
#Addition exercise
# first = float(input("Give me a number: "))
# second = float(input("Give me another number: "))
# equal = first + second
# print(f'that sums up to {equal}')

#Math (+=
kids = 25
kids += 2
print(kids)
#more math
e = 6.722222
y = -7
i = 4
result = round(e, 2)
#result = abs(y) = 7
#result = max(e, y, i) = 6.722222
#result = min(e, y, i) = -7
#result = pow(4, 2) = 16
print(result)

import math #math.sqrt, etc
print(math.pi)

#if statements and else if
claire = 1
if claire >= 2:
    print("yes")
elif claire <= 2:
    print("why?!")
else:
    print("no") #why
#practice review 9/26
true = 1
if true >= 5:
    print(7)
elif true == 0:
    print("no")
else:
    print("nah")
# X if condition else Y (conditional exp)
love = False
Claire = "Love claire" if love == True else "Not love claire"
print(Claire)
#String methods
#name = input('give me a random word:')
#print(len(name)) length
#print(name.find('w'))
#print(name.rfind('e'))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#(name.isalpha())
#print(name.isalnum())
#print(name.count('w'))
#print(name.replace("a","w"))
#Username exercise (no more than 12 chars, no space, no digits
Username = input('What is your username?: ')
len(Username)
Username.isdigit()
Username.isspace()
if len(Username) > 12 or Username.isdigit() == True or Username.isspace() == True:
    print('invalid username')
else:
    print('valid username')
#while loop
#food = input('What is my favorite food? :')
#while not food.lower() == 'ramen':
#    print("That's not my favorite food")
#    food = input('One more try. :')

#print('Yes ramen is my favorite food!')
# MAGIC 8 BALL: Simulates a Magic 8 Ball toy that gives random answers to user questions.
responses = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

import random
question = input('give 8 ball a question: ')
response_index = random.randint(0, len(responses) - 1)

print('here is your answer:', responses[response_index])
#Ride exercise
height = float(input('what is your height?(cm): '))
credit = int(input('what is your credits?: '))

if height >= 137 and credit >= 10:
  print('Enjoy the ride!')
elif height < 137 and credit >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and credit < 10:
  print('You don''t have enough credits.')
else:
  print('You have not met the requirements.')
#sorting of clans
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = int(input('Do you like Dawn o Dusk?\n1) Dawn\n2) Dusk\nEnter the number of your choice: '))
if Q1 == 1:
  Gryffindor += 1 
  Ravenclaw += 1
elif Q1 == 2:
  Hufflepuff += 1 
  Slytherin += 1
else:
  print('wrong input')

Q2 = int(input("When i'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nEnter the number of your choice: "))
if Q2 == 1:
  Gryffindor += 1 
elif Q2 == 2:
  Slytherin += 1
elif Q2 == 3:
  Ravenclaw += 1
elif Q2 == 4:
   Hufflepuff += 1
else:
  print('wrong input')

Q3 = int(input("Which of the following would you most hate people to call you?\n1) Ordinary\n2) Ignorant\n3) Cowardly\n4) Selfish\nEnter the number of your choice: "))
if Q3 == 1:
  Gryffindor += 1 
elif Q3 == 2:
  Ravenclaw += 1
elif Q3 == 3:
  Hufflepuff += 1
elif Q3 == 4:
  Slytherin += 1
else:
  print('wrong input')

Q4 = int(input("Which instrument pleases your ear the most?\n1) Violin\n2) Trumpet\n3) Piano\n4) Drum\nEnter the number of your choice: "))
if Q4 == 1:
  Ravenclaw += 1 
elif Q4 == 2:
  Gryffindor += 1
elif Q4 == 3:
  Hufflepuff += 1
elif Q4 == 4:
  Slytherin += 1
else:
  print('wrong input')

print(f'Gryffindor: {Gryffindor}\nRavenclaw: {Ravenclaw}\nHufflepuff: {Hufflepuff}\nSlytherin: {Slytherin}')
#username and password while loop function
def user_pass():
   while True:
    Username = input('Create a username: ')
    if ' ' in Username:
      print('There should be no spaces in your username, try again: ')
      continue 
    Password = input('Create a password: ')
    Confirm_Password = input('Confirm your password: ')
    while Password != Confirm_Password:
      print('Password does not match, try again: ')
      Password = input('Create a password: ')
      Confirm_Password = input('Confirm your password: ')
    print('Account succesfully created!')
    break
   
user_pass() #call the function to activate it 
#more functions
def statement1():
   Input1 = input('what is your favorite subject?: \nA) math\nB) science')
   if Input1.upper() == 'A':
      print('Same i like math too!')
   elif Input1.upper() == 'B':
      print('Same I lke science too!')
   else:
      print('Wrong input')
statement1()
#function to see if prime number
def is_prime(n):
    if n <= 1:
        print('This is not a prime number.')
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print('This is not a prime number.')
            return
    print('This is a prime number.')

is_prime(50)
#Calculator 

def calculator(num1, num2, operator):
   while True:
      if operator == "+":
         return num1 + num2
      elif operator == '-':
         return num1 - num2
      elif operator == 'x':
         return num1 * num2
      elif operator == '/':
         if num2 == 0:
            raise ValueError('Division by zero.')
         return num1 / num2
      else:
         raise ValueError('Unsupported operator.')
      
print(calculator(1, 2, "+"))

