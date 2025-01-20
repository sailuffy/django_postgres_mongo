from mongoengine import Document,StringField,ListField,DictField

class Order(Document):
    order_id= StringField(required=True,unique=True)
    customer_name=StringField(required=True)
    email=StringField(required=True)
    products=ListField(DictField())
    additional_fields=DictField()