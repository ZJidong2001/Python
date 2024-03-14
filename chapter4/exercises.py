# 练习4.1
pizzas = ['Seafood pizza', 'Sausage pizza', 'Cheese pizza', 'Beef pizza', 'Corn pizza', 'Chicken pizza']
for pizza in pizzas:
    print(f"I like {pizza.lower()}.")
print("I really love pizza!")


# 练习4.2
animals = ['cat', 'dog', 'bird', 'rabbit']
for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")
print("All of these animals would make a great pet!")


# 练习4.3
for num in range(1, 21):
    print(num)


# 练习4.4
nums = list(range(1, 1_000_001))
for num in nums:
    print(num)


# 练习4.5
nums = list(range(1, 1_000_001))
print(min(nums))
print(max(nums))
print(sum(nums))


# 练习4.6
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)


# 练习4.7
numbers_divided_by3 = list(range(3, 31, 3))
for number_divided_by3 in numbers_divided_by3:
    print(number_divided_by3)


# 练习4.8
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)


# 练习4.9
cubes = [value**3 for value in range(1, 11)]


# 练习4.10
pizzas = ['Seafood pizza', 'Sausage pizza', 'Cheese pizza', 'Beef pizza', 'Corn pizza', 'Chicken pizza']
print(f"The first three items in the list are: {pizzas[:3]}")
print(f"Three items from the middle of the list are: {pizzas[(0+len(pizzas)-1)//2-1:(0+len(pizzas)-1)//2+2]}")
print(f"The first three items in the list are: {pizzas[-3:]}")


# 练习4.11
pizzas = ['Seafood pizza', 'Sausage pizza', 'Cheese pizza', 'Beef pizza', 'Corn pizza', 'Chicken pizza']
friend_pizzas = pizzas[:]
pizzas.append('Pepperoni pizza')
friend_pizzas.append('Fruit pizza')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)


# 练习4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)
print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)


# 练习4.13
foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
for food in foods:
    print(food)
foods[3] = 'shit'  # 尝试修改元组的元素会报错
foods = ('pizza', 'spaghetti', 'carrot cake', 'cannoli', 'fried chicken')
for food in foods:
    print(food)