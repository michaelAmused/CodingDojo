from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if 'count' in request.session:
            request.session['count'] += 1
        else:
            request.session['count'] = 1
        return redirect('/result')

    else:
        return redirect('/')

def result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }
    return render(request, 'survey/result.html', context)
