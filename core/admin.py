from django.contrib.auth.admin import UserAdmin
from django.contrib import admin 
from .forms import UserCreationForm, UserChangeForm

from .models import MyUserAdmin, Curso, Coordenador, Aluno, Professor, \
    Disciplina, DisciplinaOfertada, Turma, AtividadeVinculada, \
    Atividade, EntregaAtividade, Mensagem, SolicitacaoMatricula

@admin.register(MyUserAdmin)
class CustomUsuarioAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUserAdmin

    fields_set = (
        (None,                      {'fields': ('email', 'password')}),
        ('Informações pessoais',    {'fields': ('first_name', 'last_name', 'dt_expiracao')}),
        ('Permissões',              {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permission')}),
        ('Datas importantes',       {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'first_name', 'last_name', 'email', 'dt_expiracao', 'is_staff')

    def usuario(self, instance):
        return f'{instance.usuario.get_full_name}'

    # def get_queryset(self, request):
    #     qs = super(CustomUsuarioAdmin, self).get_queryset(request)
    #     return qs.filter(email=request.user)

@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados de usuario',            {'fields':('usuario', 'rc', 'imagem')}),
        ('Contato',                     {'fields':('celular',)}),
    ]

    list_display = ('id', 'usuario', 'celular', 'rc', 'usuario', 'imagem')

    def usuario(self, instance):
        return f'{instance.usuario.first_name.get_full_name}'

    
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados de Usuario',            {'fields':('usuario', 'ra', 'imagem')}),
        ('Contato',                     {'fields':('celular',)}),
    ]

    list_display = ('id', 'usuario', 'celular', 'ra', 'usuario', 'imagem')

    def usuario(self, instance):
        return f'{instance.usuario.get_full_name}'

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados do Usuario',            {'fields':('usuario', 'rp', 'imagem')}),
        ('Contato',                     {'fields':('celular',)}),
    ]

    list_display = ('usuario', 'celular', 'rp', 'usuario', 'imagem')

    def usuario(self, instance):
        return f'{instance.usuario.get_full_name}'

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados da turma',          {'fields':('turma', 'curso')}),
        
    ]

    search_fields = ['turma']

    list_display = ('turma', 'curso')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Informações do Curso',            {'fields':('nome', 'destaque', 'descricao', 'mercado_trabalho')}),
    ('Coordenador responsavel',         {'fields':['coordenador']}),
    ('Midia',                           {'fields':('imagem', 'imagem2')}),
    ]

    #Adiociona uma caixa de pesquisa no topo da lista
    search_fields = ['nome']

    #Adiciona os campos como colunas
    list_display = ('nome', 'destaque', 'descricao', 'mercado_trabalho', 'coordenador', 'imagem', 'imagem2')

    #inlines = [TurmaInline]

class DisciplinaOfertadaAdmin(admin.StackedInline):
    model = DisciplinaOfertada
    extra = 1

    fieldsets = [
        ('Responsaveis',        {'fields':('professor', 'coordenador', 'curso')}),
        ('Data',                {'fields':('dt_inicio', 'dt_fim', 'ano', 'semestre')}),
        ('Detalhes',            {'fields':('metodologia', 'recursos', 'criterio_avaliacao', 'plano_aula', 'turma', 'disciplina')}),
    
    ]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Titulo',              {'fields':['nome']}),
    ('Detalhes',            {'fields':('status', 'data', 'carga_horaria', 'plano_ensino', 'competencias', 'habilidades', 'ementa', 'Conteudo_programatico')}),
    (None,                  {'fields':['bibliografia_basica']}),
    (None,                  {'fields':['bibliografia_complementar']}),
    (None,                  {'fields':['percentual_pratico']}),
    (None,                  {'fields':['percentual_teorico']}),
    ]

    search_fields = ['nome']

    list_display = ('nome', 'data', 'status', 'plano_ensino', 'carga_horaria', 'competencias',
    'habilidades', 'ementa', 'Conteudo_programatico', 'bibliografia_basica', 'bibliografia_complementar',
    'percentual_pratico', 'percentual_teorico')

    inlines = [DisciplinaOfertadaAdmin]

