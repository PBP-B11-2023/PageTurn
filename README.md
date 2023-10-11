# PBP_UTS

### Cerita dan Manfaat Aplikasi
Minat baca masyarakat di Indonesia masih tergolong rendah. Menurut data yang ada, persentase masyarakat yang gemar membaca di Indonesia masih jauh di bawah negara-negara maju. Hal ini menjadi tantangan tersendiri dalam meningkatkan literasi di Indonesia. Oleh karena itu, <nama_aplikasi> hadir sebagai solusi inovatif untuk mengatasi masalah ini.

<nama_aplikasi> adalah sebuah aplikasi perpustakaan digital yang memungkinkan pengguna untuk mengakses ratusan e-book dari satu aplikasi sehingga menghemat waktu dalam mencari dan mengelola buku-buku mereka. Pengguna dapat melihat status peminjaman buku (wishlist, proses penyewaan, atau telah dikembalikan), pengguna mempunyai rak buku virtual sendiri, dan pengguna dapat memberikan ulasan/rating pada buku yang telah mereka baca. Selain itu, aplikasi ini juga menampilkan rekomendasi buku yang sesuai dengan minat pengguna.

### Dataset
Pada proyek ini kami akan menggunakan dataset dari [Kaggle Amazon Top 50 Bestselling Books 2009 - 2019](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019). <br>

Kami memilih menggunakan dataset tersebut karena memiliki relevansi yang tinggi dan berisi katalog buku yang terbit tidak sampai 2 dekade lalu. Dataset ini juga sudah memenuhi persyaratan karena sudah memiliki 550 buku. Dataset ini memiliki kelengkapan yang memadai karena selain meliputi parameter utama seperti judul buku, penulis, dan tahun terbit, terdapat juga beberapa parameter tambahan seperti rating, jumlah rating, harga, dan genre secara umum.

Berikut adalah contoh dari dataset tersebut:
<table class="table table-bordered table-hover table-condensed">
<thead><tr><th title="Field #1">Name</th>
<th title="Field #2">Author</th>
<th title="Field #3">User Rating</th>
<th title="Field #4">Reviews</th>
<th title="Field #5">Price</th>
<th title="Field #6">Year</th>
<th title="Field #7">Genre</th>
</tr></thead>
<tbody><tr>
<td>10-Day Green Smoothie Cleanse</td>
<td>JJ Smith</td>
<td align="right">4.7</td>
<td align="right">17350</td>
<td align="right">8</td>
<td align="right">2016</td>
<td>Non Fiction</td>
</tr>
<tr>
<td>11/22/63: A Novel</td>
<td>Stephen King</td>
<td align="right">4.6</td>
<td align="right">2052</td>
<td align="right">22</td>
<td align="right">2011</td>
<td>Fiction</td>
</tr>
<tr>
<td>12 Rules for Life: An Antidote to Chaos</td>
<td>Jordan B. Peterson</td>
<td align="right">4.7</td>
<td align="right">18979</td>
<td align="right">15</td>
<td align="right">2018</td>
<td>Non Fiction</td>
</tr>
<tr>
<td>1984 (Signet Classics)</td>
<td>George Orwell</td>
<td align="right">4.7</td>
<td align="right">21424</td>
<td align="right">6</td>
<td align="right">2017</td>
<td>Fiction</td>
</tr>
<tr>
<td>5,000 Awesome Facts (About Everything!) (National Geographic Kids)</td>
<td>National Geographic Kids</td>
<td align="right">4.8</td>
<td align="right">7665</td>
<td align="right">12</td>
<td align="right">2019</td>
<td>Non Fiction</td>
</tr>
<tr>
<td>A Dance with Dragons (A Song of Ice and Fire)</td>
<td>George R. R. Martin</td>
<td align="right">4.4</td>
<td align="right">12643</td>
<td align="right">11</td>
<td align="right">2011</td>
<td>Fiction</td>
</tr>
<tr>
<td>A Game of Thrones / A Clash of Kings / A Storm of Swords / A Feast of Crows / A Dance with Dragons</td>
<td>George R. R. Martin</td>
<td align="right">4.7</td>
<td align="right">19735</td>
<td align="right">30</td>
<td align="right">2014</td>
<td>Fiction</td>
</tr>
<tr>
<td>A Gentleman in Moscow: A Novel</td>
<td>Amor Towles</td>
<td align="right">4.7</td>
<td align="right">19699</td>
<td align="right">15</td>
<td align="right">2017</td>
<td>Fiction</td>
</tr>
<tr>
<td align="center">.....</td>
<td align="center">.....</td>
<td align="center">.....</td>
<td align="center">.....</td>
<td align="center">.....</td>
<td align="center">.....</td>
<td align="center">.....</td>
</tr>
</tbody></table>

Peran Pengguna : 
Tidak Login : Pengguna dapat melakukan login jika sudah memiliki akun untuk masuk ke website peminjaman buku. Atau jika belum memiliki akun pengguna dapat membuat akun baru dengan membuat username dan password sehingga dapat melakukan login untuk masuk website peminjaman buku

Sudah Login : Pengguna dapat melakukan peminjaman buku, dalam arti jika buku tersebut tersedia. Untuk meminjam buku anda akan menekan button add new buku untuk peminjaman dan berpindah ke halaman peminjaman yaitu beralih pada admin. Buku yang dipinjam akan masuk ke daftar buku yang sudah dipinjam dan ditampilkan di tabel sebagai daftar buku yang dipinjam user. Lalu pengguna yang sudah login dapat mengembalikan buku dengan delete pada daftar buku tersebut, atau ingin menambahkan buku yang sama dengan menambahkan jumlah buku yang juga dapat dilakukan pada daftar buku yang sudah dipinjam tersbebut. Pengguna yang sudah login juga dapat melihat dan memberikan ulasan buku. Kemudian pengguna juga dapat request buku yang akan ditambahkan sebagai wishlist dalam kondisi jika buku belum tersedia

Admin : Menambahkan buku baru sehingga diupdate pada daftar buku yang sudah dipinjam
