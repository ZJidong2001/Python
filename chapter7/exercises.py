# 练习7.1
car = input("Please tell me what kind of car you would like to rent? ")
print(f"\nLet me see if I can find you a {car.title()}.")


# 练习7.2
number = input("Please tell me how many people would like to have a meal? ")
number = int(number)
if number > 8:
    print("\nThere is no available table for dining.")
else:
    print("\nHave a table available for dining.")


# 练习7.3
number = input("Enter a number, and I'll tell you if it can be divided by 10: ")
number = int(number)
if number % 10 == 0:
    print(f"\nThe number {number} can be divided by 10.")
else:
    print(f"\nThe number {number} can't be divided by 10.")


# 练习7.4
prompt = "Please enter the pizza toppings you want to add:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    print(f"\nAdding {pizza_topping}.")


# 练习7.5
prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif 3 <= age < 12:
            price = 10
        else:
            price = 15
        print(f"\nYour admission cost is ${price}.")


# 练习7.6
prompt = "Please enter the pizza toppings you want to add:"
prompt += "\n(Enter 'quit' when you are finished.) "
pizza_topping = ""
while pizza_topping != 'quit':
    pizza_topping = input(prompt)
    if pizza_topping != 'quit':
        print(f"\nAdding {pizza_topping}.")
prompt = "Please enter the pizza toppings you want to add:"
prompt += "\n(Enter 'quit' when you are finished.) "
active = True
while active:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        active = False
    else:
        print(f"\nAdding {pizza_topping}.")
prompt = "Please enter the pizza toppings you want to add:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    print(f"\nAdding {pizza_topping}.")


# 练习7.7
while True:
    print("I love you forever!")


# 练习7.8
sandwich_orders = ['ham', 'edd salad', 'tomato', 'tuna']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been finished:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} Sandwich")


# 练习7.9
sandwich_orders = ['ham', 'pastrami', 'edd salad', 'pastrami', 'tomato', 'tuna', 'pastrami']
print("The pastrami sandwiches have already been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


# 练习7.10
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")