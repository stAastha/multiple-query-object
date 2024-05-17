
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    all()
    data = Student.objects.all()
    data1 = data.values()
    print(data1)
    return HttpResponse(data1)

    # filter(**kwargs)
data=Student.objects.filter(stu_city='bhopal')
data1 = data.values()
    return HttpResponse(data)

 

# exclude(**kwargs)
    data=Student.objects.exclude(stu_city='bhopal')
    data1 = data.values()
        return HttpResponse(data1)

            # order_by()
    data=Student.objects.order_by('stu_city') # bydefault assendind order
    data=Student.objects.order_by('-stu_city') # desending order
    data=Student.objects.order_by('?') # arrenge in rendom manner in everyclick
    data=Student.objects.order_by('stu_name').order_by('stu_city').order_by('stu_email') # introduce Q object 
    data1 = data.values()
        return HttpResponse(data)
            # reverse()
    data=Student.objects.order_by('id').reverse()
    data=Student.objects.order_by('id').reverse()[:2] # first 2 entries
    data = Student.objects.all()[:2] # first 2 entries  
    data1 = data.values()
        return HttpResponse(data1)

            # values() it provides dict formated values
    data=Student.objects.values()
    data=Student.objects.values('stu_name','stu_city')
    return HttpResponse(data)

            # values_list(*fields, flat=False, named=False) it provides tuple formated values
    data=Student.objects.values_list()
    data=Student.objects.values_list('id','stu_name')
    data=Student.objects.values_list('id','stu_name',named=True)
        return HttpResponse(data)