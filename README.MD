Link Aplikasi PWS: https://rifqisyandi-khairurrizal-toserbaqen.pbp.cs.ui.ac.id/

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


# Pertanyaan Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data Delivary sangat peting dalam sebuah platform karena data delivery merupakan cara untuk mengirim dan menerima informasi antara berbagai bagian sistem atau antara user dan server.

2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih popouler dibandingkan XML dikarenakan JSON lebih ringan dan mudah dibaca oleh manusia karena struktur yang lebih sederhana, JSON memiliki sintaks yang mirip dengan JavaScript, dan parsing JSON cenderung lebih cepat dibandingkan dengan XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
method is_valid() digunakan untk memvalidasi isi input yang disi oleh user. Metode ini memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang telah ditetapkan pada form. Fungsi ini penting untuk mencegah data yang salah atau yang tidak sesuai dengan format masukan ke dalam sistem.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF (Cross-Site Request Forgery) token digunakan di Django untuk melindungi aplikasi dari serangan CSRF. Token ini memastikan bahwa permintaan form yang dikirim ke server berasal dari sumber yang aman. Tanpa csrf_token, aplikasi menjadi rentan terhadap serangan di mana penyerang bisa mengirimkan permintaan palsu atas nama user tanpa diketahui oleh user tersendiri. Misalnya, penyerang bisa mengeksploitasi form tanpa csrf_token untuk melakukan tindakan berbahaya seperti mengubah pengaturan akun pengguna atau melakukan transaksi tanpa izin.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Diawali dengan membuat folder baru pada folder utama, dan membuat file bernama base.html yang berfungsi sebagai kerangka umum untuk halaman web. dan menambahkan nama folder yang berisikan base.html ke dalam TEMPLATES yang terletak di dalam settings.py. Menambahkan line import uuid pada models.py untuk mengaplikasikan best practice untuk mencegah celah keamanan dan melakukan migrations karena telah mengubah models.py. Membuat file bernama forms.py yang berisi field yang akan dapat ditambahkan oleh user dan menambahkan import redirect ke dalam views.py. Membuat fungsi baru pada views.py yang menerima parameter request. Membuat file baru pada direktori main/templates bernama create_new_items.html. Dan mengubah main.html agar dapat mengoutput isi form. Membuat fungsi dimana user dapat melihat data dalam bentuk XML dan JSON dan mengembalikan data berdasarkan id dalam bentuk XML dan JSON.

