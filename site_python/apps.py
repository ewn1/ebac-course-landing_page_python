from django.apps import AppConfig  # Importa a classe base de configuração de aplicativos do Django.


# Define a classe de configuração específica para o SEU aplicativo.
class SitePythonConfig(AppConfig):
    # O tipo de campo de chave primária padrão que o Django vai usar nas tabelas deste app (como o id do Post).
    # O BigAutoField gera números inteiros grandes (64-bit), garantindo que seu site possa ter bilhões de posts sem estourar o limite.
    default_auto_field = 'django.db.models.BigAutoField'

    # O nome real e único do seu aplicativo dentro do projeto.
    # É por causa dessa linha que o Django sabe quem é o 'site_python' quando você o lista lá no settings.py.
    name = 'site_python'