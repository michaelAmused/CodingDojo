from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):

    context = {
        "date":datetime.datetime.now().strftime("%B %d, %Y"),
        "tme":datetime.datetime.now().strftime("%I:%M%p")
    }
    print context
    return render(request, 'timedisplay/index.html', context)
