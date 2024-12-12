from django.contrib import admin
from fillform.models import MyForm

@admin.register(MyForm)
class MyFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'user_phone', 'order_date', 'lead_text']
    list_filter = ['user_email', 'user_phone', 'order_date']
    search_fields = ['user_email', 'user_phone']

