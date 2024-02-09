#!/usr/bin/python3

class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor that initializes a Rectangle instance
        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal string representation of a Rectangle
        with the # character"""
        if self.height == 0 or self.width == 0:
            return ''
        rec_str = ''
        for a in range(self.height):
            for b in range(self.width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of Rectangle

        Args:
        value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of Rectangle

        Args:
        value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value


    def area(self):
        """Calculates the area of a Rectangle instance

        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance

        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
    