from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Items(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_item(self):
        return self.save(self)

class Order(models.Model):
    item_id = models.ForeignKey('Items', on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    dispatch = models.BooleanField(default=False)

    def __str__(self):
        return str(self.item_id)

    def save_order(self):
        return self.save(self)
