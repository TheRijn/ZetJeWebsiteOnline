from django.contrib import admin
from .models import Listing, Category, Bid

admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)