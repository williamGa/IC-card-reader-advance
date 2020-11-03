def restart(main):
    changer = str(input("Would you like to (S)can again? Or change to (Q)uit the program"))
    if changer == "S":
        main()
    else:
        print("See you again")

def error(main):
    print("An error has occur")
    print("Reseting settings")
    main()
def value4(main,error,restart):
    print("Value 4 test")
    goback = str(input("Would you like to change person?  (Y or N"))
    if goback == "Y":
        main()
    elif goback == "N":
        userinfo = str(input("Would you like (S)imple user info or (C)omplex user info?"))
        if userinfo == "S":
         
            restart(main)
            
        elif userinfo == "C":
            print("Name: ")
        else:
            error(main)

    else:
        error(main)
def value3(main,error,restart):

    print("Value 3 test")
    goback = str(input("Would you like to change person?  (Y or N"))
    if goback == "Y":
        main()
    elif goback == "N":
        userinfo = str(input("Would you like (S)imple user info or (C)omplex user info?"))
        if userinfo == "S":
           
            restart(main)
            
        elif userinfo == "C":
            print("Name: ")
        else:
            error(main)

    else:
        error(main)
def value2(main,error,restart):
    print("Value 2 test")
    goback = str(input("Would you like to change person?  (Y or N"))
    if goback == "Y":
        main()
    elif goback == "N":
        userinfo = str(input("Would you like (S)imple user info or (C)omplex user info?"))
        if userinfo == "S":
         
            restart(main)
            
        elif userinfo == "C":
            print("Name: ")
        else:
            error(main)

    else:
        error(main)
def value1(main,error,restart):
    
    goback = str(input("Would you like to change person?  (Y or N)"))
    if goback == "Y":
        main()
    elif goback == "N":
        userinfo = str(input("Would you like (S)imple user info or (C)omplex user info?"))
        if userinfo == "S":
          
            restart(main)
            
        elif userinfo == "C":
       
            restart(main)
        else:
            error(main)

    else:
        error(main)

def cardpro(main,enter):
    if enter == "#Enter number here":
        print("Welcome back VALUE#1")
        value1(main,error,restart)

    elif enter == "#Enter number here":
        print("Welcome back VALUE#2")
        value2(main,error,restart)

    elif enter == "#Enter number here":
        print("Welcome back VALUE#3")
        value3(main,error,restart)

    elif enter == "#Enter number here":
        print("Welcome back VALUE#4")
        value4(main,error,restart)


def main():
    enter=str(input("Please scan your card"))
    cardpro(main,enter)

main()
