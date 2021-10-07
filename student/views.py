from django.shortcuts import render
from .models import Student
from django.db import connection


# Create your views here.
def student_list_(request):
    posts = Student.objects.all()
    print(posts)
    print(posts.query)

    print("Connections Queries: ", connection.queries)

    return render(request, 'output.html', {'posts': posts})

def student_list(request):
    posts = Student.objects.filter(surname__startswith='uddin') | Student.objects.filter(surname__startswith='raihan')
    print(posts)
    # print(posts.query)

    print("Connections Queries: ", connection.queries)

    return render(request, 'output.html', {'posts': posts})
