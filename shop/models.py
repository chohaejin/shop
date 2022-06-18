from django.db import models

# Create your models here.
class Good(models.Model):
    name = models.TextField(max_length=50)
    about = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/', blank=False)

    def __str__(self):
        return self.name

class bottom(models.Model):
    name = models.TextField(max_length=50)
    about = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/', blank=False)

    def __str__(self):
        return self.name

class dress(models.Model):
    name = models.TextField(max_length=50)
    about = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/', blank=False)

    def __str__(self):
        return self.name

class top(models.Model):
    name = models.TextField(max_length=50)
    about = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/', blank=False)

    def __str__(self):
        return self.name

class outer(models.Model):
    name = models.TextField(max_length=50)
    about = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/', blank=False)

    def __str__(self):
        return self.name