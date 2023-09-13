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

#Write your code below this line 👇
import random

imput_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice} ")

# if computer_choice > imput_choice:
#   print("Computer wins!")

# if imput_choice == 0 and computer_choice ==2:
#   print("User wins!")
# elif computer_choice > imput_choice:
#   print("Computer wins!")

if imput_choice == 0 and computer_choice ==2:
  print("You win!")
elif computer_choice == 0 and imput_choice == 2:
  print("You lose!")
elif computer_choice > imput_choice:
  print("You lose!")
elif imput_choice > computer_choice:
  print("You win!")
elif computer_choice == imput_choice:
  print("It's a draw!")

#need to up
elif imput_choice >= 3 or imput_choice < 0:
  print("You type an ivalid number, game over")

# imput_choose = int(imput_choose)
# list_choose = ["Rock", "Paper", "Scissor"]
# if imput_choose == 0:
#     print(rock)
# if imput_choose == 1:
#     print(paper)
# if imput_choose == 2:
#     print(scissors)


