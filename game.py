import random
a="WELCOME"
print(a.center(70,"*"))

print(
  ''' 
s for scissors 
r for rock 
p for paper

Rule for game 
paper beats rocks
scissors beats paper
rock beats scissors 

'''
)

user=input("enter your choice ['S','R','P']: \n")
user=user.upper()

computer=random.choice(['R','S','P'])
print(f"enter your choice {user}")
print(f"enter computer choice {computer}")

if (user=='R' and computer=='S') or (user=='p' and computer=='R') or (user=='S' and computer=='P'):
  print("you are winner")
elif user==computer:
  print("draw")
elif user!=['R','S','P']:
  print("invalid key")
else:
  print("you loose")  

