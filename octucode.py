# لعبة طوبة ورقة مقص مشروع الوحدة الخامسة
rock_ascii="""
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""  
paper_ascii="""
_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________) 
"""
scissors_ascii="""
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    
import random
print("Welcome to the Rock, Paper, Scissors game: ")
confirm=input("Press enter to continue or type (help) for the rules help: ").lower()
if confirm=="help":
    print("""
                    ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆ RULES ⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
                    1) You choose and the computer chooses
                    2) Rock smashes scissors = Rock wins
                    3) Scissors cut paper = scissors win
                    4) Paper covers rock = paper wins
      """)
#     # user choice
user_choice=input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
if user_choice not in ["Rock", "Scissors", "Paper"]:
    print("Invalid choics")
else:
    if user_choice=="Rock":
        print(f"YOu chose: {rock_ascii}")
    elif user_choice=="Paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")
        # computer choice
    computer_choice=random.choice(["Rock", "Scissors", "Paper"])
    if computer_choice=="Rock":
        print(f"Computer choice:{rock_ascii}")
    elif computer_choice=="Paper":
        print(f"\nComputer chose:\n{paper_ascii}")
    else:
        print(f"\nComputer chose:\n{scissors_ascii}")

    if user_choice==computer_choice:
        print("Equality")
    elif ((user_choice=="Rock" and computer_choice=="Scissors") or 
          (user_choice=="Paper" and computer_choice=="Rock") or
          (user_choice=="Scissors" and computer_choice=="Paper")):
        print(f"You win! {user_choice} beats {computer_choice}")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}")
    

    # الحلقة التانية  اللي حلها في الحلقة 3وحدة 6 مشروع to do list  على loop (for)
done_tasks=[]
ongoing_tasks=[]
today_tasks=input("Enter your tasks for today separated by a comma: ").split(", ")
for tasks in today_tasks:
    print(f"\n{tasks}\n")
    response=input(f"Did you finish {tasks} already?\n").lower()
    if response=="yes":
        done_tasks.append(tasks)
        print("Nice job")
    else:
        ongoing_tasks.append(tasks)
        print("Try not to put it off")
    print("--------")
progress=input("Do you want to see your today's progress?(yes,no)\n").lower()
if progress=="yes":
    print(f"""
                    ♡♡♡♡♡♡ Done Tasks ♡♡♡♡♡♡
                    {done_tasks}
    """)
    print(f"""
                    ♡♡♡♡♡♡ Ogoing Tasks ♡♡♡♡♡♡
                    {ongoing_tasks}
    """)
else:
    print("Press enter to exit...") 

#   الحلقة 3 اللي حلها في الحلقة الرابعة مشروع حساب التسوق من حيت العناصر والتكلفة باستخدام ال (loop, list,sum)
# طريقة سلمى سلموزة اللي الحمد لله جامدة جمودةأوي أوي

print("\n⋆⋆⋆ Welcome to ishop calculater ⋆⋆⋆\n")
items_numbers=int(input("How many items are there in your basket today? "))
basket=[]
prices=[]
if items_numbers>0:
    print("Let's go to counting them...")
    stop_range=items_numbers+1
    for items in range(1,stop_range):
        item_name=input(f"Please tell me the name of the item number {items}: ")
        basket.append(item_name)
        print(f"What is the price of {item_name}?")
        item_price=float(input("$"))
        prices.append(item_price)
    entire_basket=input("Would you like to see your entire basket items? ").lower()

    if entire_basket=="yes":
        print(basket)
    
    else:
        input("Press enter to skip...")
    
    see_cost=input("Would you like to see how much it'll cost? ").lower()
    if see_cost=="yes":
        print("\nbuying these items will cost:")
        print(sum(prices))
    
    else:
        input("press enter to exit...")
else:
    print("Seems like you're not in the mood for shopping today")


            # طريقة ابراهيم عادل

print("\n⋆⋆⋆ Welcome to ishop calculater ⋆⋆⋆\n")
items_numbers=int(input("How many items are there in your basket today? "))
basket=[]
prices=[]
if items_numbers>0:
    print("Let's go to counting them...")
    for items in range(0,items_numbers):
        item_name=input(f"Please tell me the name of the item number {items+1}: ")
        basket.append(item_name)
        item_price=float(input(f"What is the price of {item_name}?\n$"))
        prices.append(item_price)
    entire_basket=input("Would you like to see your entire basket items? ").lower()
    if entire_basket=="yes":
        print(basket)
        see_cost=input("Would you like to see how much it'll cost? ").lower()
        if see_cost=="yes":
            print("\nbuying these items will cost:")
            print(sum(prices))
        else:
            input("Press enter to exit...")
    else:
        input("Press enter to exit...")
else:
    print("Seems like you're not in the mood for shopping today")

    #  الحلقة 4 اللي حلها في الخامسة من الوحدة السادسة مشروع نضيف كل رقم للي بعده
