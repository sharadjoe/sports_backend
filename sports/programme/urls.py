from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addProgramme/', views.add, name = 'add'),
    path('delete/<pk>', views.delete, name = 'delete'),
    path('<pk>', views.addEvent, name = 'programme'),

]
