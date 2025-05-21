from django.urls import path
from.import views
from django.contrib import admin
urlpatterns = [
    
    path('',views.WeekPage,name='week'),
    path('/monday',views.mondayPage,name='monday'),
    path('/tuesday',views.tuesdayPage,name='tuesday'),
    path('/wednesday',views.wednesdayPage,name='wednesday'),
    path('/thursday',views.thursdayPage,name='thursday'),
    path('/friday',views.fridayPage,name='friday'),
    path('/saturday',views.saturdayPage,name='saturday'),
    path('/sunday',views.sundayPage,name='sunday'),
    

]
