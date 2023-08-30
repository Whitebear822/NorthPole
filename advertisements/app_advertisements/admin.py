from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'description', 'created_date', 'updated_date', 'auction', 'display_image']
    list_filter = ['created_at', 'auction']

admin.site.register(Advertisement, AdvertisementAdmin)