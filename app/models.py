# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, _user_has_module_perms
from app.managers import AUserManager
# Create your models here.
class AUser(AbstractBaseUser,PermissionsMixin):
	username = models.CharField(max_length=12, verbose_name='Boleta / ID', unique=True, db_index=True)
	email = models.EmailField(null=True, blank = True, default = None, verbose_name = 'Correo Electrónico')
	nombre  =  models.CharField(max_length=40)
	ap_paterno = models.CharField(max_length=40, verbose_name='Apellido Paterno')
	ap_materno = models.CharField(max_length=40, verbose_name='Apellido Materno')
	fecha_nacimiento = models.DateField(default="1993-01-01")
	sexo = models.CharField(max_length=1,choices=(('M','Masculino'),('F','Femenino')))
	estado = models.SmallIntegerField(choices=((0,'Suspendido'),(1,'Regular'),(2,'Irregular')), default=1)
	tipo = models.SmallIntegerField(choices = (
			(0,'Administrador'),
			(1, 'Alumno'),
			(2, 'Profesor'),
			(3, 'Tutor'),
		), default=1)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	USERNAME_FIELD = "username"
	objects = AUserManager()
	clases = models.ManyToManyField('Clase')

	def get_full_name(self):
		return self.nombre + ' ' + self.ap_paterno + ' ' + self.ap_materno
	def get_short_name(self):
		return self.nombre + ' ' + self.ap_paterno
	def has_perm(self, perm, obj=None):
		if self.is_superuser:
			return True
		return False
	def has_module_perm(self,app_label):
		return True
	@property
	def is_active(self):
		return self.active
	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	def __unicode__(self):
		return self.username +  ' - ' +  self.get_full_name()

	class Meta:
		verbose_name = 'alumno o profesor'

class Materia(models.Model):
	keyname = models.CharField(max_length=10, verbose_name="Clave de Materia", unique=True)
	nombre = models.CharField(max_length=100, verbose_name="Nombre", unique=True)

	def __unicode__(self):
		return self.nombre

class Grupo(models.Model):
	nombre = models.CharField(max_length=5, verbose_name="Nombre", unique=True)
	salon = models.CharField(max_length=4, verbose_name="No. Salón", unique=True)
	capacidad = models.IntegerField(verbose_name="Capacidad máxima")

	def __unicode__(self):
		return self.nombre

class Horario(models.Model):
	dia = models.CharField(max_length=10, choices=(
		('L', 'Lunes'),
		('M', 'Martes'),
		('X', 'Miércoles'),
		('J', 'Jueves'),
		('V', 'Viernes'),
		('S', 'Sábado'),
	))
	hora_inicio = models.TimeField()
	hora_fin = models.TimeField()
	clase = models.ForeignKey('Clase')

	class Meta:
		unique_together = ('dia', 'hora_inicio', 'hora_fin', 'clase')

	def getTime(self):
		return str(self.hora_inicio.strftime("%H:%M")) + ' - ' + str(self.hora_fin.strftime("%H:%M"))

	def __unicode(self):
		return self.dia + ' de ' + str(self.hora_inicio.strftime("%H:%M")) + ' a: ' + str(self.hora_fin.strftime("%H:%M"))

class Clase(models.Model):
	materia = models.ForeignKey(Materia, verbose_name="Materia")
	grupo = models.ForeignKey(Grupo, verbose_name="Grupo")
	profesor = models.ForeignKey(AUser, verbose_name="Profesor")
	inscritos = models.IntegerField(blank=True, default=0)

	class Meta:
		unique_together = ('materia', 'grupo', 'profesor')
	
	def link_name(self):
		return self.grupo.nombre+"."+self.materia.nombre.replace(' ','_')

	def horarioLunes(self):
		return Horario.objects.filter(clase=self.pk, dia='L')

	def horarioMartes(self):
		return Horario.objects.filter(clase=self.pk, dia='M')

	def horarioMiercoles(self):
		return Horario.objects.filter(clase=self.pk, dia='X')

	def horarioJueves(self):
		return Horario.objects.filter(clase=self.pk, dia='J')

	def horarioViernes(self):
		return Horario.objects.filter(clase=self.pk, dia='V')

	def horarioSabado(self):
		return Horario.objects.filter(clase=self.pk, dia='S')

	def __unicode__(self):
		return self.materia.nombre + ' .. ' + self.grupo.nombre

class Publicacion(models.Model):
	creador = models.ForeignKey(AUser)
	pertenece = models.ForeignKey(Clase)
	fecha = models.DateTimeField()

	def __unicode__(self):
		return self.creador.username + " - " + self.pertenece.materia.nombre


	def __unicode__(self):
		return self.dia + " - " + self.clase.profesor

class Periodo(models.Model):
	clase = models.ForeignKey(Clase)
	numero = models.SmallIntegerField()
	inicio = models.DateField()
	fin = models.DateField()

	def __unicode__(self):
		return self.numero + ": "+ self.clase.materia.nombre

class Criterio(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=140)
	puntaje = models.FloatField()
	periodo = models.ForeignKey(Periodo)

	def __unicode__(self):
		return self.nombre

class Asistencia(models.Model):
	alumno = models.ForeignKey(AUser)
	clase = models.ForeignKey(Clase)
	fecha = models.DateField()

	def __unicode__(self):
		return self.alumno.username + '-' + self.fecha

class CalificacionCriterio(models.Model):
	alumno = models.ForeignKey(AUser)
	criterio = models.ForeignKey(Criterio)
	puntaje = models.FloatField()

	def __unicode__(self):
		return self.alumno.username 

class Task(models.Model):
	clase = models.ForeignKey(Clase)
	usuario = models.ForeignKey(AUser)
	descripcion = models.CharField(max_length=140)
	due_date = models.DateTimeField()

	def __unicode__(self):
		return self.usuario.username

class Boletin(models.Model):
	admin = models.ForeignKey(AUser)
	titulo = models.CharField(max_length=140)
	texto = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.admin.get_full_name()