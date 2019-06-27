from django.db import models
from django.contrib.auth.models import User

branch_choices=[('CSE','Computer Science And Engineering'),('MnC','Mathematics And Computing'),('ECE','Electronics And Communication Enginnering'),('EEE','Electrical And Electronics Engineering'),('CLE','Chemical Engineering'),('CE','Civil Engineering')]

class File(models.Model):
	name=models.CharField(max_length=200,)
	branch=models.CharField(max_length=3,choices=branch_choices,default='None')
	file=models.FileField(null=True,upload_to='')
	uploaded_by=models.ForeignKey(User,related_name='files', on_delete='CASCADE')
	def __str__(self):
		return self.name

class Stream(models.Model):
	name=models.CharField(unique=True,max_length=3, choices=branch_choices,default='None')
	def __str__(self):
		return self.name
	