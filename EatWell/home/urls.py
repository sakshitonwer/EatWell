from django.urls import path, re_path
from . import views

urlpatterns = [
	path('user/registration/', views.get_user_registration_form),
	path('user/registration/save/', views.save_user_details, name='saveuser'),
	path('user/search_food/', views.search_food, name='search_food'),
	path('user/login/', views.get_user_login_form, name='log_in'),
	path('user/set_log_in/', views.set_log_in, name='set_log_in'),
	path('user/get_food_items/', views.get_food_items, name='get_food_items'),
	path('user/select_product/<int:id>', views.select_product, name='select_product'),
	path('index/', views.index)
]