from django.contrib import admin
from django.http import HttpResponse

# Register your models here.

from cart.models import Cart
admin.site.register(Cart)

from cart.models import Order_details
admin.site.register(Order_details)

from cart.models import Payment
admin.site.register(Payment)