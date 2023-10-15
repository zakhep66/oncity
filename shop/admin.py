from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(Order)
admin.site.register(Value)
