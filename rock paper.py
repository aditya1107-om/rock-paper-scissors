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
images=[rock,paper,scissors]
print("welcome")
user_choice=int(input('choose rock,paper,scissor\n for rock type"0"\n for paper type "1"\n for scissor type "2" '))
if user_choice>=0 and user_choice<=2:
    print("user choice")
    print(images[user_choice])
else:
    print("invalid")
import random
computer_choice=random.randint(0,2)
print("computer choice")
print(images[computer_choice])
 
if computer_choice==2 and user_choice==0:
    print("you win!!!!")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win!!!!")
elif computer_choice==user_choice:
    print("its a draw")



