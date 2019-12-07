from django.shortcuts import render
from django.http import HttpResponse

import logging
# Create your views here.
from .forms import UserRegistrationForm
from .models import EmergencyContact, User, Ingredient, Product, ProductIngredients,UserAllergy

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
	ingredients = Ingredient.objects.all()

	form = UserRegistrationForm()
	context = {
        'form': form
    }
	
	return render(request, 'home/user_registration_form.html', context)

def save_user_details(request):
	form = UserRegistrationForm(request.POST)
	print(form.is_valid())
	if form.is_valid():
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		username = form.cleaned_data['username']
		contact = form.cleaned_data['contact']
		emergency_first_name  = form.cleaned_data['emergency_first_name']
		emergency_last_name = form.cleaned_data['emergency_last_name']
		emergency_contact = form.cleaned_data['emergency_contact']
		allergies = form.cleaned_data['allergies']
		emergency_contact_instance = EmergencyContact.objects.create(
			first_name=emergency_first_name,
			last_name=emergency_last_name,
			contact=emergency_contact)
		user_instance = User.objects.create(
				first_name=first_name,
				last_name=last_name,
				contact=contact,
				username = username,
				emergency_contact=emergency_contact_instance)
		for allergy in allergies:
			ingredient = Ingredient.objects.filter(ingredient_name=allergy).get()
			UserAllergy.objects.create(
				user=user_instance,
				allergy=ingredient
		)
		print(allergies)
		print(last_name, first_name, username, contact, emergency_first_name, emergency_last_name, emergency_contact)

		request.session['name'] = username
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

	# Getting from database
	matching_products = Product.objects.filter(product_name__contains=search_query)
	logging.warning(matching_products)
	return render(request, 'home/product_list.html', {
		'matching_products' : matching_products,
		'search_query' : search_query})


def select_product(request, id):
	select_product =  Product.objects.filter(id=id).get()
	all_ingredients = ProductIngredients.objects.filter(product_id = select_product.id).values("ingredient_id")
	username = request.session['name']
	ingredients = []

	for i in all_ingredients:
		ingredients.append(i['ingredient_id'])
	logging.warning(ingredients)
	if not username:
		return HttpResponse("No user found, Log in again")

	user = User.objects.filter(username = username).get()
	logging.warning(user)

	
	allergies = UserAllergy.objects.filter(user_id = user.id).values("allergy_id")

	user_allergy = []
	for a in allergies:
		user_allergy.append(a["allergy_id"])

	logging.warning(user_allergy)

	c = get_intersection(user_allergy, ingredients)
	
	if c > 0:
		# return HttpResponse("Dont eat")
		return render(request, 'home/thumbs_down.html')
	else:
		return render(request, 'home/thumbs_up.html')

	
	return HttpResponse("HELLO " + str(select_product.product_name))


def get_intersection(a, b):
	return len(list(set(a) & set(b)))

	
