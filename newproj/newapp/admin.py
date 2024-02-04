from django.contrib import admin
from .models import User, Payment

class UserAdmin(admin.ModelAdmin):

    list_display = ['uchastok', 'vladelec', 'area']
    search_fields = ['vladelec', 'uchastok']

    def __str__(self):
        return self.name

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'purpose_of_payment', 'the_amount']
    list_filter = ['date', 'user']
    search_fields = ['purpose_of_payment', 'user__vladelec']

admin.site.register(User, UserAdmin)
admin.site.register(Payment, PaymentAdmin)
