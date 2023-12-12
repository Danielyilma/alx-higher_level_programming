#!/usr/bin/python3
''''''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''''''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
    
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        Rectangle.validator("width", value)
        self.width = self.height = value
    
    def update(self, *args, **kwargs):
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
        dict = {key:value for key, value in super().to_dictionary().items()
                if key not in ["width", "height"]}
        dict["size"] = self.width
        return dict
