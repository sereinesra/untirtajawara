from django.shortcuts import render

# Create your views here.
def indexfh(request):
    judul = "Sejarah"
    tentang = "Fakultas Hukum Universitas Sultan Ageng Tirtayasa berdiri tahun 1981, tepatnya pada tanggal 1 Oktober 1981 dengan status sebagai STIH Serang yang bertempat di Kresidenan Banten, Jl. K.H. Sam’un dan merupakan embrio lahirnya Universitas Sultan Ageng Tirtayasa Banten. Mulai tahun 1984, STIH Serang di integrasi sesuai dengan SK Mendikbud No. 0596/0/1984, menjadi Fakultas Hukum Universitas Sultan Ageng Tirtayasa yang bertempat di Jl. Raya Jakarta KM. 4 Pakupatan – Serang. Fakultas Hukum pada tahun 1994 memperoleh status terdaftar berdasarkan SK Mendikbud No. 0597/0/1984. Pada tahun 1994 Fakultas Hukum kembali memperoleh status penetapan terdaftar kembali berdasarkan SK Ditjen Pendidikan Tinggi No. 059/Dikti/Kep./1994. Pada tahun 2000 Fakultas Hukum memperoleh status terakreditasi dengan peringkat B, berdasarkan SK BAN-PT No. 19/BAN-PT/AK-IV/VIII/2000, dengan adanya SK Akreditasi tersebut maka Fakultas Hukum dapat menyelenggarakan proses pembelajaran secara mandiri. Pada tahun 2001 status Fakultas Hukum menjadi Fakultas Hukum dari Universitas Sultan Ageng Tirtayasa Banten dengan Status Negeri, berdasarkan Kepres No. 32/2001, hingga saat ini dan beralamat di Jl. Raya Jakarta KM. 4 Pakupatan–Serang. Saat ini  fakultas Hukum terakreditasi peringkat B berdasarkan SK. No. 186/SK/BAN-PT/Ak-SURV/S/VI/2014 tertanggal 28 Juni 2014."
    konteks = {
        'title' : judul,
        'penjelasan' : tentang,
    }
    return render(request, 'bukafh.html', konteks)