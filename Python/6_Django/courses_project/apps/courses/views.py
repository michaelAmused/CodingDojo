from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    # print course.name()
    return render(request, 'courses/index.html', context)

def add_new(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        new = Course.objects.create(name=name, description=description)
        return redirect('/')
    else:
        redirect('/')

def remove(request, id):
    context = {
        'course': Course.objects.get(id=id),
    }
    return render(request, 'courses/remove.html', context)

def delete(request, id):
    context = Course.objects.get(id=id).delete()
    print context
    return redirect('/')
