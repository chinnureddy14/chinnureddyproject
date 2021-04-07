from django.db import models



class UsrRg(models.Model):
	username=models.CharField(max_length=120)
	password=models.CharField(max_length=120)
	email=models.CharField(max_length=120)
	age=models.IntegerField(default=10)
	
	def __str__(self):
		return self.username+" "+self.email


class NewData(models.Model):
	ch=[('m','male'),('f','female')]
	mobile=models.IntegerField(default=6301875441)
	gender=models.CharField(max_length=10,choices=ch)
	pid=models.OneToOneField(UsrRg,on_delete=models.CASCADE)

	
 
# Create your models here.