![XML](https://media.discordapp.net/attachments/1183391036442165391/1285803697950953546/image.png?ex=66eb9982&is=66ea4802&hm=e070f23d71b9965f0fac9ae3a9a59119e1ae56a10231b8485cbd60b2f10b1a24&=&format=webp&quality=lossless&width=1388&height=1036)

![JSON](https://cdn.discordapp.com/attachments/1183391036442165391/1285803664635723788/image.png?ex=66eb997a&is=66ea47fa&hm=38e7eabb9705a3e3a93965accfb78960bb54de557e4707314b16e2edc8f264e8&)

![XML by ID](https://cdn.discordapp.com/attachments/1183391036442165391/1285803617978417243/image.png?ex=66eb996f&is=66ea47ef&hm=ff33e4aca657a2150b5350dfedf6ef0193345f1ef4b25f3c8784c7c8da72c820&)

![JSON by ID](https://cdn.discordapp.com/attachments/1183391036442165391/1285803638404419584/image.png?ex=66eb9974&is=66ea47f4&hm=ed809b18dc09b33e3e171f73a76472902a7e9cd0ca1c03b7b6757a510518c425&)

# Pertanyaan Tugas 4

## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
HttpResponseRedirect adalah kelas yang digunakan untuk mengembalikan respons HTTP yang mengarahkan pengguna ke URL tertentu. Pada penggunaannya, kita harus memberikan URL yang dituju secara manual. Sedangkan redirect(), di sisi lain, adalah fungsi yang lebih sederhana dan fleksibel. Ia dapat menerima URL, nama view, atau objek model sebagai parameter, dan secara otomatis menentukan URL yang benar berdasarkan input tersebut.

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Dalam Django, kita bisa menghubungkan model Product dengan User menggunakan foreign key. Hal ini memungkinkan setiap produk dapat terkait dengan pengguna tertentu, seperti penjual atau pemilik produk.
```python
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```
## 3. Apa perbedaan antara authentication dan authorization, dan apa yang dilakukan saat pengguna login?
Authentication adalah proses verifikasi identitas pengguna, misalnya dengan meminta username dan password. Proses ini bertujuan untuk memastikan bahwa pengguna yang masuk adalah benar-benar pengguna yang terdaftar.

Authorization adalah proses yang menentukan apakah pengguna yang sudah terotentikasi memiliki izin untuk mengakses sumber daya tertentu. Ini bergantung pada peran dan hak akses pengguna.

Saat pengguna login:

    1. Django pertama-tama melakukan authentication, memeriksa apakah kredensial (username dan password) yang diberikan cocok dengan pengguna di database.
    2. Jika valid, pengguna akan di-authorize untuk melakukan tindakan tertentu berdasarkan izin yang mereka miliki.

Django mengimplementasikan authentication dan authorization menggunakan middleware dan model User. Django juga menyediakan sistem permission dan group yang memungkinkan kita mengatur hak akses secara granular.

## 4. Bagaimana Django mengingat pengguna yang telah login?
Django mengingat pengguna yang telah login dengan menyimpan informasi sesi pengguna dalam cookies. Saat pengguna berhasil login, Django membuat sesi baru yang terhubung dengan identitas pengguna tersebut, dan menyimpan sesi ini sebagai cookie di browser pengguna.

Cookies juga digunakan untuk keperluan lain, seperti menyimpan preferensi pengguna atau pengaturan personal. Namun, tidak semua cookies aman, karena cookies yang tidak di-secure dan tidak dienkripsi bisa diakses oleh pihak ketiga.

Untuk mengamankan cookies, Django memungkinkan penggunaan secure cookies yang hanya dikirim melalui HTTPS dan dapat dienkripsi menggunakan mekanisme seperti session framework.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama menambahkan import UserCreationForm untuk membuat form yang berfungsi untuk membuat user baru. Menambahkan fungsi register untuk menghasilkan form register secara otomatis dan menghasilkan akun user ketika form disubmit. Membuat file baru register.html di dalam direktori templates dan import register ke dalam urls.py dan menambahkan pattern url register. Tambahkan import authenticate, login, dan AuthenticationForm ke dalam views.py. Menambahkan fungsi login_user ke file views.py dan membuat file baru login.html, mengimport login_user dan menambahkan url pattern login ke dalam urls.py. Lakukan hal yang sama dengan logout. Melakukan restriksi agar user harus melakukan login sebelum bisa menggunakan fitur.

Selanjutnya kita mengimplementasikan cookies. Tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas. Menambahkan fungsionalitas menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Mengubah fungsi logout_user, response.delete_cookie('last_login') berfungsi untuk menghapus cookie last_login saat pengguna melakukan logout. Menambahkan sesi terakhir login pada main.html. Menghubungkan model dengan User menggunakan foreignkey dan melakukan migrasi karen asudah mengubah model .

# Pertanyaan Tugas 5
## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas CSS selector (juga dikenal sebagai specificity) dari yang tertinggi ke terendah adalah Inline styles, ID selectors, Class selectors, attribute selectors, dan pseudo-classes, Element selectors dan pseudo-elements, dan Universal selector (*). Jika terdapat konflik, selector dengan prioritas lebih tinggi akan diterapkan. Jika prioritasnya sama, selector yang ditulis terakhir akan digunakan.

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Dengan responsive design, pengguna dapat mengakses web aplikasi yang kita buat dengan perangkat apa saja dan ukuran layar apa saja, meningkatkan pengalama pengguna, memudahkan pemeliharaan, dan meningkatkan Search Engine Optimization
Banyak wesbite yang sudah menerapkan responsve design seperti steamcommunity. Sedangkan tidak banyak website yang belum mengimplementasikan responsive design, seperti craigslist

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah jarak di luar elemen, memisahkan elemen dari elemen lain. Sedangkan border adalah garis di sekeliling elemen yang terletak diantara margin dan padding dan padding adalah jarak antara konten dan elemennya.
Implementasi 
'''css
.element {
  margin: 10px;
  border: 2px solid black;
  padding: 5px;
}
'''

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box digunakan untuk tata letak satu dimensi (baris dan kolom), berguna untuk UI dan navigasi
Penggunaan
```css
.container {
  display: flex;
  justify-content: space-between;
}
```
Grid layout digunakan untuk tata letak dua dimensi dan cocok digunakan untuk layout halaman keseluruhan
Penggunaan
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 10px;
}
```
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
### Implementasikan fungsi untuk menghapus dan mengedit product.
Dengan menambahkan fungsi di views.py dan menambahkan import pada urls.py untuk mengakses fungsi tersebut
### Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
#### Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
Dengan membuat login.html, register html, dan create_new_items.html
#### Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
Dengan membuat card_items.html dan mengubah sedikit dari code yang terdapat di tutorial
### Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
Pada card_items.html tambahkan line
```html
 <div class="absolute top-4 right-4 flex space-x-2">
    <a href="{% url 'main:edit_item' mood_entry.pk %}" 
       class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 20 20">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    
    <a href="{% url 'main:delete_item' mood_entry.pk %}" 
       class="bg-red-500 ho6
ver:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
```
### Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
Membuat navbar.html pada folder templates yang terletak di root folder

# Pertanyaan Tugas 6
## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
### Interaktif dan Dinamis
JavaScript memungkinkan interaksi langsung pengguna dengan halaman web tanpa harus memuat ulang halaman secara keseluruhan.
### Asynchronous Operations
Dengan JavaScript, kita bisa melakukan operasi asynchronous, seperti pengambilan data dari server tanpa mengganggu pengalaman pengguna. Ini dapat dilakukan melalui fitur seperti fetch() yang menggunakan konsep asinkron untuk pengambilan data.
### Validasi Data
JavaScript dapat digunakan untuk melakukan validasi data di sisi pengguna (frontend), memastikan bahwa input yang diberikan sesuai sebelum dikirim ke server, yang dapat mengurangi beban server.
### Kompatibilitas dan Ekstensi
JavaScript adalah salah satu bahasa pemrograman web yang paling didukung dan kompatibel di semua browser, serta memiliki ekosistem besar dengan banyak pustaka dan framework seperti React, Vue, dan Angular yang mempercepat pengembangan.

## 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi await digunakan dalam konteks fungsi asinkron untuk menunggu hasil dari promise sebelum melanjutkan eksekusi kode berikutnya. Ketika kita menggunakan fetch(), yang merupakan operasi asinkron, await menunggu hingga promise yang dihasilkan fetch() terpenuhi atau ditolak.
### Apa yang Terjadi Jika Tidak Menggunakan await?
operasi fetch() akan menghasilkan promise yang belum terselesaikan dan eksekusi kode akan berlanjut tanpa menunggu respons dari server. Sebagai akibatnya, jika kita mencoba mengakses hasil fetch() secara langsung tanpa menunggu, kita mungkin mendapatkan promise yang belum selesai, yang akan menyebabkan error saat mencoba memproses data yang belum ada.

## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
csrf_exempt digunakan pada view di Django untuk menonaktifkan perlindungan Cross-Site Request Forgery (CSRF) pada permintaan tertentu, seperti AJAX POST. Secara default, Django menggunakan token CSRF untuk melindungi aplikasi dari serangan CSRF, yang mencegah pengiriman data dari sumber yang tidak sah.

## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan dan validasi data di backend sangat penting karena validasi di frontend dapat dengan mudah dilewati atau diabaikan oleh pengguna yang berusaha mengeksploitasi sistem. Data yang dikirimkan melalui jaringan bisa dimodifikasi, dan pemeriksaan hanya di frontend tidak dapat diandalkan.

Backend memiliki akses penuh untuk memastikan bahwa data yang masuk benar, aman, dan sesuai dengan aturan yang telah ditentukan. Selain itu:

### 1. Keamanan: Validasi di backend membantu mencegah serangan seperti SQL injection atau serangan lainnya yang bisa terjadi jika data pengguna tidak diproses dengan aman.
### 2. Integritas Data: Memastikan bahwa data yang masuk ke database valid dan konsisten sangat penting untuk integritas sistem.
### 3. Reliabilitas: Frontend JavaScript bisa dinonaktifkan oleh pengguna, sehingga backend tetap harus memastikan bahwa semua input yang diterima valid.

Meskipun validasi di frontend meningkatkan pengalaman pengguna (lebih cepat dan interaktif), validasi di backend tetap merupakan kebutuhan wajib untuk menjaga keamanan dan keandalan aplikasi.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Menambahkan fungsi add_product_by_ajax agar mendukung AJAX GET. Membuat tombol add product by ajax yang membuka sebuah modal yang dapat digunakan untuk menambahkan produk secara asinkronus dengan mengimplementasikan script pada main.html dan akhirnya menambahkan proteksi terhadap XSS dengan cara clean dan strip html tags pada data yang dimasukkan
