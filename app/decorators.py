from django.contrib.auth.decorators import login_required

 @login_required
 def admin_required(f):
	@wraps(f)
	def brain(request, *args, **kwargs):
		if not request.user.is_admin:	
			return redirect('/')

		return f(request,*args, **kwargs)
	return brain