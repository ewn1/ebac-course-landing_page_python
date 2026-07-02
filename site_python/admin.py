from django.contrib import admin  # Importa o motor do painel administrativo do Django.
from site_python.models.post import Post  # O jeito mais explícito e seguro é apontar direto para a pasta e o arquivo:

# Para o Post aparecer de verdade no seu painel admin, você precisa adicionar essa linha:
@admin.register(Post)  # Essa linha faz o registro do modelo usando um "Decorator" (o @)
class PostAdmin(admin.ModelAdmin):
    # Quais colunas vão aparecer na tabela de listagem do Admin:
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    
    # Adiciona uma barra de filtros na lateral direita (facilita a vida do cliente):
    list_filter = ('status', 'created_on', 'author')
    
    # Adiciona um campo de busca por título ou pelo conteúdo do post:
    search_fields = ['title', 'content']
    
    # O preenchimento automático do Slug! 
    # Enquanto você digita o título "Meu Primeiro Post", ele digita sozinho no campo slug "meu-primeiro-post"
    prepopulated_fields = {'slug': ('title',)}