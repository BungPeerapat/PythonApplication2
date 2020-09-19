
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


### การบ้านหาค่าสูงสุดใน List

#listnumber = [1,54,4,87,4,5,7,6,98,6,45,87,243,987,1,]
#listmax = 0

#print(listnumber)
#print("=================================")
#for n in listnumber:
#    print("=================================")
#    print(n)
#    print("=================================")
#    if n > listmax:
#        listmax = n
#        print(n)
#print("=================================")
#print("Max Number in listnumber is : " , listmax)

##///////////////////////////////////////////// หาค่าตัวเลข


##หาเบอร์โทรใน Database


#phonenumber = ['Bung', '0619506364'],['Pa1pai', '0995554456']

#def Selectnumber(s):
#    for n in phonenumber:
#        name = n[0]
#        phone = n[1]
#        if s == name:
#            print(phone)
#            break
#s = input("Inputname : ")
#Selectnumber(s)

##หาเบอร์โทรใน Database

##หาชื่อต่ามเบอร์โทรใน Database
phonenumber = ['Bung', '0619506364'],['Pa1pai', '0995554456']

def Selectname(n):
    for p in phonenumber:
        name = p[0]
        phone = p[1]
        if n == phone:
            print(name)
            break

n = input("inputphone : ")
Selectname(n);

##หาชื่อต่ามเบอร์โทรใน Database