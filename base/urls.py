from django.urls import path
from . import views



urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', views.getuserProfile, name='users-profile'),

    path('employee/create/', views.employeeCreate, name='employee-create'),
    path('employees/', views.getEmployees, name='employees'),
    path('employee/<str:pk>/', views.getEmployee, name='employee'),
]