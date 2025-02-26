from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class UOM(models.Model):
    uom_id = models.AutoField(primary_key=True)
    uom_name = models.CharField(max_length=100)  
    class Meta:
        db_table = 'uom'

    def __str__(self):
        return self.uom_name  

class Product(models.Model):
    product_id = models.AutoField(primary_key=True) 
    product_name = models.CharField(max_length=100) 
    uom = models.ForeignKey('UOM', on_delete=models.CASCADE, db_column='uom_id')
    class Meta:
        db_table = 'products'  
    def __str__(self):
        return self.product_name  

from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=255)   
    total = models.FloatField()                    
    order_datetime = models.DateTimeField(auto_now_add=True)  

    class Meta:
        db_table = 'orders'  

    def __str__(self):
        return f"Order {self.order_id} - {self.cust_name}"


   
class OrderDetail(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, db_column='order_id'
    )  
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, db_column='product_id'
    )  
    quantity = models.FloatField()       
    total_price = models.FloatField()    

    class Meta:
        db_table = 'order_details' 
        unique_together = (('order', 'product'),) 
        

    def __str__(self):
        return f"Order {self.order_id} - Product {self.product_id}"
