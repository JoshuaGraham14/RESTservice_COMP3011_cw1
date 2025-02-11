from django.contrib import admin
from .models import Professor, Module, Module_Instance, Professor_Module, Rating

admin.site.register(Professor)
admin.site.register(Module)
admin.site.register(Module_Instance)
admin.site.register(Professor_Module)
admin.site.register(Rating)