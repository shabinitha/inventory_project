from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length =200)
    description = models.CharField(max_length = 500)

    class Meta:
        unique_together = ("name", )

    def __str__(self):
            return self.name

class Location(models.Model):
    name = models.CharField(max_length =200)
    description = models.CharField(max_length = 500)

    class Meta:
        unique_together = ("name", )

    def __str__(self):
        return self.name

class ProductMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    qty = models.IntegerField()
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True, related_name='movements_from')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True, related_name='movements_to')
    timestamp = models.DateTimeField(auto_now_add=True)

    def formatted_timestamp(self):
        return date(self.timestamp, "F j, Y, P")

    def __str__(self):
        movement_description = f"Movement of {self.qty} (QTY) {self.product.name} at {self.formatted_timestamp()}"
    
        if self.from_location:
            movement_description += f" from {self.from_location.name}"
        
        if self.to_location:
            movement_description += f" to {self.to_location.name}"
        
        return movement_description

class ProductLocation(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')
    qty = models.IntegerField()
   

    def __str__(self):
        return  f"{self.product.name} in {self.location.name} has  {self.qty} (QTY)"