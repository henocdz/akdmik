from django.contrib import admin
from app import models as M
# Register your models here.

admin.site.register(M.AUser)
admin.site.register(M.Clase)
admin.site.register(M.Materia)
admin.site.register(M.Grupo)
admin.site.register(M.Boletin)