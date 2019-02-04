#!/usr/bin/env python3
class Cat():

    def __init__(self, name, eye_color, lives_left = -1, nr_of_paws = 4):
        self.name = name
        self.eye_color = eye_color
        self.lives_left = lives_left
        self.nr_of_paws = nr_of_paws
        self.get_nrof_paws = nr_of_paws
        self.get_name = name

    def catInfo(self):
        return "My cats name is {} and has {} eyes.".format(self.name, self.eye_color)

    def catLives(self):
        return self.lives_left

    def set_lives_left(self, lives_left):
        self.lives_left = lives_left

    def description(self):
        return "My cats name is {}, has {} eyes and {} lives left to live.".format(self.name, self.eye_color, self.lives_left)

    def set_nrof_paws(self, nr_of_paws):
        self.nr_of_paws  = nr_of_paws

    def get_nrof_paws(self):
        return self.nr_of_paws

    def nr_of_paws(self):
        return self.nr_of_paws

    def get_name(self):
        return self.name

    def description_two(self):
        return "{} has {} paws".format(self.get_name, self.nr_of_paws)

    def description_three(self):
        return "{} has {} paws but cats have {} paws.".format(self.get_name, self.nr_of_paws, self.get_nrof_paws)

from datetime import datetime

class Duration():

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def info(self):
        return '{:02}-{:02}-{:02}'.format(self.hours, self.minutes, self.seconds)

    def duration_to_sec(self, time_to_convert):
        split_time = time_to_convert.split('-')
        seconds = int(split_time[0]) * 3600 + int(split_time[1]) * 60 + int(split_time[2])
        return seconds
