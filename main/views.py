from django.shortcuts import render

def show_main(request):
    context = {
        'product' : 'fast runner',
        'price': '159000',
        'description': 'he fast',
        'name' : 'Rifqisyandi Khairurrizal',
        'kelas' : 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
