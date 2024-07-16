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

#The CODE
import random

List1 = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n" )) 
computer_choice = random.randint(0,2) 

if user_choice <= 2 and user_choice >= 0:
    user_pict = List1[user_choice]
    print(user_pict)
    computer_pict = List1[computer_choice]
    print(f" computer choose : {computer_pict}")
    if user_choice == 0 and computer_choice ==2 : 
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif computer_choice > user_choice:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw")
else:
    print("You Type an invalid number, you lose")
    
