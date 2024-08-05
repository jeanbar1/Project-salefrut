from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_produto, name="lista"),  # Página inicial da lista de produtos
    path("<int:produto_id>/", views.detalhe, name="detalhe"),  # Página de detalhes do produto

    # URLs CRUD
    path('add/', views.add_produto, name='create'),  # Adicionar um novo produto
    path('edit/<int:produto_id>/', views.edita_produto, name='update'),  # Editar um produto existente
    path('delete/<int:produto_id>/', views.deleta_produto, name='delete'),  # Deletar um produto
]
