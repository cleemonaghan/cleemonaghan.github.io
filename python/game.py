# -*- coding: utf-8 -*-
"""

Problem 2.9
This program is a "choose your own adventure" game.
The story is printed to the command line, along with choices of action.
Then the user enters some text to select their choice.
Created on Sun Jan 17 13:13:53 2021

@author: Colin Monaghan
"""
import random




def getWager(account):
    print("You currently have $%s in your account." % account)
    while True:
        value = input("Enter in an amount to wager or \"exit\" to leave.\n> ")
        if(value.strip().lower() == 'exit'):
            return None
        try:
            wager = int(value)
            if wager > account:
                print("You do not have enough money to place a wager that large.")
            elif wager < 0:
                print("That is not a valid wager.")
            else:
                return wager
        except ValueError:
            print("That is not a valid wager.")



def round(account):
    wager = getWager(account)
    if wager == None:
        return None
    print("""Time to play!
    You entered: $%s.
    Your opponent matched your entry. 
    They entered: $%s.
Press Enter to roll the dice.""" % (wager, wager))
    your_roll = -1
    their_roll = -1
    while your_roll == their_roll:
        input()
        your_roll = random.randrange(6)
        their_roll = random.randrange(6)
        print("""You rolled a %s.
They rolled a %s.""" % (your_roll+1, their_roll+1))
        if your_roll == their_roll:
            print("It is a tie, roll again.")
    if your_roll > their_roll:
        print("You won!\nYou gained $%s." % wager)
        account += wager
    else:
        print("They won.\nYou lost $%s." % wager)
        account -= wager
    return account



print("Welcome!")

#Set the starting amount to 500
account = 500

while account != None and account > 0:
    account = round(account)
    
if(account == None):
    print("Goodbye!")
else:
    print("Oh dear. It seems you are out of money.\nGoodbye!")