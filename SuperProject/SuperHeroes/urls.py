from . import views
from django.urls import path

app_name = 'SuperHeroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:supers_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_super')
]
