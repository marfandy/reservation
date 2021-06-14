from django.db import models
from django.utils import timezone


class Reservation(models.Model):
	podName 	= models.CharField(max_length=100)
	userName 	= models.CharField(max_length=100)
	phone 		= models.CharField(max_length=20,blank=True)
	status 		= models.CharField(max_length=50)
	price 		= models.IntegerField()
	bookingTime = models.DateTimeField()
	create 		= models.DateTimeField(default=timezone.now)
	update 		= models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.podName
