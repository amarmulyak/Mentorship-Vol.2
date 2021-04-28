# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
# human = Celsius(37)

# Get the temperature attribute via a getter
# print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
# print(human.to_fahrenheit())

# Output
# 37
# 98.60000000000001
# Traceback (most recent call last):
#   File "<string>", line 30, in <module>
#   File "<string>", line 16, in set_temperature
# ValueError: Temperature below -273.15 is not possible.


# using property class
class Celsius2:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


# human = Celsius(37)
# print(human.temperature)
# print(human.to_fahrenheit())
# human.temperature = -300

# Output
# Setting value...
# Getting value...
# 37
# Getting value...
# 98.60000000000001
# Setting value...
# Traceback (most recent call last):
#   File "<string>", line 31, in <module>
#   File "<string>", line 18, in set_temperature
# ValueError: Temperature below -273 is not possible


# Using @property decorator
class Celsius3:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
# human = Celsius3(37)
# print(human.temperature)
# print(human.to_fahrenheit())
# coldest_thing = Celsius3(-300)

# Output
# Setting value...
# Getting value...
# 37
# Getting value...
# 98.60000000000001
# Setting value...
# Traceback (most recent call last):
#   File "<string>", line 29, in <module>
#   File "<string>", line 4, in __init__
#   File "<string>", line 18, in temperature
# ValueError: Temperature below -273 is not possible
