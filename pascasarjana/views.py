from django.shortcuts import render

# Create your views here.
def indexpascasarjana(request):
    judul = "Program Pascasarjana"
    tentang = "Universitas Sultan Ageng Tirtayasa menawarkan program studi lanjutan di tingkat S2 dan S3 yang diselenggarakan di fakultas serta sekolah Pascasarjana."

    konteks = {
        'title' : judul,
        'penjelasan' : tentang,
    }
    return render(request, 'bukapascasarjana.html', konteks)