#Purpose Practice  on  20230926 to try out the module\def functuion and speed up the coding speed.
#2023.09.26

from art import logo
from game_data import data
import random


#format the data into printable format
def format_data(account):
  """format the data into printable one"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name},a {account_descr},from{account_country}")

#the art 
print(logo)



#Generate a random data from datapool
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"compare A: {format_data(account_a)}")
print(f"compare B: {format_data(account_b)}")
#ask for a guess
#check if the user is correct 
##Get folloer count 
##use if to check the answer
#give the result 
#show the score and keepa adding if it is right
#repeat the game until lose
#make the previous answer against the next question(position b become next position a)
#clear the screen
