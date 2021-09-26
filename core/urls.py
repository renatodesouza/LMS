from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from .views import IndexView, CursoDetailView, CoordenadorDetailView, AlunoDetailView, UsuarioView, ProfessorDetailview, BoletimAluno, my_login


app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', TemplateView.as_view(template_name='core/index2.html'), name='index2'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoDetailView.as_view(), name='aluno'),
    path('coordenador/<int:pk>/', CoordenadorDetailView.as_view(), name='coordenador'),
    path('professor/<int:pk>/', ProfessorDetailview.as_view(), name='professor'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/index.html'), name='logout'),
    #path('login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('logado/', views.my_login, name='my_login'),
    path('boletim/<int:pk>/', BoletimAluno.as_view(), name="boletim"),
    path('upload/', views.upload, name="upload"),
    #path('photo/create/', views.photo_create, name="photo_create"),
]