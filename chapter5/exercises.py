# 练习5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


# 练习5.2
str1 = 'China'
str2 = 'china'
print(str1 == str2)
print(str1.lower() == str2.lower())
num1 = 22
num2 = 50
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
age = 14
education = 'High school graduation'
if age >= 18 and education == 'High school graduation':
    print("You can fall in love!")
if age < 18 or education != 'High school graduation':
    print("You can't fall in love!")
names = ['Eric', 'John', 'Alice', 'Tom']
print('John' in names)
print('Frank' not in names)


# 练习5.3
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")


# 练习5.4
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")


# 练习5.5
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


# 练习5.6
age = 22
if age < 2:
    print("baby")
elif 2 <= age < 4:
    print("child")
elif 4 <= age < 13:
    print("youngster")
elif 13 <= age < 18:
    print("teenager")
elif 18 <= age < 65:
    print("middle ager")
else:
    print("old people")


# 练习5.7
favorite_fruits = ['apple', 'banana', 'orange']
if 'apple' in favorite_fruits:
    print("YOu really like apples!")
if 'grape' in favorite_fruits:
    print("YOu really like grapes!")
if 'orange' in favorite_fruits:
    print("YOu really like oranges!")
if 'watermelon' in favorite_fruits:
    print("YOu really like watermelons!")
if 'cherry' in favorite_fruits:
    print("YOu really like cherries!")


# 练习5.8
users = ['david', 'tom', 'admin', 'tony', 'bob']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")


# 练习5.9
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")


# 练习5.10
current_users = ['David', 'Tom', 'admin', 'Tony', 'bob']
new_users = ['Bob', 'ross', 'tom', 'Kevin', 'scott']
current_users_copy = [current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f"The username {new_user} is already in use. Please enter a different username.")
    else:
        print(f"The username {new_user} is not in use, you can use it.")


# 练习5.11
nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")