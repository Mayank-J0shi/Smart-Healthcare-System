from django.contrib import admin
from .models import Report
from .models import description
# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)

admin.site.register(Report)
admin.site.register(description)