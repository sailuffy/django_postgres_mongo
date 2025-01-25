from .models import Department , Employee
from rest_framework import serializers
from django.contrib.auth.models import User

class Register_serializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    def validate(self, data):
        if data['password1']!=data['password2']:
            raise serializers.ValidationError("Password doesn't match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password1=validated_data.pop('password1')
        user=User.objects.create(**validated_data)
        user.set_password(password1)
        user.save()
        return user

        


class Department_serializers(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['id','name']


class Employeeserializers(serializers.ModelSerializer):
    department=serializers.CharField(write_only=True)
    class Meta:
        model=Employee
        fields=['id','name','email','department']

    def create(self, validated_data):
        department_name = validated_data.pop('department')
        
        department, created = Department.objects.get_or_create(name=department_name)
        
        employee = Employee.objects.create(department=department, **validated_data)
        
        return employee
            
        

    