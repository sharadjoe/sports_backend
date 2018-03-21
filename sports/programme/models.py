from django.db import models


type_gender = (('M','Male'),('F','Female'))
type_event = (('G','Games'),('A','Athletics'))

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))



class Programme(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
  

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=35)
    typeOfEvent = models.CharField(max_length=1, choices = type_event)
    typeOfGender = models.CharField(max_length=1,choices = type_gender)
    programme = models.ForeignKey('Programme', on_delete = models.CASCADE,)

    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length=1, choices = type_gender)
    reg_no = models.CharField(max_length = 10)
    event = models.ManyToManyField(Event)
    house = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self):
        return self.reg_no