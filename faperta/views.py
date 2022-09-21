from django.shortcuts import render

# Create your views here.
def indexfaperta(request):
    tentang = "Jurusan/Program Studi yang ada di Fakultas Pertanian"
    prodi1 = "Agribisnis"
    penjelasan1  = "Pada Tahun 2009 Program Studi Sosial Ekonomi Pertanian berubah menjadi Jurusan/Program Studi Agribisnis, dengan Keputusan Rektor No. 181/H43/KR/SK/2009 dan diakreditasi kembali pada tahun 2012 dengan akreditasi B berdasarkan SK BAN PT Nomor: 024/BAN-PT/Ak-XV/S1/VIII/2012."
    prodi2 = "Agroekoteknologi"
    penjelasan2 = "Jurusan agroekoteknologi merupakan suatu upaya turut sertanya Faperta Untirta dalam menunjang pembangunan nasional dan daerah terutama dalam pengembangan pemanfaatan dan pengelolaan sumberdaya alam (SDA) dan sumberdaya Manusia (SDM) khususnya di sektor pertanian."
    prodi3 = "Ilmu Perikanan"
    penjelasan3 = "Prodi Perikanan merupakan suatu upaya turut sertanya Faperta Untirta dalam menunjang pembangunan nasional dan daerah terutama pengembangan sumberdaya manusia (SDM) di sektor perikanan."
    prodi4 = "Teknologi Pangan"
    penjelasan4 = "Program pengembangan di Program studi Teknologi Pangan adalah melaksanakan tridharma perguruan tinggi dan menyelenggarakan program studi yang berkualitas dalam pengembangan IPTEK pangan berbasis sumber daya lokal untuk mendukung Food Security."

    konteks = {
        'tentang' : tentang,
        'penjelasan1' : penjelasan1,
        'jurusan1' : prodi1,
        'jurusan2' : prodi2,
        'penjelasan2' : penjelasan2,
        'jurusan3' : prodi3,
        'penjelasan3' : penjelasan4,
        'jurusan4' : prodi4,
        'penjelasan4' : penjelasan4,
    }
    return render(request, 'faperta-muka.html', konteks)