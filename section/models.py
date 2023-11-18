from django.db import models

from common.models import BaseModel

class Section(BaseModel):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	priority = models.DecimalField(max_digits=20, decimal_places=10)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.name
	
	class Meta:
		unique_together = ('user', 'priority',)
