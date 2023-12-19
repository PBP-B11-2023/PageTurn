async function getProducts() {
    return fetch("/laporan_buku_rusak/get-product/").then((res) => res.json());
}

async function refreshProducts() {
    document.getElementById("product_table").innerHTML = "";
    const products = await getProducts();
    let htmlString = `<tr>
        <th>Name</th>
        <th>Kondisi Buku</th>
        <th>Alasan Rusak</th>
    </tr>`;
    products.forEach((item) => {
        htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.is_rusak ? "Rusak" : "Non-rusak"}</td>
            <td>${item.fields.description}</td>
        </tr>`;
    });

    document.getElementById("product_table").innerHTML = htmlString;
    document.getElementById("product_table").style.display = "table";
}

refreshProducts();

function addProduct() {
    const isRusak = document.getElementById("is-rusak").value;
    const formData = new FormData(document.querySelector('#form'));
    formData.append("is_rusak", isRusak);

    fetch("/laporan_buku_rusak/create-product-ajax/", {
        method: "POST",
        body: formData
    }).then(refreshProducts);
    document.getElementById("form").reset();
    return false;
}

document.getElementById("button_add").addEventListener("click", addProduct);

document.getElementById("filter-button").addEventListener("click", filterProducts);

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
    document.getElementById("filter-button").addEventListener("click", filterProducts);
    // Buat tabel hasil filter
    document.getElementById("product_table").innerHTML = "";
    let htmlString = `<tr>
        <th>Name</th>
        <th>Kondisi Buku</th>
        <th>Alasan Rusak</th>
    </tr>`;
    filteredProducts.forEach((item) => {
        htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.is_rusak ? "Rusak" : "Non-rusak"}</td>
            <td>${item.fields.description}</td>
        </tr>`;
    });
    document.getElementById("product_table").innerHTML = htmlString;
}
refreshProducts();