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

player_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. ")
print(player_choice)



if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
elif player_choice == "2":
    print(scissors)
else:
    print("Not a valid choice. Please try again.")

computer_choices = ["rock", "scissors", "paper"]
computer_choice = random.choice(computer_choices)

print("Computer chose:")
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
else:
    print(scissors)

#rock beats scissors
if player_choice == "0" and computer_choice == "scissors":
    print("You Win!")
#paper beats rock
elif player_choice == "1" and computer_choice == "rock":
    print("You Win!")
#scissors beats paper
elif player_choice == "2" and computer_choice == "paper":
    print("You Win!")
#draw
elif player_choice == "0" and computer_choice == "rock":
    print("Draw")
elif player_choice == "1" and computer_choice == "paper":
    print("Draw")
elif player_choice == "2" and computer_choice == "scissors":
    print("Draw")
else:
    print("You lose.")





