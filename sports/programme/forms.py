from django.forms import ModelForm
from .models import Programme, Event, House, Student

class ProgrammeForm(ModelForm):
    class Meta:
        model = Programme
        fields = ['name',]

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['programme','name','typeOfEvent','typeOfGender'] 

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['name']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name','gender','reg_no','event','house']