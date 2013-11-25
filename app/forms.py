from django import forms
from app.models import *

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = AUser
		fields = ['username', 'nombre', 'ap_paterno', 'ap_materno', 'fecha_nacimiento', 'sexo']

class MateriaForm(forms.ModelForm):
	class Meta:
		model = Materia
		
class GrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo

class GrupoForm(forms.ModelForm):
	class Meta:
		model = Clase