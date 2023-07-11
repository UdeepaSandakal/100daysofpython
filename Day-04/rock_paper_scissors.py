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

hand = [rock, paper, scissors]

human_choice = int(input("What do you choose ? \nType 0 = rock , 1 = paper , 2 = scissors : "))
computer_choice = random.randint(0, 2)

if (human_choice >= 0) and (human_choice <= 2):
    print(f"\nYou choose :\n{hand[human_choice]}")
    print(f"Computer choose :\n{hand[computer_choice]}")

    if human_choice == computer_choice:
        print("It's a draw")
    elif human_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif human_choice == 0 and computer_choice == 2:
        print("You win!")
    elif human_choice == 1 and computer_choice == 0:
        print("You win!")
    elif human_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif human_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif human_choice == 2 and computer_choice == 1:
        print("You win!")
else:
    print("You've entered wrong selection.")
