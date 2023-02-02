from . models import *
from django.contrib import admin

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodadmin)