from django.contrib import admin
from .models import GeneralInfo, Profile

# Register your models here.
admin.site.register(GeneralInfo)
admin.site.register(Profile)