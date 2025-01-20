class Orderserializer:
    @staticmethod
    def serializer(order):
        return{
            "order_id":order.order_id,
            "customer_name":order.customer_name,
            "email":order.email,
            "products":order.products,
            "additional_fields":order.additional_fields
        }