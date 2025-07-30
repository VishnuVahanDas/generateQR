from django.contrib import admin
from .models import QR


@admin.register(QR)
class QRAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_at')
