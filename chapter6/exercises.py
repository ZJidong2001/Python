# 练习6.1
person = {'first_name': 'Jidong',
          'last_name': 'Zhang',
          'age': 18,
          'city': 'Beijing',
    }
print(f"{person['last_name']} {person['first_name']} {person['age']} {person['city']}")


# 练习6.2
favorite_numbers = {'John': 6,
                    'Alice': 8,
                    'Bob': 5,
                    'David': 1,
                    'Frank': 9,
    }
name = 'John'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")
name = 'Alice'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")
name = 'Bob'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")
name = 'David'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")
name = 'Frank'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")


# 练习6.3
programming_terms = {
    '函数': '子程序',
    '变量': '其值可变',
    '缩进': 'python常用的代码格式',
    '遍历': '挨个访问',
    '枚举': '一一列举',
    }
programming_term = '函数'
print(f"{programming_term}: {programming_terms[programming_term]}")
programming_term = '变量'
print(f"{programming_term}: {programming_terms[programming_term]}")
programming_term = '缩进'
print(f"{programming_term}: {programming_terms[programming_term]}")
programming_term = '遍历'
print(f"{programming_term}: {programming_terms[programming_term]}")
programming_term = '枚举'
print(f"{programming_term}: {programming_terms[programming_term]}")


# 练习6.4
programming_terms = {
    '函数': '子程序',
    '变量': '其值可变',
    '缩进': 'python常用的代码格式',
    '遍历': '挨个访问',
    '枚举': '一一列举',
    }
for key, value in programming_terms.items():
    print(f"{key}: {value}")


# 练习6.5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yellow river': 'china',
    }
for river in rivers:
    print(f"The {river.title()} runs through {rivers[river].title()}.")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())


# 练习6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }
friends = ['edward', 'bob', 'john', 'phil']
for friend in friends:
    if friend in favorite_languages.keys():
        print(f"{friend.title()}, thank you for taking the poll.")
    else:
        print(f"{friend.title()}, please take our poll!")


# 练习6.7
people = []
person = {'first_name': 'Jidong',
          'last_name': 'Zhang',
          'age': 18,
          'city': 'Beijing',
    }
people.append(person)
person = {'first_name': 'Huateng',
          'last_name': 'Ma',
          'age': 35,
          'city': 'Hangzhou',
    }
people.append(person)
person = {'first_name': 'Qinghou',
          'last_name': 'Zong',
          'age': 72,
          'city': 'Guangzhou',
    }
people.append(person)
for people_info in people:
    print(people_info)


# 练习6.8
pets =[]
animal = {
    'breed': 'dog',
    'owner': 'Eric',
    }
pets.append(animal)
animal = {
    'breed': 'cat',
    'owner': 'John',
    }
pets.append(animal)
animal = {
    'breed': 'bird',
    'owner': 'Bob',
    }
pets.append(animal)
for pet in pets:
    print(pet)


# 练习6.9
favorite_places = {}
favorite_places['Eric'] = ['Beijing', 'Shanghai']
favorite_places['Bob'] = ['Jinan']
favorite_places['Frank'] = ['Chengdu', 'Guangdong', 'Chongqing']
for name, place in favorite_places.items():
    print(f"{name}: {place}")


# 练习6.10
favorite_numbers = {'John': [6, 4, 8],
                    'Alice': [2, 5, 7],
                    'Bob': [5],
                    'David': [1, 3, 4, 6],
                    'Frank': [2, 6, 8],
    }
for name in favorite_numbers:
    print(f"{name.title()}: {favorite_numbers[name]}")


# 练习6.11
cities = {
    'Beijing': {
        'country': 'China',
        'population': '2184.3w',
        'fact': 'the capital of China',
        },
    'NewYork': {
        'country': 'America',
        'population': '834w',
        'fact': 'the largest city in the United States',
        },
    'Sydney': {
        'country': 'Australia',
        'population': '503w',
        'fact': 'highly developed financial, manufacturing, and tourism industries',
        },
    }
for city, city_infos in cities.items():
    print(f"{city.title()}:")
    for city_info in city_infos:
        print(f"\t{city_info}: {city_infos[city_info]}")