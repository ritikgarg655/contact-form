from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from .models import contact_form
# Create your views here.

def create_form(request):
	form = contact_form()
	if request.method == 'POST':
		form = contact_form(request.POST)
		if form.is_valid():
			contact_form.objects.create(**form.cleaned_data)
			return redirect('/view/')
		else:
			print("invalid input")
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