from django.urls import path
from .views import IndexView, CursoDetailView, AlunoDetailView, UsuarioView


app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoDetailView.as_view(), name='aluno'),
    path('usuario/', UsuarioView.as_view(), name='usuario')
]