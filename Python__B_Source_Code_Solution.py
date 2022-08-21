

# ------------- Programming Begginers for Python SCS ---------------- #

#Quiz 1
"""
#Boolean
print (10 > 7)
print ('\n')

#String
print (str(73911))
print ('\n')

#Tuple
print (tuple("Thank God it's Friday"))
print ('\n')

#Float
print (float(4302))
print ('\n')

#Int
print (int(3299.35640))
print ('\n')





# Quiz 2


def myVoid():

    name = (str(input("Enter your name: ")))
    age = (int(input("Enter your age: ")))

    # Result

    print ("Your name is: ", name)
    print ("Your age is: ", age)

    #Declare the function

myVoid()



#Quiz 3



print (673 > 343)
print (9021 < 210)
print (45 > 226)
print (44 == 45)



# Quiz 4



name = (input("What is your name?: "))
print (name)

print ("As in: ", (tuple)(name))



# Quiz 5



x = 3.1415
y = int(3.1415)
print (y)



# Quiz 6



number_1 = 223
number_2 = float(number_1)

print (number_2)


# ------------------ CLass - OOP ----------------------


class User:
    pass

# make variable on class

user_1 = User()

# Create an object

user_1.Name = "Jojie"
user_1.lastName = "Bagatua"
user_1.age = 18
user_1.gender = "Male"

# print out what u want just declare the object variable
#Example:

print (user_1.Name,"\n",user_1.lastName)


# Create another object using the same class

user_2 = User()

user_2.Name = "Larcy"
user_2.lastName = "La Luna"
user_2.age = 17
user_2.gender = "Female"

print (user_2.Name,"\n",user_2.lastName)



# Create and Access the class var

class Person:
    gender = "Male"

human = Person()

print (human.gender)



# Quiz 6

class Customers:
    
    greeting = "Welcome to the Coffee Palace!"
    print (greeting)

c_1 = Customers()

c_1.Name = "Samirah"
c_1.Beverage = "Ice caffe latte"
c_1.Food = "Cinamon roll"
c_1.Total = 225

print (c_1.Beverage)
print ('\n')

c_2 = Customers()

c_2.Name = "Jerry"
c_2.Beverage = "Caramel macchiato"
c_2.Food = "Glazed doughnut"
c_2.Total = 230

print (c_2.Food)


# Arithmetic function


print ("1. ",217 * 6)
print ("2. ", 600 + 35234)
print ("3. ", 67 // 12)
print ("4. ", 56329 % 982)
print (float("5. ", 34 ** 5))


# Quiz 7

my_age = 22
mom_age = 61
sister_age = 29

print (mom_age < sister_age and my_age == 22)
print (mom_age == 61)
print (mom_age > 34 or sister_age == 22)
print (mom_age >= 54)
print (not(mom_age <= 400,my_age == 22))


#Quiz 8

x = 4345
y = 953

print (x + y)


#Quiz 9

x = 324

print (x == 210 and x < 527)


#Quiz 10


class Car:

    looks = "Cool!"

Audi = Car()

print (Audi.looks)


#Quiz 11


num1 = 9

print (num1 ** 5)




#Quiz 12


amount_of_soaps = 33
amount_of_towels = 33

print (amount_of_soaps != amount_of_towels)



#Quiz 13 --- Conditional Statement

x = 322
y = 2031

if x >= y:
    print ("x is greater than or equal to y")

elif x == y:
    print ("X is equal to Y")
else:
    print ("X is less than Y")



# Loop functions
# Looooooooooooooooooooooooooooooop
x = range(20)

for i in x :
    print (i)
 
names = ["Jojie", "Larcy", "Iceee", "Polard"]

a = range (20)

for a in names:
    print (a)
    

myloop = True

while myloop != False:
    print ("HEHE")
if  myloop== 20:
    myloop = False
    print ("End")
   
    

    #---------- pause --------#


# Quiz 13 - For Loop

furniture = ["Table", "Chair", "Cabinet", "Desk", "Couch"]

for x in furniture:
    if x == "Cabinet":
        continue
    print (x)


# Quiz 14 - While loop

i = 1

while i < 15:
    print (i)
    i+=1
else:
    print ("i is no longer less than 15")

    

#Quiz 15

clothes = ["shirt", "sock", "pants", "gloves", "shoes"]

for x in clothes:
    print (x)
    if x == "pants":
        break
        

#Quiz 16

t = 132
u = 151

if t > u:
    print("t is greater than u.")

elif t < u:
    print ("t is less than u.")

    


#Quiz 17


people = ["doctor", "teacher", "neighbor"]
adjectives = ["friendly", "kind", "smart"]

for x in people:
    for y in adjectives:

        print (x,y)
        

#Quiz 18

g = 29
h = 11

print (g%h)

#Quiz 19

cat = 53
dog = 45

if cat > dog:

    print ("Im a cat person")
    

#Quiz 20

name = "Jojie"

print (tuple(name))

"""

# --------------------- END OF MY COURSE ----------------------- #