from django.shortcuts import render
from .models import Employee
from django.views.decorators.csrf import csrf_protect

def listing(request):
	title = 'Employee Listing'
	employees = Employee.objects.all()
	return render(request, 'listing.html', {'title': title, 'employees': employees})

def selection(request, id):
	title = 'Employee Listing'
	employee = Employee.objects.get(id=id)
	return render(request, 'listing.html', {'title': title, 'employees': [employee]})

@csrf_protect
def query(request):
	query = request.POST.get('query')
	field = request.POST.get('field')

	if field == 'name':
		employees = Employee.objects.filter(name__contains=query)
	elif field == 'age':
		employees = Employee.objects.filter(age__contains=query)
	elif field == 'gender':
		employees = Employee.objects.filter(gender__contains=query)
	elif field == 'salary':
		if query.find(',') > 0 or query.find('.') > 0:
			query = float(query.replace(',', '.'))
		employees = Employee.objects.filter(salary__contains=query)

	title = 'Employee Listing'
	return render(request, 'listing.html', {'title': title, 'employees': employees})

_field = ''
def sort(request, field):
	title = 'Employee Listing'
	global _field

	if field == _field:
		employees = Employee.objects.all().order_by(field).reverse()
		_field = ''
	else:
		employees = Employee.objects.all().order_by(field)
		_field = field

	return render(request, 'listing.html', {'title': title, 'employees': employees})

def insertion(request):
	title = 'Employee Insertion'
	return render(request, 'insertion.html', {'title': title})

@csrf_protect
def save_insertion(request):
	name = request.POST.get('name')
	age = request.POST.get('age')
	gender = request.POST.get('gender')
	salary = request.POST.get('salary')
	salary = salary.replace(',', '.')

	obj = Employee(
		name = name,
		age = age,
		gender = gender,
		salary = salary
	)
	obj.save()

	title = 'Employee Listing'
	employees = Employee.objects.all()
	return render(request, 'listing.html', {'title': title, 'employees': employees})

def update(request, id):
	title = 'Employee Update'
	employee = Employee.objects.get(id=id)
	return render(request, 'update.html', {'title': title, 'employee': employee})

@csrf_protect
def save_update(request):
	id = request.POST.get('id')
	name = request.POST.get('name')
	age = request.POST.get('age')
	gender = request.POST.get('gender')
	salary = request.POST.get('salary')
	salary = salary.replace(',', '.')

	Employee.objects.filter(id=id).update(
		name = name,
		age = age,
		gender = gender,
		salary = salary
	)

	title = 'Employee Listing'
	employees = Employee.objects.all()
	return render(request, 'listing.html', {'title': title, 'employees': employees})

def delete(request, id):
	title = 'Employee Deletion'
	employee = Employee.objects.get(id=id)
	return render(request, 'delete.html', {'title': title, 'employee': employee})

@csrf_protect
def save_delete(request):
	id = request.POST.get('id')

	Employee.objects.filter(id=id).delete()

	title = 'Employee Listing'
	employees = Employee.objects.all()
	return render(request, 'listing.html', {'title': title, 'employees': employees})

def graphics(request):
	title = 'Statistic Graphics by Gender'
	employeesF = Employee.objects.filter(gender = 'F')
	employeesM = Employee.objects.filter(gender = 'M')

	'''SALARY GRAPHICS'''
	salaryF = 0
	salaryM = 0

	for f in employeesF:
		salaryF += f.salary
	for m in employeesM:
		salaryM += m.salary

	if len(employeesF) > 0:
		salaryF = salaryF / len(employeesF)
	if len(employeesM) > 0:	
		salaryM = salaryM / len(employeesM)

	'''AGE GRAPHICS'''
	ageF = 0
	ageM = 0

	for f in employeesF:
		ageF += f.age

	for m in employeesM:
		ageM += m.age

	if len(employeesF) > 0:
		ageF = ageF / len(employeesF)
	if len(employeesM) > 0:	
		ageM = ageM / len(employeesM)

	return render(request, 'graphics.html', {'title': title, 'salaryF': salaryF, 'salaryM': salaryM, 'ageF': ageF, 'ageM': ageM})

