# Author: Nicholas Hamilton
# GitHub username: haminich
# Date: 2/9/2023

class Taxicab:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.odometer = 0

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer

    def move_x(self, distance):
        self.x_coord += distance
        self.odometer += abs(distance)

    def move_y(self, distance):
        self.y_coord += distance
        self.odometer += abs(distance)
