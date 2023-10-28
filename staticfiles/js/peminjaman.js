var konz = "";
var urlBook = $("#url-get-book").data("url")
var urlItem = $("#url-get-item").data("url")
async function getItems() {
    return fetch(urlItem).then((res) => res.json())
}
async function getBooks() {
    return fetch(urlBook).then((res) => res.json())
}
async function refreshItems(){
    const checkedBoxes = document.querySelectorAll('#filterForm input[type="checkbox"]:checked');
    const checkedGenres = Array.from(checkedBoxes).map(checkbox => checkbox.value);
    const filterForm = document.getElementById('filterForm');
    document.getElementById("item-card").innerHTML = ""
    const items = await getItems();
    const books = await getBooks();
    let htmlString = ``
    items.forEach((item) => {
        const book = books.find(book => book.pk === item.fields.book);
        if(checkedGenres.includes(book.fields.genre) && (book.fields.name.toLowerCase().includes(konz.toLowerCase()) || book.fields.author.toLowerCase().includes(konz.toLowerCase()))){
            htmlString += `
                <div class="card" style="width: 200px; height: 300px; padding: 10px; margin-left: 50px; margin-bottom: 25px">
                    <a data-bs-toggle="modal" data-bs-target="#pinjamModal${item.pk}">
                        <img src="${book.fields.image}" class="card-img-top" alt="${book.fields.name} Cover" style="object-fit: contain; width: 100%; height: 100%;">
                    </a>
                </div>`
        }
    })
    document.getElementById("item-card").innerHTML = htmlString
}
refreshItems();
const filterForm = document.getElementById('filterForm');
filterForm.addEventListener('change', function() {
    refreshItems();
});
document.getElementById('search-book').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();  // Prevent form submission
        konz = this.value;
        console.log(this.value)
        refreshItems();
    }
});
async function returnBook(id) {
    const items = await getItems()
    const item = items.find(item => item.pk === parseInt(id));
    let date = new Date(item.fields.tgl_batas);
    let today = new Date();

    date.setHours(0, 0, 0, 0);
    today.setHours(0, 0, 0, 0);

    if (today <= date) {
        alert("Terima kasih sudah mengembalikan buku ini tepat waktu!")
    } else {
        alert("Lain kali jangan telat mengembalikan, ya!")
    }
    let url = $("#url-return-book").data("url")
    url = url.replace('0', id);
    fetch(url, {
        method: "POST",
    }).then(refreshItems);
    return false;
}
const buttons = document.querySelectorAll('button[name="return_button"]');

buttons.forEach((button) => {
    button.addEventListener("click", function() {
        const isConfirmed = window.confirm("Ingin mengembalikan buku ini?");
        if (!isConfirmed) {
            event.preventDefault();
        }
        else { returnBook(this.value); }
    });
});

