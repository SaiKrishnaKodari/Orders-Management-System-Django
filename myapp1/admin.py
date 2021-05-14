from django.contrib import admin
from .import models
# Register your models here.
# admin.site.register(models.customerentry)
class customerentryAdmin(admin.ModelAdmin):
    ordering = ()
    list_display=('Customername','id')
    search_fields=[]
    readonly_fields=[]
    filter_horizontal=()
    list_filter=[]
    fieldsets=()
admin.site.register(models.customerentry,customerentryAdmin) 
admin.site.register(models.Mobilemodel) 
# admin.site.register(models.CustomUser) 
class customerAdmin(admin.ModelAdmin):
    ordering = ()
    list_display=('Name','Email')
    search_fields=[]
    readonly_fields=[]
    filter_horizontal=()
    list_filter=[]
    fieldsets=()
admin.site.register(models.customer,customerAdmin) 
