from django.contrib import admin
from .models import Twit

class TwitAdmin(admin.ModelAdmin):
    list_display = ['text', 'twit_from']
admin.site.register(Twit, TwitAdmin)
# Register your models here.
