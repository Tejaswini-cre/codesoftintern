import random
while True:
        user_choise=int(input("enter the user choice based on the rules given below:\nTYPE 0 -> ROCK \nTYPE 1-> PAPER\nTYPE 2->SCISSORS"))
        print(f"user_choise  - {user_choise}")

        if user_choise>2 and user_choise<0:
         print("invalid choise,please enter the valid input")
        else:
         computer_choise=random.randint(0,2)
         print(f"computer choise - {computer_choise}")
         if user_choise==computer_choise:
           print("the game was draw")
         if user_choise==0 and computer_choise==2:
           print("user wins")
         elif user_choise==2 and computer_choise==0:
             print("user loose")
         elif user_choise>computer_choise:
             print("user wins")
         elif user_choise<computer_choise:
              print("computer wins")
         another=input("do you want play another game(yes/no)?")
         if another!='yes':
             print("thanks for playing")
             break
         else:
            print("here you go")
    
   
