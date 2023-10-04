class Animal:
    def __init__(self):
        print("I am an animal")

    def make_sound(self):
        print("[default animal sound]")


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        print("I am a cat!")

    def make_sound(self, new_sound=None):
        if new_sound:
            print(new_sound)
        else:
            print("meow")


if __name__ == '__main__':
    kitty = Cat()
    kitty.make_sound()
    kitty.make_sound('mew')
