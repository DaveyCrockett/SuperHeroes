from . import views
from django.urls import path

app_name = 'SuperHeroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:supers_id>/', views.remove_super, name='remove_super'),
    path('<int:supers_id>/', views.details, name='details'),
    path('new/', views.create, name='create_new_super'),
]
