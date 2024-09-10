from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '23051652216',
        'name': 'Rifqisyandi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
