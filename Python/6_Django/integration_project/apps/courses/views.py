from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Course, User

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
        return redirect('courses:index')
    else:
        redirect('courses:index')

def remove(request, id):
    context = {
        'course': Course.objects.get(id=id),
    }
    return render(request, 'courses/remove.html', context)

def delete(request, id):
    context = Course.objects.get(id=id).delete()
    print context
    return redirect('courses:index')

def users_courses(request):
    if request.method == 'POST':
        course_id = int(request.POST['course'])
        user_id = int(request.POST['user'])
        user = User.objects.get(id=user_id)
        course = Course.objects.get(id=course_id)
        response = course.users.add(user)
        print response

    context = {
        'users': User.objects.all().order_by('first_name','last_name'),
        'courses': Course.objects.annotate(num_users=Count('users')).order_by('name')
    }

    return render(request, 'courses/users_courses.html', context)
