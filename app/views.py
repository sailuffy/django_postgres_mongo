from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Department , Employee
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import Department_serializers,Employeeserializers,Register_serializer

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
    permission_classes=[IsAuthenticated]

class Employeeviewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializers 
    permission_classes=[IsAuthenticated]


class Registerview(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=Register_serializer

    def perform_create(self, serializer):
       self.user= serializer.save()

    def create(self, request, *args, **kwargs):
        serilizer=self.get_serializer(data=request.data)
        serilizer.is_valid(raise_exception=True)   

        self.perform_create(serializer=serilizer)

        response_data={
            "user_id":self.user.id,
            "username":self.user.username,
            "email":self.user.email,
            "message":"Sucessfully user created!!"

        }

        return Response(response_data,status=status.HTTP_201_CREATED)
        

