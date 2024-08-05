from django.urls import path
from . import views


urlpatterns = [

    path("", views.lista_vendedor, name= "lista"),
    path("<int:vendedor_id>/", views.detalhe, name='detalhe'),
    
    # urls crud
    path('add/', views.add_Vendedor, name='Add'),
    path('edit/<int:vendedor_id>/', views.edita_vendedor, name='edit'),
    path('deleta/<int:vendedor_id>/', views.deleta_vendedor, name='delete'),
]