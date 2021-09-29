import random



#the highest number wins
#setting the range for the die
min=1
max=6
x=0
y=0
player_name=input('Enter your name here:')
roll_again='yes'
while roll_again =='yes':
    if roll_again=='no':
      exit(0)
    print("Your turn")
    print('Rolling now')
    x=random.randint(min,max)
    y=random.randint(min,max)
    def dice(m):
      if m==1:
        print (u'\u2680')
      elif m==2:
        print(u'\u2681')
      elif m==3:
       print (u'\u2682')
      elif m==4:
        print (u'\u2683')
      elif m==5:
        print (u'\u2684')
      elif m==6:
        print (u'\u2685')
    dice(x)
    print('Computers turn')
    print('Rolling dice')
    dice(y)
    #setting the conditions for winning
    print("Outcome:")
    if(x==y):
      print(player_name,' it was a Draw!, would you like to roll again')
    elif(x>y):
      print('You win',player_name,'@_@')
    elif(x<y):
      print('Oh Boy Boy',player_name,'you lost')
    roll_again=input('Would you like to roll again enter yes or')
