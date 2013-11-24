#-*-encoding:utf-8-*-
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from app.decorators import admin_required
from app.forms import *
from app import models as AMod
import unicodedata
@login_required
def home(request):
	return render_to_response('index.html',{'user': request.user }, RequestContext(request))

@login_required
@admin_required
def alumnos(request):
	alls = AMod.AUser.objects.all().filter(tipo = 1, active=True).order_by('nombre')
	return render_to_response('alumnos-all.html', {'user': request.user, 'alumnos': alls}, RequestContext(request))

def logoout(request):
	logout(request)
	return redirect(reverse('home'))

@login_required
@admin_required
def alumnosEliminar(request, id):
	try:
		alumni = AMod.AUser.objects.get(pk=id)
	except:
		return redirect(reverse('alumnos'))

	if not alumni.is_admin:
		alumni.active = False
		alumni.save()

	return redirect(reverse('alumnos'))

class AlumnoNuevoView(View):
	template_name = 'alumnos.html'

	@method_decorator(login_required)
	@method_decorator(admin_required)
	def get(self,request):
		AForm = AlumnoForm()
		return render_to_response(self.template_name,{'user': request.user, 'form': AForm }, RequestContext(request))

	@method_decorator(login_required)
	@method_decorator(admin_required)
	def post(self,request):
		AForm = AlumnoForm(request.POST)

		if AForm.is_valid():
			AForm.save()

			user = AMod.AUser.objects.get(username=request.POST['username'])
			password = (user.ap_paterno[0:2] + user.ap_materno[0:1] + user.nombre[0:1] + user.fecha_nacimiento.strftime("%y%m%d"))
			password = password.lower()
			password = ''.join((c for c in unicodedata.normalize('NFD', password) if unicodedata.category(c) != 'Mn'))
			password = password.upper()
			print "\n\n\n" + password
			user.set_password(str(password))
			user.save()

			return redirect(reverse('alumnos'))
		return render_to_response(self.template_name,{'user': request.user, 'form': AForm }, RequestContext(request))

class AlumnoEditarView(View):
	template_name = 'alumnos-editar.html'

	@method_decorator(login_required)
	@method_decorator(admin_required)
	def get(self,request,id):
		try:
			i = AUser.objects.get(pk=id)
		except:
			return redirect(reverse('home'))

		AForm = AlumnoForm(instance=i)
		return render_to_response(self.template_name,{'user': request.user,'id_e':id, 'form': AForm }, RequestContext(request))

	@method_decorator(login_required)
	@method_decorator(admin_required)
	def post(self,request,id):

		try:
			i = AUser.objects.get(pk=id)
		except:
			return redirect(reverse('home'))

		AForm = AlumnoForm(request.POST, instance=i)

		if AForm.is_valid():
			AForm.save()
			return redirect(reverse('alumnos'))

		return render_to_response(self.template_name,{'user': request.user,'id_e':id, 'form': AForm }, RequestContext(request))


class LoginView(View):
	template_name = 'login.html'
	def get(self,request):
		if request.user.is_authenticated():
			return redirect('/')

		return render_to_response(self.template_name, None, RequestContext(request))

	def post(self,request):
		p = request.POST
		usr = p['user']
		pwd = p['password']
		if usr == "" or pwd == "":
			return render_to_response(self.template_name,{'error': 'Datos no validos'}, RequestContext(request))
		user = authenticate(username=usr, password = pwd)
		if user is None:
			return render_to_response(self.template_name,{'error': 'Nombre o usuario incorrectos'}, RequestContext(request))
		if not user.is_active:
			return render_to_response(self.template_name,{'error': 'Activa tu cuenta para continuar'}, RequestContext(request))
		login(request,user)
		if 'next' in request.GET:
			return redirect(request.GET['next'])
		else:
			return redirect('/')


