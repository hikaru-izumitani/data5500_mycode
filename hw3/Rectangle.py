"""
I didn't need to use ChatGPT to make Rectangle.py
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

a = Rectangle(5,3)
print(a.area())