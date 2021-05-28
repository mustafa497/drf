from django.urls import path
from . import views



urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),

    path('users/profile/', views.getuserProfile, name='users-profile'),

    path('employees/', views.getEmployees, name='employees'),
    path('employee/create/', views.createEmployee, name='employee-create'),
    path('employee/<str:pk>/', views.getEmployee, name='employee'),

    path('employee/update/<str:pk>/', views.updateEmployee, name='employee-update'),

    path('employee/delete/<str:pk>/', views.deleteEmployee, name='employee-delete'),
]