from django.contrib import admin
from django.contrib import admin
from .models import Question,Choice


admin.site.register(Question)
# Register your models here.
admin.site.register(Choice)
