class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class Human:
    def speak(self):
        return "Hello"

def make_sound(entity):
    # No type checking, only behavior matters
    print(entity.speak())

make_sound(Human())
make_sound(Dog())