numbers=[1,2,3,4,5]
total=0
print("let's add each number to the next")
for y in numbers:
    total +=y
    print(f"⇒ {total}")
    print(f"\nThe total number is: {total}\n")

    # الحلقة 6 من الوحدة 6 حل مشروع اختصار الأسماء

    names=input("Enter the first and last name of your friends separated by a comma: ").split(", ")
abbreviated_names=[]
for name in names:
    name_parts=name.split()
    print(name_parts)
    f_name=name_parts[0]
    l_name=name_parts[1]
    first_initial=f_name[0]
    last_initial=l_name[0]
    # ممكن نختصر كدة
    # first_letter=name_parts[0][0]
    # last_letter=name_parts[1][0]
    abbreviation=first_initial+"."+last_initial+"."
    abbreviated_names.append(abbreviation)
print("Abbreviated Names:")
for x in abbreviated_names:
    print(x)


    
#  الحلقة ال 7 الوحدة ال 6 مشروع إنشاء كلمة سر صعبة مكونة من حروف وارقام ورموز

import random
import string
print("Welcome to the password Generator!")
length=int(input("Enter the total number of characters in the password: "))
num_letters=int(input("Enter the number of letters in the password: "))
num_numbers=int(input("Enter the number of numbers in the password: "))
num_symbols=int(input("Enter the number of symbols in the password: "))
if length!=(num_letters+num_numbers+num_symbols):
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password")
else:
    passowrd=[]
    random_letters=random.choices(string.ascii_letters,k=num_letters)
    passowrd+=random_letters
    random_numbers=random.choices(string.digits,k=num_numbers)
    passowrd+=random_numbers
    random_symbols=random.choices(string.punctuation,k=num_symbols)
    passowrd+=random_symbols
    random.shuffle(passowrd)
    print("Generated password: ","".join(passowrd))

#   ### بطريقة اخرى او ككثر تفصيلا وترتيبا###الحلقة ال 7 الوحدة ال 6 مشروع إنشاء كلمة سر صعبة مكونة من حروف وارقام ورموز
import random
import string
print("Welcome to the password Generator!")
length=int(input("Enter the total number of characters in the password: "))
num_letters=int(input("Enter the number of letters in the password: "))
num_numbers=int(input("Enter the number of numbers in the password: "))
num_symbols=int(input("Enter the number of symbols in the password: "))
if length!=(num_letters+num_numbers+num_symbols):
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password")
else:
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    password_chars=(
        random.choices(letters,k=num_letters)+
        random.choices(numbers,k=num_numbers)+
        random.choices(symbols,k=num_symbols)
    )
    random.shuffle(password_chars)
    password="".join(password_chars)
    print("Generated password: ",password)




# مشروع تخمين الرقم الصحيح باستخدام while loop الوحدة 7 الحلقة 4

import random
secret_number=random.randint(1,10)
guess=int(input("Guess a number between 1 and 10: "))
while guess!=secret_number:
    if guess>secret_number:
        guess=int(input("Too high! Guess again: "))
    else:
        guess=int(input("Too low! Guess again: "))
print("Congratulations! You guessed the number!")


#   HANGMAN GAME Unit 8 project
HANGMANPICS = [
    '''
+---+
      |
      |
      |
      |
      |
=========
   ''',
   '''
               
  +---+
  |   |
      |
      |
      |
      |
=========
   ''',
   '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
   ''',
   '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
   ''',
   '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
   ''',
   '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
   ''',
   '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
   ''',
   '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
   '''
   ]

import random
words=["on", "sam", "near"]
random_word=random.choice(words)
####    عرض مسافات بنفس عدد حروف الكلمات   
display=["_"] * len(random_word)
print(" ".join(display))

lives=6
# طريقة اخرى
# ascii=0 

# print(HANGMANPICS[0])
print(HANGMANPICS[6-lives])

 #  قائمة لتخزين الحروف التي تم تخمينها
guessed_letter=[]

while "_" in display and lives>0:
    guessed=input("Please guess a letter: ").lower()

    # شيك لو الحرف تم تخمينه قبل وخليه يسكبه عن طريق ال continue
    if guessed in guessed_letter:
        print ("You already guessed that. Try again.")
        print(f"You have {lives} more tries")
        continue
    
    # في حالة لم يسبق تخمينه نضيفه للقائمة
    guessed_letter.append(guessed)
    
    # اشيك لو الحرف مش موجود في الكلمة 
    if guessed not in random_word:
        lives-=1
        print(HANGMANPICS[6-lives])

        # طريقة اخري
        # ascii+=1
        # print(HANGMANPICS[ascii])

### لو صحيح ((((((بدل)))))) مسافة بحرف واعرض 
    for position in range(len(random_word)):
        if random_word[position]==guessed:
            display[position]=guessed
    print(" ".join(display))
    print(f"You have {lives} more tries")

if lives ==0:
    print("""
           YOU LOSE
          """)
    print(HANGMANPICS[-1])

    # او
    # print(HANGMANPICS[6-lives])
else:
    print("""
      *************
         YOU WIN
      *************
""")