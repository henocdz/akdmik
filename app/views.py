from django.shortcuts import render, render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout

@login_required
def home(request):
	return render_to_response('index.html',{'user': request.user }, RequestContext(request))

def logoout(request):
	logout(request)
	return redirect('/')

class Login(View):
	template_name = 'login.html'
	def get(self,request):
		if request.user.is_authenticated():
			return redirect('/')

		return render_to_response(self.template_name, None, RequestContext(request))

	def post(self,request):
		print "POSTEANDOANDO"
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


