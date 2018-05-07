from django.urls import path
from school.views import HomePage,registerSchool
app_name='school'

urlpatterns = [
    path('',HomePage.as_view(),name='index'),
    path('registerSchool',registerSchool,name='register_school'),

]
