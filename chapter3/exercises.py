# 练习3.1
names = ["John", "Bob", "Eric", "David"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])

# 练习3.2
print(f"{names[0].title()}, nice to meet you!")
print(f"{names[1].title()}, nice to meet you!")
print(f"{names[2].title()}, nice to meet you!")
print(f"{names[3].title()}, nice to meet you!")

# 练习3.3
traffic = ["bicycle", "car", "bus", "plane", "motorcycle"]
print(f"Among {traffic[0]} brands, I like Giant.")
print(f"I want a BMW {traffic[1]}.")
print(f"Traveling by {traffic[2]} is very cheap.")
print(f"Traveling by {traffic[3]} is very fast.")
print(f"My friend likes to ride a {traffic[4]}.")


# 练习3.4
names = ["John", "Bob", "Eric", "David"]
print(f"{names[0].title()}, please have dinner with me!")
print(f"{names[1].title()}, please have dinner with me!")
print(f"{names[2].title()}, please have dinner with me!")
print(f"{names[3].title()}, please have dinner with me!")


# 练习3.5
name = 'Eric'
print(f"{name.title()} cannot attend dinner.")
names.remove(name)
names.append('Peter')
print(f"{names[0].title()}, please have dinner with me!")
print(f"{names[1].title()}, please have dinner with me!")
print(f"{names[2].title()}, please have dinner with me!")
print(f"{names[3].title()}, please have dinner with me!")


# 练习3.6
print("I find a larger dining table.")
names.insert(0, "Bill")
names.insert(len(names)//2, "Wendy")
names.append("Linda")
print(f"{names[0].title()}, please have dinner with me!")
print(f"{names[1].title()}, please have dinner with me!")
print(f"{names[2].title()}, please have dinner with me!")
print(f"{names[3].title()}, please have dinner with me!")
print(f"{names[4].title()}, please have dinner with me!")
print(f"{names[5].title()}, please have dinner with me!")
print(f"{names[6].title()}, please have dinner with me!")


# 练习3.7
print("Only two guests can be invited to dinner together.")
name = names.pop()
print(f"{name}, sorry, I can't invite you anymore.")
name = names.pop()
print(f"{name}, sorry, I can't invite you anymore.")
name = names.pop()
print(f"{name}, sorry, I can't invite you anymore.")
name = names.pop()
print(f"{name}, sorry, I can't invite you anymore.")
name = names.pop()
print(f"{name}, sorry, I can't invite you anymore.")
print(f"{names[0].title()}, please have dinner with me!")
print(f"{names[1].title()}, please have dinner with me!")
del names[0]
del names[0]
print(names)


# 练习3.8
places = ['Shanghai', 'Beijing', 'Tianjin', 'Jinan', 'Nanjing']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


# 练习3.9
names = ["John", "Bob", "Eric", "David"]
print(len(names))


# 练习3.10
apps = ['lol', 'csgo', 'qq', 'wechat', 'music']
print(apps)
apps.append('video')
print(apps)
apps.insert(2, 'safari')
print(apps)
del apps[4]
print(apps)
apps.pop()
print(apps)
apps.pop(1)
print(apps)
apps.remove('safari')
print(apps)
sorted_apps = sorted(apps)
print(sorted_apps)
print(apps)
sorted_apps = sorted(apps, reverse=True)
print(sorted_apps)
apps.sort()
print(apps)
apps.sort(reverse=True)
print(apps)
apps.reverse()
print(apps)
print(len(apps))