from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	tag = models.CharField(max_length=50)
	text = models.TextField()
	date_posted = models.DateTimeField()
	author = models.CharField(max_length=30)

	def __str__(self):
		return self.title