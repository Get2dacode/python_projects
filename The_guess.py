import random

tries=10
easy=random.randint(1,50)
hard=random.randint(1,500)
level=int(input('enter 1 for easy and 2 for hard:'))
if level==1:
  print('Guess a number between 1 and 50')
  secretnum=easy
else:
  print('Guess a number between 1 and 500')
  secretnum=hard

numofguesses=0
while True:
  guess=int(input('Enter a number:'))
  if(guess==secretnum):
    print('Random number guessed!')
    print('tries remaining:',tries)
    print('number of guesses it took:',numofguesses)
    break
  if(guess>secretnum):
    print('Sorry to high try again')
    tries=tries-1
    print('tries remaining:',tries)
    numofguesses=numofguesses+1
  if(guess<secretnum):
    print('Sorry to low try again')
    tries=tries-1
    print('tries remaining:',tries)
    numofguesses=numofguesses+1
  if(tries==0):
    print('out of tries')
    break
  
