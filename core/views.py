from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from .models.my_user_admin import MyUserAdmin
from .models.curso import Curso
from .models.coordenador import Coordenador
from .models.aluno import  Aluno
from .models.professor import Professor
from .models.disciplina import Disciplina
from .models.disciplina_ofertada import DisciplinaOfertada
from .models.turma import Turma
from .models.atividade_vinculada import AtividadeVinculada
from .models.atividade import Atividade
from .models.entrega_atividade import EntregaAtividade
from .models.mensagem import Mensagem
from .models.solicitacao_matricula import SolicitacaoMatricula
from .models.matricula import Matricula
from .models.photo import Photo
                
from .forms import EntregaAtividadeForm

from .uploads_files import handle_uploaded_file

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
        context['disciplinaofertadaS2'] = DisciplinaOfertada.objects.filter(curso=self.nome.id).filter(semestre=2)
        context['disciplinaofertadaS3'] = DisciplinaOfertada.objects.filter(curso=self.nome.id).filter(semestre=3)
        context['disciplinaofertadaS4'] = DisciplinaOfertada.objects.filter(curso=self.nome.id).filter(semestre=4)

        return context

class AlunoDetailView(DetailView):
    model = MyUserAdmin
    context_object_name = 'aluno_list'
    template_name = 'core/aluno.html'

    def get_queryset(self):
        self.user = get_object_or_404(MyUserAdmin, pk=self.kwargs['pk'])
        return MyUserAdmin.objects.filter(id__exact=self.user.id)

    def get_context_data(self, **kwargs):
        context = super(AlunoDetailView, self).get_context_data(**kwargs)
        context['aluno'] = Aluno.objects.get(usuario__email__exact=self.user)
        #context['atividades'] = EntregaAtividade.objects.filter(aluno__usuario__email__exact=self.user)
        #context['atividades'] = EntregaAtividade.objects.filter(atividade_vinculada__disciplina_ofertada__semestre__exact=1)
        
        context['atividades1'] = EntregaAtividade.objects.filter(atividade_vinculada__atividade_vinculada__exact="AC1").filter(atividade_vinculada__disciplina_ofertada__semestre__exact=1)
        context['atividades2'] = EntregaAtividade.objects.filter(atividade_vinculada__atividade_vinculada__exact="AC2").filter(atividade_vinculada__disciplina_ofertada__semestre__exact=1)
        
        context['atividades3'] = AtividadeVinculada.objects.filter(disciplina_ofertada__turma__turma="A")

        context['disciplinas'] = DisciplinaOfertada.objects.filter(semestre=1)
        context['mensagens'] = Mensagem.objects.filter(aluno__usuario__email__exact=self.user)
        #context['disciplinas'] = DisciplinaOfertada.objects.filter(aluno__usuario__email__exact=self.user)
        #context['notas'] = DisciplinaOfertada.objects.filter(aluno=self.nome)
        
        return context
    
class BoletimAluno(DetailView):
    model = MyUserAdmin
    context_object_name = 'aluno_list'
    template_name = 'core/boletim.html'
    
    def get_queryset(self):
        self.user = get_object_or_404(MyUserAdmin, pk=self.kwargs['pk'])
        return MyUserAdmin.objects.filter(id__exact=self.user.id)

    def get_context_data(self, **kwargs):
        context = super(BoletimAluno, self).get_context_data(**kwargs)
        context['aluno'] = Aluno.objects.get(usuario__email__exact=self.user)
        context['matricula'] = SolicitacaoMatricula.objects.get(aluno__usuario__email__exact=self.user)
        #context['curso'] = SolicitacaoMatricula.objects.get(aluno__usuario_email__exact=self.user)
        
        return context
    
    
class ProfessorDetailview(DetailView):
    model = MyUserAdmin
    context_object_name = 'professor_list'
    template_name = 'core/professor.html'
    
    def get_queryset(self):
        self.user = get_object_or_404(MyUserAdmin, pk=self.kwargs['pk'])
        return MyUserAdmin.objects.filter(id__exact=self.user.id)
    
class CoordenadorDetailView(DetailView):
    model = MyUserAdmin
    context_object_name = 'coordenador_list'
    template_name = 'core/coordenador.html'
    
    def get_queryset(self):
        self.user = get_object_or_404(MyUserAdmin, pk=self.kwargs['pk'])
        print('Saida: ', self.user.id)
        return MyUserAdmin.objects.filter(id__exact=self.user.id)
    
    def get_context_data(self, **kwargs):
        context = super(CoordenadorDetailView, self).get_context_data(**kwargs)
        context['coordenador'] = Coordenador.objects.get()
        
        return context
    

class UsuarioView(TemplateView):
    template_name = 'core/usuario.html'
    

def upload(request):
    if request.method == "POST":
        form = EntregaAtividadeForm(request.POST, request.FILES)
        if form.is_valid():    
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'core/aluno.html', {'msg':'Arquivo enviado com sucesso. '})
    else:
        form = EntregaAtividadeForm()
    return render(request, 'core/aluno.html', {'msg':'Arquivo não enviado.'})
    
def my_login(request):
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    
    return verifica_user(request, user)
    

def verifica_user(request, user):
    if user.is_superuser:
        login(request, user)
        return redirect('coordenador')
    elif user.is_staff:
        login(request, user)
        return redirect('aluno')
    return render(request, 'core/index.html')