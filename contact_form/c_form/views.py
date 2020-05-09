from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import contact_form
from .forms import form_input
# Create your views here.

def create_form(request):
	form = form_input()
	
	if request.method == 'POST' and 'contact_form' in request.POST:
		
		form = form_input(request.POST)
		
		if form.is_valid():
			
			varhash = make_password(form.cleaned_data['password'],None,'md5')
			form.cleaned_data['password'] = varhash
			f = contact_form.objects.create(**form.cleaned_data)
			last_id = f.id
			
			return HttpResponseRedirect	('../view/'+str(last_id))
	
	context = {
		"input_form" : form
	}

	return render(request,"create_form.html",context)

def view(request):
	
	details = contact_form.objects.all()
	
	context = {
		'details' : details
	}
	
	return render(request,"view.html",context)

def view_id(request,my_id):
	
	details = get_object_or_404(contact_form,id=my_id)
	context = {
		'details' : details
	}

	return render(request,"view_id.html",context)

def home(request):
	return render(request,"home.html",{})