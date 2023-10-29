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
            <div class="card" style="width: 500px; padding: 10px; margin-left: 50px; margin-bottom: 25px">
                <h5 class="card-title ms-2 mt-2 mb-2">${book.fields.name}</h5>
                <div class="ms-2 mt-2 mb-2" style="display: flex; align-items: center;">
                    <div style="flex: 0.5;">
                        <img src="${book.fields.image}" class="card-img-top" alt="${book.fields.name} Cover" style="contain; width: 100px; height: auto">
                    </div>
                    <div style="flex: 1.5;">
                        <p><strong>Tanggal Peminjaman:</strong> ${item.fields.tgl_dipinjam}</p>
                        <p><strong>Tanggal Pengembalian:</strong> ${item.fields.tgl_dikembalikan}</p>
                    </div>
                </div>
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