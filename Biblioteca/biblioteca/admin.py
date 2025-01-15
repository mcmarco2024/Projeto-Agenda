from django.contrib import admin
from .models import Livro, Usuário, Emprestimo

class Livro_Admin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'gênero',
    'data de publicação', 'ISBN', 'descrição',)
    list_display = ('titulo', 'autor',)
    list_per_page = 10
    search_fields = ('titulo',)

admin.site.register (Livro, Livro_Admin)

class Usuário_Admin(admin.ModelAdmin):
    list_display = ('Nome', 'e-mail', 'telefone', papel,)
    list_display_links = ('Nome', 'e-mail',)
    list_per_page = 10

admin.site.register (Usuário, Usuário_Admin)
    
class Empréstimo_Admin(admin.ModelAdmin):
    list_display = ('livro', 'Usuário',)
    list_display_links = ('livro', 'usuários',)
    list_per_page = 10
   
admin.site.register (Empréstimo, Empréstimo_Admin)
    
