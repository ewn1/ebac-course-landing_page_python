from django.urls import path
from site_python import views # Importamos a View que criamos

urlpatterns = [
    # Rota da Home:
    # O primeiro argumento '' significa que é a página inicial do blog.
    # O 'PostView.as_view()' transforma a nossa Classe em algo que o sistema de rotas entende.
    # O 'name="home"' é o apelido de ouro que usamos lá no teste com o reverse('home').
    path('', views.PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),  # Rota para detalhes do post, usando slug como identificador.
]