import { getAllBooks, searchBooks } from '../api/data.js';
import { html } from '../lib.js';

const searchTemplate = (books, onSearch, params = '') => html`
<section id="search-page" class="dashboard">
    <h1>Search</h1>
    
    <form @submit=${onSearch}>
        <input type="text" name="search" .value=${params}>
        <input type="submit" value="search">
    </form>

    ${books.length == 0 
        ? html`<p class="no-books">No books in database!</p>`
        : html`<ul class="other-books-list">
            ${books.map(bookPreview)}
        </ul>`
    }
    <!-- Display paragraph: If there are no books in the database -->
    
</section>`;

const bookPreview =(book) => html`
<li class="otherBooks">
    <h3>${book.title}</h3>
    <p>Type: ${book.type}</p>
    <p class="img"><img src=${book.imageUrl}></p>
    <a class="button" href="/details/${book._id}">Details</a>
</li>`

export async function searchPage(ctx) {
    const params = ctx.querystring.split('=')[1];
    let books = [];

    if (params) {
        books = await searchBooks(decodeURIComponent(params));
    }
    ctx.render(searchTemplate(books, onSearch, params));

    function onSearch(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const search = formData.get('search');

        if (search) {
            ctx.page.redirect('/search?query=' + encodeURIComponent(search));
        }
    }
}