logo = """

 ,_   _,  _,,  ,    ,_  _   ,_  _,,_      _,  _, ___,_, _,  _, ,_   _, 
 |_) / \,/  |_/     |_)'|\  |_)/_,|_)    (_, /  ' | (_,(_, / \,|_) (_, 
'| \'\_/'\_'| \    '|   |-\'| '\_'| \     _)'\_  _|_,_) _)'\_/'| \  _) 
 '  `'     `'  `    '   '  `'    `'  `   '     `'   '  '   '   '  `'   

"""
print(logo)

import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

game_images = [rock, paper, scissors]

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")

else:
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")

elif computer_choice == 0 and user_choice == 2:
  print("You lose")

elif computer_choice > user_choice:
    print("You lose!")

elif user_choice > computer_choice:
    print("You win!")

elif computer_choice == user_choice:
  print("It's a draw")



   # -----------------------------------------


# n1 = input("Enter the first number: ")
# n2 = input("Enter the second number: ")

# try:
#     n1 = float(n1)
#     n2 = float(n2)

#     if n1 <= 100 and n2 <= 100:
#         add = n1 + n2
#         sub= n1 - n2
#         mul = n1 * n2
#         div = n1 / n2

#         print("n1 + n2:", add)
#         print("n1 - n2:", sub)
#         print("n1 * n2:", mul)
#         print("n1 / n2:", div)

#     else:
#         print("Please enter numbers less than or equal to 100")

# except ValueError:
#     print("Please enter valid numbers")