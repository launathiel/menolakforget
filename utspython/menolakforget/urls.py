from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('subjects/', views.subjects, name='subjects'),
    path('create_assignment/', views.createAssignment, name="create_assignment"),
    path('update_assignment/<str:pk>/', views.updateAssignment, name="update_assignment"),
    path('delete_assignment/<str:pk>/', views.deleteAssignment, name="delete_assignment"),
    path('about/', views.about, name='about'),
]