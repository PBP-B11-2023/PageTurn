$(document).ready(function() {
    let currentCardIndex = 0;
    if (performance.navigation.type === 1) {
        // Full page reload
        console.log('Full page reload');
    } else {
        // Not a full page reload
        console.log('Not a full page reload');
    }

    // Fetch the books using AJAX
    $.get("/get_favourite_books/", function(data) {
        const books = data.favourite_books;
        const bookListElement = $('.book-list');

        // Clear existing book list
        bookListElement.empty();

        books.forEach((book, index) => {
            const cardHtml = `<div class="card" id="card-${index}">
                <img src="${book.image}" alt="${book.name} Cover">
                <h2>${book.name}</h2>
                <p>Author: ${book.author}</p>
                <p>Rating: ${book.rating}</p>
                <p>Price: $${book.price}</p>
                <p>Year: ${book.year}</p>
                <p>Genre: ${book.genre}</p>
                <a class="read-more-link" href="#">Read More</a>
                <div class="description hidden">${book.description}</div>
            </div>`;
            bookListElement.append(cardHtml);
        });


        const cards = $('.card');
        const totalCards = cards.length;
        $(cards[currentCardIndex]).show();

        $('#next-button').click(function() {
            $(cards[currentCardIndex]).hide();
            currentCardIndex = (currentCardIndex + 1) % totalCards;
            $(cards[currentCardIndex]).show();
        });

        $('#prev-button').click(function() {
            $(cards[currentCardIndex]).hide();
            currentCardIndex = (currentCardIndex - 1 + totalCards) % totalCards;
            $(cards[currentCardIndex]).show();
        });


        $('.read-more-link').click(function() {
            console.log('Script is running');
            const description = $(this).siblings('.description').html();
            const popup = document.createElement('div');
            popup.className = 'popup';
            popup.innerHTML = '<div class="popup-content">' + description + '</div';

            document.body.appendChild(popup);

            popup.style.display = 'block'; 

            popup.addEventListener('click', () => {
                popup.style.display = 'none'; 
                popup.remove();
            });
        });
    });
});
