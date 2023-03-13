from django.contrib import admin

from .models import OnSaleHouse, RentalHouse

# Register your models here.


admin.site.register(OnSaleHouse)
admin.site.register(RentalHouse)