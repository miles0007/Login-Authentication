# from django.https import HttpResponse
from django.shortcuts import redirect

def unaunth_user(view_func):
	def wrapper_func(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request,*args,**kwargs)

	return wrapper_func