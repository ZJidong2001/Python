# 练习9.1
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently operating.")
restaurant = Restaurant('KFC', 'fast food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 练习9.2
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently operating.")
restaurant1 = Restaurant('Beijing roast duck', 'Shandong cuisine')
restaurant2 = Restaurant('Lanzhou stretched noodles', 'Northwest cuisine')
restaurant3 = Restaurant('Haidilao', 'Hot Pot')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# 练习9.3
class User:
    def __init__(self, first, last, loc):
        self.first_name = first.title()
        self.last_name = last.title()
        self.location = loc
    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")
    def greeter_user(self):
        print(f'Welcome {self.first_name} {self.last_name} from {self.location}!')
user1 = User('Zhang', 'Jidong', 'Beijing')
user2 = User('albert', 'einstein', 'princeton')
user1.describe_user()
user1.greeter_user()
user2.describe_user()
user2.greeter_user()


# 练习9.4
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently operating.")
    def set_number_served(self, num):
        if num >= self.number_served:
            self.number_served = num
        else:
            print("You can't reduce the number of people already served.")
    def increment_number_served(self, num):
        self.number_served += num
restaurant = Restaurant('KFC', 'fast food')
print(restaurant.number_served)
restaurant.number_served = 1_000
print(restaurant.number_served)
restaurant.set_number_served(2_000)
print(restaurant.number_served)
restaurant.increment_number_served(500)
print(restaurant.number_served)


# 练习9.5
class User:
    def __init__(self, first, last, loc):
        self.first_name = first.title()
        self.last_name = last.title()
        self.location = loc
        self.login_attempts = 0
    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")
    def greeter_user(self):
        print(f'Welcome {self.first_name} {self.last_name} from {self.location}!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user = User('Zhang', 'Jidong', 'Beijing')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)


# 练习9.6
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently operating.")
    def set_number_served(self, num):
        if num >= self.number_served:
            self.number_served = num
        else:
            print("You can't reduce the number of people already served.")
    def increment_number_served(self, num):
        self.number_served += num
class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, 'ice-cream')
        self.flavors = flavors
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor}")
ice_cream_stand = IceCreamStand('Haagen-Dazs', ['chocolate', 'vanilla', 'strawberries'])
ice_cream_stand.show_flavors()


# 练习9.7
class User:
    def __init__(self, first, last, loc):
        self.first_name = first.title()
        self.last_name = last.title()
        self.location = loc
        self.login_attempts = 0
    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")
    def greeter_user(self):
        print(f'Welcome {self.first_name} {self.last_name} from {self.location}!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first, last, loc, privileges):
        super().__init__(first, last, loc)
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
admin = Admin('Zhang', 'Jidong', 'Beijing', ['can add post', 'can delete post', 'can ban user'])
admin.show_privileges()


# 练习9.8
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
class User:
    def __init__(self, first, last, loc):
        self.first_name = first.title()
        self.last_name = last.title()
        self.location = loc
        self.login_attempts = 0
    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")
    def greeter_user(self):
        print(f'Welcome {self.first_name} {self.last_name} from {self.location}!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first, last, loc, privileges):
        super().__init__(first, last, loc)
        self.privileges = Privileges(privileges)
admin = Admin('Zhang', 'Jidong', 'Beijing', ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()


# 练习9.9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("Please fill gas tank!")
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 255
        print(f"This car can go about {range} miles on a full charge.")
    def unprade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")
electric_car = ElectricCar('nissan', 'leaf', 2024)
electric_car.battery.get_range()
electric_car.battery.unprade_battery()
electric_car.battery.get_range()


# 练习9.10
import restaurant
res = restaurant.Restaurant('Beijing roast duck', 'Shandong cuisine')
print(res.describe_restaurant())


# 练习9.11
from user import Admin
admin = Admin('Zhang', 'Jidong', 'Beijing', ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()


# 练习9.12
from admin2 import Admin
admin = Admin('Zhang', 'Jidong', 'Beijing', ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()


# 练习9.13
from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))
die1 = Die()
for i in range(10):
    die1.roll_die()
die2 = Die(10)
for i in range(10):
    die2.roll_die()
die3 = Die(20)
for i in range(10):
    die3.roll_die()


# 练习9.14
from random import choice
my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']
answers = []
i = 0
while i < 4:
    answer = choice(my_list)
    if answer not in answers:
        answers.append(answer)
        i += 1
answers.sort()
print(answers)
print("As long as these four numbers or letters are on the lottery ticket, you will win the big prize")


# 练习9.15
from random import choice
count = 0
my_ticket = ['3', 'a', '2', 'b']
my_ticket.sort()
print(my_ticket)
my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']
while True:
    answers = []
    i = 0
    while i < 4:
        answer = choice(my_list)
        if answer not in answers:
            answers.append(answer)
            i += 1
    answers.sort()
    count += 1
    print(answers)
    if my_ticket == answers:
        break
print(f"Execute {count} cycles to win the jackpot.")