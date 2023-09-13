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

imput_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor ")
imput_choose = int(imput_choose)
list_choose = ["Rock", "Paper", "Scissor"]
if imput_choose == 0:
    print(rock)
if imput_choose == 1:
    print(paper)
if imput_choose == 2:
    print(scissors)


