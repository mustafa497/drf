from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.employeeCreate, name='employee-create'),
]