# @admin.register(DisciplinaOfertada)
# class DisciplinaOfertadaAdmin(admin.ModelAdmin):
#     fieldsets = [
#     ('Data',                {'fields':('dt_inicio', 'dt_fim', 'ano', 'semestre')}),
#     ('Detalhes',            {'fields':('metodologia', 'recursos', 'criterio_avaliacao', 'plano_aula', 'turma', 'disciplina')}),
#     ('Responsaveis',        {'fields':('professor', 'coordenador', 'curso')}),
#     ]

#     search_fields = ['disciplina']

#     list_display = ('disciplina', 'coordenador', 'professor', 'curso', 'semestre', 'turma', 'dt_inicio', 'dt_fim', 'ano')

class AtividadeVinculadaAdmin(admin.TabularInline):
    model = AtividadeVinculada
    extra = 1

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',              {'fields':('titulo',)}),
        ('Professor',           {'fields':['professor']}),
        ('Detalhes',            {'fields':('descricao', 'conteudo', 'tipo', 'extras')}),
    ]

    search_fields = ['titulo']

    list_display = ('titulo', 'descricao', 'conteudo', 'tipo', 'extras', 'professor')

    list_display_links = ('titulo',)

    inlines = [AtividadeVinculadaAdmin]

# @admin.register(AtividadeVinculada)
# class AtividadeVinculadaAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Disciplina',          {'fields':('disciplina_ofertada',)}),
#         ('Professor',           {'fields':('professor',)}),
#         ('Detalhes',            {'fields':('rotulo', 'status', 'atividade')}),
#         ('Entrega',             {'fields':('dt_inicio', 'dt_fim')}),
        
#     ]

#     search_fields = ['status']

#     list_display = ('status', 'rotulo', 'dt_inicio', 'dt_fim', 'atividade', 'professor', 'disciplina_ofertada')

@admin.register(EntregaAtividade)
class EntregaAtividadeAdim(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',                      {'fields':['titulo']}),
        ('Datas',                       {'fields':('dt_entrega', 'dt_avaliacao' )}),
        ('Participantes',               {'fields':('aluno', 'professor')}),
        ('Informações',                 {'fields':('atividade_vinculada', 'status', 'resposta', 'nota',  )}),
        ('Observacão',                  {'fields':['obs']}),
        ('Anexos',                      {'fields':['file']}),
    ]

    search_fields = ['titulo']

    list_display = ('titulo', 'resposta', 'dt_entrega', 'status', 'nota', 'dt_avaliacao', 'obs', 'aluno', 'atividade_vinculada', 'professor', 'file')

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Assunto',                 {'fields':['assunto']}),
        ('Conteudo',                {'fields':['conteudo']}),
        ('Situação',                {'fields':['status']}),
        ('Data',                    {'fields':['dt_envio', 'dt_resposta']}),
        ('Resposta',                {'fields':['resposta']}),
        (None,                      {'fields':['referencia']}),
        ('Aluno',                   {'fields':['aluno']}),
        ('Professor',               {'fields':['professor']}),
    ]

    search_fields = ['assunto']

    list_display = ('assunto', 'referencia', 'conteudo', 'status', \
         'dt_envio', 'dt_resposta', 'resposta', 'aluno', 'professor')

@admin.register(SolicitacaoMatricula)
class SolicitacaoMatriculaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Curso',                           {'fields':['curso']}),
        ('Coordenador',                     {'fields':['coordenador']}),
        ('Aluno',                           {'fields':['aluno']}),
        ('Data',                            {'fields':['dt_solicitacao']}),
        ('Situação',                        {'fields':['status']}),
    ]

    search_fields = ['dt_solicitacao']

    list_display = ('dt_solicitacao', 'status', 'aluno', 'curso', 'coordenador')



