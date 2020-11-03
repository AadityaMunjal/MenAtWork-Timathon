from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<int:pk>/', views.update_task, name='update_task'),  
    path('delete_task/<int:pk>/', views.delete, name='delete_task'),
    path('how-to/', views.howTo, name='how-to'),
]
