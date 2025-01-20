from .models import Department , Employee
from rest_framework import serializers

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
            
        

    