from django import forms

class UserRegistrationForm(forms.Form):
	first_name  = forms.CharField(label='first_name', max_length=100)
	last_name = forms.CharField(label='last_name', max_length=100)
	username = forms.CharField(label='last_name', max_length=100)
	contact = forms.CharField(label='contact', max_length=10)
	user_name = forms.CharField(label='user_name', max_length=100)
	emergency_first_name  = forms.CharField(label='emergency_first_name', max_length=100)
	emergency_last_name = forms.CharField(label='emergency_last_name', max_length=100)
	emergency_contact = forms.CharField(label='emergency_contact', max_length=10)


class UserLogInForm(forms.Form):
	username = forms.CharField(label='last_name', max_length=100)