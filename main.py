from replit import db
import getpass
import os
import time
import datetime
import random
from dotenv import load_dotenv

from stocks import real_symbols
from stocks import printsymbolpricesandstuff
from stocks import stonke

#Allow the user to view their stock portfolio and how much they have invested in each stock.
#Add a leaderboard to show the top 10 users with the most money.
#Create a mini-game where the user can earn extra money or experience points.
#Add a news section where the user can see the latest stock market news and updates.
#Allow the user to invest in more than just stocks, such as commodities or mutual funds.
#Create a tutorial section to help new users understand the basics of the game.
#Add a feature to allow the user to borrow money from the bank to invest in stocks.
#Allow the user to set alerts for specific stocks to notify them of any changes in price.
#Create different levels of difficulty, each with their own challenges and rewards.
load_dotenv()

scrtee = os.getenv("INFO")
scrteee = os.getenv("INFOO")
scrteeee = os.getenv("INFOOO")

keys = db.keys()
values = db.values()

rihtnow = datetime.datetime.now()
date_string = rihtnow.strftime("%d/%m/%Y")


def wow():
  print("\n" * 30)  #NEW LINES


def shevessmoocha(amount, plusorminus):
  the_money = db.get(username1)
  split_the_money = the_money.split()  #["money", "exp"]
  monnehy = split_the_money[0]  #["money"]

  if plusorminus == "plus":
    newmonnehy = float(monnehy) + float(amount)
    updated_stufefe = str(newmonnehy) + " " + str(split_the_money[1])
  elif plusorminus == "minus":
    newmonnehy = float(monnehy) - float(amount)
    updated_stufefe = str(newmonnehy) + " " + str(split_the_money[1])
  db[username1] = updated_stufefe


def historychange(nameyes):
  list_of_three = db.get(username3)
  seperatedlen = []

  seperatedlen = list_of_three

  seperatedlen.append(nameyes)
  db[username3] = seperatedlen


def checkstocks():
  global listofstonke
  refreshvariables()
  stonke_list = db.get(username2)
  listofstonke = {}

  for key, value in stonke_list.items():
    if value >= 1:
      listofstonke[key] = value
  if len(listofstonke) == 0:
    print("Stocks you have: None")
  elif len(listofstonke) > 0:
    print("Stocks you have:\n")
    for kee, vaa in listofstonke.items():
      print(f"{kee}: {vaa}")


