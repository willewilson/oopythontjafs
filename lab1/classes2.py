#!/usr/bin/env python3
class Cat():

    def __init__(self, name , eye_color, lives_left = -1):
        self.name = name
        self.eye_color = eye_color
        self.lives_left = lives_left

    def catInfo(self):
        return "My cats name is {} and has {} eyes.".format(self.name, self.eye_color)

    def catLives(self):
        return self.lives_left

    def set_lives_left(self, lives_left):
        self.lives_left = lives_left
