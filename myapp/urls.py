from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('templates/myapp/register.html', views.move_to_registration, name='move_to_registration'),
    path('templates/myapp/result.html', views.move_to_result, name='move_to_result')
]