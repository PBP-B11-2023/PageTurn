var konz = "";
var url = $("#url-get-book").data("url")
async function getBooks() {
    return fetch(url).then((res) => res.json())
}
async function refreshBooks() {
    const checkedBoxesGenres = document.querySelectorAll('#filterForm input[type="checkbox"][name="genre"]:checked');
    const checkedGenres = Array.from(checkedBoxesGenres).map(checkbox => checkbox.value);
    const checkedBoxesReady = document.querySelectorAll('#filterForm input[type="checkbox"][name="isReady"]:checked');
    const checkedReady = Array.from(checkedBoxesReady).map(checkbox => checkbox.value);
    const filterForm = document.getElementById('filterForm');
    document.getElementById("book-card").innerHTML = ""
    const books = await getBooks();
    let htmlString = ``
    books.forEach((book) => {
        if(checkedGenres.includes(book.fields.genre) && ((book.fields.is_dipinjam && checkedReady.includes("1")) || (!book.fields.is_dipinjam && checkedReady.includes("0"))) && (book.fields.name.toLowerCase().includes(konz.toLowerCase()) || book.fields.author.toLowerCase().includes(konz.toLowerCase()))){
            htmlString += `
                <div class="card ${book.fields.is_dipinjam ? 'bg-danger' : 'bg-white'}" style="width: 200px; height: 300px; padding: 10px; margin-left: 50px; margin-bottom: 25px" data-bs-toggle="modal" data-bs-target="#kosongModal${book.pk}">
                    <img src="${book.fields.image}" class="card-img-top" alt="${book.fields.name} Cover" style="object-fit: contain; width: 100%; height: 100%;">
                </div>`
        }
    })
    document.getElementById("book-card").innerHTML = htmlString
}
refreshBooks();
const filterForm = document.getElementById('filterForm');
filterForm.addEventListener('change', function() {
    refreshBooks();
});

document.getElementById('search-book').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();  // Prevent form submission
        konz = this.value;
        refreshBooks();
    }
});
const buttons = document.querySelectorAll('button[name="add_button"]');

buttons.forEach((button) => {
    button.addEventListener("click", function() {
        var form = this.form
        var durasi_peminjaman = form.elements['durasi_peminjaman'].value;
        let kosong = false;
        if (durasi_peminjaman === ""){
            kosong = true;
        }
        durasi_peminjaman = parseInt(durasi_peminjaman)
        if(durasi_peminjaman < 1 || durasi_peminjaman > 14 || kosong) {
            alert("Durasi peminjaman hanya bisa 1 sampai 14 hari!")
            return;
        }
        var isConfirmed = window.confirm("Apakah Anda yakin ingin meminjam buku ini?");
        if (isConfirmed) {
            let url = $("#url-add-book").data("url")
            let id = $(this).data("id");
            url = url.replace('0', id);
            console.log(url)
            fetch(url, {
                method: "POST",
                body: new FormData(form)
            }).then(response => {
                if(response.ok) {
                    form.reset()
                    window.location.href = $("#url-back").data("url");
                } else {
                    console.error('Error:', response.status);
                }
            })
            return false
        }
    });
});

$(document).ready(async function() {
    var hash = window.location.hash.substring(1);
    if (hash) {
        books = await getBooks()
        console.log(books)
        console.log(hash)
        var x = document.getElementById("kosongModal" + hash)
        var bootstrapModal = new bootstrap.Modal(x);
        x.addEventListener('click', function (event) {
            if (event.target.dataset.bsDismiss === 'modal') {
                bootstrapModal.hide();
            }
        });
        bootstrapModal.show();
    }
});