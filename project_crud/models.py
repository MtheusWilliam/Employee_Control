from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(max_length=1) 
	salary = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return self.name

