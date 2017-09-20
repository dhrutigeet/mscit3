from django.db import models

# Create your models here.
class mscit(models.Model):
	snm=models.CharField(max_length=200)
	pnm= models.TextField()
	
class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic/', default = 'pic/no-img.jpg')
