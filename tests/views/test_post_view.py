import pytest  # Motor dos nossos testes automatizados.
from django.urls import reverse  # O Localizador de URLs do Django.


# Avisa o Pytest que esse teste precisa acessar o banco de dados (caso a view busque posts, por exemplo).
@pytest.mark.django_db
def test_post_view(client):
    # O que é esse argumento 'client'?
    # É uma fixture nativa do pytest-django. Ela simula um navegador de internet (como Chrome ou Firefox) 
    # invisível dentro do teste, permitindo que a gente faça requisições HTTP para o nosso próprio site.

    # O Comando 'reverse':
    # Em vez de escrever a URL "na mão" (como '/home/'), nós passamos o NOME que demos para a rota.
    # O 'reverse' vai lá no arquivo urls.py, procura quem se chama 'home' e descobre o caminho real.
    # Isso é excelente porque se amanhã você mudar a URL de '/home/' para '/inicio/', o seu teste não quebra!
    url = reverse('home')

    # Simulando o Clique:
    # O "navegador fake" (client) faz uma requisição do tipo GET (de buscar/abrir página) na URL que descobrimos.
    # Ele guarda toda a resposta do servidor (HTML, status, cookies) dentro da variável 'response'.
    response = client.get(url)

    # A Hora da Verdade (Assert):
    # Na internet, o código '200 OK' significa que a página carregou com absoluto sucesso.
    # Tradução da linha: "Eu afirmo que o código de status da resposta do servidor é IGUAL a 200".
    assert response.status_code == 200
    assert b"Hello World!" in response.content # precisa ser b"..." porque o conteúdo da resposta é em bytes, não em string.