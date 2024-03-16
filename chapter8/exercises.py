# 练习8.1
def display_message():
    """显示本章的主题"""
    print("The theme of this chapter is function.")
display_message()


# 练习8.2
def favorite_book(title):
    """显示我喜欢的书"""
    print(f"One of my favorite books is {title}.")
favorite_book('Alice in Wonderland')


# 练习8.3
def make_shirt(size, printed_words):
    """说明衣服的尺码和字样"""
    print(f"The size of the shirt is {size}, and the printed words are {printed_words}.")
make_shirt('XXL', 'China')
make_shirt(printed_words='hello', size='L')


# 练习8.4
def make_shirt(size='L', printed_words='I love Python'):
    """说明衣服的尺码和字样"""
    print(f"The size of the shirt is {size}, and the printed words are {printed_words}.")
make_shirt()
make_shirt('M')
make_shirt(printed_words='hello')


# 练习8.5
def describe_city(city, country='china'):
    """接受一座城市的名字以及该城市所属的国家"""
    print(f"{city.title()} is in {country.title()}.")
describe_city('Beijing')
describe_city('Shanghai')
describe_city('Reykjavik', 'Iceland')


# 练习8.6
def city_country(city, country):
    """返回城市的名称及所属的国家"""
    return f"{city}, {country}".title()
print(city_country('Beijing', 'China'))
print(city_country('Shanghai', 'China'))
print(city_country('Santiago', 'Chile'))


# 练习8.7
def make_album(singer, album):
    return {'singer': singer, 'album': album}
album1 = make_album('周杰伦', '七里香')
print(album1)
album2 = make_album('刀郎', '山歌寥哉')
print(album2)
album3 = make_album('刘德华', '爱意')
print(album3)
def make_album(singer, album, number=None):
    album = {'singer': singer, 'album': album}
    if number:
        album['number'] = number
    return album
album1 = make_album('周杰伦', '七里香')
print(album1)
album2 = make_album('刀郎', '山歌寥哉', number=11)
print(album2)


# 练习8.8
def make_album(singer, album, number=None):
    album = {'singer': singer, 'album': album}
    if number:
        album['number'] = number
    return album

while True:
    print("\nPlease tell me the singer's name and his album:")
    print("(enter 'q' at any time to quit)")
    singer = input("Singer: ")
    if singer == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break
    print("Please tell me the number of songs on this album.(If you are unsure, please enter 'no'):")
    number = input("Number: ")
    if number == 'q':
        break
    if number == 'no':
        musician = make_album(singer, album)
    else:
        musician = make_album(singer, album, int(number))
    print(musician)


# 练习8.9
def show_messages(messages):
    for message in messages:
        print(message)
messages = ['I', 'love', 'you', 'forever']
show_messages(messages)


# 练习8.10
def send_messages(messages, sent_messages):
    while messages:
        send_message = messages.pop()
        print(send_message)
        sent_messages.append(send_message)
messages = ['I', 'love', 'you', 'forever']
sent_messages = []
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)


# 练习8.11
def send_messages(messages, sent_messages):
    while messages:
        send_message = messages.pop()
        print(send_message)
        sent_messages.append(send_message)
messages = ['I', 'love', 'you', 'forever']
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)


# 练习8.12
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_sandwich('mushrooms')
make_sandwich('olives', 'green peppers')
make_sandwich('peppero', 'pineapple', 'extra cheese')


# 练习8.13
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Zhang', 'Jidong',
                             location='Beijing',
                             field='Artificial Intelligence',
                             university="China Agricultural University")
print(user_profile)


# 练习8.14
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)


# 练习8.15
"""在printing_models.py与printing_functions.py完成"""


# 练习8.16
"""在add.py与main.py完成"""