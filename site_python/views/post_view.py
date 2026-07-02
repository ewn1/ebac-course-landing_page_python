from django.http import HttpResponse  # A ferramenta que empacota uma resposta de texto/HTML para enviar ao navegador.
from django.views import generic      # O pacote do Django que traz as estruturas prontas de Views em formato de Classe.


# Padrão CBV (Class-Based View):
# Criamos a nossa classe 'PostView' herdando de 'generic.View'.
# Isso diz ao Django: "Essa classe vai controlar a inteligência de uma das páginas do nosso blog".
class PostView(generic.View):
    
    # O Método 'get':
    # O Django é inteligente. Se o usuário entrar na página apenas para "ler/visualizar" (Requisição GET),
    # o framework vai ignorar tudo e executar especificamente esta função 'get'.
    #
    # Argumentos:
    # - request: É o objeto que carrega as informações de quem está acessando (IP, navegador, dados do usuário).
    # - *args e **kwargs: São os "portões abertos" do Python para aceitar qualquer parâmetro extra que venha da URL (como o ID de um post).
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")  # Retorna uma resposta de texto simples para o navegador.