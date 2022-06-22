from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length=255)
	#title_tag = models.CharField(max_length=255, default=title)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #cascade miatt törlésnél az összes postot törli
	body = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	post_time = models.TimeField(auto_now_add=True)
	snippet = models.CharField(max_length=255)


	def __str__(self):
		return self.title + ' | ' + str(self.author)


	def get_absolute_url(self):
		return reverse('home')