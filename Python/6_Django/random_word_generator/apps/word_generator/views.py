from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'word_generator/index.html')

def attempt(request):
    if request.method == 'POST':
        if 'count' in request.session:
            request.session['count'] = request.session['count'] + 1
        else:
            request.session['count'] = 1

        print request.POST
        csrf_word = request.POST['csrfmiddlewaretoken']
        print csrf_word
        rand_word = ''
        for i in range(14):
            rand_word = rand_word + csrf_word[i]
        request.session['random_word'] = str(rand_word)
        print request.session['count']
        print request.session['random_word']
        return redirect('/')

    else:
        return redirect('/')
