import random

print("Welcome to Roll-a-Dice !.....")
print("type yes to continue")
res = str(input("Do you want to roll the dice : "))
print("type yes to continue")

if res == "yes":
    
 
 
 response = "y"
  
while response == "y":
     
    
    no = random.randint(1,6)
     
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print("The value is 1")
    if no == 2:
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[-----]")
        print("The value is 2")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        print("The value is 3")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        print("The value is 4")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        print("The value is 5")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        print("The value is 6")
         
    x=input("press y to roll again and n to exit:")
    if x == "n":
        print("Thanks for playing, see you next time :)")
        break
l=str(input("Rate my dice simulator from 1 - 5 = "))
if l == "1":
     print("thanks, i will try to improve")
if l == "2":
     print("thanks, i will try to improve")
if l == "3":
     print("thanks, i will try to improve")   
if l == "4":
     print("thanks you so much <33333")  
if l == "5":
     print("thanks you so much <33333")      
    