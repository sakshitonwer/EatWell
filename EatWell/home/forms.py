from django import forms
from .models import EmergencyContact, User, Ingredient

class UserRegistrationForm(forms.Form):
	# ingredients = Ingredient.objects.all()
	# print(ingredients)
	all_ingredients = []
	# for ingredient in ingredients:
		# all_ingredients.append(ingredient.ingredient_name)
	first_name  = forms.CharField(label='first_name', max_length=100)
	last_name = forms.CharField(label='last_name', max_length=100)
	username = forms.CharField(label='last_name', max_length=100)
	contact = forms.CharField(label='contact', max_length=10)
	user_name = forms.CharField(label='user_name', max_length=100)
	emergency_first_name  = forms.CharField(label='emergency_first_name', max_length=100)
	emergency_last_name = forms.CharField(label='emergency_last_name', max_length=100)
	emergency_contact = forms.CharField(label='emergency_contact', max_length=10)
	allergies = forms.MultipleChoiceField(choices=tuple([(ingredient, ingredient) for ingredient in all_ingredients]), widget=forms.CheckboxSelectMultiple())



class UserLogInForm(forms.Form):
	username = forms.CharField(label='last_name', max_length=100)


class ProductListForm(forms.Form):
	product = forms.ChoiceField(label='product_name')