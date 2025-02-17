from django.contrib import admin
from .models import Professor, Module, ModuleInstance, ProfessorModule, Rating

admin.site.register(Professor)
admin.site.register(Module)
admin.site.register(ModuleInstance)
admin.site.register(ProfessorModule)
admin.site.register(Rating)