from replit import db #the database
import getpass #for the password
import os #secrets
import time 
import datetime
import random


#Allow the user to view their stock portfolio and how much they have invested in each stock.
#Add a leaderboard to show the top 10 users with the most money.
#Create a mini-game where the user can earn extra money or experience points.
#Add a news section where the user can see the latest stock market news and updates.
#Allow the user to invest in more than just stocks, such as commodities or mutual funds.
#Create a tutorial section to help new users understand the basics of the game.
#Add a feature to allow the user to borrow money from the bank to invest in stocks.
#Allow the user to set alerts for specific stocks to notify them of any changes in price.
#Create different levels of difficulty, each with their own challenges and rewards.


keys = db.keys()
values = db.values()


def signup():
  usrnme = input("\nEnter your desired username: ") 
  if usrnme in db.keys():
    print("That username is already taken. Please choose another one. (Type \"go back\" to go back to the menu)")
    signup()
  elif usrnme == "go back":
    Start()
  elif usrnme.isalpha() == False:
    print("You can only have letters in your username.")
    signup()
  elif len(usrnme) <= 1:
    print("Your username can only be 2-10 letters long.")
    signup()
  elif len(usrnme) >= 11:
    print("Your username can only be 2-10 letters long.")
    signup()


  else:
    pswrd = getpass.getpass(prompt = "\nEnter your desired password: ", stream = None) # creates the paswrd
    print('*' * len(pswrd))
    print("\n")

    pswrd2 = getpass.getpass(prompt = "Confirm your desired password: ", stream = None) # confirms the paswrd
    print('*' * len(pswrd2))

    if pswrd != pswrd2: # checks if the password equals the password
      print("You wrote your password wrong. Try again.")
      signup()
    else:
      print("Ok, now use that username and password to sign in. (Run again)")
      db[usrnme] = pswrd
      db[usrnme + "1"] = "500 1" #for the game, it is "money  experience_level "
      db[usrnme + "2"] = {'DOGE-CAD': 0, 'SBUX': 0, 'AAPL': 0, 'TSLA': 0, 'AMZN': 0, 'MSFT': 0, 'NVDA': 0, 'META': 0, 'NFLX': 0, "ISRG": 0, 'BA': 0, 'ADBE': 0, 'MA': 0, 'RML.NS': 0, 'ZC=F': 0, 'EQIX': 0, 'REGN': 0, 'MELI': 0, 'MKL': 0, 'MTD': 0, 'CMG': 0, '^RUT': 0, 'TPL': 0, "ALI=F": 0, 'AZO': 0, 'BKNG': 0, 'SEB': 0, 'NVR': 0, 'NXT.L': 0, 'LDSVF': 0, 'LISP.SW': 0, 'BTC-CAD': 0, 'LISN.SW': 0, '0QKN.L': 0, 'BRK-A': 0} # the stocks. 
      db[usrnme + "3"] = ["You made an account!"] #history
      Start() #exits so they need to use their username to sign in

def Start():
  while True:
    loginsignup = input("Would you like to login or signup? (Enter 'login' or 'signup'): ")
    if loginsignup.lower() == "login":
      login()
      break
    elif loginsignup.lower() == "signup":
      signup()
      break
    else:
      print("Invalid input. Please enter either 'login' or 'signup'.")

Start()