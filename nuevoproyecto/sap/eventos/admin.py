from django.contrib import admin

from eventos.models import Cliente, Tipo, Adicional, Notific

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tipo)
admin.site.register(Adicional)
admin.site.register(Notific)


