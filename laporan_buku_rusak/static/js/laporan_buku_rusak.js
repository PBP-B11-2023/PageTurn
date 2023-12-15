<<<<<<< HEAD
// Ini adalah fungsi async untuk mengambil produk buku dari server menggunakan fetch.
=======
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
async function getProducts() {
    return fetch("/laporan_buku_rusak/get-product/").then((res) => res.json());
}

<<<<<<< HEAD
// Fungsi ini menghapus isi tabel produk dan memperbarui dengan data produk terbaru.
async function refreshProducts() {
    document.getElementById("product_table").innerHTML = ""; // Menghapus isi tabel
    const products = await getProducts(); // Mengambil produk dari server
=======
async function refreshProducts() {
    document.getElementById("product_table").innerHTML = "";
    const products = await getProducts();
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
    let htmlString = `<tr>
        <th>Name</th>
        <th>Kondisi Buku</th>
        <th>Alasan Rusak</th>
    </tr>`;
    products.forEach((item) => {
<<<<<<< HEAD
        // Membuat baris baru untuk setiap produk dan mengisinya dengan data produk
=======
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
        htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.is_rusak ? "Rusak" : "Non-rusak"}</td>
            <td>${item.fields.description}</td>
        </tr>`;
    });

<<<<<<< HEAD
    document.getElementById("product_table").innerHTML = htmlString; // Menyisipkan data produk ke dalam tabel
    document.getElementById("product_table").style.display = "table"; // Menampilkan tabel
}

// Memanggil fungsi refreshProducts() untuk mengisi tabel saat halaman dimuat.
refreshProducts();

// Fungsi ini dipanggil saat tombol "Add Product" diklik.
=======
    document.getElementById("product_table").innerHTML = htmlString;
    document.getElementById("product_table").style.display = "table";
}

refreshProducts();

>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
function addProduct() {
    const isRusak = document.getElementById("is-rusak").value;
    const formData = new FormData(document.querySelector('#form'));
    formData.append("is_rusak", isRusak);

<<<<<<< HEAD
    // Mengirim data produk baru ke server sebagai permintaan POST dan kemudian memperbarui tampilan produk.
=======
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
    fetch("/laporan_buku_rusak/create-product-ajax/", {
        method: "POST",
        body: formData
    }).then(refreshProducts);
<<<<<<< HEAD
    document.getElementById("form").reset(); // Mengosongkan formulir
    return false; // Mencegah pengiriman formulir dengan metode POST default.
}

// Menambahkan event listener pada tombol "Add Product" untuk menjalankan fungsi addProduct() saat tombol tersebut diklik.
document.getElementById("button_add").addEventListener("click", addProduct);

// Menambahkan event listener pada tombol "Filter" untuk menjalankan fungsi filterProducts() saat tombol tersebut diklik.
document.getElementById("filter-button").addEventListener("click", filterProducts);

// Fungsi ini akan digunakan untuk menerapkan filter pada daftar produk berdasarkan kondisi buku yang dipilih.
=======
    document.getElementById("form").reset();
    return false;
}

document.getElementById("button_add").addEventListener("click", addProduct);

document.getElementById("filter-button").addEventListener("click", filterProducts);

>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
async function filterProducts() {
    const nonRusak = document.getElementById("non-rusak-checkbox").checked;
    const rusak = document.getElementById("rusak-checkbox").checked;

    const products = await getProducts();
    const filteredProducts = products.filter((item) => {
        const isRusak = item.fields.is_rusak;

        if (nonRusak && rusak) {
            return true; // Tampilkan semua buku
        } else if (nonRusak) {
            return !isRusak; // Tampilkan yang non-rusak
        } else if (rusak) {
            return isRusak; // Tampilkan yang rusak
        }

        return false; // Tidak ada yang dipilih
    });
<<<<<<< HEAD

    // Menghapus isi tabel produk dan memperbarui dengan data produk yang difilter.
=======
    document.getElementById("filter-button").addEventListener("click", filterProducts);
    // Buat tabel hasil filter
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
    document.getElementById("product_table").innerHTML = "";
    let htmlString = `<tr>
        <th>Name</th>
        <th>Kondisi Buku</th>
        <th>Alasan Rusak</th>
    </tr>`;
    filteredProducts.forEach((item) => {
<<<<<<< HEAD
        // Membuat baris baru untuk setiap produk yang difilter dan mengisinya dengan data produk.
=======
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
        htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.is_rusak ? "Rusak" : "Non-rusak"}</td>
            <td>${item.fields.description}</td>
        </tr>`;
    });
<<<<<<< HEAD

    document.getElementById("product_table").innerHTML = htmlString; // Menyisipkan data produk yang difilter ke dalam tabel
}

// Memanggil fungsi refreshProducts() saat halaman dimuat.
refreshProducts();
=======
    document.getElementById("product_table").innerHTML = htmlString;
}
refreshProducts();
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
