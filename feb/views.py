from django.shortcuts import render

# Create your views here.
def indexfeb(request):
    tentang1 = "Sejarah"
    tentang2 = "Visi dan Misi"
    konteks = {
        'tentang1' : tentang1,
        'tentang2' : tentang2,
    }
    return render(request, 'bukafeb.html')