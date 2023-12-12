#!/usr/bin/python3
'''Square class implementaion module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class implementation'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize the object'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''string representation of the object'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        '''size getter method'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter method'''
        Rectangle.validator("width", value)
        self.width = self.height = value

    def update(self, *args, **kwargs):
        '''update the object attribute'''
        if args:
            attrib = [self.id, self.size, self.x, self.y]
            for i, val in enumerate(args):
                attrib[i] = val
            self.id, self.size, self.x, self.y = tuple(attrib)
        else:
            Rectangle.update(self, **kwargs)
            if "size" in kwargs.keys():
                self.size = int(kwargs["size"])

    def to_dictionary(self):
        '''changing object data to dictionary representation'''
        dict = {key: value for key, value in super().to_dictionary().items()
                if key not in ["width", "height"]}
        dict["size"] = self.width
        return dict
