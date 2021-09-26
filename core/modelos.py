# from django.db.models.deletion import CASCADE
# from core.views import upload
# import uuid
# from datetime import date
# from django.db import models
# from stdimage import StdImageField, JPEGField
# from django.contrib.auth.models import BaseUserManager, AbstractUser


# def get_file_path(_instance, filename):
#     ext = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'
#     return filename
                  
# class UserManager(BaseUserManager):

#     use_in_migration = True

#     def _create_user_manager(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('O E-mail é necessario')

#         email = self.normalize_email(email)
#         user = self.model(email=email, password=password, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user_manager(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('O super usuario precisa ter o atributo is_superuser=True')

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('O super usuario precisa ter o atributo is_staff=True')

#         return self._create_user_manager(email, password, **extra_fields)

# class MyUserAdmin(AbstractUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     dt_expiracao = models.DateTimeField('Data de Expiracao', default=date(year=1900, month=1, day=1))
#     is_staff = models.BooleanField('Menbro da equipe', default=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'dt_expiracao']

#     def __str__(self):
#         return self.email

#     objects = UserManager()

# #------------------------------------------------------------------------------------
# #-------------------------------CLASSES LMS------------------------------------------
# #------------------------------------------------------------------------------------

# class Coordenador(models.Model):
    
#     celular = models.CharField(max_length=20)
#     rc = models.IntegerField(default=0)
#     usuario = models.ForeignKey(MyUserAdmin, on_delete=models.PROTECT, related_name='coordenador_usuario')
#     imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
#     data_expiracao = models.DateField('Data de Expiracao', default=date(year=1900, month=1, day=1))

#     class Meta:
#         verbose_name = 'Coordenador'
#         verbose_name_plural = 'Coordenadores'

#     def __str__(self):
#         return self.usuario.first_name

# class Aluno(models.Model):
#     celular = models.CharField(max_length=20)
#     ra = models.IntegerField()
#     usuario = models.ForeignKey(MyUserAdmin, on_delete=models.PROTECT, related_name='aluno_usuario')
#     imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
#     data_expiracao = models.DateField('Data de Expiracao', default=date(year=1900, month=1, day=1))
    
#     class Meta:
#         verbose_name = 'Aluno'
#         verbose_name_plural = 'Alunos'
        
#         permissions = [('aluno_access', 'alunos_change')]
        

#     def __str__(self):
#         return self.usuario.first_name

# class Professor(models.Model):
#     celular = models.CharField(max_length=20)
#     rp = models.IntegerField()
#     usuario = models.ForeignKey(MyUserAdmin, on_delete=models.PROTECT, related_name='professor_usuario')
#     imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
#     data_expiracao = models.DateField('Data de Expiracao', default=date(year=1900, month=1, day=1))

#     class Meta:
#         verbose_name = 'Professor'
#         verbose_name_plural = 'Professores'

#     def __str__(self):
#         return self.usuario.first_name

# class Curso(models.Model):
#     nome = models.CharField(max_length=255)
#     descricao = models.TextField(max_length=2000, default=None)
#     destaque = models.CharField(max_length=255, default=None)
#     mercado_trabalho = models.TextField(max_length=1000)
#     coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE, default=None)
#     imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 1500, 'height': 500, 'crop': True}})
#     imagem2 = StdImageField('Imagem dois', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
    
#     class Meta:
#         verbose_name = 'Curso'
#         verbose_name_plural = 'Cursos'

#     def __str__(self):
#         return self.nome

# class Turma(models.Model):
#     A = 'A'
#     B = 'B'
#     C = 'C'
#     D = 'D'
#     escolha_turma = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'),]
    
#     turma = models.CharField(max_length=4, choices=escolha_turma)
#     curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = 'Turma'
#         verbose_name_plural = 'Turmas'

#     def __str__(self):
#         return self.turma

# class Disciplina(models.Model):
#     ABERTO = 'AB'
#     FECHADO = 'FC'

#     escolha_status = [(ABERTO, 'Aberto'), (FECHADO, 'Fechado')]

#     nome = models.CharField(max_length=255, unique=True)
#     data = models.DateField()
#     status = models.CharField(max_length=2, choices=escolha_status, default=ABERTO)   
#     plano_ensino = models.TextField(max_length=5000)
#     carga_horaria = models.IntegerField()
#     competencias = models.TextField(max_length=1000)
#     habilidades = models.TextField(max_length=1000)
#     ementa = models.TextField(max_length=5000)
#     Conteudo_programatico = models.TextField(max_length=5000)
#     bibliografia_basica = models.TextField(max_length=1000)
#     bibliografia_complementar = models.TextField(max_length=1000)
#     percentual_pratico = models.DecimalField(max_digits=13, decimal_places=2)
#     percentual_teorico = models.DecimalField(max_digits=13, decimal_places=2)

#     class Meta:
#         verbose_name = 'Disciplina'
#         verbose_name_plural = 'Disciplinas'

#     def __str__(self):
#         return self.nome

# class DisciplinaOfertada(models.Model):
#     turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
#     disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
#     professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
#     coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
#     curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
#     dt_inicio = models.DateField()
#     dt_fim = models.DateField()
#     ano = models.IntegerField()
#     semestre = models.IntegerField()
#     metodologia = models.TextField(max_length=255)
#     recursos = models.TextField(max_length=255)
#     criterio_avaliacao = models.TextField(max_length=1000)
#     plano_aula = models.TextField(max_length=1000)
    

#     class Meta:
#         unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')
#         verbose_name_plural = 'Disciplinas Ofertadas'

#     def __str__(self):
#         return self.disciplina.nome

