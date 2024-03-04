class Rectangle:
    def __init__(self, width, height):
        if width > 0:
            self.width = width
        else:
            raise AttributeError
        if height > 0:
            self.height = height
        else: 
            raise AttributeError
            

    def get_area(self):
        if self.width < 0 or self.height < 0:
            return -1
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height