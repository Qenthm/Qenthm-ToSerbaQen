Link Aplikasi PWS: https://rifqisyandi-khairurrizal-toserbaqenn.pbp.cs.ui.ac.id/

1. Membuat Proyek Django Baru
    Saya memulai pengerjaan tugas individu 2 PBP ini dengan menjalankan perintah,
    django-admin startproject ToserbaQen .

2. Membuat Aplikasi main
    Dilanjutkan dengan membuat aplikasi bernama main di dalam projek Django dengan perintah,
    python manage.py startapp main

3. Mengisi file main/models.py
    Mengisi file models.py yang terletak di dalam direktori main dengan,
    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()

        def __str__(self):
            return self.name
    
    untuk menambahkan field yang akan ditampilkan di web, yaitu nama produk, harga produk, dan deskripsi produk

4. Membuat dan mengaplikasikan migrasi model
    Membuat migrasi model dengan menjalankan perintah,
    python manage.py makemigrations

    Untuk menerapkan migrasi tersebut dengan cara menjalankan perinthah,
    python manage.py migrate 

5. Mengedit file views.py
    Mengimport fungsi render dari django.shortcuts dengan from django.shortcuts import render
    Membuat fungsi show_main yang berisi
    def show_main(request):
        context = {
            'product' : 'fast runner',
            'price': '159000',
            'description': 'he fast',
            'name' : 'Rifqisyandi Khairurrizal',
            'kelas' : 'PBP E'
        }

        return render(request, "main.html", context)
    Ini merupakan deklarasi definisi untuk variabel-variabel yang akan digunakan untuk diperlihatkan di main.html

6. Routing URL aplikasi main
    Pada urls.py yang berada di direktori main, tambahkan line app_name = 'main'
    dan tambahkan isi urlpatterns dengan path(' ', show_main, name='show_main')
    pindah ke direktori utama ToserbaQen dan membuka urls.py menambahkan

    from django.urls import path, include

    dan menambahkan path('', include('main.urls')) pada urlpatterns

![Bagan](https://cdn.discordapp.com/attachments/1183391036442165391/1283274262135701577/Screenshot_2024-09-11_at_10.48.01.png?ex=66e265ca&is=66e1144a&hm=dbd06be2c791c13abf154f171944cf97fec89a8a8f2f98f135602aff03958e08&)

Client mengirim request kepada server Django. Django menangani request dengan mencari pola URL yang sesuai di file urls.py. Routing dilakukan dan menemukan fungsi show_main yang terletak di dalam views.py. Setelah request diarahkan ke views.py, Django menjalankan fungsi yang sesuai. Fungsi ini akan mengolah data dan menentukan apa yang harus ditampilkan di halaman tersebut. Jika fungsi di views.py membutuhkan data dari database, ia akan mengambilnya melalui model (misalnya Product). Django menggunakan ORM untuk mengubah query pada model menjadi perintah SQL dan mengembalikan data yang relevan. Setelah data diproses oleh views.py, biasanya data tersebut ditampilkan menggunakan template HTML. Template ini menggabungkan data dari model dan logika dari view untuk membuat halaman web yang akan dikirimkan kembali ke client. Setelah template diproses, Django mengembalikan response berupa halaman HTML ke browser client, yang kemudian menampilkan halaman tersebut kepada pengguna.

B.

Jawaban Pertanyaan

    1. Jelaskan fungsi git dalam pengembangan perangkat lunak: 
    Git adalah sistem kontrol versi terdistribusi yang digunakan untuk melacak perubahan pada kode sumber. Git memungkinkan beberapa pengembang untuk bekerja pada proyek yang sama secara bersamaan tanpa bentrok, mengelola versi kode, dan memfasilitasi kolaborasi dengan tim menggunakan platform seperti GitHub. Dengan Git, pengembang dapat menyimpan sejarah kode, melakukan rollback ke versi sebelumnya, dan membuat cabang untuk fitur baru.

    2. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?: 
    Django adalah framework yang ramah bagi pemula karena menyediakan berbagai fitur out-of-the-box seperti ORM, sistem template, autentikasi, dan admin panel, sehingga memudahkan pengembang untuk fokus pada logika aplikasi. Django juga mendukung praktik terbaik dalam pengembangan perangkat lunak, seperti pola arsitektur Model-View-Template (MVT). Django memiliki dokumentasi yang sangat baik, sehingga cocok untuk memulai belajar pengembangan web.

    3. Mengapa model pada Django disebut sebagai ORM?: 
    Model di Django disebut sebagai ORM (Object-Relational Mapping) karena Django menyediakan mekanisme untuk menghubungkan objek Python dengan tabel database tanpa harus menulis SQL secara langsung. Setiap model di Django mewakili tabel dalam database, dan Django mengkonversi operasi pada objek menjadi perintah SQL yang diperlukan untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada database.
