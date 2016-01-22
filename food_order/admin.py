from django.contrib import admin
from .models import Food, Order, User
# Register your models here.

class OrderInline(admin.TabularInline):
    model = Order
    extra = 3


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username',            {'fields': ['username']}),
        ('Password non secure', {'fields': ['password']}),
    ]
    inlines = [OrderInline]

admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(Food)
admin.site.register(Order)
