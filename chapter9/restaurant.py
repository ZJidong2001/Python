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