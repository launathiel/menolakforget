from django.db import models
from datetime import datetime 

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=200, null=True)
	kelas = models.CharField(max_length=200, null=True)
	nim = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Subject(models.Model):

	name = models.CharField(max_length=200, null=True)
	semester = models.IntegerField()
	sks = models.IntegerField()

	def __str__(self):
		return self.name

class Assignment(models.Model):
	STATUS = (
			('Unassigned', 'Unassigned'),
			('Assigned', 'Assigned'),
			)

	CATEGORY = (
			('Assignment', 'Assignment'),
			('Quiz', 'Quiz'),
			) 
	student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
	subject = models.ForeignKey(Subject, null=True, on_delete= models.SET_NULL)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	deadline = models.DateTimeField(default=datetime.now, blank=True, null=True)

	def __str__(self):
		return self.subject.name