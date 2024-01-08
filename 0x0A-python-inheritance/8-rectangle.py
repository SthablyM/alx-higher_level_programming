#!/usr/bin/python3
 class Rectangle(BaseGeometry):
     def __init__(self, width, height):
         self.width = width
         self.height = height

         self.integer_validator("width", width)
         self.integer_validator("height", height)
