from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request, data):
    print data
    if data == '/':
        context = {
            'pics': ['donatello.jpg', 'leonardo.jpg', 'michelangelo.jpg', 'raphael.jpg']
        }
    elif data == 'blue':
            context = {
                'pics': ['leonardo.jpg']
            }
    elif data == 'orange':
        context = {
            'pics': ['michelangelo.jpg']
        }
    elif data == 'red':
        context = {
            'pics': ['raphael.jpg']
        }
    elif data == 'purple':
        context = {
            'pics': ['donatello.jpg']
        }
    else:
        context = {
            'pics': ['notapril.jpg']
        }

    return render(request, 'ninjas/ninjas.html', context)
