from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from .models import contact_form
from .forms import form_input
# Create your views here.

def create_form(request):
	form = form_input()
	if request.method == 'POST' and 'contact_form' in request.POST:
		form = form_input(request.POST)
		if form.is_valid():
			contact_form.objects.create(**form.cleaned_data)
			all_id = contact_form.objects.all()
			last_id = 0
			for i in all_id:
				last_id = i.id
			return redirect('contact_form/view/'+last_id)
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