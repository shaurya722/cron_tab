from django.contrib import admin

from home.models import Document, Test

# Register your models here.
admin.site.register(Test)
admin.site.register(Document)