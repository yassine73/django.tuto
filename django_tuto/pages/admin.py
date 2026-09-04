from django.contrib import admin
from .models import Male, Female, Product, User, Video, Viewer

# Register your models here.
admin.site.register(Male)
admin.site.register(Female)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Video)
admin.site.register(Viewer)