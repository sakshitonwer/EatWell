from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import UserRegistrationForm
from .models import EmergencyContact, User

# Create your views here.
def index(request):
	# return HttpResponse("Hello world")
	# allergy = Allergy.objects.all()[:10]

	# context = {
	# 	'title': 'Sakshi',
	# 	'allergy': allergy
	# }
	# return render(request, 'allergy/index.html', context)
	# return HttpResponse("HELLO")
	return render(request, 'home/index.html')

def get_user_registration_form(request):
	return render(request, 'home/user_registration_form.html')

def save_user_details(request):
	form = UserRegistrationForm(request.POST)
	print(form.is_valid())
	if form.is_valid():
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		contact = form.cleaned_data['contact']
		user_name = form.cleaned_data['user_name']
		emergency_first_name  = form.cleaned_data['emergency_first_name']
		emergency_last_name = form.cleaned_data['emergency_last_name']
		emergency_contact = form.cleaned_data['emergency_contact']
		emergency_contact_instance = EmergencyContact.objects.create(first_name=emergency_first_name, last_name=emergency_last_name, contact=emergency_contact)
		user_instance = User.objects.create(first_name=first_name, last_name=last_name, contact=contact, emergency_contact=emergency_contact_instance, user_name=user_name)
		# allergy_instance = Allergy.objects.create(title=title, body=body)
		print(last_name, first_name, user_name, contact, emergency_first_name, emergency_last_name, emergency_contact)


	return HttpResponse("HELLO")
