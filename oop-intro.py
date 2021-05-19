class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def Area(self):
        print("I am a: "+ self.name + "\n" +
              "I have " + self.side + "sides")

obj_shape=Shapes("shape", "so many")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def Area(self):
        result = self.length * self.width
        return result

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        result = self.radius *self.radius* 3.14
        return result

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        result = 0.5 * self.base * self.height
        return result

obj_book=Rectangle(10, 7)
obj_screen=Rectangle(5, 7)
obj_orange=Circle(5)
obj_samoosa=Triangle(3, 5)

print("The area of a book is " + str(obj_book.Area()))
print("The area of a book is " + str(obj_screen.Area()))
print("The area of an Orange is " + str(obj_orange.Area()))
print("The area of a Samoosa is " + str(obj_samoosa.Area()))
