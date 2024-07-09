from django.contrib import admin
from .models import Сarbohydrates

# Register your models here.


@admin.register(Сarbohydrates)
class СarbohydratesAdmin(admin.ModelAdmin):
    list_display = ['user', 'cur_sugar', 'carbohydrate', 'cur_time']