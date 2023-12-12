#!/usr/bin/python3
''''''
from models.base import Base


class Rectangle(Base):
    ''''''
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validator(name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.validator("y", value)
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        if args:
            attrib = [self.id, self.width, self.height, self.x, self.y]
            for i, val in enumerate(args):
                attrib[i] = val
            self.id, self.width, self.height, self.x, self.y = tuple(attrib)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.__dict__["id"] = value
                else:
                    if "_Rectangle__" + key in self.__dict__.keys():
                        self.__dict__["_Rectangle__" + key] = value

    def to_dictionary(self):
        dict = {}
        for key, val in self.__dict__.items():
            dict[key.split("_Rectangle__")[-1]] = val
        return dict