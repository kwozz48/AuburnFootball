# This program allows the user to enter player or coach information for the Auburn football team
# It also writes the input members data to a text file

import os

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name_func (self):
        self.full_name = self.first_name + ' ' + self.last_name
        return (self.full_name)

class Coach (Person): #Inherits from 'Person' class
    def __init__(self, first_name, last_name, age, title, pay, years_as_coach):
        Person.__init__(self, first_name, last_name, age)
        self.title = title
        self.pay = pay
        self.years_as_coach = years_as_coach

    def apply_bonus (self):
        bonus = int(self.years_as_coach * .01 * self.pay)
        self.pay = self.pay + bonus
        self.bonus = bonus

        #2 ways to print the statement. Second way is commented out
        return ("\n{}'s base salary is ${}. {}'s bonus is ${}\n".format(self.full_name_func(), self.pay, self.full_name_func(), (bonus)))
        #print ("%s's bonus is $%s" % (self.full_name_and_pay(), self.pay))

class Player (Person): #Inherits from 'Person' class
    def __init__(self, first_name, last_name, age, position, height, weight):
        Person.__init__(self, first_name, last_name, age)
        self.position = position
        self.height = height
        self.weight = weight

    def print_info (self):
        print ("\n{} is a {} for the Auburn University football team. He is {} years old, {} ft tall, and {} lbs.\n".format(self.full_name_func(), self.position, self.age, self.height, self. weight))

def create_database ():
    #Creates text file with header for stored data
    database_header = ['First Name   ', '   Last Name   ', '   Age   ']
    file = open("auburn_database.txt", 'w')
    for i in database_header:
        file.write(i)
    file.close()

def add_member_to_database(*args):
    #Adds members data to text file
    file = open('auburn_database.txt', 'a')
    file.write('\n')
    for i in args:
        file.write('   ' + i + '  ')
    file.close()
'''
#Section is commented out. It is included to save time while testing/writing code
Gus_Malzahn = Coach('Gus', 'Malzahn', 52, 'Head Coach', 7000000, 7)
print(Gus_Malzahn.apply_bonus())
Jarrett_Stidham = Player('Jarrett', 'Stidham', 24, 'QB', "6'"'2"', 215)
print(Jarrett_Stidham.print_info())
create_database()
add_member_to_database(Gus_Malzahn.first_name, ' ', Gus_Malzahn.last_name, str(Gus_Malzahn.age))
'''

#Allows you to manually enter coaches' and players' info. Commented out to save time when testing program
coaches = []
players = []

num_new_members = int(input('Please enter the number of new members: '))

new_members = list(range(1, num_new_members))
a = 0

while a < num_new_members:
    for i in new_members:
        new_person_job = input("\nBegin entering the new member's information. Enter 'coach' for a new coach or 'player' for a new player: ")

        if new_person_job.lower() == 'coach':
            coach_first_name = input("Enter the coach's first name: ")
            coach_last_name = input("Enter the coach's last name: ")
            coach_age = int(input("Enter the coach's age: "))
            title = input("Enter the coach's title: ")
            salary = int(input("Enter the coach's salary: "))
            years_as_coach = int(input("Enter years that the coach has been with Auburn University: "))
            i = Coach(coach_first_name, coach_last_name, coach_age, title, salary, years_as_coach)
            coaches.append(i)
            a += 1

        elif new_person_job.lower() == 'player':
            player_first_name = input("Enter the player's first name: ")
            player_last_name = input("Enter the player's last name: ")
            player_age = int(input("Enter the player's age: "))
            position = input("Enter the player's position: ")
            height = str(input("Enter the player's height."))
            weight = int(input("Enter the player's weight: "))
            i = Player(player_first_name, player_last_name, player_age, position, height, weight)
            players.append(i)
            a += 1

        else:
            print ("You did not enter 'coach' or 'player'.")
            break

print (coaches[0].full_name_func())
print (coaches[0].apply_bonus())
create_database()
#Writes info to data file
add_member_to_database(coaches[0].first_name, ' ', coaches[0].last_name, str(coaches[0].age))
print (players[0].full_name_func())
print (players[0].print_info())
create_database()
#Writes info to data file
add_member_to_database(players[0].first_name, ' ', players[0].last_name, str(players[0].age))
