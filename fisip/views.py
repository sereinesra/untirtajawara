from django.shortcuts import render

# Create your views here.
def indexfisip(request):
    return render(request, 'bukafisip.html')