def stockss():
  global money
  wow()

  immediatebuy = input(
      "Do you want to buy a stock, look at the stocks, sell a stock, or go back to the menue? \n(write \"buy\" or \"look\" or \"sell\" or \"menue\"): "
  )
  if immediatebuy.lower() == "look":
    print("Stocks are:\n")
    time.sleep(1)
    printsymbolpricesandstuff()
    time.sleep(2)
    stockss()
  elif immediatebuy.lower() != "look" and immediatebuy.lower(
  ) != "buy" and immediatebuy.lower() != "sell" and immediatebuy.lower(
  ) != "menue":
    print("I don't understand what you mean by that.")
    time.sleep(1)
    stockss()
  elif immediatebuy.lower() == "menue":
    menue()
  elif immediatebuy.lower() == "buy":
    whichstock = input(
        "\nWhich stock do you want to buy? (write the stock symbol): ")
    if whichstock not in real_symbols:
      print("That is not one of the stock symbols.")
      time.sleep(2)
      stockss()
    else:
      fakekey, fakevalue = stonke(whichstock, whichstock)
      keye = fakekey
      cost_of_stock = float(fakevalue)
      rusuress = input("Are you sure you want to buy " + str(keye) + " for $" +
                       str(float(cost_of_stock)) + "? (write Yes or No): ")
      if rusuress.lower() == "no":
        stockss()
      elif rusuress.lower() == "yes":
        pass
      elif rusuress.lower() != "yes" or "no":
        print("I don't understand what you mean.")
        time.sleep(1)
        menue()

      shares = int(
          input("How many shares do you want to buy of " + keye + "?: "))

      if shares <= 0:
        dooyouwanttobuy = input(
            "You don't wan't to buy any stocks? (write Yes or No): ")
        if dooyouwanttobuy.lower() == "yes":
          menue()
        elif dooyouwanttobuy.lower() == "no":
          stockss()
        else:
          print("I don't know what you mean by that.")
          menue()

      cost = float(shares) * float(cost_of_stock)
      if float(cost) > float(money):
        print("Insufficient funds.")
        time.sleep(1)
        stockss()
      else:
        #money = float(money) - float(cost) delte this?
        loading_screen(random.choice([1, 2, 3]))

        shevessstocks(keye, shares, "plus")  #putting it in the stoks they have

        shevessmoocha(cost, "minus")

        print("Transaction complete.\n")
        print(f"You bought {shares} share(s) of {keye}!")
        wowyouboughtsommit = f"You bought {shares} share(s) of {keye} at {date_string}!"
        historychange(wowyouboughtsommit)
        refreshvariables()
        time.sleep(2)
        wow()
        menue()
  elif immediatebuy.lower() == "sell":
    print("\n")  #newline
    checkstocks()  #print which stocks you have
    print("\n")

    wannabuyorselle = input(
        "Do you want to sell a stock or go to the menue? (write \"sell\" or \"menue\"): "
    )
    if wannabuyorselle.lower() == "menue":
      menue()
    elif wannabuyorselle.lower() != "sell" and wannabuyorselle.lower(
    ) != "menue":
      print("You didn't write \"sell\" or \"menue\".")
      stockss()
    elif wannabuyorselle.lower() == "sell":
      sellwhichonese = input(
          "\nWhich symbol(s) do you want to sell?: ")  #the name of symbol
      if sellwhichonese not in listofstonke:
        print("\nYou don't have that symbol.")
        time.sleep(1)
        stockss()
      elif sellwhichonese in listofstonke:
        howmanywannasell = input(
            "\nHow many shares do you want to sell?: ")  #shares
        if int(howmanywannasell) > listofstonke[sellwhichonese]:
          print("\nYou don't have that many shares.")
          time.sleep(1)
          stockss()
        elif int(howmanywannasell) <= listofstonke[sellwhichonese]:
          dakey, davalue = stonke(sellwhichonese, sellwhichonese)
          multiply = float(davalue) * float(howmanywannasell)

          shevessstocks(sellwhichonese, howmanywannasell, "minus")

          shevessmoocha(multiply, "plus")
          print("Sell complete.")
          refreshvariables()
          time.sleep(2)
          menue()


def refreshvariables():
  findvariables = db[username + "1"]
  findvariablesforstonk = db.get(username + "2")
  findvariable_history = db.get(username + "3")

  moneyexpereience = findvariables.split()
  moneyexpereiences = findvariablesforstonk
  global money
  global experience_level
  global stocks
  global history
  money = moneyexpereience[0]
  experience_level = moneyexpereience[1]
  stocks = moneyexpereiences
  history = findvariable_history


def menue():
  rounded_moocha = round(float(money), 2)
  formattedmoocha = "{:,}".format(rounded_moocha)

  refreshvariables()
  time.sleep(0.001)
  refreshvariables()

  print("\nMoney: ", formattedmoocha, "$")
  print("Experience level: ", experience_level)
  print("\nStocks:\n")
  for k, v in stocks.items():
    v_as_notzero = ""
    if v == 0:
      v_as_notzero = "-"
    elif v != 0:
      v_as_notzero = v
    print(f"{k}: {v_as_notzero}")

  answr = input(
      "\nWrite 'stocks', 'codes', 'history' or 'mystocks' to go there: ")

  if answr.lower() == "stocks":
    stockss()

  elif answr.lower() == "codes":
    code = input("What is your code?: ")
    if code == scrtee:
      db.clear()
      print("Clear complete.\n")
      exit()
    elif code == scrteee:
      keys = db.keys()
      values = db.values()
      print(keys)
      print(values)
    elif code == scrteeee:
      asiaepfspi = input("Plus/minus: ")
      ashoiasefiasp = input("Amount: ")
      if asiaepfspi.lower() == "plus":
        shevessmoocha(ashoiasefiasp, "plus")
        refreshvariables()
        menue()
      elif asiaepfspi.lower() == "minus":
        shevessmoocha(ashoiasefiasp, "minus")
        refreshvariables()
        menue()
    else:
      print("That is not a code.")
      menue()

  elif answr.lower() == "mystocks":
    checkstocks()
    time.sleep(2)
    menue()

  elif answr.lower() == "history":
    print("\n")
    for i in history:
      print("'" + str(i) + "'")
    time.sleep(2)
    menue()

  else:
    print("I don't understand what you mean.")
    time.sleep(1)
    answr = ""
    wow()
    menue()


