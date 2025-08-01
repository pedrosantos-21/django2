from django.contrib import admin
from.models import Produto 

#Conceito de Decorator -> Decorator: No Python, um decorator é uma função especial que modifica o comportamento de outra função ou classe.
@admin.register(Produto) #: Esse decorator registra o modelo Produto no Django Admin, associando-o à classe ProdutoAdmin.
# O decorator @admin.register(Produto) registra o modelo Produto no Django Admin usando a configuração da classe ProdutoAdmin.@admin.register(Produto) 
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'ativo', 'slug', 'criado', 'modificado','descricao')
   # search_fields = ('nome',)
    #prepopulated_fields = {'slug': ('nome',)}  # Preenche o campo slug automaticamente com base no nome do produto
    
# Register your models here.
