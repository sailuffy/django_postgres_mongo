from django.urls import path,include
from .mongo_views import Orderview
from rest_framework.routers import DefaultRouter
from .views import Departmentviewset, Employeeviewset,Registerview
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register(r'departments',Departmentviewset)
router.register(r'employess',Employeeviewset)

urlpatterns=[
    
    path("api/login",TokenObtainPairView.as_view(),name="login"),
    path("api/refresh",TokenRefreshView.as_view(),name="Refresh_token"),
    path("register",Registerview.as_view(),name="register_view"),
    path("orders/",Orderview.as_view(),name='order-list'),
    path('',include(router.urls))
] 
