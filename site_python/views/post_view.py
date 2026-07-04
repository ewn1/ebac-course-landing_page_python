from django.http import HttpResponse  # A ferramenta que empacota uma resposta de texto/HTML para enviar ao navegador.
from django.views import generic

from site_python.models.post import Post      # O pacote do Django que traz as estruturas prontas de Views em formato de Classe.


# Padrão CBV (Class-Based View):
# Isso diz ao Django: "Essa classe vai controlar a inteligência de uma das páginas do nosso blog".
class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # Aqui definimos a query que vai buscar os posts no banco de dados, filtrando apenas os ativos (status=1) e ordenando por data de criação decrescente.
    template_name = 'index.html' # Aqui definimos o template que será usado para renderizar a página.

class PostDetail(generic.DetailView):
    model = Post # Aqui definimos o modelo que será usado para buscar os detalhes de um post específico.
    template_name = 'post_detail.html'  # Aqui definimos o template que será usado para renderizar a página de detalhes do post.