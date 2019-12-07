from django import forms
from .models import EmergencyContact, User, Ingredient

class UserRegistrationForm(forms.Form):
	ingredients = Ingredient.objects.all()
	print(ingredients)
	all_ingredients = []
	for ingredient in ingredients:
		all_ingredients.append(ingredient.ingredient_name)
	first_name  = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	username = forms.CharField(label='User Name', max_length=100)
	contact = forms.CharField(label='Contact', max_length=10)
	emergency_first_name  = forms.CharField(label='Emergency First Name', max_length=100)
	emergency_last_name = forms.CharField(label='Emergency Last Name', max_length=100)
	emergency_contact = forms.CharField(label='Emergency Contact', max_length=10)
	allergies = forms.MultipleChoiceField(
		label='Allergies',
		choices=tuple([(ingredient, ingredient) for ingredient in all_ingredients]),
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'foobar'}))

class UserLogInForm(forms.Form):
	username = forms.CharField(label='last_name', max_length=100)
