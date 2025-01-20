from django.urls import path,include
from .mongo_views import Orderview
from rest_framework.routers import DefaultRouter
from .views import Departmentviewset, Employeeviewset

router=DefaultRouter()
router.register(r'departments',Departmentviewset)
router.register(r'employess',Employeeviewset)

urlpatterns=[
  
    path("orders/",Orderview.as_view(),name='order-list'),
    path('',include(router.urls))
] 
