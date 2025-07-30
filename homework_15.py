# Task 1

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.first_name.title()} {self.last_name.title()} and I'm {self.age} years old")

first_person = Person("Carl", "Johnson", 26)

first_person.talk()


# Task 2

class Dog:
    age_factor = 7

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


first_dog = Dog("Meow", 5)

print(first_dog.human_age())


# Task 3

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, list_channels):
        self.list_channels = list_channels
        self.current_channel = self.list_channels[0]

    def get_current_channel(self):
        return self.current_channel

    def first_channel(self):
        self.current_channel = self.list_channels[0]
        return self.current_channel

    def last_channel(self):
        self.current_channel = self.list_channels[-1]
        return self.current_channel

    def turn_channel(self, value):
        if  0 < value <= len(self.list_channels):
            self.current_channel = self.list_channels[value-1]
        else:
            raise ValueError
        return self.current_channel

    def next_channel(self):
        if self.list_channels.index(self.current_channel) + 1 < len(self.list_channels):
            self.current_channel = self.list_channels[self.list_channels.index(self.current_channel) + 1]
        elif self.list_channels.index(self.current_channel) + 1 == len(self.list_channels):
            self.current_channel = self.list_channels[0]
        return self.current_channel

    def previous_channel(self):
        self.current_channel = self.list_channels[self.list_channels.index(self.current_channel) - 1]
        return self.current_channel

    def exists(self, value):
        if isinstance(value, str) and value in self.list_channels:
            return "Yes"
        elif isinstance(value, int) and 0 < value <= len(self.list_channels):
            return "Yes"
        else:
            return "No"


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.get_current_channel() == "BBC"

assert controller.exists(4) == "No"

assert controller.exists("BBC") == "Yes"
