from django import forms
from app.models import *
from django.contrib.auth import get_user_model

Usuario = get_user_model()
class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ['username', 'nombre', 'ap_paterno', 'ap_materno', 'fecha_nacimiento', 'sexo']

class MateriaForm(forms.ModelForm):
	class Meta:
		model = Materia

class GrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo

class ClaseForm(forms.ModelForm):
	class Meta:
		model = Clase
		exclude = ['inscritos']
	def __init__(self,*args, **kwargs):
		super(ClaseForm, self).__init__(*args,**kwargs)
		self.fields['profesor'].queryset = AUser.objects.filter(tipo=2)

class BoletinForm(forms.ModelForm):
	class Meta:
		model = Boletin
		fields = ['titulo','texto']

class HorarioForm(forms.ModelForm):
	class Meta:
		model = Horario
		widgets = {
			'hora_inicio': forms.TextInput(attrs={'class': 'timeI'}),
			'hora_fin': forms.TextInput(attrs={'class': 'timeI'})
		}