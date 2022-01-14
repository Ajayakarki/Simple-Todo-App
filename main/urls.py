from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = 'to-do-index'),
    path('update/<int:pk>/',views.update, name = 'to-do-update'),
    path('delete/<int:pk>/',views.delete, name= 'to-do-delete'),
]

