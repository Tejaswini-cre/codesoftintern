def calculator():
  while True:

    try:
        a=int(input("enter the first number"))
        b=int(input("enter the secomd number"))
        c=input("enter the operation +,_,*,/,//")
        if c=='+':
            print(f"result is {a+b}")
        elif c=='-':
            print(f"result is {a-b}")
        elif c=='*':
            print(f"result is {a*b}")
        elif c=='/':
            print(f"result is {a/b}")
        elif c=='//':
            print(f"result is {a//b}")
        else:
            print('invalid input')
        another=input("do you want to continue another operation(yes/no)")
        if another!='yes':
            print("thank you!you are existing now")
            break
        else:
            print("please continue the task")
            


    except ZeroDivisionError:
        print("any number divisible by 0 its given infinity")
    except ValueError:
        print("string is not available")
    finally:
        print("thank you for the task")
calculator()
        
         
