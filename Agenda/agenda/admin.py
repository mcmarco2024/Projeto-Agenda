from .models import contatos
from django.contrib import admin
class Contatos_Admin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereço', 'email',)
    list_display_links = ('nome', 'telefone',)
    list_per_page = 10
    search_fields = ('nome',)

admin.site.register (contatos, Contatos_Admin)

