print("Welcome to Paper, Rock and Scissors Game.\n If you want to play you can type your number:\n Paper = 1\n Rock = 2\n Scissors = 3")
choice = int(input("Type a number:\n"))
variables = [1,2,3]
import random
computers_move = random.choice(variables)
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

if choice != 1 and choice != 2 and choice != 3:
  print("Rerun the program and type correct number!")
else:
  if choice == 1 and computers_move == 1:
    print(f"Your choice:\n {paper} \n Computer's choice:\n {paper} \n It's a draw. ")
  elif choice == 2 and computers_move == 2:
    print(f"Your choice:\n {rock} \n Computer's choice:\n {rock} \n It's a draw. ")
  elif choice == 3 and computers_move == 3:
    print(f"Your choice:\n {scissors} \n Computer's choice:\n {scissors} \n It's a draw. ")
  elif choice == 1 and computers_move == 2:
     print(f"Your choice:\n {paper} \n Computer's choice:\n {rock} \n You won. ")
  elif choice == 1 and computers_move == 3:
     print(f"Your choice:\n {paper} \n Computer's choice:\n {scissors} \n You lost.")
  elif choice == 2 and computers_move ==1:
    print(f"Your choice:\n {rock} \n Computer's choice:\n {paper} \n You lost.")
  elif choice == 2 and computers_move ==3:
     print(f"Your choice:\n {rock} \n Computer's choice:\n {scissors} \n You won. ")
  elif choice == 3 and computers_move ==1:
     print(f"Your choice:\n {scissors} \n Computer's choice:\n {paper} \n You won. ")
  elif choice == 3 and computers_move ==2:
    print(f"Your choice:\n {scissors} \n Computer's choice:\n {rock} \n You lost.")