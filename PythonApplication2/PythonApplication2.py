#x = int(input("Please Input Number : "))
#name = str(input("Your name is : "))
#Age = int(input("Please input Age : "))
#y = int(12)
#z = int(1)

##while z <= y:
##    print(x , " * " , z , " = " , x*z)
##    z = z + 1
    
##    if z == y:
##        print("My Name is {}".format(name))
##        myage = "My Age is {} ".format(Age)

##        print("Your Age is : " + myage[11])

def calculator():

    x = int(input("please input number : "))
    name = str(input("your name is : "))
    age = int(input("please input age : "))
    y = int(12)
    z = int(1)

    while z <= y:
        if name == "Break":
            print(type(name))
            break
    
        if z == y:
            print("my name is {}".format(name))
            myage = "my age is {} ".format(age)

            print("your age is : " + myage[11])
            print("===========================")
            print(x , " * " , z , " = " , x*z)
            z = z + 1
            calculator()

calculator()