from django.db import models


type_gender = (('M','Male'),('F','Female'))
type_event = (('G','Games'),('A','Athletics'))

class Programme(models.Model):
    name = models.CharField(max_length=20)  


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