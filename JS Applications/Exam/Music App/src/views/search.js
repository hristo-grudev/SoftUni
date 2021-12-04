import { searchAlbums } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

let userData = null;

const searchTemplate = (albums, onSearch, params = '') => html`
<section id="searchPage">
    <h1>Search by Name</h1>
    <form @submit=${onSearch}>
        <div class="search">
            <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name" .value=${params}>
            <button class="button-list" type="submit">Search</button>
        </div>
    </form>
    <h2>Results:</h2>

    <div class="search-result">
        ${albums.length == 0 
            ? html`<p class="no-result">No result.</p>`
            : html`${albums.map(bookPreview)}`
        }
        
    </div>
</section>`;

const bookPreview =(album) => html`
<div class="card-box">
    <img src=${album.imgUrl}>
    <div>
        <div class="text-center">
            <p class="name">Name: ${album.name}</p>
            <p class="artist">Artist: ${album.artist}</p>
            <p class="genre">Genre: ${album.genre}</p>
            <p class="price">Price: $${album.price}</p>
            <p class="date">Release Date: ${album.date}</p>
        </div>
        <div class="btn-group">
            ${userData
                ? html`<a href="/details/${album._id}" id="details">Details</a>`
                : null
            }
        </div>
    </div>
</div>`;

export async function searchPage(ctx) {
    userData = getUserData();
    const params = ctx.querystring.split('=')[1];
    let albums = [];

    if (params) {
        albums = await searchAlbums(decodeURIComponent(params));
    }
    ctx.render(searchTemplate(albums, onSearch, params));

    function onSearch(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const search = formData.get('search');

        if (search) {
            ctx.page.redirect('/search?query=' + encodeURIComponent(search));
        }
    }
}