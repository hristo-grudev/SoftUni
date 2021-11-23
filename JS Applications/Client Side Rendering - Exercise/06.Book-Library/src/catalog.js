import { getBooks, html, until } from './utility.js';

const catalogTemplate = (booksPromise) => html`
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        ${until(booksPromise), html`<tr><td colspan="3">Loading&hellip;</td></tr>`}
    </tbody>
</table>`;


const bookRow = (book) => html`
<tr>
    <td>${book.title}</td>
    <td>${book.author}</td>
    <td>
        <button class="edit">Edit</button>
        <button class="delete">Delete</button>
    </td>
</tr>`;

export function showCatalog(ctx) {
    return catalogTemplate();
}

async function loadBooks() {
    const books = await getBooks();

    return Object.values(books).map(bookRow);
}