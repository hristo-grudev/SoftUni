import { getAllAlbums } from '../api/data.js';
import { html } from '../lib.js';
import { getUserData } from '../util.js';

let userData = null;

const catalogTemplate = (albums) => html`
<section id="catalogPage">
    <h1>All Albums</h1>
        ${albums.length == 0
            ? html`<p>No Albums in Catalog!</p>`
            : albums.map(albumCard)} 
</section>`;

const albumCard = (album) => html `
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


export async function catalogPage(ctx) {
    userData = getUserData();
    const albums = await getAllAlbums();
    ctx.render(catalogTemplate(albums, userData));
}