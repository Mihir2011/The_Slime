import os

input("Citizen: Welcome Mr. Knight")
input("Citizen: We all need help from the slimes so we need you")
input("Citizen: Please fight the slimes for us")
input("*You recieved a WoodSword Lv-1")
os.system('cls')

input("A Wild slime apeared")
ask1 = input("Your HP - 50/50 \nSlime HP - 25/25 \nWhat will you do \n1. Atack \n2. Shop")
if ask1 == "1":
    os.system('cls')
    print("You did 25 damage to the slime")
    print("Slime did 15 damage to you")
    print("Congratuations on winning your first fight")
    input("You got 12 gold")
    
if ask1 == "2":
    os.system('cls')
    print("shop")
    print("1. Upgrade weapon Lv - 20 gold")
    print("2. Potion - 15 gold")



    
