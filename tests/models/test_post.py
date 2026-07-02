import pytest  # Importa o Pytest, o motor que vai rodar e validar os nossos testes.

from site_python.factories import PostFactory  # Importa a fábrica de posts que acabamos de traduzir.


# O que é uma @pytest.fixture?
# Pense na fixture como um "preparador de cenário". 
# É uma função que cria objetos ou prepara o ambiente que seus testes vão usar repetidamente.
@pytest.fixture
def post_published():
    # Cria e retorna um post fictício usando a fábrica, mas fixando o título como 'pytest with factory'.
    # Nos bastidores, como vimos na fábrica, ele também cria um usuário falso para ser o autor!
    return PostFactory(title='pytest with factory')


# O que é esse @pytest.mark.django_db?
# É um selo de segurança do Pytest para o Django. Ele avisa: 
# "Atenção Pytest, este teste vai mexer com banco de dados!".
# Sem essa marcação, o Django bloqueia o teste para proteger seu banco de dados real de ser poluído com lixo de teste.
@pytest.mark.django_db
def test_create_published_post(post_published):
    # Nota: Passamos a função 'post_published' (a fixture ali de cima) como argumento do teste.
    # O Pytest é inteligente: ele roda a fixture primeiro, pega o post criado e entrega aqui dentro do teste.

    # O Comando 'assert' (A hora da verdade):
    # Todo teste precisa de uma afirmação. O 'assert' checa se uma condição é verdadeira.
    # Tradução da linha abaixo: "Eu afirmo que o título do post que foi criado é IGUAL a 'pytest with factory'".
    assert post_published.title == 'pytest with factory'