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
		username = form.cleaned_data['username']
		contact = form.cleaned_data['contact']
		user_name = form.cleaned_data['user_name']
		emergency_first_name  = form.cleaned_data['emergency_first_name']
		emergency_last_name = form.cleaned_data['emergency_last_name']
		emergency_contact = form.cleaned_data['emergency_contact']
		emergency_contact_instance = EmergencyContact.objects.create(first_name=emergency_first_name, last_name=emergency_last_name, contact=emergency_contact)
		user_instance = User.objects.create(
				first_name=first_name, 
				last_name=last_name, 
				contact=contact,
				username = username,
				emergency_contact=emergency_contact_instance)
		# allergy_instance = Allergy.objects.create(title=title, body=body)
		print(last_name, first_name, user_name, contact, emergency_first_name, emergency_last_name, emergency_contact)

		request.session['name'] = username
		assert false, locals()
		return render(request, 'home/search_food.html')

def get_user_login_form(request):
	return render(request, 'home/user_log_in_form.html')

def set_log_in(request):
	request.session['name'] = request.POST.get('username')
	# return HttpResponse("HELLO " + str(request.session['name']))
	return render(request, 'home/search_food.html')

def search_food(request):
	username = request.session['name']
	if not username:
		return HttpResponse("No user found, Log in again")
	user = User.objects.values('username')
	return render(request, 'home/search_text_box.html')


def get_food_items(request):
	username = request.session['name']
	if not username:
		return HttpResponse("No user found, Log in again")
	user = User.objects.values('username')
	search_query = request.POST.get('query');
	return HttpResponse("Searching for " + str(search_query) + "...")

	
