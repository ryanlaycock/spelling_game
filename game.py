#freds main bit of the game(it is just the logic)
import random
import time
import os
from random import randint

def jumble(word,jumble_):
  array = list(word)
  wordlen = len(word)
  counter = 0
  while counter < jumble_:
    temp = []
    lettre_sel = random.randint(0,wordlen-1)
    temp = array[lettre_sel]
    lettre_swp = random.randint(0,(wordlen-1))
    while lettre_swp == lettre_sel:
      lettre_swp = random.randint(0,(wordlen-1))
    array[lettre_sel] = array[lettre_swp]
    array[lettre_swp] = temp
    counter +=1
    
  array = ''.join(str(each) for each in array)
  return array  
  


def rundmc(look,jumble_,words):
  input("press enter to start::")
  print("")
  print("you have 10 seconds to look at each word")
  counter = 0
  while counter <= 20:
    word = random.choice(words)
    print(word)
    time.sleep(look) 
    os.system('clear')
  
    jumbled_word = jumble(word,jumble_)
    print("please correct the errors %s" %(jumbled_word))
    user_ans = input("::")
    if user_ans == word:
      #place holder for jims variable
      print("#MAGIC BEANS")
      os.system("clear")
    else:
      print("nope")
      os.system("clear")
    
    counter +=1
    
  
  


def game(words):
  diff ='easy'
  print("there will be 20 words in a round.")
  print("you are on %s difficulty" %(diff) )
  if diff == 'easy':
    print("you are on easy difficulty, you get 10 seconds to look at the word")
    word_look = 2
    word_jumble = 1
    rundmc(word_look,word_jumble,words)


words = ['Abba', 'Abba__']    # for testing purposes
game(words)