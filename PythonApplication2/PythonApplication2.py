
#def calculator():

#    x = int(input("please input number : "))
#    name = str(input("your name is : "))
#    age = int(input("please input age : "))
#    y = int(12)
#    z = int(1)

#    while z <= y:
#        if name == "Break":
#            print(type(name))
#            break
    
#        if z == y:
#            print("my name is {}".format(name))
#            myage = "my age is {} ".format(age)

#            print("your age is : " + myage[11])
#            print("===========================")
#            print(x , " * " , z , " = " , x*z)
#            z = z + 1
#            calculator()

#calculator()

    #///////////////////////////////////////////// หาค่าตัวเลข

##Test
#def guess_number(number):
#    my_number = 47
#    if number > 47:
#        return "Number is so Hight"
#    elif number < 47:
#        return "Number is so Low"
#    elif number == 47:
#        return "This is Your Number."


#while True:

#    x = int(input("Your Number is : "))
#    guess_number(x)
#    res = guess_number(x)
#    if res != "This is Your Number.":
#        print(guess_number)
#        elif guess_number == "This is Your Number."
#            print("This is Your Number")
#            break

#///////////////////////////////////////////// หาค่าตัวเลข


## การบ้านหาค่าสูงสุดใน List

listnumber = [1,54,4,87,4,5,7,6,98,6]
listmax = 0

print(listnumber)
print("=================================")
for n in listnumber:
    if n > listmax:
        listmax = n
print("Max Number in listnumber is : " , listmax)


