from django.db import models

# Create your models here.

class EmergencyContact(models.Model):
	id = models.AutoField(primary_key=True)
	first_name  = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	contact = models.CharField(max_length=10)

class Ingredient(models.Model):
	id = models.AutoField(primary_key=True)
	ingredient_name  = models.CharField(max_length=100)

class User(models.Model):
	id = models.AutoField(primary_key=True)
	first_name  = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100, unique=True, default = "not_applicable")
	contact = models.CharField(max_length=10)
	emergency_contact = models.OneToOneField(EmergencyContact, on_delete = models.CASCADE)

class UserAllergy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


