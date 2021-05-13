from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer, UserSerializerWithTOken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithTOken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data 
   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getuserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEmployee(request, pk):
    employee = Employee.objects.get(userid=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)