def gamestart():
  menue()


def shevessstocks(name, times, plusorminus):
  old_list = db.get(username2)

  if plusorminus == "plus":
    old_list[name] += int(times)
  elif plusorminus == "minus":
    old_list[name] -= int(times)

    db[username2] = old_list


def loading_screen(num):
  countxxx = 0
  for i in range(1, num * 3 + 1):
    if countxxx == 0:
      print("Loading.")
    elif countxxx == 1:
      print("Loading..")
    elif countxxx == 2:
      print("Loading...")
      countxxx = -1  # reset to -1 since count will be incremented below
    countxxx += 1
    time.sleep(0.01)  # adds a delay 0.8


def finduser():  #Gets the account info
  global username1
  global username2
  global username3
  global money
  global experience_level
  global stocks
  global history

  username1 = username + "1"
  username2 = username + "2"
  username3 = username + "3"

  findvariables = db[username + "1"]
  findvariablesforstonk = db.get(username + "2")
  findvariable_history = db.get(username + "3")

  moneyexpereience = findvariables.split()

  moneyexpereiences = findvariablesforstonk  #keep

  history = findvariable_history
  money = moneyexpereience[0]
  experience_level = moneyexpereience[1]
  stocks = moneyexpereiences

  loading_screen(random.choice([0, 1, 2]))
  gamestart()


def signup():
  usrnme = input("\nEnter your desired username: ")
  if usrnme in db.keys():
    print(
        "That username is already taken. Please choose another one. (Type \"go back\" to go back to the menu)"
    )
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
    pswrd = getpass.getpass(prompt="\nEnter your desired password: ",
                            stream=None)  # creates the paswrd
    print('*' * len(pswrd))
    print("\n")

    pswrd2 = getpass.getpass(prompt="Confirm your desired password: ",
                             stream=None)  # confirms the paswrd
    print('*' * len(pswrd2))

    if pswrd != pswrd2:  # checks if the password equals the password
      print("You wrote your password wrong. Try again.")
      signup()
    else:
      print("Ok, now use that username and password to sign in. (Run again)")
      db[usrnme] = pswrd
      db[usrnme +
         "1"] = "500 1"  #for the game, it is "money  experience_level "
      db[usrnme + "2"] = {
          'DOGE-CAD': 0,
          'SBUX': 0,
          'AAPL': 0,
          'TSLA': 0,
          'AMZN': 0,
          'MSFT': 0,
          'NVDA': 0,
          'META': 0,
          'NFLX': 0,
          "ISRG": 0,
          'BA': 0,
          'ADBE': 0,
          'MA': 0,
          'RML.NS': 0,
          'ZC=F': 0,
          'EQIX': 0,
          'REGN': 0,
          'MELI': 0,
          'MKL': 0,
          'MTD': 0,
          'CMG': 0,
          '^RUT': 0,
          'TPL': 0,
          "ALI=F": 0,
          'AZO': 0,
          'BKNG': 0,
          'SEB': 0,
          'NVR': 0,
          'NXT.L': 0,
          'LDSVF': 0,
          'LISP.SW': 0,
          'BTC-CAD': 0,
          'LISN.SW': 0,
          '0QKN.L': 0,
          'BRK-A': 0
      }  # the stocks.
      db[usrnme + "3"] = ["You made an account!"]  #history
      Start()  #exits so they need to use their username to sign in


def login():
  global username
  username = input("\nEnter your username?: ")
  if username not in keys:
    print("Invalid username. Please try again. (run again to go to menu)")
    login()
  else:
    password = getpass.getpass(prompt="\nEnter your password: ", stream=None)
    print('*' * len(password))
    print("\n")
    if password != db[username]:
      print("That password does not match the username. Try again.")
      login()
    else:
      finduser()


def Start():
  while True:
    loginsignup = input(
        "Would you like to login or signup? (Enter 'login' or 'signup'): ")
    if loginsignup.lower() == "login":
      login()
      break
    elif loginsignup.lower() == "signup":
      signup()
      break
    else:
      print("Invalid input. Please enter either 'login' or 'signup'.")


Start()
