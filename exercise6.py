#snake water gun
import random
print("\t\t\t\t\tWelcome to Snake-Water-gun Game\n")
list=["s","w","g"]
count = 0
human_point = 0
computer_point = 0
while(count<10):
    human = input("Enter\ns for snake\n"
                  "w for water \n"
                  "and g for gun\n")

    computer = random.choice(list)
    print("YOu entered", human, "and computer entered ",computer,"\n\n")
    if human==computer:
        print(f"its a tie\n computer:{computer_point}\nyour:{human_point}")
    #if human choose snake
    elif human=="s" and computer=="w":
        print("you win\n\n")
        human_point= human_point+1
        print(f"your point is {human_point}and computer point is{computer_point}\n\n")
    elif human=="s" and computer=="g":
        print("you loose")
        computer_point = computer_point+1
        print(f"your point is {human_point}and computer point is{computer_point}\n\n")
     #if human choose water
    elif human=="w" and computer=="s":
        print("you loose")
        computer_point = computer_point + 1
        print(f"your point is {human_point}and computer point is{computer_point}\n\n")
    elif human=="w" and computer=="g":
        print("you win")
        human_point = human_point + 1
        print(f"your point is {human_point}and computer point is{computer_point}\n\n")
    #if human choose gun
    elif human=="g" and computer=="s":
        print("you win")
        human_point = human_point + 1
        print(f"your point is {human_point}and computer point is{computer_point}\n\n")
    elif human=="g" and computer=="w":
        print("you loose")
        computer_point = computer_point + 1
        print(f"your point is {human_point}and computer point is{computer_point}\n\n")
    else:
        print("wrong in put try again\n\n")
    count= count+1
    print(f" no of chance left = {10-count}\n\n")
if human_point>computer_point:
    print("Congratulation you win\n\n")
    print(f"your point = {human_point} and computer point = {computer_point}\n\n")
elif human_point<computer_point:
    print("you loose\n\n")
    print(f"your point = {human_point} and computer point = {computer_point}\n\n")
else:
    print(" its a tie\n\n")
    print(f"your point = {human_point} and computer point = {computer_point}\n\n")
