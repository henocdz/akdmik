from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps

def admin_required(f):
	@wraps(f)
	def brain(request, *args, **kwargs):
		#print type(request)

		if not request.user.tipo is 0:	
			return redirect('/')

		return f(request,*args, **kwargs)
	return brain