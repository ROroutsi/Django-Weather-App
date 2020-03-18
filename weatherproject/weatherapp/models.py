from django.db import models

class city(models.Model):

	city_name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'cities'	

	def __str__(self):
		return self.city_name	