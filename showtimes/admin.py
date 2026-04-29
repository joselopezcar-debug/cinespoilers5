from django.contrib import admin
from .models import Showtime  # NUEVO

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'start_time', 'room', 'price')