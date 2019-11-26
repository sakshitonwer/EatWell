from django.urls import path, re_path
from . import views

urlpatterns = [
	path('user/registration/', views.get_user_registration_form),
	path('user/registration/save/', views.save_user_details, name='saveuser'),
	path('index/', views.index)
]