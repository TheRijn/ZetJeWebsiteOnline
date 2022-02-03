from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Listing, Category, Bid, User


admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(User, UserAdmin)
