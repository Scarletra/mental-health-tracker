from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2206081332',
        'name': 'Fernando Valentino',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)