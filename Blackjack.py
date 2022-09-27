import os
import random
from Art import Logo

# {List of all cards in a deck}
Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Close_Program = False
while not Close_Program:
    User_Type = input("Do yo want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if User_Type == "y":
        os.system('cls') # {Clear console}
        print(Logo)

        # {}
        User_Cards = random.sample(Cards, 2)
        Computer_Cards = random.sample(Cards, 2)
        # {The Computer has to give a score higher than 17}
        for Computer_Score in Computer_Cards:
            Computer_Score = sum(Computer_Cards)
            if 17 >= Computer_Score:
                Computer_Cards.append(random.choice(Cards))
                # {Value of an Ace (1 or 11)}
                if 11 in Computer_Cards and Computer_Score > 21:
                    Computer_Cards.remove(11)
                    Computer_Cards.append(1)
        # {Functions}
        def Score_User_Cards():
            """Function that sums all User cards to get a score"""
            User_Score = sum(User_Cards)
            return User_Score

        def User_Ace():
            """Function that decides what is the value of an Ace (1 or 11)"""
            if 11 in User_Cards and Score_User_Cards() > 21:
                User_Cards.remove(11)
                User_Cards.append(1)

        def All_Cards():
            """Function that shows User/Computer's final hand and final score"""
            print(f"    Your final hand: {User_Cards}, final score: {Score_User_Cards()}")
            print(f"    Computer's final hand: {Computer_Cards}, final score: {Computer_Score}")

        def Winner():
            """Function that decides who is the winner"""
            if Score_User_Cards() == 21:
                print("* You win :) *")
            elif Score_User_Cards() > 21:
                print("* You went over. You lose :( *")
            elif Computer_Score > 21 and 21 > Score_User_Cards():
                print("* Opponent went over. You win :) *")
            elif Score_User_Cards() == Computer_Score:
                print("* Draw :| *")
            elif Computer_Score > Score_User_Cards():
                print("* You lose :( *")
            elif Score_User_Cards() > Computer_Score:
                print("* You win :) *")

        def Show_Cards():
            """Function that shows User cards and score. Only shows computer's first card. Ask the user to take another card if can/want"""
            print(f"    Your cards: {User_Cards}, current score: {Score_User_Cards()}")
            print(f"    Computer's first card: {Computer_Cards[0]}")
            if 21 > Score_User_Cards():
                Type_Another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if Type_Another == "y":
                    User_Cards.append(random.choice(Cards))
                    Score_User_Cards()
                    User_Ace()
                    Show_Cards()
                else:
                    All_Cards()
                    Winner()
            else:
                All_Cards()   
                Winner()
        Show_Cards()
    else:
        Close_Program = True