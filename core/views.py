from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView
from core.models import Curso, DisciplinaOfertada, Aluno


class IndexView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'core/index.html'
    
    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursoImg1'] = Curso.objects.order_by('?')[:3]
        context['cursoImg'] = Curso.objects.order_by('?')[:6]
        return context

class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'core/curso.html'

    def get_queryset(self):
        self.nome = get_object_or_404(Curso, pk=self.kwargs['pk'])
        return Curso.objects.filter(nome=self.nome)

    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        context['disciplinaofertadaS1'] = DisciplinaOfertada.objects.filter(curso=self.nome.id).filter(semestre=1)

        return context

class AlunoDetailView(DetailView):
    model = Aluno
    context_object_name = 'aluno_list'
    template_name = 'core/aluno.html'

    def get_queryset(self):
        self.nome = get_object_or_404(Aluno, pk=self.kwargs['pk'])
        return Aluno.objects.filter(id=self.nome.id)

    def get_context_data(self, **kwargs):
        context = super(AlunoDetailView, self).get_context_data(**kwargs)
        #context['disciplinas'] = DisciplinaOfertada.objects.filter(solicitacaomatricula__aluno__id=self.nome.id)
        #context['disciplinas'] = DisciplinaOfertada.objects.filter(curso=self.nome.id)

        return context

class UsuarioView(TemplateView):
    template_name = 'core/usuario.html'