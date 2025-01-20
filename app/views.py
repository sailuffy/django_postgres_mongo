from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Department , Employee
from .serializers import Department_serializers,Employeeserializers

# class EmployeeListview(APIView):
#     def get(self,request):
#         employess=Employee.objects.all()
#         serializer=Employeeserializers(employess,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=Employeeserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Departmentviewset(viewsets.ModelViewSet):
    queryset=Department.objects.all()   
    serializer_class=Department_serializers

class Employeeviewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializers 




