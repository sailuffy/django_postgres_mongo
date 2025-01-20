from django.http import JsonResponse
from .mongo_models import Order
from .mongo_serilaizers import Orderserializer
from rest_framework.views import APIView
import json

class Orderview(APIView):
    def get(self,request):
        orders=Order.objects.all()
        data=[Orderserializer.serializer(order) for order in orders]
        return JsonResponse(data,safe=False)
    
    def post(self,request):
        try:
            data=json.loads(request.body)
            order=Order(**data)
            order.save()

            return JsonResponse({"message":"order created order","ordre":Orderserializer.serializer(order)},status=201)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=400)