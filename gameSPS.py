"""
Cases:
A - Stone
Stone - Stone = tie
Stone - Paper = Paper win
Stone - Scissor = Stone win

B - Paper
Paper - Paper = tie
Paper - Stone = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor - Scissor = tie
Scissor - Paper = Scissor win
Scissor - Stone = Stone win
"""
import random
item_list = ["Stone", "Paper", "Scissor"]

user_choice = input("Enter your move:")
comp_choice = random.choice(item_list)

print(f"User_Choice:{user_choice}, Computer_Choice:{comp_choice}")

if user_choice == comp_choice:
    print("Tie")
elif user_choice == "Stone":
    if comp_choice == "Paper":
        print("Paper covers Stone = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers Stone, You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Stone smashes scissor, Computer win")
