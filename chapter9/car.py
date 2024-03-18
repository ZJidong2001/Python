class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles


# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()


# class Battery:
#     """一次模拟电动汽车电池的简单尝试"""
#
#     def __init__(self, battery_size=40):
#         """初始化电池的属性"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """打印一条描述电池容量的信息"""
#         print(f"This car has a {self.battery_size}-KWh battery.")
#
#     def get_range(self):
#         """打印一条消息，指出电池的续航里程"""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 255
#
#         print(f"This car can go about {range} miles on a full charge.")
#
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """先初始化父类的属性，再初始化电动汽车特有的属性"""
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         """电动汽车没有油箱"""
#         print("This car doesn't have a gas tank!")