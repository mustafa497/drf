from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer, UserSerializerWithToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithTOken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data 
   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)

        return Response(serializer.data)
    except:
        message = {'detail': 'User with these credentials already exists.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def getuserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createEmployee(request):
    employee = Employee.objects.create(
        number='Sample Number',
        optin=False,
        userid='Sample userid',
    )

    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateEmployee(request, pk):
    data = request.data
    employee = Employee.objects.get(id=pk)

    employee.number = data['number']
    employee.optin = data['optin']
    employee.userid = data['userid']

    employee.save()

    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteEmployee(request, pk):
    employeeForDeletion = Employee.objects.get(id=pk)
    employeeForDeletion.delete()
    return Response('Employee was deleted')