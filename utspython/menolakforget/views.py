from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .forms import AssignmentForm


def home(request):
	assignments = Assignment.objects.all()
	students = Student.objects.all()

	total_assignments = assignments.count()
	assigned = assignments.filter(status='Assigned').count()
	unassigned = assignments.filter(status='Unassigned').count()

	context = {'assignments':assignments, 'students':students,
	'total_assignments':total_assignments,'assigned':assigned,
	'unassigned':unassigned }

	return render(request, 'menolakforget/dashboard.html', context)

def subjects(request):
	subjects = Subject.objects.all()

	return render(request, 'menolakforget/subjects.html', {'subjects':subjects})

def about(request):
	return render(request, 'menolakforget/about.html')

def createAssignment(request):
	form = AssignmentForm()
	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'menolakforget/order_form.html', context)

def updateAssignment(request, pk):

	assignment = Assignment.objects.get(id=pk)
	form = AssignmentForm(instance=assignment)

	if request.method == 'POST':
		form = AssignmentForm(request.POST, instance=assignment)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'menolakforget/order_form.html', context)

def deleteAssignment(request, pk):
	assignment = Assignment.objects.get(id=pk)
	if request.method == "POST":
		assignment.delete()
		return redirect('/')

	context = {'item':assignment}
	return render(request, 'menolakforget/delete.html', context)