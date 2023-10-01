from art import logo,vs
from game_data import data
import random
from replit import clear

#format the data into printable format
def format_data(account):
  """format the data into printable one"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name},a {account_descr},from{account_country}")
#check if the user is correct 
def check_answer(guess,a_followers,b_followers):
  """Take the user guess and follower counts and return if they got it right"""
  if a_followers>b_followers:
    return guess =="a"
  else:
    return guess =="b"

#the art 
print(logo)
score=0
game_should_countinued = True
account_b=random.choice(data)
while game_should_countinued:
  #Generate a random data from datapool
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"compare A: {format_data(account_a)}")
  print(vs)
  print(f"compare B: {format_data(account_b)}")
  #ask for a guess
  guess=input("Who has more follower? Type 'A'or 'B': ").lower()
  
  
  ##Get folloer count 
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  
  clear()
  print(logo)
#clear the screen

  #give the result 
  #show the score and keepa adding if it is right
  
  if is_correct:
    score +=1
    print(f"You are right! Your current score:{score}")
  else:
    print(f"Sorry, that's not right.Your current score:{score}")
    game_should_countinued = False





