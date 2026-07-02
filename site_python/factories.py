import factory  # O motor principal. É a biblioteca Factory Boy que cria as estruturas das fábricas.
from faker import Factory as FakerFactory  # Biblioteca Faker, usada para gerar dados falsos realistas (nomes, textos, e-mails).

from django.contrib.auth.models import User  # Importa o modelo de Usuário padrão do próprio Django.
from django.utils.timezone import now  # Ferramenta do Django para pegar a data/hora atual correta (com fuso horário).

from site_python.models import Post  # O modelo que VOCÊ criou! A fábrica precisa dele para saber como é a estrutura de um Post.

faker = FakerFactory.create()  # Liga o motor do Faker. A partir daqui, a variável 'faker' consegue gerar qualquer dado aleatório.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User  # Avisa o Factory Boy: "Esta fábrica foi feita para construir objetos do modelo User (do Django)".

    # Define o campo email com um formato de e-mail seguro e falso (ex: usuario@example.net)
    email = factory.Faker("safe_email")
    
    # Define o username dinamicamente. O 'LazyAttribute' e o 'lambda' dizem para o Python:
    # "Não use o mesmo nome sempre. Toda vez que eu chamar a fábrica, execute 'faker.name()' e gere um nome novo".
    username = factory.LazyAttribute(lambda x: faker.name())

    # IMPORTANTE: Este método abaixo é o "pulo do gato" para senhas no Django!
    @classmethod
    def _prepare(cls, create, **kwargs):
        # 1. Tenta pegar a senha dos argumentos (se você passou uma). Se não passou, deixa nulo.
        password = kwargs.pop("password", None)
        
        # 2. Chama a criação padrão do Django para criar o usuário com os outros campos (username, email).
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        
        # 3. O Django NÃO guarda senhas em texto puro por segurança; ele precisa criptografá-las (fazer o hash).
        # É exatamente isso que esse bloco faz: se houver uma senha, ele a criptografa usando 'set_password()'.
        if password:
            user.set_password(password)
            if create:
                user.save()  # Salva o usuário com a senha criptografada no banco de dados de teste.
            return user
        

class PostFactory(factory.django.DjangoModelFactory):
    # Usa o LazyAttribute para gerar um título falso aleatório (uma frase/sentença do Faker) para cada post.
    title = factory.LazyAttribute(lambda x: faker.sentence())
    
    # Preenche o campo de data de criação com o momento exato em que o post está sendo gerado no teste.
    created_on = factory.LazyAttribute(lambda x: now())
    
    # O SUPERPODER DO FACTORY BOY: Relacionamentos (Chave Estrangeira / ForeignKey)
    # Um Post precisa obrigatoriamente de um Autor (User). 
    # O 'SubFactory(UserFactory)' diz: "Django, quando eu criar um Post e não disser quem é o autor, 
    # use automaticamente a fábrica de usuários acima para criar um usuário novo e amarrar como autor deste post".
    author = factory.SubFactory(UserFactory)
    
    # Define o status padrão do post como 0 (geralmente usado para 'Rascunho' em blogs).
    status = 0

    class Meta:
        model = Post  # Avisa o Factory Boy: "Esta fábrica foi feita para construir objetos do SEU modelo Post".