# class Atividade(models.Model):
#     titulo = models.CharField(max_length=255, unique=True)
#     descricao = models.TextField(max_length=255)
#     conteudo = models.TextField(max_length=255)
#     tipo = models.TextField(max_length=255)
#     extras = models.TextField(max_length=255)
#     professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = 'Atividade'
#         verbose_name_plural = 'Atividades'

#     def __str__(self):
#         return self.titulo

# class AtividadeVinculada(models.Model):
#     ABERTA = 'ABERTA'
#     FECHADA = 'FECHADA'
#     PRORROGADA = 'PRORROGADA'
    
#     AC1 = 'AC1'
#     AC2 = 'AC2'
#     AC3 = 'AC3'
#     AC4 = 'AC4'
#     AC5 = 'AC5'
#     AC6 = 'AC6'
#     AC7 = 'AC7'
#     AC8 = 'AC8'
#     AC9 = 'AC9'
#     AC10 = 'AC10'

#     escolha_status = [
#                     (ABERTA, 'Aberta'),
#                     (FECHADA, 'Fechada'),
#                     (PRORROGADA, 'Prorrogada'),]
    
#     escolha_atividade = [(AC1, 'AC1'),
#                          (AC2, 'AC2'),
#                          (AC3, 'AC3'),
#                          (AC4, 'AC4'),
#                          (AC5, 'AC5'),
#                          (AC6, 'AC6'),
#                          (AC7, 'AC7'),
#                          (AC8,  'AC8'),
#                          (AC9, 'AC9'),
#                          (AC10, 'AC10')]

#     status = models.CharField(max_length=15, choices=escolha_status)
#     atividade_vinculada = models.CharField('Atividade Complementar', max_length=4, choices=escolha_atividade, default=AC1)
#     rotulo = models.CharField(max_length=255)
#     dt_inicio = models.DateField('Data Inicio', default=date(year=1900, month=1, day=1))
#     dt_fim = models.DateField('Data Fim', default=date(year=1900, month=1, day=1))
#     atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
#     professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
#     disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name_plural = 'Atividades Vinculadas'

#     def __str__(self):
#         return self.rotulo

# class EntregaAtividade(models.Model):
#     ENTREGUE = 'EN'
#     CORRIGIDO = 'CO'

#     escolha_status = [(ENTREGUE, 'Entregue'), (CORRIGIDO, 'Corrigido')]

#     titulo = models.CharField(max_length=100)
#     resposta = models.TextField(max_length=255)
#     dt_entrega = models.DateField()
#     status = models.CharField(max_length=2, choices=escolha_status, default=ENTREGUE)
#     nota = models.DecimalField(max_digits=5, decimal_places=2)
#     dt_avaliacao = models.DateField()
#     obs = models.TextField(max_length=255)
#     aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
#     atividade_vinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.PROTECT)
#     professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
#     file = models.FileField(upload_to='file', null=True, blank=True)

#     class Meta:
#         verbose_name_plural = 'Entrega das Atividades'

#     def __str__(self):
#         return self.atividade_vinculada.atividade.titulo

# class Mensagem(models.Model):
#     ENVIADO = 'EN'
#     LIDO = 'LI'
#     RESPONDIDO = 'RE'

#     escolha_status = [(ENVIADO, 'Enviado'), (LIDO, 'Lido'), (RESPONDIDO, 'Respondido')]

#     assunto = models.TextField(max_length=255)
#     referencia = models.TextField(max_length=255)
#     conteudo = models.TextField(max_length=255)
#     status = models.CharField(max_length=3, choices=escolha_status)
#     dt_envio = models.DateField()
#     dt_resposta = models.DateField()
#     resposta = models.TextField(max_length=1000)
#     aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
#     professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name_plural = 'Mensagens'

#     def __str__(self):
#         return self.assunto


# class SolicitacaoMatricula(models.Model):
#     SOLICITADA = 'SO'
#     REJEITADA = 'RE'
#     APROVADA = 'AP'
#     CANCELADA = 'CA'

#     escolha_status = [(SOLICITADA, 'Solicitada'),
#                     (REJEITADA, 'Rejeitada'),
#                     (APROVADA, 'Aprovada'),
#                     (CANCELADA, 'Cancelada'),]

#     dt_solicitacao = models.DateField()
#     status = models.CharField(max_length=4, choices=escolha_status, default=SOLICITADA)
#     aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
#     curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None)
#     coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
#     #disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    
#     class Meta:
#         verbose_name_plural = 'Solicitação de Matricula'

#     def __str__(self):
#         return self.status


# class Matricula(models.Model):
#     ATIVA = 'AV'
#     CANCELADA = 'CA'
#     TRANCADA = 'TA'
#     ANALISE = 'AE'

#     escolha_situacao = [
#         (ATIVA, 'Ativa'),
#         (CANCELADA, 'Cancelada'),
#         (TRANCADA, 'Trancada'),
#         (ANALISE, 'Analise')
#         ]

#     dt_inicio = models.DateField()
#     dt_fim = models.DateField()
#     status = models.CharField(max_length=4, choices=escolha_situacao, default=ANALISE)
#     aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
#     curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None)
#     turma = models.ForeignKey(Turma, on_delete=models.PROTECT, default=None)
#     solicitacao_matricula = models.ForeignKey(SolicitacaoMatricula, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = 'Matricula'
#         verbose_name_plural = 'Matriculas'

#     def __str__(self):
#         return self.status

# class Photo(models.Model):
#     photo = models.ImageField('foto', upload_to='')
#     usuario = models.ForeignKey(MyUserAdmin,
#     on_delete=models.CASCADE, 
#     related_name='photos')

#     class Meta:
#         ordering = ('pk')
#         verbose_name = 'foto'
#         verbose_name_plural = 'fotos'

#     def __str__(self):
#         return str(self.user)

