from django.db import models

# Create your models here.
## One to One.
## Male can't take more than female also female can't take more than male.
class Female(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name

class Male(models.Model):
    name = models.CharField(max_length=50, null=True)
    girl = models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
            return self.name

    ## on_delete values
    # models.CASCADE, when Male deleted, related Female also will be delted
    # models.PROTECT, when Male deleted, related Female will not delete

## One to Many
## A user can take one or more products
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    content = models.TextField(max_length=5000, null=True)
    image = models.ImageField(upload_to="photos/%y/%m/%d", null=True)
    def __str__(self):
            return self.name

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

## Many to Many
## A viewer can watch one or more videos, also video can be viewed by one or more viewers
class Video(models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
            return self.title

class Viewer(models.Model):
    name = models.CharField(max_length=50, null=True)
    watch = models.ManyToManyField(Video, null=True)
    def __str__(self):
        return self.name
