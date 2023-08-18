from django.db import models


class MenuItem(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='menu_iamges/')
    price=models.DecimalField(max_digits=7,decimal_places=2)
def __str__(self):
    return self.name

class OrderModel(models.Model):
    created_on=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    items=models.ManyToManyField('MenuItem',related_name='order',blank=True)
def __str__(self):
    return f'Order: {self.created_on.strftime("%b %d %I:%M %p")}'