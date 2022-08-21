

#-------- Intermidiate Python Course SCS--------#


"""
def great_function ():

    print ("Welcome to hawaii!")

    

 #------------------------------------------------------------#



 # __init__ method #


class User:

    def __init__(self, hero, name, level):

        self.hero = hero
        self.name = name
        self.level = level


Account_1 = User ("Mage", "Polard", 573)
Account_2 = User ("MarksMan", "Larcy", 574)

print (Account_1.level, Account_2.hero)



# 1.5 Coding Exercises

class Customers():

    greeting = "Welcome to Caffee Palace!"

    def __init__ (self, name, beverage, food, total):

        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced cafe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

print (Customers.greeting)

print (c_2.name, c_2.beverage, c_2.food, c_2.total)
print (c_4.name, c_4.beverage, c_4.food, c_4.total)



#---------------------------Inheritance__________________#

class User:

    def __init__ (self, username, password):

        self.username = username
        self.password = password


    def displayUser(self):

        print ("-- USER --\n")
        print ("Username: ", self.username)
        print ("Password: ", self.password)


class Admin(User):
    
    def __init__ (self, username, password, code):

        self.code = code
        super().__init__(username, password)


    def displayAdmin(self):

        print ("-- ADMIN --\n")
        print ("Username: ", self.username)
        print ("Password: ", self.password)
        print ("Code: ", self.code)




user_1 = User ("jojie", "01001010")
admin_1 = Admin ("larcy", "010100100", "12345")

user_1.displayUser()
admin_1.displayAdmin()


# 1.9 Coding Exercises


class ClubMembers:

    def __init__(self, name, birthday, age, favorite_food, goal):

        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def Club(self):

        print ("Name: ", self.name)
        print ("Birthday: ", self.birthday)
        print ("Age: ", self.age)
        print ("Favorite Food: ", self.favorite_food)
        print ("Goal: ", self.goal)

class ClubOfficers(ClubMembers):

    def __init__ (self, name, birthday, age, favorite_food, goal, position):

        self.position = position

        super().__init__ (name, birthday, age, favorite_food, goal)

    def Cluboff(self):

            print ("Name: ", self.name)
            print ("Birthday: ", self.birthday)
            print ("Age: ", self.age)
            print ("Favorite Food: ", self.favorite_food)
            print ("Goal: ", self.goal)
            print ("Position: ", self.position)

m_1 = ClubMembers("Tom ", "January 16 ", "14 ", "Ice Cream", "To be happy")
o_4 = ClubOfficers("Vera ", "June 22 ", "16 ", "Beef stroganoff ", "To be the world's greatest chef", "Treasurer\n")

m_1.Club()
o_4.Cluboff()
    
        """






