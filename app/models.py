from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    